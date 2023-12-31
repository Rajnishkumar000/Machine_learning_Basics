# IMPORTTING LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTING DATASET
dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

# ENCODING CATEGORICAL DATA
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
c=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X = np.array(c.fit_transform(X))
print(dataset.head())

# SPLITTING THE DATASET INTO TRAINING AND TEST SET
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

# TRAINING THE MULTIPLE REGRESSION MODEL ON THE TRAINING SET
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

# PREDICTNG TEST SET RESULT
y_pred=regressor.predict(x_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),axis=1))

# EXTRA
# Making a single prediction (for example the profit of a startup with R&D Spend = 160000,
# Administration Spend = 130000, Marketing Spend = 300000 and State = 'California')

print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))

# Getting the final linear regression equation with the values of the coefficients

print(regressor.coef_)
print(regressor.intercept_)


# Therefore, the equation of our multiple linear regression model is:
#
# Profit=86.6×Dummy State 1−873×Dummy State 2+786×Dummy State 3+0.773×R&D Spend+0.0329×Administration+0.0366×Marketing Spend+42467.53