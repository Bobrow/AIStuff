import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
print("Loading Dataset")
dataset = pd.read_csv('student_marks.csv')
print("Loaded Dataset")
print(dataset.shape)
print(dataset.head())
print(dataset.describe())
dataset.plot(x='Hours',y='Marks',style='o')
plt.title("Hours vs Marks(%)")
plt.xlabel("Hours")
plt.ylabel("Marks (%)")
plt.show()
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
print("Splitting Dataset")
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
print("Done!")
print(X_train, X_test, y_train, y_test)
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)
print(linear_regressor.intercept_)
print(linear_regressor.coef_)
pred_y = linear_regressor.predict(X_test)
df = pd.DataFrame({'Actual':y_test,'Predicted':pred_y})
print(df)
mae=metrics.mean_absolute_error(y_test,pred_y)
mse=metrics.mean_squared_error(y_test,pred_y)
print('MAE:',mae)
print('MSE:',mse)
print('RMSE:', np.sqrt(mse))
