# Feature Dictionary

## Target Variable

| Feature | Type | Description | Example | Business Meaning |
|------|------|------------|---------|------------------|
| Churn | Binary | 1 = Churned, 0 = Active | 1 | Customer did not purchase in the next 3 months |

---

## RFM Features

| Feature | Type | Description | Range | Business Meaning |
|------|------|------------|-------|------------------|
| Recency | Integer | Days since last purchase | 0–600 | Lower value means more recently active |
| Frequency | Integer | Number of unique purchases | 1–200+ | Higher means more loyal |
| TotalSpent | Float | Total amount spent (£) | 0–50000+ | Customer lifetime value |
| AvgOrderValue | Float | Average spend per order (£) | 0–5000 | Indicates spending behavior |
| TotalItems | Integer | Total items purchased | 1–5000 | Measures purchase volume |
| UniqueProducts | Integer | Number of distinct products bought | 1–1000 | Shows product diversity |

---

## Temporal Features

| Feature | Type | Description | Range | Business Meaning |
|------|------|------------|-------|------------------|
| CustomerLifetimeDays | Integer | Days between first and last purchase | 0–700 | Length of customer relationship |
| Purchases_Last30Days | Integer | Purchases in last 30 days | 0–50 | Recent engagement |
| Purchases_Last60Days | Integer | Purchases in last 60 days | 0–100 | Medium-term activity |
| Purchases_Last90Days | Integer | Purchases in last 90 days | 0–150 | Churn risk indicator |
| OrdersPerDay | Float | Frequency normalized by lifetime | 0–5 | Purchase velocity |
| RevenuePerDay | Float | Spend normalized by lifetime | 0–1000 | Revenue contribution rate |

---

## Behavioral & Derived Features

| Feature | Type | Description | Range | Business Meaning |
|------|------|------------|-------|------------------|
| AvgItemsPerOrder | Float | Items bought per order | 0–100 | Basket size indicator |
| AvgRevenuePerItem | Float | Spend per item (£) | 0–500 | Price sensitivity |
| ProductsPerOrder | Float | Product variety per order | 0–50 | Shopping diversity |
| ItemsPerProduct | Float | Average quantity per product | 0–100 | Bulk buying behavior |
| ProductDiversityRatio | Float | Unique products / total items | 0–1 | Preference variety |
| SpendPerOrder | Float | Spend per transaction (£) | 0–5000 | Order value consistency |
| SpendPerProduct | Float | Spend per product (£) | 0–5000 | Product-level value |
| FrequencyToLifetimeRatio | Float | Frequency normalized by lifetime | 0–2 | Engagement intensity |
| ItemsPerDay | Float | Items purchased per day | 0–50 | Consumption rate |
| RecencyToLifetimeRatio | Float | Recency normalized by lifetime | 0–1 | Inactivity proportion |
| Recent30to60Ratio | Float | Short-term engagement ratio | 0–5 | Engagement decay |
| Recent60to90Ratio | Float | Medium-term engagement ratio | 0–5 | Churn trend indicator |

---

## Feature Engineering Decisions

These features were selected to capture customer value, engagement, loyalty, and churn risk.  
RFM features summarize overall customer value.  
Temporal features capture activity trends over time.  
Derived ratios normalize behavior across customers with different lifetimes.

---

## Feature Interactions

- High **Recency** + Low **Purchases_Last30Days** → High churn probability  
- High **Frequency** + High **TotalSpent** → Loyal customers  
- Declining **Recent30to60Ratio** → Early churn signal  

---

## Feature Importance Hypothesis

-- Based on business understanding, the most important predictors of churn are:

1. Recency  
2. Purchases_Last30Days  
3. Frequency  
4. TotalSpent  
5. CustomerLifetimeDays  
6. RevenuePerDay  

-- These features directly reflect customer engagement and inactivity patterns.
