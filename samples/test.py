#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

from jobtree import Tier, generate_job_tree

def tier_2_fn(df, param_dict):
    var_1 = int(param_dict['VAR_1'])
    var_2_arr = [str(i) for i in range(var_1, var_1+2)]
    return { 'VAR_2': var_2_arr }

tier_list = [ Tier('tier_1.csv'), Tier(tier_2_fn) ]
job_file_list = ['params.input']

generate_job_tree(tier_list, job_file_list, call_sub_prog = False)

# Running this script should generate a directory tree that looks like this:

# 1/
# |-- 1
# |   `-- params.input
# `-- 2
#     `-- params.input
# 2/
# |-- 2
# |   `-- params.input
# `-- 3
#     `-- params.input
# 3/
# |-- 3
# |   `-- params.input
# `-- 4
#     `-- params.input

# Where the {VAR_1} and {VAR_2} in each params.input file is replaced with
# the corresponding variables
