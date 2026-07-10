import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Model Performance",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Model: Gradient Boosting")

st.sidebar.info("""
**Developer:** Bobo

**Dataset:** Ames Housing Dataset

**Algorithm:** Gradient Boosting Regressor
""")

if page == "Home":

    st.title("House Price Prediction")

    banner_path = Path(__file__).parent / "house.jpg"

    st.image(
        str(banner_path),
        use_container_width=True
    )

    st.write(
        "Fill in the house details below and click **Predict Price**."
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

    if st.button("Predict Price"):

        input_data = pd.DataFrame({
            "OverallQual": [overall_qual],
            "GrLivArea": [gr_liv_area],
            "GarageCars": [garage_cars],
            "GarageArea": [garage_area],
            "TotalBsmtSF": [total_bsmt],
            "FullBath": [full_bath],
            "YearBuilt": [year_built],
            "TotRmsAbvGrd": [total_rooms],
            "LotArea": [lot_area],
            "Neighborhood": [neighborhood]
        })

        prediction = model.predict(input_data)

        st.markdown(
            f"""
            <div class="prediction-box">
                <h2>Estimated House Price</h2>
                <p class="prediction-price">
                    ${prediction[0]:,.0f}
                </p>
            </div>
            """,
            unsafe_allow_html=True
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
        "$18,215"
    )

    col3.metric(
        "RMSE",
        "$28,061"
    )

    st.markdown("---")

    st.write("""
The Gradient Boosting Regression model achieved excellent performance
on the Ames Housing dataset.

- **R² Score:** 89.73%
- **Mean Absolute Error:** $18,215
- **Root Mean Squared Error:** $28,061

These results indicate that the model explains almost 90% of the
variation in house prices.
""")

elif page == "About":

    st.title("About This Project")

    st.write("""
## House Price Prediction using Machine Learning

This application predicts residential house prices using a
Gradient Boosting Regression model trained on the Ames Housing Dataset.

### Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

### Features

- Predict house prices
- Interactive user interface
- Machine Learning model
- Responsive layout

### Developer

**Bobo**
""")

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Developed by <strong>Bobo</strong><br>
        House Price Prediction using Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)