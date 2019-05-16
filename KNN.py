import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.neighbors import *
from sklearn.metrics import *
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_names = ['Slength','Swidth','Plength','Pwidth','Class']
dataset = pd.read_csv(iris_url, names=iris_names)
print(dataset.head())
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
feature_scale = sklearn.preprocessing.StandardScalar()
feature_scale.fit(X_train)
X_train = feature_scalar.transform(X_train)
X_test = feature_scalar.transform(X_test)
knn_clasifier = KNeigborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, Y_train)
pred_y = knn_classifier.predict(X_test)
print(confusion_matrix(Y_test,pred_y))
print(classification_report(Y_test,pred_y))
