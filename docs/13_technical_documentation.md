# Technical Documentation

## 1. System Architecture

The system follows an end-to-end machine learning pipeline from raw data ingestion to model deployment as a web application.

### High-Level Flow:
Raw Transaction Data  
→ Data Cleaning  
→ Feature Engineering  
→ Model Training & Evaluation  
→ Model Selection  
→ Deployment (Streamlit App)

### Architecture Components:
- **Data Layer**: CSV-based transactional dataset
- **Processing Layer**: Python scripts for cleaning and feature engineering
- **Model Layer**: Multiple ML models trained and compared
- **Application Layer**: Streamlit web application
- **Deployment Layer**: Streamlit Community Cloud

---

## 2. Data Pipeline

The data pipeline is implemented using modular Python scripts for clarity and reproducibility.

### Step 1: Data Acquisition
**Script:** `src/01_data_acquisition.py`  
- Downloads or loads the raw e-commerce transaction dataset
- Saves raw data to `data/raw/`

### Step 2: Data Cleaning
**Script:** `src/02_data_cleaning.py`  
Key cleaning steps:
- Remove rows with missing `CustomerID`
- Remove cancelled invoices (`InvoiceNo` starting with 'C')
- Remove negative quantities and zero prices
- Remove duplicates
- Create `TotalPrice = Quantity × UnitPrice`

Output:
- Cleaned data saved to `data/processed/cleaned_transactions.csv`

### Step 3: Data Validation
**Notebook:** `notebooks/02_data_validation.ipynb`  
- Validates no missing values
- Ensures all prices and quantities are positive
- Confirms correct data types
- Generates validation report JSON

### Step 4: Feature Engineering
**Script:** `src/03_feature_engineering.py`  
Transforms transaction-level data into customer-level features.

Feature categories:
- **RFM Features**: Recency, Frequency, Monetary
- **Behavioral Features**: Basket size, purchase intervals
- **Temporal Features**: Lifetime, recent activity windows
- **Product Features**: Product diversity, price preferences
- **Segmentation**: RFM-based customer segments
- **Target Variable**: Churn (based on observation window)

Output:
- `data/processed/customer_features.csv`
- `data/processed/feature_names.json`

### Step 5: Data Preparation for Modeling
**Script:** `src/04_model_preparation.py`  
- Removes `CustomerID`
- Encodes categorical features
- Scales numerical features
- Performs stratified train/validation/test split
- Saves prepared datasets and scaler

---

## 3. Model Architecture

### Models Implemented:
- Logistic Regression (Baseline)
- Decision Tree
- Random Forest
- XGBoost (Gradient Boosting)
- Neural Network (MLPClassifier)

### Selected Model:
**Random Forest Classifier**

#### Reason for Selection:
- Highest ROC-AUC score among evaluated models
- Good balance between precision and recall
- Robust to noise and overfitting
- Handles nonlinear relationships well

### Model Configuration:
- Ensemble of decision trees
- Bootstrap sampling
- Majority voting for classification
- Feature importance extraction supported

### Target Variable:
- **Churn = 1** → Customer did not purchase in the observation period
- **Churn = 0** → Customer remained active

---

## 4. API Reference

### Prediction Module
**File:** `app/predict.py`

#### Available Functions:
- `load_model()` → Loads trained ML model
- `load_scaler()` → Loads feature scaler
- `preprocess_input()` → Aligns and scales input features
- `predict()` → Returns churn class (0 or 1)
- `predict_proba()` → Returns churn probability (0–1)

Supports:
- Single customer prediction
- Batch prediction via CSV upload

---

## 5. Deployment Architecture

### Deployment Platform:
**Streamlit Community Cloud (Free)**

### Deployment Flow:
1. Code pushed to public GitHub repository
2. Streamlit Cloud pulls repository
3. Dependencies installed via `requirements.txt`
4. App launched using `app/streamlit_app.py`

### Application Features:
- Home / Overview page
- Single customer churn prediction
- Batch CSV prediction
- Model performance dashboard
- Documentation section

### Live Deployment:
- Public URL accessible via Streamlit Cloud
- No local setup required for end users

---

## 6. Troubleshooting

### Common Issues & Solutions

#### Issue 1: Feature mismatch error
**Cause:** Input features do not match training features  
**Solution:**  
- Use `feature_names.json`
- Ensure preprocessing aligns input to trained feature set

#### Issue 2: High churn rate
**Cause:** Incorrect observation window selection  
**Solution:**  
- Use dynamic time-based cutoff (last 90 days)

#### Issue 3: Streamlit deployment dependency error
**Cause:** Incompatible package versions  
**Solution:**  
- Use flexible versions in `requirements.txt`
- Avoid strict pinning for NumPy on cloud environments

#### Issue 4: Model warnings during prediction
**Cause:** Feature name mismatch warning from sklearn  
**Solution:**  
- Warnings are non-fatal and safe to ignore
- Ensure correct feature alignment during preprocessing

---

## 7. Summary

This technical architecture ensures:
- Modular, reproducible data processing
- Robust model evaluation and selection
- Scalable deployment via cloud-based web app
- Clear separation between data, model, and application layers
