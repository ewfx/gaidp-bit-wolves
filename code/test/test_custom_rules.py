import pandas as pd
from custom_rules import validate_transaction_amount, validate_currency_format, validate_transaction_date

def test_validate_transaction_amount():
    df = pd.DataFrame([{"Transaction_Amount": 100, "Reported_Amount": 101}])
    df = validate_transaction_amount(df)
    assert df.loc[0, "Valid_Transaction"] == True

def test_validate_currency_format():
    df = pd.DataFrame([{"Currency": "USD"}, {"Currency": "us"}])
    df = validate_currency_format(df)
    assert df.loc[0, "Valid_Currency"] == True
    assert df.loc[1, "Valid_Currency"] == False

def test_validate_transaction_date():
    df = pd.DataFrame([{"Transaction_Date": "2100-01-01"}])
    df = validate_transaction_date(df)
    assert df.loc[0, "Valid_Transaction_Date"] == False