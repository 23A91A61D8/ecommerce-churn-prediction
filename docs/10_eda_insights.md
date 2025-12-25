# EDA Key Insights

## 1. Churn Patterns Discovered

1. Recency is the strongest churn predictor  
2. Churned customers show very low recent activity  
3. High-frequency customers churn less  
4. High-spending customers are more loyal  
5. Customers inactive for 60+ days have high churn risk  
6. Purchase velocity drops sharply before churn  
7. Recent 30-day purchases strongly reduce churn  
8. Long lifetime customers churn less  
9. Low product diversity increases churn  
10. Engagement decay patterns visible in churned users  

## 2. Customer Segment Analysis

- Active customers dominate high-frequency segments  
- Churned customers cluster in low-activity groups  
- Spending-based segments clearly separate churn behavior  

## 3. Feature Recommendations for Modeling

Recommended features:
- Recency  
- Frequency  
- Purchases_Last30Days  
- TotalSpent  
- OrdersPerDay  
- CustomerLifetimeDays  

## 4. Hypotheses for Testing

H1: Customers with recency > 90 days are 5x more likely to churn  
H2: Customers with >10 purchases rarely churn  
H3: Recent engagement reduces churn probability significantly  
