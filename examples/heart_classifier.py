
import pandas as pd

from prettymetrics.clf import Classifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

data                                = pd.read_csv("examples/dataset/heart.csv")

X                                   = data.drop(['output'], axis = 1)
y                                   = data['output']

X_train, X_test, y_train, y_test    = train_test_split(X, y, test_size = .3,random_state = 123)

clf                                 = Classifier(verbose = 0, ignore_warnings = True, custom_metric = None)
models, predictions                 = clf.fit(X_train, X_test, y_train, y_test)

print(models)