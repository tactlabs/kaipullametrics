

from prettymetrics.reg import Regressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import pandas as pd

df      = pd.read_csv('examples/dataset/insurance.csv')

dummy   = pd.get_dummies(df.region, prefix = 'region')
region  = df.region
df      = df.drop(['region'], axis = 1)
df      = pd.concat([df, dummy], axis = 1)

gender_le   = LabelEncoder()
smoker_le   = LabelEncoder()

df['sex']       = gender_le.fit_transform(df.sex)
df['smoker']    = smoker_le.fit_transform(df.smoker)

X = df.drop(['charges'], axis = 1)
Y = df['charges']

X_train, X_test, Y_train, Y_test    = train_test_split(X, Y, test_size=0.15)

reg                                 = Regressor(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions                  = reg.fit(X_train, X_test, Y_train, Y_test)
print(models)
