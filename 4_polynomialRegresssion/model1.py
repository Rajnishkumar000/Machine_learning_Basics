
# IMPORTING THE LIBDRARIES

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# IMPORTING THE DATASET
dataset=pd.read_csv('Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values
# plt.plot(X,y)
# plt.show()

# TRAINING THE LINEAR REGRESSION MODEL
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,y)


# plt.plot(X,y)
# plt.show()
# print(dataset)

# TRAINING THE POLYNOMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)#CREATES MATRIX FOR DEGREE 2 SAY 1 X X^2
x_poly=poly_reg.fit_transform(X)
print(x_poly)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)

# VISUALIZING THE LINEAR REGRESSION RESULT
plt.scatter(X,y,color='red')
plt.plot(X,lin_reg.predict(X))
plt.title('Linear Regression model')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()

# VISUALIZING THE POLYNOMIAL REGRESSION RESULT
plt.scatter(X,y,color='red')
plt.plot(X,lin_reg2.predict(x_poly))
plt.title('Polynomial Regression model')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()

#VISUALIZING THE POLYNOMIAL REGRESSION RESULT FOR HIGHER RESOLUTION RESULT
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()

# PREDICTION NEW RESULT WITH LINEAR
a=lin_reg.predict([[6.5]])
print(a)

# PREDICTING NEW RESULT WITH POLYNOMIAL
b=lin_reg2.predict(poly_reg.fit_transform([[6.5]]))
print(b)
