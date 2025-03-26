import pandas as pd
import genai_data_profiling as gp

def test_module_imports():
    assert hasattr(gp, 'CORPORATE_LOAN_RULES')
    assert hasattr(gp, 'apply_custom_rules')

def test_rules_and_custom_apply():
    df = pd.DataFrame({
        "Transaction_Amount": [100],
        "Reported_Amount": [100],
        "Currency": ["USD"],
        "Transaction_Date": ["2020-01-01"]
    })
    # Apply corporate loan rules
    for rule in gp.CORPORATE_LOAN_RULES[:5]:  # test a subset to avoid requiring full dataset columns
        df = rule(df)
    df = gp.apply_custom_rules(df)
    assert "Valid_Transaction" in df.columns
    assert "Valid_Currency" in df.columns
    assert "Valid_Transaction_Date" in df.columns