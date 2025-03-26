import pandas as pd
from corporate_loan_rules import validate_country, validate_zip_code, validate_customer_id

def test_validate_country():
    df = pd.DataFrame([{"Country": "US"}, {"Country": "USA"}])
    df = validate_country(df)
    assert df.loc[0, "Country"] == True
    assert df.loc[1, "Country"] == False

def test_validate_zip_code():
    df = pd.DataFrame([{"Zip_Code": "12345"}, {"Zip_Code": "123"}])
    df = validate_zip_code(df)
    assert df.loc[0, "Zip_Code"] == True
    assert df.loc[1, "Zip_Code"] == False

def test_validate_customer_id():
    df = pd.DataFrame([{"Customer_ID": "ABC123"}, {"Customer_ID": "A,BC"}])
    df = validate_customer_id(df)
    assert df.loc[0, "Customer_ID"] == True
    assert df.loc[1, "Customer_ID"] == False