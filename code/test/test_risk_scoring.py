import pandas as pd
from risk_scoring import assign_risk_score

def test_high_risk():
    df = pd.DataFrame([{"Transaction_Amount": 6000, "Valid_Transaction": True, "Valid_Currency": True}])
    result = assign_risk_score(df)
    assert result.loc[0, "Risk_Score"] == "HIGH"

def test_medium_risk_invalid_transaction():
    df = pd.DataFrame([{"Transaction_Amount": 100, "Valid_Transaction": False, "Valid_Currency": True}])
    result = assign_risk_score(df)
    assert result.loc[0, "Risk_Score"] == "MEDIUM"

def test_low_risk():
    df = pd.DataFrame([{"Transaction_Amount": 100, "Valid_Transaction": True, "Valid_Currency": True}])
    result = assign_risk_score(df)
    assert result.loc[0, "Risk_Score"] == "LOW"