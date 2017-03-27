# job_tree

A tool to facilitate creating and running flat or hierarchical job trees.

## What this tool does

If you use either PBS or SLURM and you want to run a series of jobs that are very similar but differ in 1 or more parameter values or input files, this tool could help.

## Installation

Install using `pip install job_tree`. Click [here](https://pypi.python.org/pypi/job_tree) to view this on the Python Package Index site. If you don't have `pip` on your computer, then [download Anaconda](https://www.continuum.io/downloads). You don't need root permissions. If you're on Linux, the download will give you a `bash` script that you just run using something like `bash Anaconda2-2.4.0-Linux-x86_64.sh`. This will give you a python distribution that includes `pip`.

## Usage

This tool operates on the concept of input files, a job submission file, and one or more "tier" files, which contain the levels of the variables you want to vary. There is no limit to the number of input files you can have, and no default name for input files. The default name for job submission files is `sub.sh`, and the default names for the "tier" files are `tier_1.csv`, `tier_2.csv`, etc. There is also no limit to how many tier files you can have, but I doubt anyone will ever use more than 3. You can use other names than these, but then you'll have to type more if you use the command-line tool.

There are 2 ways to use this. For simple studies, the command line tool may be the easiest. For example, say you want to run multiple jobs that each uses an input file `params.input` that looks like this:

```
10       # VAR_1 value
100      # VAR_2 value
```

For each job, you want to have a different value for `VAR_1`. You would make a `params.input` file in your study's base directory with a bracket-surrounded variable to be replaced, like this:

```
{VAR_1}  # VAR_1 value
100      # VAR_2 value
```

If you want to run 3 jobs that have `10`, `20`, or `30` as the value of `VAR_1` you could make a file named `tier_1.csv` with the following contents:

```
VAR_1
1
2
3
```

You also have a submission script `sub.sh` with the following contents:

```
#!/bin/bash

#PBS -N {JOB_NAME}
#PBS -l nodes=1:ppn=1

cd $PBS_O_WORKDIR

# Run a stupid task
/path/to/my/program.exe params.input > output.log
```

The `JOB_NAME` variable and any variables included in your tier files can be placed in your submit file or any of your input files. In this case, since there's only 1 tier, `JOB_NAME` will be the same as `VAR_1`, but if you have multiple tiers, it would look something like `VAR_1-VAR_2` with the right values replaced.

With these files all in the base directory of your study, you can type

```
job_tree params.input
```

and the tool will create directories `1/`, `2/`, and `3/`, copy `params.input` and `sub.sh` into each directory, replace `{VAR_1}` and `{JOB_NAME}` with `1`, `2`, or `3` to match the directory it's in, and submit each job using `qsub` (or `sbatch` if that's what's available).

If your files don't have the default names, say `my_submit_file` instead of `sub.sh`, and `var1.txt` instead of `tier_1.csv`, and say you have another input file called `other_params.input`, your command would look like this:

```
job_tree --sub_file my_submit_file params.input other_params.input -t var1.txt
```

For more complicated studies, it may be better to write a short python script that calls the `job_tree` function. Look in the [samples](https://github.com/benlindsay/job_tree/tree/master/samples) folder for examples of how to do that.
