import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

print("Loading data for XGBoost...")

X_train = pd.read_csv("data/processed/X_train.csv")
X_val = pd.read_csv("data/processed/X_val.csv")

y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
y_val = pd.read_csv("data/processed/y_val.csv").values.ravel()

model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

model.fit(X_train, y_train)

val_probs = model.predict_proba(X_val)[:, 1]
roc_auc = roc_auc_score(y_val, val_probs)

print(f"XGBoost ROC-AUC: {roc_auc:.4f}")

joblib.dump(model, "models/xgboost.pkl")
print("XGBoost model saved")
