import pandas as pd
import os
from datetime import datetime

RAW_DATA_PATH = "data/raw/online_retail.csv"
PROFILE_PATH = "data/raw/data_profile.txt"


def download_dataset():
    """
    Download the Online Retail dataset and save to data/raw/online_retail.csv

    Dataset Source:
    Kaggle E-Commerce Data (UCI Online Retail II mirror)
    https://www.kaggle.com/datasets/carrie1/ecommerce-data
    """

    print("Starting dataset acquisition...")

    # Ensure directory exists
    os.makedirs("data/raw", exist_ok=True)

    # NOTE:
    # Kaggle does not allow direct download via URL without authentication.
    # So we assume the user has manually downloaded the dataset
    # and placed it in data/raw/ as data.csv

    source_file = "data/raw/data.csv"

    if not os.path.exists(source_file):
        raise FileNotFoundError(
            "Dataset not found.\n"
            "Please download from Kaggle and place as data/raw/data.csv"
        )

    # Load CSV and save standardized filename
    df = pd.read_csv(source_file, encoding="latin1")

    df.to_csv(RAW_DATA_PATH, index=False)

    print(f"Dataset downloaded and standardized at: {RAW_DATA_PATH}")
    print(f"Download completed at: {datetime.now()}")

    return True


def load_raw_data():
    """
    Load the raw dataset and return DataFrame

    Returns:
        pd.DataFrame: Raw dataset
    """
    print("Loading raw dataset...")

    df = pd.read_csv(RAW_DATA_PATH, encoding="latin1")

    print(f"Loaded dataset shape: {df.shape}")
    return df


def generate_data_profile(df):
    """
    Generate initial data profile and save to data/raw/data_profile.txt

    Includes:
    - Number of rows and columns
    - Column names and data types
    - Memory usage
    - Sample preview
    """

    print("Generating data profile...")

    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        f.write("DATA PROFILE REPORT\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"Generated on: {datetime.now()}\n\n")

        f.write(f"Total Rows: {df.shape[0]}\n")
        f.write(f"Total Columns: {df.shape[1]}\n\n")

        f.write("Column Names and Data Types:\n")
        f.write("-" * 40 + "\n")
        f.write(df.dtypes.to_string())
        f.write("\n\n")

        f.write("Memory Usage:\n")
        f.write("-" * 40 + "\n")
        memory_usage = df.memory_usage(deep=True).sum() / (1024 ** 2)
        f.write(f"{memory_usage:.2f} MB\n\n")

        f.write("First 5 Rows Preview:\n")
        f.write("-" * 40 + "\n")
        f.write(df.head().to_string())

    print(f"Data profile saved to: {PROFILE_PATH}")


if __name__ == "__main__":
    download_dataset()
    df = load_raw_data()
    generate_data_profile(df)
