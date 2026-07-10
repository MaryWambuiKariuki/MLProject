import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide"
)

st.title("House Price Prediction")
st.write(
    """
    Predict the selling price of a house using a machine learning model trained on the Ames Housing dataset.
    """
)