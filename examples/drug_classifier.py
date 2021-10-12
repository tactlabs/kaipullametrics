


import pandas as pd 
from prettymetrics.clf import Classifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df= pd.read_csv('examples/dataset/drug200.csv')



Sex_le = LabelEncoder()
BP_le  = LabelEncoder()
Cholesterol_le = LabelEncoder()
Drug_le = LabelEncoder()

df['Sex'] = Sex_le.fit_transform(df.Sex)
df['BP'] = BP_le.fit_transform(df.BP)
df['Cholesterol'] = Cholesterol_le.fit_transform(df.Cholesterol)
df['Drug'] = Drug_le.fit_transform(df.Drug)

X = df.drop(['Drug'], axis = 1)
Y = df['Drug']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15)


clf = Classifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(X_train, X_test, Y_train, Y_test)

print(models)