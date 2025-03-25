# remediation.py
"""
Module to generate remediation messages based on validation failures and risk score.
Can be adapted for more advanced recommendation engines or compliance workflows.
"""

def suggest_remediation(df):
    def get_remedy(row):
        if not row.get("Valid_Currency", True):
            return "Fix currency format to ISO 4217."
        elif not row.get("Valid_Transaction", True):
            return "Adjust Transaction_Amount to match Reported_Amount."
        elif not row.get("Valid_Transaction_Date", True):
            return "Correct the Transaction_Date (can't be in future)."
        elif row.get("Risk_Score") == "HIGH":
            return "Manual audit required due to high amount."
        return "No action needed."

    df["Remediation"] = df.apply(get_remedy, axis=1)
    return df
