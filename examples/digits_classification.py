

from prettymetrics.clf import Classifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


def run_():

    data                                = load_digits()
    X                                   = data.data
    y                                   = data.target

    X_train, X_test, y_train, y_test    = train_test_split(X, y, test_size = .3, random_state = 123)

    clf                                 = Classifier(verbose = 0,ignore_warnings = True, custom_metric = None)
    models, predictions                 = clf.fit(X_train, X_test, y_train, y_test)

    print(models)


def startpy():
    
    run_()


if __name__ == '__main__':
    startpy()