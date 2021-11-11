
from prettymetrics.reg import Regressor
from sklearn.model_selection import train_test_split
from  sklearn.preprocessing import LabelEncoder
import pandas as pd



def run_():

    data    = pd.read_csv("/home/saaisri/Desktop/tact/prettymetrics/new/diamonds_data.csv")

    clarity_le      = LabelEncoder()
    
    data["clarity"] = clarity_le.fit_transform(data.clarity)

    X = data.drop(["price"], axis =1)
    y = data["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = .2,random_state = 123)

    reg                 = Regressor(verbose = 0,ignore_warnings = True, custom_metric = None)
    models, predictions = reg.fit(X_train, X_test, y_train, y_test)

    print(models)


def startpy():
    
    run_()


if __name__ == '__main__':
    startpy()