# genai_data_profiling_streamLiut_integrated_Langchain_GPT.py
"""
Streamlit UI integrated with LangChain + GPT for Data Profiling
"""
import streamlit as st
import pandas as pd
import os
from corporate_loan_rules import CORPORATE_LOAN_RULES
from custom_rules import apply_custom_rules
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="GenAI Data Profiler", layout="wide")
st.title("📊 GenAI Data Profiler for Corporate Loans")

uploaded_file = st.file_uploader("Upload your CSV file for profiling", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📄 Preview of Uploaded Data", df.head())

    # Apply corporate loan rules
    for rule in CORPORATE_LOAN_RULES:
        df = rule(df)

    # Apply domain-specific rules
    df = apply_custom_rules(df)

    # Calculate risk score per row
    df['Risk_Level'] = df.apply(score_risk, axis=1)

    # Generate remediation suggestions using GPT
    if OPENAI_API_KEY:
        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.2)
        df['Remediation'] = df.apply(lambda row: suggest_remediation(row, llm), axis=1)
    else:
        df['Remediation'] = "❌ OPENAI_API_KEY not set"

    # Display results
    st.write("### ✅ Validation Results")
    st.dataframe(df)

    # Download option
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Validated CSV", csv, "validated_output.csv", "text/csv")
else:
    st.info("👈 Please upload a CSV file to get started.")
