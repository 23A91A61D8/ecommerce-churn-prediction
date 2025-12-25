# Data Cleaning Report
# Executive Summary

Original dataset size: 541,909 rows

Cleaned dataset size: 333,234 rows

Rows removed: 208,675

Retention rate: 61.49%

Data quality score: 100% completeness (no missing values in final dataset)

The data cleaning process significantly improved data quality while retaining a sufficient volume of meaningful transactions for reliable churn modeling.

# Cleaning Steps Applied
# Step 1: Missing CustomerID Removal

Rows removed: ~135,080

Reasoning: CustomerID is mandatory for customer-level churn analysis and cannot be imputed.

Impact: Enabled accurate customer aggregation and churn labeling.

# Step 2: Cancelled Invoice Removal

Rows removed: ~9,000

Reasoning: Invoices starting with 'C' represent cancellations, not completed purchases.

Impact: Prevented distortion of revenue and frequency metrics.

# Step 3: Negative Quantity Removal

Rows removed: ~8,000

Reasoning: Negative quantities indicate returns, which complicate churn interpretation.

Impact: Ensured all transactions represent positive purchase behavior.

# Step 4: Zero or Negative Price Removal

Rows removed: ~1,000

Reasoning: Zero or negative prices indicate data entry errors or non-commercial transactions.

Impact: Improved reliability of monetary features.

# Step 5: Missing Description Removal

Rows removed: ~1,400

Reasoning: Product descriptions are important for product-level insights and validation.

Impact: Improved consistency of product-related analysis.

# Step 6: Outlier Removal (IQR Method)

Rows removed: ~50,000

Reasoning: Extremely high quantities or prices distort statistical and ML models.

Impact: Reduced skewness and stabilized feature distributions.

# Step 7: Duplicate Removal

Rows removed: ~3,000

Reasoning: Duplicate transactions inflate frequency and revenue.

Impact: Ensured each transaction is counted only once.

# Step 8: Derived Feature Creation

Columns added:

TotalPrice

Year

Month

DayOfWeek

Hour

Impact: Enabled temporal and revenue-based analysis.

# Step 9: Data Type Conversion

Actions:

CustomerID → integer

StockCode → category

Country → category

Impact: Improved memory efficiency and model performance.

# Data Quality Improvements
Metric	Before	After	Improvement
Missing Values	>135,000	0	100%
Duplicate Rows	~3,000	0	100%
Invalid Prices	~1,000	0	100%
Negative Quantities	~8,000	0	100%
# Challenges Faced
# Challenge 1: High Missing CustomerID Rate

Solution: Removed rows with missing CustomerID

Lesson Learned: Unique identifiers should never be imputed in customer-level modeling.

# Challenge 2: Handling Returns and Cancellations

Solution: Removed cancelled invoices and negative quantities

Lesson Learned: Business context is essential when interpreting transactional data.

# Challenge 3: Extreme Outliers

Solution: Applied IQR-based filtering

Lesson Learned: Statistical outlier detection improves model robustness.

# Final Dataset Characteristics

Rows: 333,234

Columns: 13

Memory usage: Reduced significantly using categorical dtypes

Date range: 2009–12–01 to 2011–12–09

Countries: 38

# Recommendations for Future Improvements

Retain cancellation data as a behavioral feature instead of removing it

Explore advanced outlier handling techniques like winsorization

Integrate customer demographics for richer churn modeling

Implement incremental data validation pipelines