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
job_file_list = ['params.input']

# Generate a flat job tree and don't submit the jobs
job_tree(tier_list, job_file_list, submit = False)

# Running this script should generate a directory tree that looks like this:

# ~ $ tree
# .
# |-- 1-1-100
# |   `-- params.input
# |-- 1-1-200
# |   `-- params.input
# |-- 1-2-100
# |   `-- params.input
# |-- 1-2-200
# |   `-- params.input
# |-- 2-2-100
# |   `-- params.input
# |-- 2-2-200
# |   `-- params.input
# |-- 2-3-100
# |   `-- params.input
# |-- 2-3-200
# |   `-- params.input
# |-- 3-3-100
# |   `-- params.input
# |-- 3-3-200
# |   `-- params.input
# |-- 3-4-100
# |   `-- params.input
# |-- 3-4-200
# |   `-- params.input
# |-- params.input
# |-- test.py
# `-- tier_1.csv

# Where the {VAR_1}, {VAR_2}, and {VAR_3} in each params.input file is replaced
# with the corresponding variables. {CUM_JOB_NAME} is replaced by the name of
# the job directory it belongs to
