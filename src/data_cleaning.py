import pandas as pd
import os

# This script loads raw sales data, cleans column names, handles missing values, removes invalid rows, and saves the clean data to a new CSV file.

def load_data(file_path: str) -> pd.DataFrame:
    """Load raw sales data from a CSV file"""
    # Load the CSV file into a pandas DataFrame
    # Need a dataframe to perform data manipulation operations
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names by stripping whitespace and converting to lowercase"""
    # Convert column names to lowercase and strip whitespace
    # Consistent naming (snake_case) makes attributes easier to access in code
    df.columns = df.columns.str.strip().str.lower()
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handles missing values in critical columns"""
    # Fill missing 'qty' with 0 and drop rows where 'price' is missing
    # Cannot calculate revenue without price, but missing quantity might imply zero sales
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = df['qty'].fillna(0)
    df = df.dropna(subset=['price'])
    return df

def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with invalid data"""
    # Remove rows where 'qty' or 'price' are negative
    # Negative values for these fields do not make sense in a sales context
    
    # This checks that BOTH qty and price are greater than or equal to 0
    df = df[(df['qty'] >= 0) & (df['price'] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)           # Step 1
    df_clean = handle_missing_values(df_clean)      # Step 2
    df_clean = remove_invalid_rows(df_clean)        # Step 3
    # This strips whitespace from the specific columns
    df_clean['prodname'] = df_clean['prodname'].astype(str).str.replace('"', '').str.strip().str.title()
    df_clean['category'] = df_clean['category'].astype(str).str.replace('"', '').str.strip().str.title()
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())