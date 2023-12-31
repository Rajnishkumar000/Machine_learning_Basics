import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Salary_Data.csv')
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()#minimize the sum of squares
regressor.fit(x_train, y_train)

y_predict = regressor.predict(x_test)
# print(y_predict)

# VISUALISING THE TRAINING SET
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')#original line vs trained line
# plt.plot(x_train,y_train, color = 'blue') THIS WILL LEAD TO ONE TO ONE PLOT
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# VISUALISING THE TEST SET
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')#original line vs trained line
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print(regressor.predict([[12]]))

print(regressor.coef_)
print(regressor.intercept_)
