import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
# Load the dataset
dataset=pd.read_csv('titanic.csv')

# Check data types of all columns
data_types = dataset.dtypes
print(data_types)

# Count unique values in each column
unique_counts = dataset.nunique()
print(unique_counts)

# Generate summary statistics
# describe functions gives us mean standard deviation and many more
summary = dataset.describe()
print(summary)

