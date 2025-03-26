import pandas as pd
from remediation import suggest_remediation

def test_remediation_currency():
    df = pd.DataFrame([{"Valid_Currency": False, "Valid_Transaction": True, "Valid_Transaction_Date": True, "Risk_Score": "LOW"}])
    df = suggest_remediation(df)
    assert "Fix currency format" in df.loc[0, "Remediation"]

def test_remediation_high_risk():
    df = pd.DataFrame([{"Valid_Currency": True, "Valid_Transaction": True, "Valid_Transaction_Date": True, "Risk_Score": "HIGH"}])
    df = suggest_remediation(df)
    assert "Manual audit required" in df.loc[0, "Remediation"]