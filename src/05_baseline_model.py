import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

print("Loading prepared data...")

X_train = pd.read_csv("data/processed/X_train.csv")
X_val = pd.read_csv("data/processed/X_val.csv")

y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
y_val = pd.read_csv("data/processed/y_val.csv").values.ravel()

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

val_probs = model.predict_proba(X_val)[:, 1]
roc_auc = roc_auc_score(y_val, val_probs)

print(f"Validation ROC-AUC: {roc_auc:.4f}")

joblib.dump(model, "models/logistic_regression.pkl")
print("Baseline model saved")
