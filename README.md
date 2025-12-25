# ecommerce-churn-prediction
🛒 E-Commerce Customer Churn Prediction
📌 Project Overview

Customer churn is one of the biggest challenges faced by e-commerce businesses. Retaining an existing customer is significantly cheaper than acquiring a new one, yet many customers silently stop purchasing without warning.

This project builds an end-to-end machine learning system to predict customer churn using historical transaction data. The solution transforms raw transactional data into customer-level behavioral features, trains multiple machine learning models, evaluates their performance, and deploys the best model as an interactive Streamlit web application for real-time churn prediction.

The final system helps businesses identify high-risk customers early, enabling targeted retention strategies that reduce revenue loss and improve customer lifetime value.

🧠 Business Problem

The goal is to predict whether a customer is likely to churn (stop purchasing) in the next 3 months based on past behavior.

Why this matters:

Churned customers result in direct revenue loss

Retention campaigns are cheaper than re-acquisition

Early churn prediction enables proactive engagement

Business Objective:

Accurately identify high-risk customers so retention campaigns can be targeted efficiently.

📊 Dataset

Source: Online Retail Dataset (UCI Machine Learning Repository / Kaggle)

Size: ~333,000 transactions

Period: December 2009 – December 2011

Granularity: Transaction-level (Invoice-based)

🛠️ Methodology
1️⃣ Data Cleaning

Key cleaning steps applied:

Removed rows with missing CustomerID

Removed cancelled invoices

Removed negative or zero quantities and prices

Removed duplicate records

Ensured valid date ranges

Created clean, consistent transaction data

2️⃣ Feature Engineering

Transaction-level data was transformed into customer-level features, including:

RFM Features

Recency

Frequency

TotalSpent

AverageOrderValue

UniqueProducts

TotalItems

Behavioral Features

AverageDaysBetweenPurchases

BasketSize statistics

Preferred shopping day and hour

Country diversity

Temporal Features

CustomerLifetimeDays

PurchaseVelocity

Purchases in last 30 / 60 / 90 days

Segmentation

RFM-based customer segments (Champions, Loyal, At Risk, Lost)

Final dataset:

~3,000–3,400 customers

30+ engineered features

3️⃣ Models Evaluated
Model	ROC-AUC	Precision	Recall
Logistic Regression	~0.74	~0.62	~0.60
Decision Tree	~0.71	~0.57	~0.45
Random Forest	~0.75	~0.58	~0.59
XGBoost	~0.73	~0.56	~0.55
Neural Network	~0.70	~0.55	~0.54
4️⃣ Final Model

Selected Model: Random Forest Classifier

Reason: Best balance of ROC-AUC, precision, recall, and robustness

Test ROC-AUC: ~0.75

Churn Rate: ~38%

⚙️ Installation & Usage
🔹 Local Setup
Clone the repository
git clone https://github.com/23A91A61D8/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction

Install dependencies
pip install -r requirements.txt

Run data pipeline
python src/01_data_acquisition.py
python src/02_data_cleaning.py
python src/03_feature_engineering.py

Run model training
jupyter notebook notebooks/05_advanced_models.ipynb

Launch web app
streamlit run app/streamlit_app.py

🌐 Live Application

🔗 Deployed Streamlit App:
https://ecommerce-churn-prediction-4mqebfbjtxfjcmampcblqb.streamlit.app/

📁 Project Structure
ecommerce-churn-prediction/
│
├── app/
│   ├── streamlit_app.py
│   └── predict.py
│
├── data/
│   └── processed/
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 03_feature_eda.ipynb
│   ├── 04_baseline_model.ipynb
│   ├── 05_advanced_models.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_cross_validation.ipynb
│
├── deployment/
│   └── deployment_guide.md
│
├── docs/
│   ├── 07_data_cleaning_report.md
│   ├── 09_feature_dictionary.md
│   ├── 10_eda_insights.md
│   ├── 11_model_selection.md
│   └── 12_business_impact_analysis.md
│
├── visualizations/
├── requirements.txt
├── README.md
└── submission.json

📈 Results & Business Impact

Recency is the strongest predictor of churn

Customers inactive for 60+ days show high churn risk

Targeted retention reduces unnecessary campaign costs

Model enables data-driven customer engagement

Business Value:

Reduced churn

Lower retention costs

Improved customer lifetime value

Actionable insights for marketing teams