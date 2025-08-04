import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("🧠 Customer Segmentation with KMeans")
st.markdown("Predict which segment a customer belongs to.")

# Input fields
age = st.number_input("Customer Age", min_value=10, max_value=100, value=30)
income = st.number_input("Annual Income (in $1000s)", min_value=1, max_value=200, value=50)
score = st.slider("Spending Score (1 - 100)", 1, 100, 50)

if st.button("Predict Cluster"):
    # Prepare and scale input
    user_input = np.array([[age, income, score]])
    user_scaled = scaler.transform(user_input)

    # Predict cluster
    cluster = kmeans.predict(user_scaled)[0]
    st.success(f"🧩 The customer belongs to Cluster **{cluster}**.")
