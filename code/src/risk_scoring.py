# risk_scoring.py
"""
Module for assigning risk scores based on domain logic.
Modify this file to adapt scoring for different datasets or use cases.
"""

def assign_risk_score(df):
    def score(row):
        if row.get("Transaction_Amount", 0) > 5000:
            return "HIGH"
        elif not row.get("Valid_Transaction", True) or not row.get("Valid_Currency", True):
            return "MEDIUM"
        return "LOW"

    df["Risk_Score"] = df.apply(score, axis=1)
    return df
