# This in an attempt to work out example from
# https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

import pandas as pd
import Quandl
import math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression

#Extract the data from Quandl
#https://www.quandl.com/
df = Quandl.get('WIKI/GOOGL')
#print df.head(10)

#Extract Fetaures
df = df[[ 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume' ]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/df['Adj. Low'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100

#Feature
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

#label
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print( df.head())

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=10)
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)

print( accuracy )

clf = svm.SVR()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)

print( accuracy )
