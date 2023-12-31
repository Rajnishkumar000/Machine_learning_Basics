import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
dataset=pd.read_csv("iris.csv")
print(dataset.head())

# Separate features and target
# X=df.iloc[:,:-1]
# y=df.iloc[:,-1]
X = dataset.drop('target',axis=1)
y = dataset['target']
print(X)
print(y)



# Split the dataset into an 80-20 training-test set
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=1)



# Apply feature scaling on the training and test sets
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



# Print the scaled training and test sets
print("Scaled Training Set:")
print(X_train)
print("\nScaled Test Set:")
print(X_test)