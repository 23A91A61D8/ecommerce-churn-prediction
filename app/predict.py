import pandas as pd
import joblib
import numpy as np
import json

# --------------------------------------------------
# Paths
# --------------------------------------------------
MODEL_PATH = "models/best_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURE_NAMES_PATH = "data/processed/feature_names.json"

# --------------------------------------------------
# Load artifacts
# --------------------------------------------------
def load_model():
    return joblib.load(MODEL_PATH)

def load_scaler():
    return joblib.load(SCALER_PATH)

def load_feature_names():
    with open(FEATURE_NAMES_PATH, "r") as f:
        return json.load(f)   # ✅ feature_names.json is a LIST

# Load once (cached in memory)
model = load_model()
scaler = load_scaler()
FEATURE_NAMES = load_feature_names()

# --------------------------------------------------
# Preprocess input
# --------------------------------------------------
def preprocess_input(input_df: pd.DataFrame):
    """
    Align input features exactly with training features
    """

    # Create full feature dataframe with zeros
    full_df = pd.DataFrame(
        np.zeros((1, len(FEATURE_NAMES))),
        columns=FEATURE_NAMES
    )

    # Fill provided values
    for col in input_df.columns:
        if col in full_df.columns:
            full_df[col] = input_df[col].values[0]

    # Scale using trained scaler
    full_df_scaled = scaler.transform(full_df)

    return full_df_scaled

# --------------------------------------------------
# Prediction functions
# --------------------------------------------------
def predict(input_df: pd.DataFrame):
    X = preprocess_input(input_df)
    return int(model.predict(X)[0])

def predict_proba(input_df: pd.DataFrame):
    X = preprocess_input(input_df)
    return float(model.predict_proba(X)[0][1])
