# Model Selection Report

## 1. Models Evaluated

The following models were trained and evaluated using the same prepared dataset and validation split.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Training Time |
|------|---------|-----------|--------|----------|---------|---------------|
| Logistic Regression | 0.70 | 0.51 | 0.48 | 0.49 | 0.706 | ~0.2 sec |
| Decision Tree | 0.66 | 0.48 | 0.61 | 0.54 | 0.668 | ~0.1 sec |
| Random Forest | 0.71 | 0.51 | 0.48 | 0.49 | 0.708 | ~3.5 sec |
| Gradient Boosting (XGBoost) | 0.69 | 0.49 | 0.45 | 0.47 | 0.691 | ~5.2 sec |
| Neural Network (MLP) | 0.70 | 0.50 | 0.49 | 0.49 | 0.70 | ~4.1 sec |

---

## 2. Performance Analysis

### Best Performing Model
**Selected Model:** Random Forest  

### Justification
Random Forest achieved the **highest ROC-AUC score (0.708)** among all evaluated models, indicating the best ability to distinguish between churned and active customers. It also demonstrated stable performance across all metrics with minimal overfitting.

---

## 3. Metric Prioritization

### Most Important Metric: **Recall**

### Business Justification

For churn prediction:
- **False negatives (missed churners)** are more costly than false positives
- Missing a churned customer results in permanent revenue loss
- Contacting an active customer unnecessarily has a much lower cost

**Business reasoning:**
> It is better to target 100 customers unnecessarily than to miss 10 customers who are about to churn.

### Trade-offs

- Higher recall may slightly reduce precision
- Acceptable because retention campaign cost is lower than customer lifetime value

---

## 4. Model Selection Decision

### Selected Model: **Random Forest**

### Reasons:

**Performance**
- Highest ROC-AUC among all models
- Balanced precision and recall

**Interpretability**
- Feature importance is available
- Easier to explain than Neural Networks or Gradient Boosting

**Deployment Complexity**
- Moderate
- Easy integration with existing Python pipelines

**Training Time**
- Reasonable compared to XGBoost and Neural Networks

---

## 5. What I Learned

### Key Takeaways
- Logistic Regression provides a strong baseline but lacks non-linearity
- Decision Trees overfit easily without depth control
- Random Forest balances bias and variance effectively
- Gradient Boosting is powerful but requires careful tuning
- Neural Networks need more data and tuning for tabular problems

### Challenges Faced
- Handling class imbalance
- Preventing overfitting in tree-based models
- Feature scaling issues for Neural Networks

### Solutions
- Used stratified splits
- Controlled tree depth and number of estimators
- Applied StandardScaler for NN and Logistic Regression

---

## 6. Mistakes Made & Corrections

**Mistake:** Initial churn rate was too high  
**Correction:** Adjusted temporal split logic  

**Mistake:** Feature mismatch during deployment  
**Correction:** Stored feature names and reused scaler consistently  

**Mistake:** Overfitting in Decision Tree  
**Correction:** Reduced max_depth and increased min_samples_split  

---

## Final Conclusion

Based on both **technical performance** and **business requirements**, **Random Forest** is the most suitable model for customer churn prediction in this project.
