# import packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# importing data
df = pd.read_csv('headbrain1.csv')

# head of the data
print(df.head())

X= df['Head Size(cm^3)']
y=df['Brain Weight(grams)']

# using the train test split function
X_train, X_test, y_train, y_test = train_test_split(X,y , random_state=104, test_size=0.25, shuffle=True)

# printing out train and test sets

print('X_train : ')
print(X_train.head())
print('')
print('X_test : ')
print(X_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())
