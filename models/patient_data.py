# Import TensorFlow and other libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the data
# The data should have four columns: pulse, blood_pressure, temperature, and status
# The status column should have three possible values: 0 for normal, 1 for critical, and 2 for emergency
data = pd.read_csv("vitals_data.csv")

# Function to convert blood pressure values
def convert_bp(bp):
    numerator, denominator = bp.split("/")
    numerator = float(numerator)
    denominator = float(denominator)
    return (numerator + denominator) / 2

# Apply the blood pressure conversion function to the 'blood_pressure' column
data["blood_pressure"] = data["blood_pressure"].apply(convert_bp)

# Split the data into features and labels
X = data.iloc[:, :-1].values  # All columns except the last one
y = data.iloc[:, -1].values   # The last column

# Scale the features to have zero mean and unit variance
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model architecture
model = keras.Sequential([
  layers.Dense(16, activation="relu", input_shape=(3,)),  # Input layer for three features
  layers.Dense(8, activation="relu"),  # Hidden layer
  layers.Dense(3, activation="softmax")  # Output layer for three classes
])

# Compile the model with loss function, optimizer, and metrics
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model with the training data
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model with the testing data
model.evaluate(X_test, y_test)

# Save the model to a file
model.save("vitals_model.h5")
