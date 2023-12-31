import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

dataset=pd.read_csv('Data.csv')
# X=dataset.iloc[:-1,:-1].values
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
noOfmissingData=dataset.isnull().sum()


# Print the number of missing entries in each column
print("Missing data: \n",noOfmissingData)


print(X)
print(y)
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

imputer.fit(X[:,1:3])#calculate according to simple imputer
X[:,1:3]=imputer.transform(X[:,1:3])#replace the calculated value
print(X)

