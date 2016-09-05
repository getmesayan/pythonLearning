import pandas as pd
import numpy as np

#
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html
#
# Series is a one-dimensional labeled array capable of holding any data type
# (integers, strings, floating point numbers, Python objects, etc.).
#
# The axis labels are collectively called as axis

#
#s = pd.Series( data, index = index )
#
# 1) From ndarray
# 2) from dict
# 3) from scalar

# From dict
data = dict(a='apple', b='banana')

# Sorted keys will become the indexes
s = pd.Series(data)
print s
# a     apple
# b    banana
# dtype: object


#If indexes are passed then values for matching keys are pulled out
# Missing keys will be assigned nan
print pd.Series(data, index=['a', 'c'])
# a    apple
# c      NaN
# dtype: object

# #From ndarray
# If data is an ndarray, index must be passed with same length as data
# If no index is passed then index in autogenerated as 0 - len-1
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print s
# a   -0.354594
# b    1.146475
# c   -0.398209
# d   -0.912020
# e   -1.475925
# dtype: float64

s = pd.Series(np.random.randn(5))
# 0   -1.235387
# 1   -0.580856
# 2    0.668264
# 3   -0.669413
# 4   -0.591085
# dtype: float64
print s

#3 From scalar
# An index must be provided
print pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
# dtype: float64
# a    5.0
# b    5.0
# c    5.0
# d    5.0
# e    5.0
# dtype: float64