import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# Set title
st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Prediction App")

# Load model
try:
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    with open(model_path, "rb") as f:
        model = joblib.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please train the model first and save it as model.pkl in models folder.")
    st.stop()

# Define feature input fields
st.header("Enter House Details")

# Example features — change based on your dataset
area = st.number_input("Area (in square feet)", min_value=100.0, max_value=10000.0, value=1200.0, step=50.0)
bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.slider("Number of Bathrooms", min_value=1, max_value=10, value=2)

# Convert input into DataFrame
input_df = pd.DataFrame([[area, bedrooms, bathrooms]], columns=["area", "bedrooms", "bathrooms"])

# Predict button
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Estimated House Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
