from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

df=pd.read_csv('Data.csv')
print(df.head())
print()
print()
print()
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[0] )], remainder='passthrough')
print(ct.fit_transform(X))

X = np.array(ct.fit_transform(X))


from sklearn.preprocessing import LabelEncoder
l = LabelEncoder()
y = l.fit_transform(y)

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

# print(x_train)
# print(y_train)
# print(x_test)
# print(y_test)
sc=StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

print(x_train)
print(x_test)


