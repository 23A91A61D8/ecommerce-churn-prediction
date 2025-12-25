import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import json
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
DATA_PATH = Path("data/processed/customer_features.csv")
OUTPUT_DIR = Path("data/processed")
MODEL_DIR = Path("models")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Load data
# -----------------------------
print("Loading customer features...")
df = pd.read_csv(DATA_PATH)

# -----------------------------
# 2. Separate target
# -----------------------------
y = df["Churn"]
X = df.drop(columns=["Churn"])

# -----------------------------
# 3. Remove CustomerID
# -----------------------------
if "CustomerID" in X.columns:
    X = X.drop(columns=["CustomerID"])

# -----------------------------
# 4. Drop Country (not recommended)
# -----------------------------
if "Country" in X.columns:
    X = X.drop(columns=["Country"])

# -----------------------------
# 5. One-Hot Encode CustomerSegment
# -----------------------------
if "CustomerSegment" in X.columns:
    X = pd.get_dummies(X, columns=["CustomerSegment"], drop_first=False)

# -----------------------------
# 6. Identify numerical columns
# -----------------------------
numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()

# -----------------------------
# 7. Train / Validation / Test Split (70 / 15 / 15)
# -----------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.30,
    stratify=y,
    random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.50,
    stratify=y_temp,
    random_state=42
)

# -----------------------------
# 8. Scale numerical features only
# -----------------------------
scaler = StandardScaler()

X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_val[numeric_cols] = scaler.transform(X_val[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

# -----------------------------
# 9. Save prepared datasets
# -----------------------------
X_train.to_csv(OUTPUT_DIR / "X_train.csv", index=False)
X_val.to_csv(OUTPUT_DIR / "X_val.csv", index=False)
X_test.to_csv(OUTPUT_DIR / "X_test.csv", index=False)

y_train.to_csv(OUTPUT_DIR / "y_train.csv", index=False)
y_val.to_csv(OUTPUT_DIR / "y_val.csv", index=False)
y_test.to_csv(OUTPUT_DIR / "y_test.csv", index=False)

# -----------------------------
# 10. Save scaler
# -----------------------------
joblib.dump(scaler, MODEL_DIR / "scaler.pkl")

# -----------------------------
# 11. Save feature names
# -----------------------------
with open(OUTPUT_DIR / "feature_names.json", "w") as f:
    json.dump(list(X.columns), f, indent=4)

# -----------------------------
# 12. Print summary
# -----------------------------
print("\nDATA PREPARATION SUMMARY")
print("-" * 50)
print(f"Original features (before encoding): {df.shape[1] - 2}")
print(f"Features after encoding: {X.shape[1]}")
print(f"Training samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")
print(f"Test samples: {len(X_test)}")
print(f"Churn rate in train: {y_train.mean() * 100:.2f}%")
print(f"Churn rate in test: {y_test.mean() * 100:.2f}%")
print("-" * 50)

print("Model preparation completed successfully!")
