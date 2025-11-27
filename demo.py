import streamlit as st
import pandas as pd

st.set_page_config(page_title="AHK Demo Form", layout="centered")

st.title("Autohotkey Use Case Demonstration Form")

# ----- FORM -----
with st.form("ahk_demo_form"):
    text_value = st.text_input("Type Something (your shortcut-expanded text)")
    
    saved_option = st.selectbox(
        "Choose a Category",
        ["General", "Automation", "Productivity", "Other"]
    )

    submitted = st.form_submit_button("Submit")

# ----- OUTPUT -----
if submitted:
    st.success("Form submitted!")

    # Create DataFrame
    df = pd.DataFrame(
        {
            "Input Text": [text_value],
            "Category": [saved_option]
        }
    )

    st.subheader("📊 Dashboard Output")
    st.write("Here's what you submitted:")
    st.dataframe(df, use_container_width=True)

    st.info("Next Step: This could simulate how Autohotkey saves and expands text.")
