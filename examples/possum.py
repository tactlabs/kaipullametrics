
from prettymetrics.reg import Regressor
from sklearn.model_selection import train_test_split

import pandas as pd

data = pd.read_csv("examples/dataset/possum.csv")

data = data.dropna()

from  sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

data["Pop"] = le.fit_transform(data.Pop)
data["sex"] = le.fit_transform(data.sex)

X = data.drop(["age"], axis =1)
y = data["age"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = .2,random_state = 123)

reg = Regressor(verbose = 0,ignore_warnings = True, custom_metric = None)
models, predictions = reg.fit(X_train, X_test, y_train, y_test)

print(models)