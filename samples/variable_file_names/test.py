#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

from job_tree import job_tree

job_file_list = ['params.input']
tier_list = ['tier_1.csv']

# Include variable in submission file name so th
sub_file_str = 'sub-{VAR_1}.sh'

# Generate a flat job tree submit the jobs.
# Add 'submit = False' to prevent submission.
job_tree(job_file_list, tier_list, sub_file=sub_file_str)

# Running this script should generate a directory tree that looks like this:

# ~ $ tree
# .
# |-- 1
# |   |-- 1.e3654648
# |   |-- 1.o3654648
# |   |-- files.log
# |   |-- params.input
# |   `-- sub-1.sh
# |-- 2
# |   |-- 2.e3654649
# |   |-- 2.o3654649
# |   |-- files.log
# |   |-- params.input
# |   `-- sub-2.sh
# |-- params.input
# |-- sub-1.sh
# |-- sub-2.sh
# |-- test.py
# `-- tier_1.csv

# Where the {VAR_1} in each input file is replaced with the corresponding
# value. {JOB_NAME} is replaced by hyphen-separated string representing the
# directory tree in which it resides
