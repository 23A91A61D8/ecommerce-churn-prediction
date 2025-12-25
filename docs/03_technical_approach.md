# Technical Approach
# Why Classification (Not Regression)

The objective of this project is to predict customer churn, which is a binary outcome:

1 → Customer has churned (no purchase in the last 90 days)

0 → Customer is active

Since the target variable represents two discrete classes, this problem is best modeled as a classification task, not regression. Regression would attempt to predict a continuous value, which is not aligned with the business requirement of identifying churned vs. non-churned customers.

Classification models also allow the use of business-relevant evaluation metrics such as ROC-AUC, Precision, Recall, and F1-score, which are critical for assessing churn prediction performance.

# Feature Engineering Strategy

Effective churn prediction requires transforming raw transactional data into meaningful customer-level features. The project focuses on the following feature engineering approaches:

RFM Features (Recency, Frequency, Monetary)
Capture how recently and frequently customers purchase, and how much they spend.

Behavioral Patterns
Features such as average order value, product diversity, purchase velocity, and spending consistency help characterize customer behavior.

Temporal Features
Time-based features (e.g., customer lifetime, recent purchase activity) are engineered using a temporal split to avoid data leakage.

These features enable the model to learn patterns associated with customer engagement and disengagement.

# Multi-Model Strategy

Multiple machine learning algorithms are tested to identify the best-performing model for churn prediction. This includes:

Logistic Regression (baseline, interpretable)

Decision Tree

Random Forest

XGBoost

Different algorithms capture different types of relationships in the data. By comparing multiple models, the project ensures:

Robust performance evaluation

Better generalization

Selection of the most suitable model based on business and technical metrics

# Deployment Strategy Overview

The final model is deployed using a Streamlit web application, allowing users to:

Enter customer features

View churn probability predictions

Analyze customer risk levels

The entire solution is Dockerized to ensure reproducibility and consistent evaluation across environments. The application is deployed using free-tier cloud services, making it publicly accessible.