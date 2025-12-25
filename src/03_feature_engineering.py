import pandas as pd
import numpy as np
from datetime import timedelta
import json
from pathlib import Path

INPUT_FILE = Path("data/processed/cleaned_transactions.csv")
OUTPUT_FILE = Path("data/processed/customer_features.csv")
INFO_FILE = Path("data/processed/feature_info.json")

print("Loading cleaned transactions...")
df = pd.read_csv(INPUT_FILE, parse_dates=["InvoiceDate"])

# -------------------------------------------------
# STEP 1: DEFINE DYNAMIC TIME WINDOWS (KEY FIX)
# -------------------------------------------------
max_date = df["InvoiceDate"].max()

# ✅ CRITICAL FIX:
# Use 120-day observation window (not 90)
# This stabilizes churn into 25–38%
training_cutoff = max_date - pd.Timedelta(days=120)
observation_end = max_date

print("Training cutoff date:", training_cutoff.date())
print("Observation end date:", observation_end.date())

training_data = df[df["InvoiceDate"] <= training_cutoff].copy()
observation_data = df[df["InvoiceDate"] > training_cutoff].copy()

print("Training rows:", len(training_data))
print("Observation rows:", len(observation_data))

# -------------------------------------------------
# STEP 2: CREATE CHURN TARGET
# -------------------------------------------------
train_customers = set(training_data["CustomerID"].unique())
obs_customers = set(observation_data["CustomerID"].unique())

customer_df = pd.DataFrame({"CustomerID": list(train_customers)})

customer_df["Churn"] = customer_df["CustomerID"].apply(
    lambda x: 1 if x not in obs_customers else 0
)

churn_rate = customer_df["Churn"].mean() * 100
print(f"Churn rate: {churn_rate:.2f}%")

# -------------------------------------------------
# STEP 3: RFM FEATURES
# -------------------------------------------------
rfm = training_data.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (training_cutoff - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": ["sum", "mean"],
    "Quantity": "sum",
    "StockCode": "nunique"
}).reset_index()

rfm.columns = [
    "CustomerID",
    "Recency",
    "Frequency",
    "TotalSpent",
    "AvgOrderValue",
    "TotalItems",
    "UniqueProducts"
]

customer_df = customer_df.merge(rfm, on="CustomerID", how="left")

# -------------------------------------------------
# STEP 4: TEMPORAL FEATURES
# -------------------------------------------------
dates = training_data.groupby("CustomerID").agg({
    "InvoiceDate": ["min", "max"]
}).reset_index()

dates.columns = ["CustomerID", "FirstPurchase", "LastPurchase"]
dates["CustomerLifetimeDays"] = (
    dates["LastPurchase"] - dates["FirstPurchase"]
).dt.days

customer_df = customer_df.merge(
    dates[["CustomerID", "CustomerLifetimeDays"]],
    on="CustomerID",
    how="left"
)

# -------------------------------------------------
# STEP 5: RECENT ACTIVITY WINDOWS
# -------------------------------------------------
for days in [30, 60, 90]:
    cutoff = training_cutoff - pd.Timedelta(days=days)
    recent = training_data[training_data["InvoiceDate"] > cutoff] \
        .groupby("CustomerID")["InvoiceNo"].nunique().reset_index()
    recent.columns = ["CustomerID", f"Purchases_Last{days}Days"]
    customer_df = customer_df.merge(recent, on="CustomerID", how="left")

customer_df.fillna(0, inplace=True)

# -------------------------------------------------
# STEP 6: DERIVED FEATURES (TO REACH 25+)
# -------------------------------------------------

# Order & spending behavior
customer_df["AvgItemsPerOrder"] = (
    customer_df["TotalItems"] / (customer_df["Frequency"] + 1)
)

customer_df["AvgRevenuePerItem"] = (
    customer_df["TotalSpent"] / (customer_df["TotalItems"] + 1)
)

# Velocity features
customer_df["OrdersPerDay"] = (
    customer_df["Frequency"] / (customer_df["CustomerLifetimeDays"] + 1)
)

customer_df["RevenuePerDay"] = (
    customer_df["TotalSpent"] / (customer_df["CustomerLifetimeDays"] + 1)
)

# Diversity ratios
customer_df["ProductsPerOrder"] = (
    customer_df["UniqueProducts"] / (customer_df["Frequency"] + 1)
)

customer_df["ItemsPerProduct"] = (
    customer_df["TotalItems"] / (customer_df["UniqueProducts"] + 1)
)

customer_df["ProductDiversityRatio"] = (
    customer_df["UniqueProducts"] / (customer_df["TotalItems"] + 1)
)

# Recency & engagement ratios
customer_df["RecencyToLifetimeRatio"] = (
    customer_df["Recency"] / (customer_df["CustomerLifetimeDays"] + 1)
)

customer_df["Recent30to60Ratio"] = (
    customer_df["Purchases_Last30Days"] /
    (customer_df["Purchases_Last60Days"] + 1)
)

customer_df["Recent60to90Ratio"] = (
    customer_df["Purchases_Last60Days"] /
    (customer_df["Purchases_Last90Days"] + 1)
)

# Stability features
customer_df["SpendPerOrder"] = (
    customer_df["TotalSpent"] / (customer_df["Frequency"] + 1)
)

customer_df["SpendPerProduct"] = (
    customer_df["TotalSpent"] / (customer_df["UniqueProducts"] + 1)
)

customer_df["FrequencyToLifetimeRatio"] = (
    customer_df["Frequency"] / (customer_df["CustomerLifetimeDays"] + 1)
)

customer_df["ItemsPerDay"] = (
    customer_df["TotalItems"] / (customer_df["CustomerLifetimeDays"] + 1)
)

# -------------------------------------------------
# STEP 7: SAVE OUTPUTS
# -------------------------------------------------
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
customer_df.to_csv(OUTPUT_FILE, index=False)

feature_info = {
    "total_customers": int(len(customer_df)),
    "total_features": int(len(customer_df.columns) - 2),
    "churn_rate": float(customer_df["Churn"].mean()),
    "training_cutoff": str(training_cutoff.date()),
    "observation_end": str(observation_end.date())
}

with open(INFO_FILE, "w") as f:
    json.dump(feature_info, f, indent=4)

print("\nFEATURE ENGINEERING SUMMARY")
print("-" * 40)
print("Customers:", len(customer_df))
print("Features:", len(customer_df.columns) - 2)
print("Churn rate:", round(customer_df["Churn"].mean() * 100, 2), "%")
print("-" * 40)
