
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Autohotkey Demo - Multi Input", layout="centered")

st.title("Autohotkey Use Case Demonstration")

# Initialize persistent dataframe in session_state
if "records" not in st.session_state:
    st.session_state.records = []

# ----- FORM -----
with st.form("ahk_form"):
    st.subheader("Fill the form")

    col1, col2 = st.columns(2)
    with col1:
        text_value = st.text_input("Text Input (Ex: your shortcut output)")
        category = st.selectbox(
            "Choose Category",
            ["General", "Automation", "Productivity", "Other"]
        )
        extra_text2 = st.text_input("Additional Notes 2")
    with col2:
        extra_text = st.text_input("Additional Notes")
        priority = st.selectbox(
            "Priority Level",
            ["Low", "Medium", "High"]
        )
        extra_text3 = st.text_input("Additional Notes 3")
        priority2 = st.selectbox(
            "Priority Level 2",
            ["Low", "Medium", "High"]
        )

    submitted = st.form_submit_button("Submit")

# ----- PROCESS FORM -----
if submitted:
    new_row = {
        "Text": text_value,
        "Notes": extra_text,
        "Category": category,
        "Priority": priority,
        "Notes 2": extra_text2,
        "Notes 3": extra_text3,
        "Priority 2": priority2
    }

    # Append new row to existing list
    st.session_state.records.append(new_row)

    st.success("Submitted successfully!")

# ----- DATAFRAME OUTPUT -----
if st.session_state.records:
    st.subheader("📊 Dashboard – Collected Records")

    df = pd.DataFrame(st.session_state.records)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No submissions yet. Fill the form above.")
