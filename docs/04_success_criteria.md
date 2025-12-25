# Success Criteria Matrix

The success of the customer churn prediction system is evaluated using clearly defined performance thresholds. Each metric is measured across three levels to ensure minimum viability, target performance, and stretch (excellent) performance.

Criteria	 Minimum	Target	 Stretch
ROC-AUC	      0.75	     0.80	  0.85
Precision	  0.70	     0.75	  0.80
Recall	      0.65	     0.70	  0.75
# Explanation of Metrics

ROC-AUC
Measures the model’s ability to distinguish between churned and active customers across all classification thresholds.

Precision
Ensures that customers predicted as churners are truly at risk, minimizing unnecessary retention costs.

Recall
Ensures that most actual churners are correctly identified, supporting proactive retention strategies.