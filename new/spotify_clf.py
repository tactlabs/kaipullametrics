

import pandas as pd
from prettymetrics.clf import Classifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def run_():

    df  = pd.read_csv('/home/saaisri/Desktop/tact/prettymetrics/new/spotify.csv')

    X   = df[df.columns[:-1]]
    y   = df['liked']

    X_train, X_test, y_train, y_test    = train_test_split(X, y, test_size = .5, random_state = 123)
    clf = Classifier(verbose = 0, ignore_warnings = True, custom_metric = None)
    models,predictions                  = clf.fit(X_train, X_test, y_train, y_test)

    print(models)

def startpy():
    
    run_()


if __name__ == '__main__':
    startpy()