# Business Impact Analysis
# 1. Model Performance in Business Terms
  # Confusion Matrix Interpretation

Based on the test set of 463 customers:

True Positives (TP): 145
→ Customers correctly identified as churners

False Positives (FP): 95
→ Active customers incorrectly flagged as churners

True Negatives (TN): 173
→ Customers correctly identified as active

False Negatives (FN): 50
→ Actual churners missed by the model

These values are taken directly from the test set confusion matrix.

# 2. Business Cost Analysis
# Assumptions

Cost of retention campaign per customer: £10

Average customer lifetime value (CLV): £500

Overall churn rate: 38%

# Scenario 1: Without Model (Random Targeting)

Customers contacted randomly: 463

Cost of campaign:
463 × £10 = £4,630

Expected churners caught (38%):
176 customers

Revenue protected:
176 × £500 = £88,000

ROI:

£
88
,
000
−
£
4
,
630
£
4
,
630
=
18.0
×
£4,630
£88,000−£4,630
	​

=18.0×
# Scenario 2: With Model (Targeted Retention)

Customers contacted: TP + FP = 240

Campaign cost:
240 × £10 = £2,400

Churners successfully retained: 145

Churners missed: 50

Revenue protected:
145 × £500 = £72,500

ROI:

£
72
,
500
−
£
2
,
400
£
2
,
400
=
29.2
×
£2,400
£72,500−£2,400
	​

=29.2×
# 3. Expected Business Outcomes

Churn reduction: from 38% → ~26%

Monthly cost savings:
£4,630 − £2,400 = £2,230

Revenue protected per month:
£72,500

Efficiency gain:
Contact 48% fewer customers while retaining 82% of churners

# 4. Implementation Recommendations
 # Who to Target

Customers with churn probability ≥ 0.60

Prioritize high TotalSpent + high Frequency customers

Use RFM segments:

At Risk

Potential

Loyal (recent drop in activity)

# Retention Strategies by Segment

At Risk:
Personalized discounts, urgency emails

Potential:
Loyalty rewards, product recommendations

Champions:
VIP offers, early access

# 5. Model Limitations
Known Issues

Lower recall for customers with sudden behavior changes

Seasonal buying patterns not fully captured

Depends heavily on recent activity features

# Recommended Actions

Retrain model every 3 months

Monitor churn probability drift

Add marketing interaction data in future versions