# corporate_loan_rules.py
"""
Validation functions for Corporate Loan Data fields (based on FR Y-14Q).
Each function applies field-specific business rules, regex validations, type checks,
and allowable values using MDRM documentation.
"""
import pandas as pd
import re
from datetime import datetime

CORPORATE_LOAN_RULES = []

# ────────────────────────────────────────────────────────────────────────────────
# Field 1: Customer ID
# MDRM Code: CLCOM047
# Description: Must be unique; no carriage return, line feed, comma, or unprintable characters
# ────────────────────────────────────────────────────────────────────────────────
def validate_customer_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Customer_ID'] = df['Customer_ID'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 2: Internal ID
# MDRM Code: CLCOM300
# ────────────────────────────────────────────────────────────────────────────────
def validate_internal_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Internal_ID'] = df['Internal_ID'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 3: Original Internal ID
# MDRM Code: CLCOG064
# ────────────────────────────────────────────────────────────────────────────────
def validate_original_internal_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Original_Internal_ID'] = df['Original_Internal_ID'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 4: Obligor Name
# MDRM Code: CLCO9017
# ────────────────────────────────────────────────────────────────────────────────
def validate_obligor_name(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Obligor_Name'] = df['Obligor_Name'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 5: City
# MDRM Code: CLCO9130
# ────────────────────────────────────────────────────────────────────────────────
def validate_city(df):
    df['City'] = df['City'].astype(str).str.strip().ne("")
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 6: Country
# MDRM Code: CLCO9031
# ────────────────────────────────────────────────────────────────────────────────
def validate_country(df):
    pattern = r'^[A-Z]{2}$'
    df['Country'] = df['Country'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 7: Zip Code
# MDRM Code: CLCO9220
# ────────────────────────────────────────────────────────────────────────────────
def validate_zip_code(df):
    pattern = r'^\d{5}$'
    df['Zip_Code'] = df['Zip_Code'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 8: Industry Code
# MDRM Code: CLCO4537
# ────────────────────────────────────────────────────────────────────────────────
def validate_industry_code(df):
    pattern = r'^\d{4,6}$'
    df['Industry_Code'] = df['Industry_Code'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 9: Industry Code Type
# MDRM Code: CLCOM297
# ────────────────────────────────────────────────────────────────────────────────
def validate_industry_code_type(df):
    df['Industry_Code_Type'] = df['Industry_Code_Type'].astype(str).isin(['1','2','3'])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 10: Obligor Internal Risk Rating
# MDRM Code: CLCOG080
# ────────────────────────────────────────────────────────────────────────────────
def validate_internal_risk_rating(df):
    df['Internal_Risk_Rating'] = df['Internal_Risk_Rating'].astype(str).str.strip().ne("")
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 11: TIN (TIN)
# MDRM Code: CLCO6191
# Description: Taxpayer Identification Number; format must be #########, ##-#######, or 'NA'
# Rule: Accept valid TIN formats or 'NA'
# ────────────────────────────────────────────────────────────────────────────────
def validate_tin(df):
    pattern = r'^(\d{9}|\d{2}-\d{7}|NA)$'
    df['TIN'] = df['TIN'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 12: Stock Exchange
# MDRM Code: CLCO4534
# Description: Free-text stock exchange name or 'NA'
# ────────────────────────────────────────────────────────────────────────────────
def validate_stock_exchange(df):
    df['Stock_Exchange'] = df['Stock_Exchange'].astype(str).str.strip().ne("")
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 13: Ticker Symbol (TKR)
# MDRM Code: CLCO4539
# Description: Free-text or 'NA'
# ────────────────────────────────────────────────────────────────────────────────
def validate_ticker_symbol(df):
    df['Ticker_Symbol'] = df['Ticker_Symbol'].astype(str).str.strip().ne("")
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 14: CUSIP
# MDRM Code: CLCO9161
# Description: First 6 chars of CUSIP or 'NA'
# ────────────────────────────────────────────────────────────────────────────────
def validate_cusip(df):
    pattern = r'^[A-Za-z0-9]{6}$|^NA$'
    df['CUSIP'] = df['CUSIP'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 15: Internal Credit Facility ID
# MDRM Code: CLCOM142
# Description: Unique identifier; must not contain unprintables, carriage return, or comma
# ────────────────────────────────────────────────────────────────────────────────
def validate_internal_credit_facility_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Internal_Credit_Facility_ID'] = df['Internal_Credit_Facility_ID'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 16: Original Internal Credit Facility ID
# MDRM Code: CLCOM296
# Description: Same rules as Field 15. Multiple IDs allowed separated by comma
# ────────────────────────────────────────────────────────────────────────────────
def validate_original_credit_facility_id(df):
    pattern = r'^[^\r\n\x00-\x1F\x7F]+$'
    df['Original_Credit_Facility_ID'] = df['Original_Credit_Facility_ID'].astype(str).str.match(pattern)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 18: Origination Date
# MDRM Code: CLCO9912
# Description: Date of credit agreement origination
# Rule: Must be in yyyy-mm-dd format and before or equal to today
# ────────────────────────────────────────────────────────────────────────────────
def validate_origination_date(df):
    def is_valid_date(date_str):
        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            return d <= datetime.today()
        except:
            return False
    df['Origination_Date'] = df['Origination_Date'].astype(str).apply(is_valid_date)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 19: Maturity Date
# MDRM Code: CLCO9914
# Description: Maturity date or '9999-01-01' for demand loans
# ────────────────────────────────────────────────────────────────────────────────
def validate_maturity_date(df):
    def is_valid_maturity(date_str):
        try:
            return bool(datetime.strptime(date_str, "%Y-%m-%d"))
        except:
            return date_str == "9999-01-01"
    df['Maturity_Date'] = df['Maturity_Date'].astype(str).apply(is_valid_maturity)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 20: Credit Facility Type
# MDRM Code: CLCOG072
# Description: Number from 0 to 19
# ────────────────────────────────────────────────────────────────────────────────
def validate_credit_facility_type(df):
    df['Credit_Facility_Type'] = df['Credit_Facility_Type'].astype(str).isin([str(i) for i in range(20)])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 21: Other Credit Facility Type Description
# ────────────────────────────────────────────────────────────────────────────────
def validate_other_credit_facility_type_desc(df):
    df['Other_Credit_Facility_Desc'] = df.apply(
        lambda x: True if x['Credit_Facility_Type'] != '0' or (x['Credit_Facility_Type'] == '0' and x['Other_Credit_Facility_Type_Description'].strip() != '') else False,
        axis=1
    )
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 22: Credit Facility Purpose
# ────────────────────────────────────────────────────────────────────────────────
def validate_credit_facility_purpose(df):
    df['Credit_Facility_Purpose'] = df['Credit_Facility_Purpose'].astype(str).isin([str(i) for i in list(range(0, 31)) + [33]])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 23: Other Credit Facility Purpose Description
# ────────────────────────────────────────────────────────────────────────────────
def validate_other_credit_facility_purpose_desc(df):
    df['Other_Credit_Facility_Purpose_Desc'] = df.apply(
        lambda x: True if x['Credit_Facility_Purpose'] != '0' or (x['Credit_Facility_Purpose'] == '0' and x['Other_Credit_Facility_Purpose_Description'].strip() != '') else False,
        axis=1
    )
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 24: Committed Exposure Global
# ────────────────────────────────────────────────────────────────────────────────
def validate_committed_exposure(df):
    df['Committed_Exposure'] = df['Committed_Exposure'].apply(lambda x: isinstance(x, (int, float)) and x >= 0)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 25: Utilized Exposure Global
# ────────────────────────────────────────────────────────────────────────────────
def validate_utilized_exposure(df):
    df['Utilized_Exposure'] = df['Utilized_Exposure'].apply(lambda x: isinstance(x, (int, float)) and x >= 0)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 26: Line Reported on FR Y-9C
# ────────────────────────────────────────────────────────────────────────────────
def validate_line_reported_on_fry9c(df):
    df['Line_Reported_on_FR_Y9C'] = df['Line_Reported_on_FR_Y9C'].astype(str).isin([str(i) for i in range(1, 12)])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 27: Line of Business
# ────────────────────────────────────────────────────────────────────────────────
def validate_line_of_business(df):
    df['Line_of_Business'] = df['Line_of_Business'].astype(str).str.strip().ne("")
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 28: Cumulative Charge-offs
# ────────────────────────────────────────────────────────────────────────────────
def validate_cumulative_chargeoffs(df):
    def is_valid(val):
        return val == 'NA' or (isinstance(val, (int, float)) and val >= 0)
    df['Cumulative_Chargeoffs'] = df['Cumulative_Chargeoffs'].apply(is_valid)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 32: # Days Principal or Interest Past Due
# ────────────────────────────────────────────────────────────────────────────────
def validate_days_past_due(df):
    df['Days_Past_Due'] = df['Days_Past_Due'].apply(lambda x: isinstance(x, int) and x >= 0)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 33: Non-Accrual Date
# MDRM Code: CLCOG078
# Description: Date the credit facility was placed on non-accrual or '9999-12-31' if not applicable
# Rule: Must be a valid yyyy-mm-dd date format or '9999-12-31'
# ────────────────────────────────────────────────────────────────────────────────
def validate_non_accrual_date(df):
    def is_valid_non_accrual(date_str):
        try:
            return bool(datetime.strptime(date_str, "%Y-%m-%d"))
        except:
            return date_str == "9999-12-31"
    df['Non_Accrual_Date'] = df['Non_Accrual_Date'].astype(str).apply(is_valid_non_accrual)
    return df
    
# ────────────────────────────────────────────────────────────────────────────────
# Field 34: Participation Flag
# MDRM Code: CLCO6135
# ────────────────────────────────────────────────────────────────────────────────
def validate_participation_flag(df):
    df['Participation_Flag'] = df['Participation_Flag'].astype(str).isin(['1', '2', '3', '4', '5'])
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 35: Lien Position
# MDRM Code: CLCOK450
# Description: Must be one of the integer codes 1 to 4
# Allowable values:
#   1 = First-Lien Senior
#   2 = Second Lien
#   3 = Senior Unsecured
#   4 = Contractually Subordinated
# ────────────────────────────────────────────────────────────────────────────────
def validate_lien_position(df):
    allowed_values = ['1', '2', '3', '4']
    df['Lien_Position'] = df['Lien_Position'].astype(str).isin(allowed_values)
    return df
    
    
# ────────────────────────────────────────────────────────────────────────────────
# Field 36: Security Type
# MDRM Code: CLCOM298
# Description: Must be one of the integer codes 0 to 6
# Allowable values:
#   0 = Real Estate only
#   1 = Cash and Marketable Securities
#   2 = Accounts Receivable and Inventory
#   3 = Fixed Assets excluding Real Estate
#   4 = Blanket Lien
#   5 = Other
#   6 = Unsecured
# ────────────────────────────────────────────────────────────────────────────────
def validate_security_type(df):
    allowed_values = ['0', '1', '2', '3', '4', '5', '6']
    df['Security_Type'] = df['Security_Type'].astype(str).isin(allowed_values)
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 37: Interest Rate Variability
# MDRM Code: CLCOK461
# Description: Indicates whether the interest rate is Fixed, Floating, Mixed, or Entirely fee based
# Allowable values:
#   1 = Fixed
#   2 = Floating
#   3 = Mixed
#   4 = Entirely fee based
# ────────────────────────────────────────────────────────────────────────────────
def validate_interest_rate_variability(df):
    allowed_values = ['1', '2', '3', '4']
    df['Interest_Rate_Variability'] = df['Interest_Rate_Variability'].astype(str).isin(allowed_values)
    return df


def validate_interest_rate(df):
    def is_valid_rate(val):
        if str(val).strip().upper() == 'NA':
            return True
        try:
            val = float(val)
            return 0 <= val <= 1  # Assuming 0% to 100% in decimal form
        except:
            return False

    df['Interest_Rate'] = df['Interest_Rate'].apply(is_valid_rate)
    return df


def validate_interest_rate_index(df):
    allowed_values = ['1', '2', '3', '4', '5', '6', '7']
    df['Interest_Rate_Index'] = df['Interest_Rate_Index'].astype(str).isin(allowed_values)
    return df


def validate_interest_rate_spread(df):
    def is_valid_spread(val):
        if str(val).strip().upper() == 'NA':
            return True
        try:
            float(val)  # Allow negative spreads too
            return True
        except:
            return False

    df['Interest_Rate_Spread'] = df['Interest_Rate_Spread'].apply(is_valid_spread)
    return df

def validate_interest_rate_ceiling(df):
    def is_valid_ceiling(val):
        val = str(val).strip().upper()
        if val in ['NA', 'NONE']:
            return True
        try:
            float(val)
            return True
        except:
            return False

    df['Interest_Rate_Ceiling'] = df['Interest_Rate_Ceiling'].apply(is_valid_ceiling)
    return df


def validate_interest_rate_floor(df):
    def is_valid_floor(val):
        val = str(val).strip().upper()
        if val in ['NA', 'NONE']:
            return True
        try:
            float(val)
            return True
        except:
            return False

    df['Interest_Rate_Floor'] = df['Interest_Rate_Floor'].apply(is_valid_floor)
    return df


def validate_tax_status(df):
    df['Tax_Status'] = df['Tax_Status'].astype(str).isin(['1', '2'])
    return df


def validate_tax_status(df):
    df['Tax_Status'] = df['Tax_Status'].astype(str).isin(['1', '2'])
    return df


def validate_guarantor_internal_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Guarantor_Internal_ID'] = df['Guarantor_Internal_ID'].astype(str).apply(lambda x: True if x.strip().upper() == 'NA' else bool(re.match(pattern, x)))
    return df


def validate_guarantor_name(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]+$'
    df['Guarantor_Name'] = df['Guarantor_Name'].astype(str).apply(lambda x: True if x.strip().upper() == 'NA' else bool(re.match(pattern, x)))
    return df


def validate_guarantor_tin(df):
    pattern = r'^(\d{3}-\d{2}-\d{4}|\d{9}|NA)$'
    df['Guarantor_TIN'] = df['Guarantor_TIN'].astype(str).str.upper().str.match(pattern)
    return df


def validate_guarantor_internal_risk_rating(df):
    df['Guarantor_Internal_Risk_Rating'] = df['Guarantor_Internal_Risk_Rating'].astype(str).apply(lambda x: True if x.strip().upper() == 'NA' else bool(x.strip()))
    return df


def validate_entity_internal_id(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]*$'
    df['Entity_Internal_ID'] = df['Entity_Internal_ID'].astype(str).str.match(pattern)
    return df


def validate_entity_name(df):
    pattern = r'^[^\r\n,\x00-\x1F\x7F]*$'
    df['Entity_Name'] = df['Entity_Name'].astype(str).str.match(pattern)
    return df
    
# ────────────────────────────────────────────────────────────────────────────────
# Field 51: Entity Internal Risk Rating
# MDRM Code: CLCEG080
# ────────────────────────────────────────────────────────────────────────────────
def validate_entity_internal_risk_rating(df):
    df['Entity_Internal_Risk_Rating'] = df['Entity_Internal_Risk_Rating'].astype(str).str.strip().ne("")
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 52: Date of Financials
# MDRM Code: CLCE9999
# ────────────────────────────────────────────────────────────────────────────────
def validate_date_financials(df):
    df['Date_Financials'] = pd.to_datetime(df['Date_Financials'], errors='coerce').notna()
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 53: Date of Last Audit
# MDRM Code: CLCE4929
# ────────────────────────────────────────────────────────────────────────────────
def validate_date_last_audit(df):
    df['Date_Last_Audit'] = pd.to_datetime(df['Date_Last_Audit'], errors='coerce').notna()
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 54: Net Sales Current
# MDRM Code: CLCEM301
# ────────────────────────────────────────────────────────────────────────────────
def validate_net_sales_current(df):
    df['Net_Sales_Current'] = df['Net_Sales_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 55: Net Sales Prior Year
# MDRM Code: CLCEM302
# ────────────────────────────────────────────────────────────────────────────────
def validate_net_sales_prior_year(df):
    df['Net_Sales_Prior_Year'] = df['Net_Sales_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 56: Operating Income
# ────────────────────────────────────────────────────────────────────────────────
def validate_operating_income(df):
    df['Operating_Income'] = df['Operating_Income'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 57: Depreciation & Amortization
# ────────────────────────────────────────────────────────────────────────────────
def validate_depreciation_amortization(df):
    df['Depreciation_Amortization'] = df['Depreciation_Amortization'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 58: Interest Expense
# MDRM Code: CLCEM305
# ────────────────────────────────────────────────────────────────────────────────
def validate_interest_expense(df):
    df['Interest_Expense'] = df['Interest_Expense'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 59: Net Income Current
# MDRM Code: CLCEM306
# ────────────────────────────────────────────────────────────────────────────────
def validate_net_income_current(df):
    df['Net_Income_Current'] = df['Net_Income_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 60: Net Income Prior Year
# MDRM Code: CLCEM307
# ────────────────────────────────────────────────────────────────────────────────
def validate_net_income_prior_year(df):
    df['Net_Income_Prior_Year'] = df['Net_Income_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 61: Cash & Marketable Securities
# MDRM Code: CLCEM308
# ────────────────────────────────────────────────────────────────────────────────
def validate_cash_marketable_securities(df):
    df['Cash_Marketable_Securities'] = df['Cash_Marketable_Securities'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 62: Accounts Receivable (A/R) Current
# MDRM Code: CLCEM309
# ────────────────────────────────────────────────────────────────────────────────
def validate_accounts_receivable_current(df):
    df['AR_Current'] = df['Accounts_Receivable_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 63: Accounts Receivable (A/R) Prior Year
# MDRM Code: CLCEM310
# ────────────────────────────────────────────────────────────────────────────────
def validate_accounts_receivable_prior_year(df):
    df['AR_Prior_Year'] = df['Accounts_Receivable_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 64: Inventory Current
# MDRM Code: CLCEM311
# ────────────────────────────────────────────────────────────────────────────────
def validate_inventory_current(df):
    df['Inventory_Current'] = df['Inventory_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 65: Inventory Prior Year
# MDRM Code: CLCEM312
# ────────────────────────────────────────────────────────────────────────────────
def validate_inventory_prior_year(df):
    df['Inventory_Prior_Year'] = df['Inventory_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 66: Current Assets Current
# MDRM Code: CLCEM313
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_assets_current(df):
    df['Current_Assets_Current'] = df['Current_Assets_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 67: Current Assets Prior Year
# MDRM Code: CLCEM314
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_assets_prior_year(df):
    df['Current_Assets_Prior_Year'] = df['Current_Assets_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 68: Tangible Assets
# MDRM Code: CLCEM315
# ────────────────────────────────────────────────────────────────────────────────
def validate_tangible_assets(df):
    df['Tangible_Assets'] = df['Tangible_Assets'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 69: Fixed Assets
# MDRM Code: CLCEM316
# ────────────────────────────────────────────────────────────────────────────────
def validate_fixed_assets(df):
    df['Fixed_Assets'] = df['Fixed_Assets'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 70: Total Assets Current
# MDRM Code: CLCE2170
# ────────────────────────────────────────────────────────────────────────────────
def validate_total_assets_current(df):
    df['Total_Assets_Current'] = df['Total_Assets_Current'].apply(lambda x: str(x).isdigit())
    return df
    
# ────────────────────────────────────────────────────────────────────────────────
# Field 71: Total Assets Prior Year
# MDRM Code: CLCEM317
# ────────────────────────────────────────────────────────────────────────────────
def validate_total_assets_prior_year(df):
    df['Total_Assets_Prior_Year'] = df['Total_Assets_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 72: Accounts Payable Current
# MDRM Code: CLCE3066
# ────────────────────────────────────────────────────────────────────────────────
def validate_accounts_payable_current(df):
    df['Accounts_Payable_Current'] = df['Accounts_Payable_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 73: Accounts Payable Prior Year
# MDRM Code: CLCEM325
# ────────────────────────────────────────────────────────────────────────────────
def validate_accounts_payable_prior_year(df):
    df['Accounts_Payable_Prior_Year'] = df['Accounts_Payable_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 74: Short Term Debt
# MDRM Code: CLCEM319
# ────────────────────────────────────────────────────────────────────────────────
def validate_short_term_debt(df):
    df['Short_Term_Debt'] = df['Short_Term_Debt'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 75: Current Maturities of Long Term Debt
# MDRM Code: CLCEM320
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_maturities_long_term_debt(df):
    df['Current_Maturities_Long_Term_Debt'] = df['Current_Maturities_Long_Term_Debt'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 76: Current Liabilities Current
# MDRM Code: CLCEM321
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_liabilities_current(df):
    df['Current_Liabilities_Current'] = df['Current_Liabilities_Current'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 77: Current Liabilities Prior Year
# MDRM Code: CLCEM322
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_liabilities_prior_year(df):
    df['Current_Liabilities_Prior_Year'] = df['Current_Liabilities_Prior_Year'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 78: Long Term Debt
# MDRM Code: CLCEM323
# ────────────────────────────────────────────────────────────────────────────────
def validate_long_term_debt(df):
    df['Long_Term_Debt'] = df['Long_Term_Debt'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 79: Minority Interest
# MDRM Code: CLCE4484
# ────────────────────────────────────────────────────────────────────────────────
def validate_minority_interest(df):
    df['Minority_Interest'] = df['Minority_Interest'].apply(lambda x: str(x).isdigit() or str(x).strip().upper() == 'NA')
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 80: Total Liabilities
# MDRM Code: CLCE2950
# ────────────────────────────────────────────────────────────────────────────────
def validate_total_liabilities(df):
    df['Total_Liabilities'] = df['Total_Liabilities'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 81: Retained Earnings
# MDRM Code: CLCE3247
# ────────────────────────────────────────────────────────────────────────────────
def validate_retained_earnings(df):
    df['Retained_Earnings'] = df['Retained_Earnings'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 82: Capital Expenditures
# MDRM Code: CLCEM324
# ────────────────────────────────────────────────────────────────────────────────
def validate_capital_expenditures(df):
    df['Capital_Expenditures'] = df['Capital_Expenditures'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 83: Special Purpose Entity Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_special_purpose_entity_flag(df):
    df['Special_Purpose_Entity_Flag'] = df['Special_Purpose_Entity_Flag'].isin([1, 2])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 86: Lower of Cost or Market Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_locom_flag(df):
    df['LOCOM'] = df['LOCOM'].isin([1, 2, 3])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 87: SNC Internal Credit ID
# ────────────────────────────────────────────────────────────────────────────────
def validate_snc_internal_credit_id(df):
    df['SNC_Internal_Credit_ID'] = df['SNC_Internal_Credit_ID'].apply(lambda x: x == 'NA' or bool(re.match(r'^[^,\r\n\f]+$', str(x))))
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 88: Probability of Default (PD)
# ────────────────────────────────────────────────────────────────────────────────
def validate_probability_of_default(df):
    def is_valid_pd(x):
        if str(x).upper() == 'NA':
            return True
        try:
            val = float(x)
            return 0 <= val <= 1
        except:
            return False
    df['PD'] = df['Probability_of_Default'].apply(is_valid_pd)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 89: Loss Given Default (LGD)
# MDRM Code: CLCOG081
# ────────────────────────────────────────────────────────────────────────────────
def validate_loss_given_default(df):
    def is_valid_lgd(x):
        if str(x).upper() == 'NA':
            return True
        try:
            val = float(x)
            return 0 <= val <= 1
        except:
            return False
    df['LGD'] = df['LGD'].apply(is_valid_lgd)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 90: Exposure At Default (EAD)
# ────────────────────────────────────────────────────────────────────────────────
def validate_exposure_at_default(df):
    def is_valid_ead(x):
        return str(x).isdigit() or str(x).strip().upper() == 'NA'
    df['EAD'] = df['EAD'].apply(is_valid_ead)
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 91: Renewal Date
# ────────────────────────────────────────────────────────────────────────────────
def validate_renewal_date(df):
    def is_valid_date(x):
        return str(x).strip() == '9999-12-31' or bool(re.match(r'^\d{2}-\d{2}-\d{4}$', str(x)))
    df['Renewal_Date'] = df['Renewal_Date'].apply(is_valid_date)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 92: Credit Facility Currency
# ────────────────────────────────────────────────────────────────────────────────
def validate_credit_facility_currency(df):
    df['Credit_Facility_Currency'] = df['Credit_Facility_Currency'].apply(lambda x: bool(re.match(r'^[A-Z]{3}$', str(x).strip())))
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 93: Collateral Market Value
# ────────────────────────────────────────────────────────────────────────────────
def validate_collateral_market_value(df):
    df['Collateral_Market_Value'] = df['Collateral_Market_Value'].apply(lambda x: str(x).isdigit() or str(x).strip().upper() == 'NA')
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 94: Prepayment Penalty Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_prepayment_penalty_flag(df):
    df['Prepayment_Penalty_Flag'] = df['Prepayment_Penalty_Flag'].isin([1, 2, 3])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 95: Entity Industry Code
# ────────────────────────────────────────────────────────────────────────────────
def validate_entity_industry_code(df):
    df['Entity_Industry_Code'] = df['Entity_Industry_Code'].apply(lambda x: str(x).isdigit() and 4 <= len(str(x)) <= 6)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 96: Participation Interest
# ────────────────────────────────────────────────────────────────────────────────
def validate_participation_interest(df):
    def is_valid_participation(x):
        if str(x).strip().upper() == 'NA':
            return True
        try:
            val = float(x)
            return 0 <= val <= 1
        except:
            return False
    df['Participation_Interest'] = df['Participation_Interest'].apply(is_valid_participation)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 97: Leveraged Loan Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_leveraged_loan_flag(df):
    df['Leveraged_Loan_Flag'] = df['Leveraged_Loan_Flag'].isin([1, 2])
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 98: Disposition Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_disposition_flag(df):
    df['Disposition_Flag'] = df['Disposition_Flag'].isin(list(range(9)))
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 99: Disposition Schedule Shift
# ────────────────────────────────────────────────────────────────────────────────
def validate_disposition_schedule_shift(df):
    df['Disposition_Schedule_Shift'] = df['Disposition_Schedule_Shift'].apply(lambda x: bool(re.match(r'^[A-Z]\.[A-Z]\.\d$', str(x).strip())) or str(x).strip().upper() == 'NA')
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 100: Syndicated Loan Flag
# ────────────────────────────────────────────────────────────────────────────────
def validate_syndicated_loan_flag(df):
    df['Syndicated_Loan_Flag'] = df['Syndicated_Loan_Flag'].isin([0, 1, 2, 3, 4])
    return df


# ────────────────────────────────────────────────────────────────────────────────
# Field 101: Target Hold
# ────────────────────────────────────────────────────────────────────────────────
def validate_target_hold(df):
    def is_valid_target_hold(x):
        return str(x).strip().upper() == 'NA' or re.match(r'^\d+(\.\d{1,4})?$', str(x))
    df['Target_Hold'] = df['Target_Hold'].apply(is_valid_target_hold)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 102: ASC326-20
# ────────────────────────────────────────────────────────────────────────────────
def validate_asc326_20(df):
    df['ASC326_20'] = df['ASC326_20'].apply(lambda x: str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 103: Purchased Credit Deteriorated Noncredit Discount
# ────────────────────────────────────────────────────────────────────────────────
def validate_pcd_noncredit_discount(df):
    df['PCD_Noncredit_Discount'] = df['PCD_Noncredit_Discount'].apply(lambda x: x == '' or str(x).isdigit())
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 104: Current Maturity Date
# ────────────────────────────────────────────────────────────────────────────────
def validate_current_maturity_date(df):
    def is_valid_date(x):
        try:
            datetime.strptime(x, "%Y-%m-%d")
            return True
        except:
            return x == '9999-01-01'
    df['Current_Maturity_Date'] = df['Current_Maturity_Date'].apply(is_valid_date)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 105: Committed Exposure Global Par Value
# ────────────────────────────────────────────────────────────────────────────────
def validate_committed_exposure_global_par(df):
    def is_valid_committed_exposure(x):
        return str(x).upper() == 'NA' or re.match(r'^-?\d+$', str(x))
    df['Committed_Exposure_Global_Par'] = df['Committed_Exposure_Global_Par'].apply(is_valid_committed_exposure)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 106: Utilized Exposure Global Par Value
# ────────────────────────────────────────────────────────────────────────────────
def validate_utilized_exposure_global_par(df):
    def is_valid_utilized_exposure(x):
        return str(x).upper() == 'NA' or re.match(r'^-?\d+$', str(x))
    df['Utilized_Exposure_Global_Par'] = df['Utilized_Exposure_Global_Par'].apply(is_valid_utilized_exposure)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 107: Committed Exposure Global Fair Value
# ────────────────────────────────────────────────────────────────────────────────
def validate_committed_exposure_global_fair(df):
    def is_valid_committed_fair(x):
        return str(x).upper() == 'NA' or re.match(r'^-?\d+$', str(x))
    df['Committed_Exposure_Global_Fair'] = df['Committed_Exposure_Global_Fair'].apply(is_valid_committed_fair)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 108: Utilized Exposure Global Fair Value
# ────────────────────────────────────────────────────────────────────────────────
def validate_utilized_exposure_global_fair(df):
    def is_valid_utilized_fair(x):
        return str(x).upper() == 'NA' or re.match(r'^-?\d+$', str(x))
    df['Utilized_Exposure_Global_Fair'] = df['Utilized_Exposure_Global_Fair'].apply(is_valid_utilized_fair)
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 109, 110: DO NOT USE – No validation functions.

# ────────────────────────────────────────────────────────────────────────────────
# Field 111: Obligor LEI
# ────────────────────────────────────────────────────────────────────────────────
def validate_obligor_lei(df):
    df['Obligor_LEI'] = df['Obligor_LEI'].apply(lambda x: re.match(r'^[A-Z0-9]{20}$', str(x)) or str(x).upper() == 'NA')
    return df

# ────────────────────────────────────────────────────────────────────────────────
# Field 112: Primary Source of Repayment LEI
# ────────────────────────────────────────────────────────────────────────────────
def validate_psr_lei(df):
    df['PSR_LEI'] = df['PSR_LEI'].apply(lambda x: re.match(r'^[A-Z0-9]{20}$', str(x)) or str(x).upper() == 'NA')
    return df


# Extend the rule registry
CORPORATE_LOAN_RULES.extend([
    validate_target_hold,
    validate_asc326_20,
    validate_pcd_noncredit_discount,
    validate_current_maturity_date,
    validate_committed_exposure_global_par,
    validate_utilized_exposure_global_par,
    validate_committed_exposure_global_fair,
    validate_utilized_exposure_global_fair,
    validate_obligor_lei,
    validate_psr_lei,
    validate_country,
    validate_city,
    validate_accounts_payable_current,
    validate_accounts_payable_prior_year,
    validate_accounts_receivable_current,
    validate_accounts_receivable_prior_year,
    validate_capital_expenditures,
    validate_cash_marketable_securities,
    validate_collateral_market_value,
    validate_committed_exposure,
    validate_credit_facility_currency,
    validate_credit_facility_purpose,
    validate_credit_facility_type,
    validate_cumulative_chargeoffs,
    validate_current_assets_current,
    validate_current_assets_prior_year,
    validate_current_liabilities_current,
    validate_current_liabilities_prior_year,
    validate_current_maturities_long_term_debt,
    validate_cusip,
    validate_customer_id,
    validate_date_financials,
    validate_date_last_audit,
    validate_days_past_due,
    validate_depreciation_amortization,
    validate_disposition_flag,
    validate_disposition_schedule_shift,
    validate_entity_industry_code,
    validate_entity_internal_id,
    validate_entity_internal_risk_rating,
    validate_entity_name,
    validate_exposure_at_default,
    validate_fixed_assets,
    validate_guarantor_internal_id,
    validate_guarantor_internal_risk_rating,
    validate_guarantor_name,
    validate_guarantor_tin,
    validate_industry_code,
    validate_industry_code_type,
    validate_interest_expense,
    validate_interest_rate,
    validate_interest_rate_ceiling,
    validate_interest_rate_floor,
    validate_interest_rate_index,
    validate_interest_rate_spread,
    validate_interest_rate_variability,
    validate_internal_credit_facility_id,
    validate_internal_id,
    validate_internal_risk_rating,
    validate_inventory_current,
    validate_inventory_prior_year,
    validate_leveraged_loan_flag,
    validate_lien_position,
    validate_line_of_business,
    validate_line_reported_on_fry9c,
    validate_locom_flag,
    validate_long_term_debt,
    validate_loss_given_default,
    validate_maturity_date,
    validate_minority_interest,
    validate_net_income_current,
    validate_net_income_prior_year,
    validate_net_sales_current,
    validate_net_sales_prior_year,
    validate_non_accrual_date,
    validate_obligor_name,
    validate_operating_income,
    validate_original_credit_facility_id,
    validate_original_internal_id,
    validate_origination_date,
    validate_other_credit_facility_purpose_desc,
    validate_other_credit_facility_type_desc,
    validate_participation_flag,
    validate_participation_interest,
    validate_prepayment_penalty_flag,
    validate_probability_of_default,
    validate_renewal_date,
    validate_retained_earnings,
    validate_security_type,
    validate_short_term_debt,
    validate_snc_internal_credit_id,
    validate_special_purpose_entity_flag,
    validate_stock_exchange,
    validate_syndicated_loan_flag,
    validate_tangible_assets,
    validate_tax_status,
    validate_ticker_symbol,
    validate_tin,
    validate_total_assets_current,
    validate_total_assets_prior_year,
    validate_total_liabilities,
    validate_utilized_exposure
])

