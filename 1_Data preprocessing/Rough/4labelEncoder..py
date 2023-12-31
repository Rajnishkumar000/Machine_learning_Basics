from sklearn.preprocessing import LabelEncoder

# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Example categorical labels
labels = ['cat', 'dog', 'bird', 'cat']

# Fit the LabelEncoder on the labels and transform them
numeric_labels = label_encoder.fit_transform(labels)

print("Original labels:", labels)
print("Encoded labels:", numeric_labels)