import pandas as pd
import joblib
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score

print("Loading validation data...")

# Load validation data
X_val = pd.read_csv("data/processed/X_val.csv")
y_val = pd.read_csv("data/processed/y_val.csv").values.ravel()

# Model paths
models = {
    "Logistic Regression": "models/logistic_regression.pkl",
    "Decision Tree": "models/decision_tree.pkl",
    "Random Forest": "models/random_forest.pkl",
    "XGBoost": "models/xgboost.pkl"
}

results = []

print("\nEvaluating models...\n")

# Evaluate each model
for model_name, model_path in models.items():
    model = joblib.load(model_path)

    y_pred = model.predict(X_val)
    y_prob = model.predict_proba(X_val)[:, 1]

    roc_auc = roc_auc_score(y_val, y_prob)
    precision = precision_score(y_val, y_pred)
    recall = recall_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)

    results.append({
        "Model": model_name,
        "ROC_AUC": round(roc_auc, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1_Score": round(f1, 4)
    })

# Create comparison DataFrame
results_df = pd.DataFrame(results).sort_values(by="ROC_AUC", ascending=False)

print("MODEL COMPARISON RESULTS")
print("-" * 50)
print(results_df)
print("-" * 50)

# Identify best model
best_model_name = results_df.iloc[0]["Model"]
print(f"Best model based on ROC-AUC: {best_model_name}")

# Save best model for deployment
best_model_path_map = {
    "Logistic Regression": "models/logistic_regression.pkl",
    "Decision Tree": "models/decision_tree.pkl",
    "Random Forest": "models/random_forest.pkl",
    "XGBoost": "models/xgboost.pkl"
}

best_model_path = best_model_path_map[best_model_name]
best_model = joblib.load(best_model_path)

joblib.dump(best_model, "models/best_model.pkl")

print(f"Best model saved successfully as models/best_model.pkl")
