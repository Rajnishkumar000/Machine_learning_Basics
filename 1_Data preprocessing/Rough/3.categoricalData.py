import pandas as pd

# Load your dataset (replace 'Data.csv' with your dataset file)
dataset = pd.read_csv('Data.csv')
print(dataset.head())
# Get a list of column names with categorical data types
categorical_columns = dataset.select_dtypes(include=['object', 'category','float','double']).columns
print(categorical_columns)
print()
print()
print()
# Display the unique value counts for each categorical column
for column in categorical_columns:
    unique_values = dataset[column].unique()
    num_unique = len(unique_values)
    print(f"Column '{column}' has {num_unique} unique values:")
    print(unique_values)
    print('\n')
