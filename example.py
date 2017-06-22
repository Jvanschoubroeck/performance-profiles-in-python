#!/usr/bin/env python3

import pandas as pd
import numpy as np
from optperfprofpy import calc_perprof

# Example 1, testing the handling of the exception that
# occurs when the feasibility column is not present
problems = pd.Series([1, 1, 2, 2, 3, 3], dtype=int, name='problem')
methods = pd.Series(['A', 'B', 'A', 'B', 'A', 'B'], dtype=str, name='method')
objective_vals = pd.Series([2, 20, 25, 5, 30, 4], dtype=float, name='obj')
example_1_df = pd.DataFrame([problems, methods, objective_vals]).T

print('Running problem 1, no warnings should be printed.')
calc_perprof(example_1_df, ['problem'], ['obj'], ['method'])

# Example 2, testing the raising of a warning when negative values are present and
# when we combine columns to form the problem definition
variable_1 = pd.Series([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], dtype=float, name='var_1')
variable_2 = pd.Series([1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2,], dtype=float, name='var_2')
methods = pd.Series(['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'], dtype=str, name='method')
objective_vals = pd.Series([-2, -1, 2, 20, 25, 5, 17, 6, 30, 4, 2, 1], dtype=float, name='obj')
example_df = pd.DataFrame([variable_1, variable_2, methods, objective_vals]).T
example_df['feas'] = True

print('Running problem 2, unwanted scaling warning + not solving 100 percent of problems print expected.')
calc_perprof(example_df, ['var_1', 'var_2'], ['obj'], ['method'])