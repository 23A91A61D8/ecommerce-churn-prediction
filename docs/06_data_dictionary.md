# Data Dictionary
# Raw Dataset

File Name: online_retail.csv
Source: UCI Online Retail II / Kaggle
Time Period: 2009 – 2011

# Column-Level Description
| Column Name | Data Type | Description | Example Values | Missing % | Notes |
|------------|----------|-------------|---------------|-----------|-------|
| InvoiceNo | String | Invoice number; invoices starting with 'C' indicate cancellations | 536365, C536365 | 0% | Unique identifier |
| StockCode | String | Product identifier code | 85123A | 0% | Some non-standard alphanumeric codes exist |
| Description | String | Product name or description | WHITE HANGING HEART T-LIGHT HOLDER | ~0.3% | Clean required |
| Quantity | Integer | Number of units purchased per transaction | 6, -1 | 0% | Negative values indicate returns |
| InvoiceDate | DateTime | Date and time of transaction | 2010-12-01 08:26:00 | 0% | Range: 2009–2011 |
| UnitPrice | Float | Price per unit in GBP (£) | 2.55 | 0% | Some zero values exist |
| CustomerID | Float | Unique customer identifier | 17850.0 | ~25% | High missing rate |
| Country | String | Customer country | United Kingdom | 0% | 38 unique countries |

# Data Quality Issues Identified

Missing CustomerID values (~25%)

Missing Description values (~0.3%)

Cancelled transactions (InvoiceNo starting with 'C')

Negative quantities indicating returns

Zero or negative unit prices

Duplicate transaction records

Extreme quantity and price outliers

# Data Cleaning Required

Remove rows with missing CustomerID

Impute missing Description values with a placeholder

Remove cancelled invoices

Remove transactions with negative quantities

Remove or cap extreme quantity and price outliers using IQR method

Convert InvoiceDate to datetime format

Remove duplicate transaction records