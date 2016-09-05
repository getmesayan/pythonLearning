import pandas as pd

# Pandas can be constructued from a variety of other datastructure like
# Dicts
# Series
# Dataframes etc
#
# While constructing one can provide index(row labels) or columns(column labels )

#
# From Dict or Series of Dicts
data = dict(a=pd.Series([1, 2, 3], index=['a', 'b', 'c']), b=pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']))

print pd.DataFrame(data)
#
#      a  b
# a  1.0  1
# b  2.0  2
# c  3.0  3
# d  NaN  4

print pd.DataFrame(data, index=['d', 'b', 'a'])
#      a  b
# d  NaN  4
# b  2.0  2
# a  1.0  1

print pd.DataFrame(data, index=['d', 'b', 'a'], columns=['b', 'c'])
#    b    c
# d  4  NaN
# b  2  NaN
# a  1  NaN
#
# From dicts of ndarrays/list
# All the arrays/lists must be of same length. If index is passed it must be of same length as array

data = dict(a=[1, 2, 3], b=[4, 5, 6])
print pd.DataFrame( data )
#    a  b
# 0  1  4
# 1  2  5
# 2  3  6

data = [dict(name='Prince', surname= 'Charles', crap='aaa'), dict(name='he', surname= 'man', crapper='ddd')]
print pd.DataFrame( data, columns=['surname', 'name'], index=['first', 'second'])
#
#         surname    name
# first   Charles  Prince
# second      man      he

#From a Series
print pd.DataFrame( pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))
#      0
# a  5.0
# b  5.0
# c  5.0
# d  5.0
# e  5.0