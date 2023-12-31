# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load the dataset
dataset=pd.read_csv('pima.csv')


# Identify missing data (assumes that missing data is represented as NaN)
noOfmissingData=dataset.isnull().sum()


# Print the number of missing entries in each column
print("Missing data: \n",noOfmissingData)
# Configure an instance of the SimpleImputer class
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(X)
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')




# Fit the imputer on the DataFrame
imputer.fit(X[:,1:3])

# Apply the transform to the DataFrame
X[:,1:3]=imputer.transform(X[:,1:3])

#Print your updated matrix of features
print(X)