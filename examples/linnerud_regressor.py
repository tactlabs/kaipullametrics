import prettymetrics

from prettymetrics.supervised import LazyRegressor
from sklearn.datasets import load_linnerud
from sklearn.model_selection import train_test_split

data = load_linnerud()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.2,random_state =123)

reg = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = reg.fit(X_train, X_test, y_train, y_test)
print(models)


