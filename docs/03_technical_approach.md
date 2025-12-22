# Technical Approach

## Problem Type
This is a binary classification problem where the goal is to predict whether a customer
will churn (1) or remain active (0).

## Feature Engineering Strategy
Transactional data will be aggregated to customer level.
Key features include:
- RFM metrics
- Purchase behavior patterns
- Temporal activity features

## Modeling Strategy
Multiple machine learning models will be trained and compared, including:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting (XGBoost)
- Neural Network

## Deployment Strategy
The final selected model will be deployed using a Streamlit web application.
The application will support single and batch predictions and provide model insights.
