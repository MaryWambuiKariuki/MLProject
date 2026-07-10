import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide"
)

st.title(" House Price Prediction")

st.write("""
Welcome to the **House Price Prediction** application.

This application uses a **Gradient Boosting Regression Model**
trained on the Ames Housing Dataset.
""")