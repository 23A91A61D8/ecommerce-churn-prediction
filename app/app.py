import streamlit as st
import joblib
import numpy as np
import warnings

warnings.filterwarnings("ignore")


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="E-Commerce Churn Prediction")

st.title("🛒 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

# -----------------------------
# Load model & scaler
# -----------------------------
model = joblib.load("models/logistic_regression.pkl")
scaler = joblib.load("models/scaler.pkl")

# -----------------------------
# User input
# -----------------------------
st.subheader("Enter Customer Features")

recency = st.number_input("Recency (days)", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
total_spent = st.number_input("Total Spent", min_value=0.0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
total_items = st.number_input("Total Items", min_value=0)
unique_products = st.number_input("Unique Products", min_value=0)
customer_lifetime = st.number_input("Customer Lifetime (days)", min_value=0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Churn"):
    # Create full feature vector (same shape as training)
    input_features = np.zeros((1, scaler.n_features_in_))

    # Fill known features (order matches training)
    input_features[0, 0] = recency
    input_features[0, 1] = frequency
    input_features[0, 2] = total_spent
    input_features[0, 3] = avg_order_value
    input_features[0, 4] = total_items
    input_features[0, 5] = unique_products
    input_features[0, 6] = customer_lifetime

    # Scale (NumPy → NumPy, exactly like training)
    input_scaled = scaler.transform(input_features)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"⚠️ Customer likely to churn (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Probability: {probability:.2f})")
