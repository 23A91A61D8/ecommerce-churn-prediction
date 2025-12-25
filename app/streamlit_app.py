import streamlit as st
import pandas as pd
import joblib
import json
import matplotlib.pyplot as plt
from predict import predict, predict_proba


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# ---------------------------------------------------
# Load model & scaler (cached)
# ---------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")

@st.cache_resource
def load_scaler():
    return joblib.load("models/scaler.pkl")

model = load_model()
scaler = load_scaler()

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Single Customer Prediction",
        "Batch Prediction",
        "Model Dashboard",
        "About"
    ]
)

# ---------------------------------------------------
# PAGE 1: HOME / OVERVIEW
# ---------------------------------------------------
if page == "Home":
    st.title("🛒 Customer Churn Prediction System")

    st.markdown("""
    ### 📌 Project Overview
    This application predicts whether an **e-commerce customer is likely to churn**
    (i.e., not purchase in the next 3 months).

    ### 🎯 Business Goal
    - Identify customers at risk of churn
    - Enable **targeted retention campaigns**
    - Reduce revenue loss

    ### 🧠 Model
    - Best Model: **Random Forest**
    - Metric Focus: **ROC-AUC, Recall**
    """)

    st.info("Use the sidebar to navigate through the application.")

# ---------------------------------------------------
# PAGE 2: SINGLE CUSTOMER PREDICTION
# ---------------------------------------------------
elif page == "Single Customer Prediction":
    st.title("🔍 Single Customer Churn Prediction")

    st.write("Enter customer details below:")

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input("Days Since Last Purchase", min_value=0, max_value=500)
        frequency = st.number_input("Number of Purchases", min_value=1, max_value=200)
        total_spent = st.number_input("Total Amount Spent (£)", min_value=0.0)
        avg_order_value = st.number_input("Average Order Value (£)", min_value=0.0)

    with col2:
        total_items = st.number_input("Total Items Purchased", min_value=0)
        unique_products = st.number_input("Unique Products Purchased", min_value=0)
        customer_lifetime = st.number_input("Customer Lifetime (days)", min_value=0)

    if st.button("Predict Churn Risk"):
        input_df = pd.DataFrame([{
            "Recency": recency,
            "Frequency": frequency,
            "TotalSpent": total_spent,
            "AvgOrderValue": avg_order_value,
            "TotalItems": total_items,
            "UniqueProducts": unique_products,
            "CustomerLifetimeDays": customer_lifetime
        }])

        churn_class = predict(input_df)
        churn_prob = float(predict_proba(input_df))

        st.subheader("📊 Prediction Result")

        if churn_class == 1:
            st.error(f"⚠️ High Churn Risk — Probability: {churn_prob:.2%}")
            st.markdown("**Recommendation:** Start retention campaign immediately.")
        else:
            st.success(f"✅ Low Churn Risk — Probability: {churn_prob:.2%}")
            st.markdown("**Recommendation:** Maintain engagement strategy.")

# ---------------------------------------------------
# PAGE 3: BATCH PREDICTION
# ---------------------------------------------------
elif page == "Batch Prediction":
    st.title("📂 Batch Customer Churn Prediction")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        try:
            batch_df = pd.read_csv(uploaded_file)

            st.write("Preview of uploaded data:")
            st.dataframe(batch_df.head())

            batch_df["Churn_Prediction"] = batch_df.apply(
                lambda row: predict(pd.DataFrame([row])) , axis=1
            )
            batch_df["Churn_Probability"] = batch_df.apply(
                lambda row: float(predict_proba(pd.DataFrame([row]))), axis=1
            )

            st.success("Predictions generated successfully!")
            st.dataframe(batch_df.head())

            st.download_button(
                "Download Results",
                batch_df.to_csv(index=False),
                file_name="churn_predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Error processing file: {e}")

# ---------------------------------------------------
# PAGE 4: MODEL DASHBOARD
# ---------------------------------------------------
elif page == "Model Dashboard":
    st.title("📈 Model Performance Dashboard")

    try:
        with open("models/model_comparison.csv") as f:
            st.write("Model comparison data available.")

        st.markdown("""
        **Best Model:** Random Forest  
        **Key Metrics:** ROC-AUC, Precision, Recall
        """)

    except:
        st.warning("Model performance artifacts not found.")

# ---------------------------------------------------
# PAGE 5: ABOUT / DOCUMENTATION
# ---------------------------------------------------
elif page == "About":
    st.title("📘 About This Application")

    st.markdown("""
    ### How to Use
    - Use **Single Prediction** for one customer
    - Use **Batch Prediction** for multiple customers
    - View model details in **Model Dashboard**

    ### Features Used
    - Recency
    - Frequency
    - Total Spent
    - Average Order Value
    - Product Diversity
    - Customer Lifetime

    ### Developer
    **Venkata Lakshmi**  
    Data Analytics & Machine Learning Project
    """)
