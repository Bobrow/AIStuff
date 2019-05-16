import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
dataset = pd.read_csv('fuel_consumption.csv')
sys.__stdout__ = sys.stdout
print(dataset.head())
print(dataset.shape)
print(dataset.describe())
X= dataset[['Tax','Income','Highways','Licence']]
y= dataset['Consumption']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)
coeff = pd.DataFrame(linear_regressor.coef_,X.columns,columns=['Coefficient'])
print(coeff)
pred_y = linear_regressor.predict(X_test)
df = pd.DataFrame({'Actual':y_test, 'Predicted':pred_y})
print(df)
mae=metrics.mean_absolute_error(y_test,pred_y)
mse=metrics.mean_squared_error(y_test,pred_y)
rmse=np.sqrt(mse)
print('MAE:',mae)
print('MSE:',mse)
print('RMSE:',rmse)
