# House Price Prediction Using Machine Learning

A machine learning web application that predicts the selling price of a house based on its features. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, with the **Gradient Boosting Regressor** selected as the final prediction model.

---

## Project Overview

House prices are influenced by many factors such as the size of the house, its location, the quality of construction, and the number of rooms. This project uses machine learning to estimate the selling price of a house using the **Ames Housing Dataset**.

The application provides a user-friendly interface where users can enter house details and receive an estimated selling price instantly.

---

## Features

- Interactive Streamlit web application
- Predicts house prices in real time
- Clean and responsive user interface
- Professional sidebar navigation
- Model performance dashboard
- Attractive custom styling using CSS
- Banner image on the homepage

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- CSS

---

## Dataset

This project uses the **Ames Housing Dataset**, which contains detailed information about residential properties.

Dataset files include:

- train.csv
- test.csv
- data_description.txt

The dataset contains information such as:

- Overall house quality
- Living area
- Garage size
- Basement area
- Number of bathrooms
- Lot area
- Neighborhood
- Year built
- Total rooms
- Selling price

---

## Machine Learning Models Evaluated

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

The **Gradient Boosting Regressor** achieved the best overall performance and was selected as the final model.

---

## Model Performance

| Metric | Value |
|---------|-------|
| R² Score | **0.8973** |
| Mean Absolute Error (MAE) | **18,215** |
| Root Mean Squared Error (RMSE) | **28,061** |

---

## Project Structure

```
MLProject/
│
├── app/
│   ├── app.py
│   ├── style.css
│   └── house.jpg
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── data_description.txt
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   ├── 01_Exploratory_Data_Analysis.ipynb
│   └── 02_Model_Training.ipynb
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Move into the project folder:

```bash
cd House-Price-Prediction
```

Create a virtual environment:

```bash
python3 -m venv venvML
```

Activate it:

### Linux/macOS

```bash
source venvML/bin/activate
```

### Windows

```bash
venvML\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app/app.py
```

The application will open automatically in your web browser.

---

## Application Screenshots

Add screenshots of:

- Home Page
- Prediction Form
- Prediction Result
- Model Performance Page
- About Page

Example:

```
screenshots/
├── home.png
├── prediction.png
├── performance.png
└── about.png
```

---

## Future Improvements

- Include all neighborhoods from the dataset
- Deploy the application online
- Add interactive visualizations
- Improve feature engineering
- Train additional ensemble models
- Add prediction confidence intervals

---

## Author

**Bobo**

Bachelor of Science in Information and Communication Technology

Machine Learning Project

---

## 📄 License

This project was developed for educational purposes as part of a university Machine Learning course.# MLProject
