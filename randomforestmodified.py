# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


data = pd.read_csv(r'C:\users\gufran\desktop\data\diabetes1.csv')
data['chol_hdl_ratio']=data['chol_hdl_ratio'].str.replace('"', ' ', 2)
data['bmi']=data['bmi'].str.replace('"', ' ', 2)
data['waist_hip_ratio']= data['waist_hip_ratio'].str.replace('"', ' ', 2)

data['chol_hdl_ratio']= pd.to_numeric(data['chol_hdl_ratio'].str.replace(',', '.'))
data['bmi']= pd.to_numeric(data['bmi'].str.replace(',', '.'))
data['waist_hip_ratio']= pd.to_numeric(data['waist_hip_ratio'].str.replace(',', '.'))

X=data[[ 'cholesterol', 'glucose', 'hdl_chol','chol_hdl_ratio', 'age', 'weight', 'bmi', 'systolic_bp', 'diastolic_bp', 'waist_hip_ratio']]  # Features
y=data['diabetes']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# pickling the model
import pickle
pickle_out = open("clf.pkl", "wb")
pickle.dump(clf, pickle_out)
pickle_out.close()
