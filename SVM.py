import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
dataset = pd.read_csv("bill_authentication.csv")
print(dataset.shape,"\n",dataset.head())
X = dataset.drop('Class', axis=1)
Y = dataset['Class']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20)
svc_classifier = SVC(kernel='linear')
svc_classifier.fit(X_train, Y_train)
pred_y = svc_classifier.predict(X_test)
print(confusion_matrix(Y_test,pred_y))
print(classification_report(Y_test,pred_y))
