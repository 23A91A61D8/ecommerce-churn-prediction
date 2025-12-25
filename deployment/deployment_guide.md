# Deployment Guide

## Platform
Streamlit Community Cloud (Free)

---

## Prerequisites
- GitHub account
- Public GitHub repository
- Streamlit application code committed to GitHub
- `requirements.txt` present in root directory

---

## Repository Structure

ecommerce-churn-prediction/
├── app/
│ ├── streamlit_app.py
│ └── predict.py
├── models/
│ ├── best_model.pkl
│ └── scaler.pkl
├── data/
│ └── processed/
│ └── feature_names.json
├── requirements.txt
├── README.md
└── deployment/
└── deployment_guide.md


---

## Step-by-Step Deployment

### 1. Prepare Repository
- Ensure all code is committed and pushed to GitHub
- Confirm `app/streamlit_app.py` exists
- Ensure trained model files are present in `models/`
- Ensure `requirements.txt` contains all dependencies

---

### 2. Create `requirements.txt`

The following dependencies are required:

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.26.0
scikit-learn>=1.3.0
joblib>=1.3.0
plotly>=5.17.0
matplotlib>=3.7.0

---

### 3. Deploy on Streamlit Cloud

Go to: https://share.streamlit.io

Sign in using GitHub

Click New App

Select:

Repository: ecommerce-churn-prediction

Branch: main

Main file path: app/streamlit_app.py

Click Deploy

Wait 2–5 minutes for the build to complete

## Post-Deployment Checklist

✔ App loads successfully
✔ Single customer prediction works
✔ Batch prediction works
✔ Model dashboard displays correctly
✔ No critical errors in Streamlit logs

# Live Application URL

https://ecommerce-churn-prediction-4mqebfbjtxfjcmampcblqb.streamlit.app/

# Notes

Minor sklearn version warnings do not affect functionality

Feature alignment handled via feature_names.json

Application uses cached model loading for performance