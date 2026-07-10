import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load trained model
model = joblib.load("../models/house_price_model.pkl")
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Model Performance",
        "About"
    ]
)

st.sidebar.success("Model: Gradient Boosting")

st.sidebar.info("""
Developer:
Bobo

Machine Learning Project

Dataset:
Ames Housing Dataset
""")

if page == "Home":
    st.title("House Price Prediction")

    st.write(
        "Enter the house details below and click **Predict Price**."
    )

    col1, col2 = st.columns(2)

    with col1:

        overall_qual = st.slider(
            "Overall Quality",
            1,
            10,
            5
        )

        gr_liv_area = st.number_input(
            "Above Ground Living Area (sq ft)",
            min_value=300,
            max_value=6000,
            value=1500
        )

        garage_cars = st.slider(
            "Garage Capacity",
            0,
            5,
            2
        )

        garage_area = st.number_input(
            "Garage Area (sq ft)",
            min_value=0,
            max_value=1500,
            value=500
        )

        total_bsmt = st.number_input(
            "Basement Area (sq ft)",
            min_value=0,
            max_value=4000,
            value=900
        )

    with col2:

        full_bath = st.slider(
            "Full Bathrooms",
            0,
            4,
            2
        )

        year_built = st.slider(
            "Year Built",
            1872,
            2010,
            2000
        )

        total_rooms = st.slider(
            "Total Rooms Above Ground",
            2,
            15,
            7
        )

        lot_area = st.number_input(
            "Lot Area (sq ft)",
            min_value=1000,
            max_value=100000,
            value=9000
        )

        neighborhood = st.selectbox(
            "Neighborhood",
            [
                "NAmes",
                "CollgCr",
                "OldTown",
                "Edwards",
                "Somerst",
                "NridgHt",
                "Gilbert",
                "Sawyer",
                "NWAmes",
                "BrkSide"
            ]
        )

elif page == "Model Performance":

    st.title("Model Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "R² Score",
        "0.8973"
    )

    col2.metric(
        "MAE",
        "18,215"
    )

    col3.metric(
        "RMSE",
        "28,061"
    )

elif page == "About":

    st.title("About This Project")

    st.write("""
    ### House Price Prediction

    This project uses a Gradient Boosting Regressor
    trained on the Ames Housing Dataset.

    Technologies Used

    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Joblib

    Developed by Bobo.
    """)