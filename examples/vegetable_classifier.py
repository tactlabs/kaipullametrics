

import pandas as pd 

from prettymetrics.clf import Classifier
from sklearn.model_selection import train_test_split


df= pd.read_csv('examples/dataset/Vegetable_market.csv')


df = df.rename(columns={'Deasaster Happen in last 3month': 'Disaster'})
df = df.rename(columns={'Vegetable condition': 'Condition'})


from sklearn.preprocessing import LabelEncoder

Vegetable_le = LabelEncoder()
Season_le  = LabelEncoder()
Month_le = LabelEncoder()
Temp_le = LabelEncoder()
Disaster_le = LabelEncoder()
Condition_le = LabelEncoder()

df['Vegetable'] = Vegetable_le.fit_transform(df.Vegetable)
df['Season'] = Season_le .fit_transform(df.Season)
df['Month'] = Month_le.fit_transform(df.Month)
df['Temp'] = Temp_le.fit_transform(df.Temp)
df['Disaster'] = Disaster_le.fit_transform(df.Disaster)
df['Condition'] = Condition_le.fit_transform(df.Condition)




X = df.drop(['Vegetable'], axis = 1)
Y = df['Vegetable']


from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15)


clf = Classifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(X_train, X_test, Y_train, Y_test)

print(models)