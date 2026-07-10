import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Sidebar
# =========================

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

    st.write("""
    Welcome!

    This application predicts the selling price of a house using
    Machine Learning.

    Simply enter the house details and click **Predict Price**.
    """)


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