#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

from job_tree import job_tree

# Tier 1 is 3 values of VAR_1 (1, 2, and 3) found in 'tier_1.csv'
tier_1_csv_file = 'tier_1.csv'

# Tier 2 is 2 values of VAR_2 for each VAR_1, defined as a function of VAR_1
def tier_2_func(df, param_dict):
    var_1 = int(param_dict['VAR_1'])
    var_2_arr = [var_1, var_1 + 1]
    return { 'VAR_2': var_2_arr }

# Tier 3 is 2 values of VAR_3 (100 and 200) defined in a python dictionary
tier_3_dict = {'VAR_3': [100,200]}

tier_list = [ tier_1_csv_file, tier_2_func, tier_3_dict ]
job_file_list = ['params.input', 'sub.sh']

# Generate a hierarchical job tree submit the jobs.
# Add 'submit = False' to prevent submission.
job_tree(job_file_list, tier_list, flat = False)

# Running this script should generate a directory tree that looks like this:

# ~ $ tree
# .
# |-- 1
# |   |-- 1
# |   |   |-- 100
# |   |   |   |-- 1-1-100.e3654621
# |   |   |   |-- 1-1-100.o3654621
# |   |   |   |-- files.log
# |   |   |   |-- params.input
# |   |   |   `-- sub.sh
# |   |   `-- 200
# |   |       |-- 1-1-200.e3654622
# |   |       |-- 1-1-200.o3654622
# |   |       |-- files.log
# |   |       |-- params.input
# |   |       `-- sub.sh
# |   `-- 2
# |       |-- 100
# |       |   |-- 1-2-100.e3654623
# |       |   |-- 1-2-100.o3654623
# |       |   |-- files.log
# |       |   |-- params.input
# |       |   `-- sub.sh
# |       `-- 200
# |           |-- 1-2-200.e3654624
# |           |-- 1-2-200.o3654624
# |           |-- files.log
# |           |-- params.input
# |           `-- sub.sh
# |-- 2
# |   |-- 2
# |   |   |-- 100
# |   |   |   |-- 2-2-100.e3654625
# |   |   |   |-- 2-2-100.o3654625
# |   |   |   |-- files.log
# |   |   |   |-- params.input
# |   |   |   `-- sub.sh
# |   |   `-- 200
# |   |       |-- 2-2-200.e3654626
# |   |       |-- 2-2-200.o3654626
# |   |       |-- files.log
# |   |       |-- params.input
# |   |       `-- sub.sh
# |   `-- 3
# |       |-- 100
# |       |   |-- 2-3-100.e3654627
# |       |   |-- 2-3-100.o3654627
# |       |   |-- files.log
# |       |   |-- params.input
# |       |   `-- sub.sh
# |       `-- 200
# |           |-- 2-3-200.e3654628
# |           |-- 2-3-200.o3654628
# |           |-- files.log
# |           |-- params.input
# |           `-- sub.sh
# |-- 3
# |   |-- 3
# |   |   |-- 100
# |   |   |   |-- 3-3-100.e3654629
# |   |   |   |-- 3-3-100.o3654629
# |   |   |   |-- files.log
# |   |   |   |-- params.input
# |   |   |   `-- sub.sh
# |   |   `-- 200
# |   |       |-- 3-3-200.e3654630
# |   |       |-- 3-3-200.o3654630
# |   |       |-- files.log
# |   |       |-- params.input
# |   |       `-- sub.sh
# |   `-- 4
# |       |-- 100
# |       |   |-- 3-4-100.e3654631
# |       |   |-- 3-4-100.o3654631
# |       |   |-- files.log
# |       |   |-- params.input
# |       |   `-- sub.sh
# |       `-- 200
# |           |-- 3-4-200.e3654632
# |           |-- 3-4-200.o3654632
# |           |-- files.log
# |           |-- params.input
# |           `-- sub.sh
# |-- job_tree.py
# |-- job_tree.pyc
# |-- params.input
# |-- sub.sh
# |-- test.py
# `-- tier_1.csv

# Where the {VAR_1}, {VAR_2}, and {VAR_3} in each params.input file is replaced
# with the corresponding variables. {JOB_NAME} is replaced by
# hyphen-separated string representing the directory tree in which it resides
