from sklearn.preprocessing import StandardScaler
import numpy as np

# Create an instance of StandardScaler
scaler = StandardScaler()

# Example data
data = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# =====================
# Using .fit method
# =====================

# Fit the scaler on the data to compute mean and standard deviation
scaler.fit(data)

# =====================
# Using .transform method
# =====================
# Transform the data using the computed mean and standard deviation
transformed_data = scaler.transform(data)

# Display original and transformed data
print("Original data:")
print(data)
print("\nTransformed data:")
print(transformed_data)
