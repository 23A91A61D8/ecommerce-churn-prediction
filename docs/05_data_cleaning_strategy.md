# Data Cleaning Strategy
# 1. Missing Values Strategy
# CustomerID (Missing: ~25%)

Decision: DROP

Reasoning:
CustomerID is the primary key required for customer-level churn prediction and feature engineering. Rows with missing CustomerID cannot be reliably assigned to any customer, making them unusable for churn modeling.

Impact:
Approximately 135,000 rows are removed, reducing noise while ensuring data integrity for customer-level analysis.

# Description (Missing: <1%)

Decision: IMPUTE

Approach:
Replace missing descriptions with a placeholder value such as "Unknown".

Reasoning:
Description is not a critical feature for churn prediction. Imputing avoids unnecessary row loss while preserving transactional records.

# 2. Handling Cancellations
# Issue

Invoices starting with the letter 'C' indicate cancelled transactions.

# Available Strategies

Option A: Remove all cancelled transactions

Option B: Retain cancellations as behavioral indicators

# Chosen Strategy: Option A – Remove all cancellations
# Reasoning

Cancelled transactions do not represent completed purchases and can distort spending, frequency, and revenue-based features. Since churn prediction focuses on genuine customer engagement, removing cancellations ensures accurate representation of purchasing behavior.

# 3. Negative Quantities
# Issue

Negative quantities represent returned items.

# Strategy

Remove transactions with Quantity < 0

# Reasoning

Returns introduce negative values that distort purchase frequency, total spend, and quantity-based metrics. Removing these records ensures consistency and prevents misleading feature calculations.

# 4. Outliers
# Quantity Outliers

Detection Method: Interquartile Range (IQR)

Threshold:
Values outside

𝑄
1
−
1.5
×
𝐼
𝑄
𝑅
and
𝑄
3
+
1.5
×
𝐼
𝑄
𝑅
Q1−1.5×IQRandQ3+1.5×IQR

Action: Remove extreme outliers

# Price Outliers

# Strategy:
Remove transactions with UnitPrice ≤ 0 and extremely high prices beyond the IQR threshold.

# Reasoning:
Extreme prices likely represent data entry errors and can disproportionately influence model learning.

# 5. Data Type Conversions

InvoiceDate: Converted to datetime format for temporal analysis

CustomerID: Converted to integer after removing missing values

UnitPrice: Already numeric; validated for positive values

Quantity: Ensured integer type after cleaning

# 6. Duplicate Handling
# Strategy

Identify duplicates using all transaction-level fields:

InvoiceNo, StockCode, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

Remove exact duplicate rows while retaining the earliest valid record

# Reasoning

Duplicate transactions can inflate frequency and monetary features, leading to biased churn predictions. Removing true duplicates ensures accurate customer behavior representation.