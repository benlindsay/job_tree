#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

from job_tree import Tier, generate_job_tree

def tier_2_fn(df, param_dict):
    var_1 = int(param_dict['VAR_1'])
    var_2_arr = [str(i) for i in range(var_1, var_1+2)]
    return { 'VAR_2': var_2_arr }

tier_list = [ Tier('tier_1.csv'), Tier(tier_2_fn) ]
job_file_list = ['params.input']

generate_job_tree(tier_list, job_file_list, call_sub_prog = False)

# Running this script should generate a directory tree that looks like this:

# 1-1/
# `-- params.input
# 1-2/
# `-- params.input
# 2-2/
# `-- params.input
# 2-3/
# `-- params.input
# 3-3/
# `-- params.input
# 3-4/
# `-- params.input

# If you add 'flat_tree = False' to the arguments of generate_job_tree, like the
# line below, you'll get hierarchical directory structure.

# generate_job_tree(tier_list, job_file_list, call_sub_prog = False, flat_tree = False)

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
