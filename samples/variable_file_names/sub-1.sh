#!/bin/bash

#PBS -N {JOB_NAME}
#PBS -l nodes=1:ppn=1

cd $PBS_O_WORKDIR

# Run a stupid task
ls > files.log
