# Churn Definition
# Problem Statement

The objective of this project is to predict customer churn for an e-commerce business.
Churn must be clearly and consistently defined so that the machine learning model can learn meaningful customer behavior patterns.

In this context, customer churn refers to customers who become inactive and stop purchasing over a defined future period.

# Approach: Observation Window Method

To avoid data leakage and ensure a realistic churn definition, a time-based observation window approach is used.

# Step 1: Define Time Windows
  # Total Data Period

Start Date: 2009-12-01

End Date: 2011-12-09

Duration: Approximately 24 months

# Training Period

Start: 2009-12-01

End: 2011-09-09

Duration: ~21 months

Purpose:

Used to calculate all customer-level features such as recency, frequency, monetary value, and behavioral patterns.

No future information is used in feature creation.

# Observation Period

Start: 2011-09-10

End: 2011-12-09

Duration: 3 months (90 days)

Purpose:

Used only to observe whether a customer made at least one purchase after the training period.

Determines churn status.

# Step 2: Churn Label Definition

A customer is labeled as churned if:

The customer made at least one purchase during the training period, and

The customer made no purchases during the 90-day observation period

# Target Variable Encoding

Churn = 1: Customer churned (inactive in observation window)

Churn = 0: Customer active (at least one purchase in observation window)

# Rationale for This Definition

Aligns with common industry practices for churn modeling

Avoids future data leakage

Reflects realistic business use cases such as retention campaigns

Provides a clear binary classification target for machine learning models
-----------------------------------------------------------------------------
# Step 2: Churn Definition

A customer is classified based on their purchasing activity across the defined time windows.

# Churned Customer (Churn = 1)

A customer is considered CHURNED if:

They made at least one purchase during the training period, AND

They made zero purchases during the observation period (next 3 months)

# Active Customer (Churn = 0)

A customer is considered ACTIVE if:

They made at least one purchase during the training period, AND

They made at least one purchase during the observation period

This definition ensures a clear, time-based separation between feature creation and churn labeling, avoiding data leakage and aligning with real-world churn prediction scenarios.
-----------------------------------------------------------------
# Step 3: Implementation Logic
  # Pseudo-code
  training_cutoff = '2011-09-09'
  observation_end = '2011-12-09'
  These dates are examples based on the full dataset
(2009-12-01 to 2011-12-09)

# Dynamic Approach (Recommended)

To make the churn definition robust and reusable, a dynamic, data-driven approach is used:

Identify the latest transaction date in the cleaned dataset

Set the observation period end to this latest date

Define the training cutoff as 90 days before the observation end

This guarantees a fixed 3-month observation window regardless of dataset size

max_date = df['InvoiceDate'].max()
observation_end = max_date
training_cutoff = max_date - pd.Timedelta(days=90)

# Identify Customers in Training Period
training_customers = transactions[
    transactions['InvoiceDate'] <= training_cutoff
]['CustomerID'].unique()


These customers are eligible for churn evaluation.

# Identify Customers in Observation Period
observation_customers = transactions[
    (transactions['InvoiceDate'] > training_cutoff) &
    (transactions['InvoiceDate'] <= observation_end)
]['CustomerID'].unique()


These customers are considered active during the observation window.

# Determine Churned Customers
churned_customers = set(training_customers) - set(observation_customers)


Customers present in the training period but absent in the observation period are labeled as churned

Customers present in both periods are labeled as active
-----------------------------------------------------------------
# Step 4: Expected Distribution
# Expected Churn Rate

Based on typical e-commerce customer behavior:

Expected churn rate: 20% – 40%

If churn rate is below 10% or above 60%, the churn logic should be reviewed for errors.

This expected range ensures:

Sufficient churned customers for model learning

Balanced classification performance

Realistic business interpretation

# Justification for 3-Month Observation Window

The churn definition uses a 3-month (90-day) observation window for the following reasons:

Common industry standard for e-commerce churn analysis

Avoids overly short windows affected by seasonal behavior

Avoids overly long windows that label too many customers as churned

Aligns with quarterly business planning and retention campaigns

# Validation Criteria

To ensure correctness and avoid data leakage, the following validation rules are enforced:

Churn rate falls between 20% and 40%

No data leakage:

All features are created only from the training period

Observation period is used only for churn labeling

Clear temporal separation between training and observation windows