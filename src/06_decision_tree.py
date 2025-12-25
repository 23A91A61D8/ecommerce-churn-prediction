import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

print("Loading data for Decision Tree...")

X_train = pd.read_csv("data/processed/X_train.csv")
X_val = pd.read_csv("data/processed/X_val.csv")

y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
y_val = pd.read_csv("data/processed/y_val.csv").values.ravel()

model = DecisionTreeClassifier(
    max_depth=6,
    min_samples_split=20,
    random_state=42
)

model.fit(X_train, y_train)

val_probs = model.predict_proba(X_val)[:, 1]
roc_auc = roc_auc_score(y_val, val_probs)

print(f"Decision Tree ROC-AUC: {roc_auc:.4f}")

joblib.dump(model, "models/decision_tree.pkl")
print("Decision Tree model saved")
