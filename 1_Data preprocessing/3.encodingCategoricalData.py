import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]


im=SimpleImputer(missing_values=np.nan,strategy='mean')

# Fit the imputer on the DataFrame
im.fit(X[:,1:3])

# Apply the transform to the DataFrame
X[:,1:3]=im.transform(X[:,1:3])
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0] )], remainder='passthrough')
# print(ct)
# print(ct.fit_transform(X))
X = np.array(ct.fit_transform(X))
print(X)

from sklearn.preprocessing import LabelEncoder #for yes and no
le = LabelEncoder()
y = le.fit_transform(y)
print(y)