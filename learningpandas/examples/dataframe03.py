# Column selection, addition, deletion
#
# Getting, setting, and deleting columns works with the same syntax as the analogous dict operations:
import pandas as pd

data = dict(a=pd.Series([1, 2, 3], index=['a', 'b', 'c']), b=pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']))

df = pd.DataFrame(data)

#Adding a column
df['c'] = df['a'] * 3

print df

#      a  b    c
# a  1.0  1  3.0
# b  2.0  2  6.0
# c  3.0  3  9.0
# d  NaN  4  NaN

#Deleting a column

df = df[['a', 'c']]
print df

#      a    c
# a  1.0  3.0
# b  2.0  6.0
# c  3.0  9.0
# d  NaN  NaN


df['d'] = df['a'] + 1
df['e'] = df['d'] * 3

del df['a']
print df

#      c    d     e
# a  3.0  2.0   6.0
# b  6.0  3.0   9.0
# c  9.0  4.0  12.0
# d  NaN  NaN   NaN

c = df.pop('c')

print c

# a    3.0
# b    6.0
# c    9.0
# d    NaN
# Name: c, dtype: float64
