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

# Generate a flat job tree submit the jobs.
# Add 'submit = False' to prevent submission.
job_tree(job_file_list, tier_list)

# Running this script should generate a directory tree that looks like this:

# ~ $ tree
# .
# |-- 1-1-100
# |   |-- 1-1-100.e3654633
# |   |-- 1-1-100.o3654633
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 1-1-200
# |   |-- 1-1-200.e3654634
# |   |-- 1-1-200.o3654634
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 1-2-100
# |   |-- 1-2-100.e3654635
# |   |-- 1-2-100.o3654635
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 1-2-200
# |   |-- 1-2-200.e3654636
# |   |-- 1-2-200.o3654636
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 2-2-100
# |   |-- 2-2-100.e3654637
# |   |-- 2-2-100.o3654637
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 2-2-200
# |   |-- 2-2-200.e3654638
# |   |-- 2-2-200.o3654638
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 2-3-100
# |   |-- 2-3-100.e3654639
# |   |-- 2-3-100.o3654639
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 2-3-200
# |   |-- 2-3-200.e3654640
# |   |-- 2-3-200.o3654640
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 3-3-100
# |   |-- 3-3-100.e3654641
# |   |-- 3-3-100.o3654641
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 3-3-200
# |   |-- 3-3-200.e3654642
# |   |-- 3-3-200.o3654642
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 3-4-100
# |   |-- 3-4-100.e3654643
# |   |-- 3-4-100.o3654643
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- 3-4-200
# |   |-- 3-4-200.e3654644
# |   |-- 3-4-200.o3654644
# |   |-- files.log
# |   |-- params.input
# |   `-- sub.sh
# |-- job_tree.py
# |-- job_tree.pyc
# |-- params.input
# |-- sub.sh
# |-- test.py
# `-- tier_1.csv

# Where the {VAR_1}, {VAR_2}, and {VAR_3} in each params.input file is replaced
# with the corresponding variables. {JOB_NAME} is replaced by
# hyphen-separated string representing the directory tree in which it resides
