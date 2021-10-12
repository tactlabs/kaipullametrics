

import pandas as pd
from prettymetrics.reg import Regressor
from sklearn import datasets
from sklearn.utils import shuffle
import numpy as np

df  = pd.read_csv('examples/dataset/insurance.csv')

df['smoker']    = pd.get_dummies(df['smoker'])['yes']
df['sex']       = pd.get_dummies(df['sex'])['male']

df.drop('region', axis = 1, inplace = True)

X, y    = shuffle(df[df.columns[:-1]], df['charges'], random_state=13)
X       = X.astype(np.float32)

offset  = int(X.shape[0] * 0.9)

X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

reg = Regressor(verbose=0, ignore_warnings=False, custom_metric=None)
models, predictions = reg.fit(X_train, X_test, y_train, y_test)

print(models)