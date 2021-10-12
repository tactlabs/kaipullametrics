
from prettymetrics.supervised import LazyClassifier
from sklearn.model_selection import train_test_split

import pandas as pd

data = pd.read_csv("examples/dataset/Star_data.csv")

from sklearn.preprocessing import LabelEncoder

SpType_le = LabelEncoder()

data['SpType'] = SpType_le.fit_transform(data.SpType)

X = data.drop(['TargetClass'], axis = 1)
y = data['TargetClass']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.3,random_state =123)

clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)