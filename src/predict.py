# predict.py
import joblib
import numpy as np
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
model = joblib.load(model_path)

# Sample input [area, bedrooms, bathrooms]
# You can modify this input
# input_data = np.array([[3000, 3, 2]])

# # Make prediction
# predicted_price = model.predict(input_data)
# print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")
