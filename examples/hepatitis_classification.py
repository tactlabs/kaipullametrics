

import pandas as pd

from prettymetrics.clf import Classifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

df=pd.read_csv("examples/dataset/hepatitis.csv")

df.drop('PROTIME',axis=1,inplace=True)

X=df[df.columns[1:]]
y=df['Class']


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.5,random_state =123)

clf = Classifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)