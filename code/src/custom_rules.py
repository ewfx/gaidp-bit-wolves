# custom_rules.py
"""
Reusable validation rule functions for custom profiling.
Add or remove rules based on the dataset for the hackathon.
"""
import re
from datetime import datetime
import pandas as pd

def validate_transaction_amount(df):
    df["Valid_Transaction"] = (df["Transaction_Amount"] - df["Reported_Amount"]).abs() <= (df["Transaction_Amount"] * 0.01)
    return df

def validate_currency_format(df):
    df["Valid_Currency"] = df["Currency"].astype(str).apply(lambda x: bool(re.match(r"^[A-Z]{3}$", x)))
    return df

def validate_transaction_date(df):
    today = datetime.today().strftime('%Y-%m-%d')
    df["Valid_Transaction_Date"] = pd.to_datetime(df["Transaction_Date"], errors='coerce') <= pd.to_datetime(today)
    return df

def apply_custom_rules(df):
    # Example: apply one or more validations from corporate_loan_rules.py
    df = ""

    return df

# Register the rules to apply them dynamically
CUSTOM_RULES = [
    validate_transaction_amount,
    validate_currency_format,
    validate_transaction_date,
]
