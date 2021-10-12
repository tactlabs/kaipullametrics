from prettymetrics.clf import Classifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data                                = load_iris()
X                                   = data.data
y                                   = data.target

X_train, X_test, y_train, y_test    = train_test_split(X, y, test_size = .5, random_state = 123)

clf                                 = Classifier(verbose = 0, ignore_warnings = True, custom_metric = None)
models,predictions                  = clf.fit(X_train, X_test, y_train, y_test)

print(models)