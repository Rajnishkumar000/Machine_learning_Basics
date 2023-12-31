from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Create an instance of MinMaxScaler
scaler = MinMaxScaler()

# Example data
data = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# =====================
# Using .fit method
# =====================

# Fit the scaler on the data to compute the minimum and maximum values for each feature
scaler.fit(data)

# Display the learned parameters (min and max values for each feature)
print("Learned parameters:")
print("Min values:", scaler.data_min_)
print("Max values:", scaler.data_max_)

# Note: The .transform method is not used here.

# =====================
# Apply the learned scaling parameters to new data
# =====================

# New data to be transformed using the learned parameters
new_data = np.array([[7.0, 8.0], [9.0, 10.0]])

# Transform the new data using the learned parameters
scaled_new_data = scaler.transform(new_data)

# Display the transformed new data
print("\nTransformed new data:")
print(scaled_new_data)
