import pandas as pd
import numpy as np
from datetime import datetime
import json
import logging
import os

# -----------------------------
# Logging setup
# -----------------------------
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/data_cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DataCleaner:
    """
    Comprehensive data cleaning pipeline for Online Retail dataset
    """

    def __init__(self, input_path="data/raw/online_retail.csv"):
        self.input_path = input_path
        self.df = None
        self.cleaning_stats = {
            "original_rows": 0,
            "rows_after_cleaning": 0,
            "rows_removed": 0,
            "missing_values_before": {},
            "missing_values_after": {},
            "steps_applied": []
        }

    # -----------------------------
    # Step 1: Load data
    # -----------------------------
    def load_data(self):
        logging.info("Loading raw dataset")

        self.df = pd.read_csv(
            self.input_path,
            encoding="latin1",
            parse_dates=["InvoiceDate"]
        )

        self.cleaning_stats["original_rows"] = len(self.df)
        self.cleaning_stats["missing_values_before"] = self.df.isnull().sum().to_dict()

        logging.info(f"Loaded dataset with {len(self.df)} rows")
        return self

    # -----------------------------
    # Step 2: Remove missing CustomerID
    # -----------------------------
    def remove_missing_customer_ids(self):
        logging.info("Removing missing CustomerIDs")

        initial_rows = len(self.df)
        self.df = self.df.dropna(subset=["CustomerID"])
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "remove_missing_customer_ids",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 3: Remove cancelled invoices
    # -----------------------------
    def handle_cancelled_invoices(self):
        logging.info("Removing cancelled invoices")

        initial_rows = len(self.df)
        self.df = self.df[~self.df["InvoiceNo"].astype(str).str.startswith("C")]
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "handle_cancelled_invoices",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 4: Remove negative quantities
    # -----------------------------
    def handle_negative_quantities(self):
        logging.info("Removing negative quantities")

        initial_rows = len(self.df)
        self.df = self.df[self.df["Quantity"] > 0]
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "handle_negative_quantities",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 5: Remove zero / negative prices
    # -----------------------------
    def handle_zero_prices(self):
        logging.info("Removing zero or negative prices")

        initial_rows = len(self.df)
        self.df = self.df[self.df["UnitPrice"] > 0]
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "handle_zero_prices",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 6: Remove missing descriptions
    # -----------------------------
    def handle_missing_descriptions(self):
        logging.info("Removing missing descriptions")

        initial_rows = len(self.df)
        self.df = self.df.dropna(subset=["Description"])
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "handle_missing_descriptions",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 7: Remove outliers using IQR
    # -----------------------------
    def remove_outliers(self):
        logging.info("Removing outliers using IQR")

        initial_rows = len(self.df)

        # Quantity IQR
        Q1_q = self.df["Quantity"].quantile(0.25)
        Q3_q = self.df["Quantity"].quantile(0.75)
        IQR_q = Q3_q - Q1_q

        self.df = self.df[
            (self.df["Quantity"] >= Q1_q - 1.5 * IQR_q) &
            (self.df["Quantity"] <= Q3_q + 1.5 * IQR_q)
        ]

        # UnitPrice IQR
        Q1_p = self.df["UnitPrice"].quantile(0.25)
        Q3_p = self.df["UnitPrice"].quantile(0.75)
        IQR_p = Q3_p - Q1_p

        self.df = self.df[
            (self.df["UnitPrice"] >= Q1_p - 1.5 * IQR_p) &
            (self.df["UnitPrice"] <= Q3_p + 1.5 * IQR_p)
        ]

        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "remove_outliers",
            "rows_removed": rows_removed,
            "method": "IQR",
            "threshold": 1.5
        })

        return self

    # -----------------------------
    # Step 8: Remove duplicates
    # -----------------------------
    def remove_duplicates(self):
        logging.info("Removing duplicate rows")

        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates()
        rows_removed = initial_rows - len(self.df)

        self.cleaning_stats["steps_applied"].append({
            "step": "remove_duplicates",
            "rows_removed": rows_removed
        })

        return self

    # -----------------------------
    # Step 9: Add derived columns
    # -----------------------------
    def add_derived_columns(self):
        logging.info("Adding derived columns")

        self.df["TotalPrice"] = self.df["Quantity"] * self.df["UnitPrice"]
        self.df["Year"] = self.df["InvoiceDate"].dt.year
        self.df["Month"] = self.df["InvoiceDate"].dt.month
        self.df["DayOfWeek"] = self.df["InvoiceDate"].dt.dayofweek
        self.df["Hour"] = self.df["InvoiceDate"].dt.hour

        self.cleaning_stats["steps_applied"].append({
            "step": "add_derived_columns",
            "columns_added": ["TotalPrice", "Year", "Month", "DayOfWeek", "Hour"]
        })

        return self

    # -----------------------------
    # Step 10: Convert data types
    # -----------------------------
    def convert_data_types(self):
        logging.info("Converting data types")

        self.df["CustomerID"] = self.df["CustomerID"].astype(int)
        self.df["StockCode"] = self.df["StockCode"].astype("category")
        self.df["Country"] = self.df["Country"].astype("category")

        self.cleaning_stats["steps_applied"].append({
            "step": "convert_data_types"
        })

        return self

    # -----------------------------
    # Step 11: Save cleaned data & stats
    # -----------------------------
    def save_cleaned_data(self):
        os.makedirs("data/processed", exist_ok=True)

        self.df.to_csv("data/processed/cleaned_transactions.csv", index=False)

        self.cleaning_stats["rows_after_cleaning"] = len(self.df)
        self.cleaning_stats["rows_removed"] = (
            self.cleaning_stats["original_rows"] -
            self.cleaning_stats["rows_after_cleaning"]
        )
        self.cleaning_stats["missing_values_after"] = self.df.isnull().sum().to_dict()

        with open("data/processed/cleaning_statistics.json", "w") as f:
            json.dump(self.cleaning_stats, f, indent=4, default=str)

        print("\nDATA CLEANING SUMMARY")
        print("-" * 40)
        print(f"Original rows: {self.cleaning_stats['original_rows']:,}")
        print(f"Cleaned rows: {self.cleaning_stats['rows_after_cleaning']:,}")
        print(f"Retention rate: {(self.cleaning_stats['rows_after_cleaning'] / self.cleaning_stats['original_rows'] * 100):.2f}%")

        return self

    # -----------------------------
    # Run full pipeline
    # -----------------------------
    def run_pipeline(self):
        print("Starting data cleaning pipeline...")

        self.load_data() \
            .remove_missing_customer_ids() \
            .handle_cancelled_invoices() \
            .handle_negative_quantities() \
            .handle_zero_prices() \
            .handle_missing_descriptions() \
            .remove_outliers() \
            .remove_duplicates() \
            .add_derived_columns() \
            .convert_data_types() \
            .save_cleaned_data()

        print("Data cleaning pipeline completed successfully!")
        return self.df


# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    cleaner = DataCleaner("data/raw/online_retail.csv")
    cleaned_df = cleaner.run_pipeline()
    print(f"\nFinal dataset shape: {cleaned_df.shape}")
