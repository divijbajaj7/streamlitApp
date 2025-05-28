import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Load model and preprocessor
model = joblib.load("adaboost_model1.pkl")
preprocessor = joblib.load("preprocessor1.pkl")

# Load a banner or UI image
st.image("Loan_Prediction_using__Machine_Learning_Project.webp", use_column_width=True)

st.title("🏦 Loan Approval Prediction App")
st.write("Fill out the details to check if the loan will be approved ✅ or not ❌")

# User input form
def user_input_features():
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Married = st.selectbox('Married', ['Yes', 'No'])
    Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
    Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox('Self Employed', ['Yes', 'No'])
    ApplicantIncome = st.number_input('Applicant Income', min_value=0)
    CoapplicantIncome = st.number_input('Coapplicant Income', min_value=0.0)
    LoanAmount = st.number_input('Loan Amount (in thousands)', min_value=0.0)
    Loan_Amount_Term = st.number_input('Loan Term (in days)', min_value=0.0)
    Credit_History = st.selectbox('Credit History', [1.0, 0.0])
    Property_Area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

    data = {
        'Gender': Gender,
        'Married': Married,
        'Dependents': Dependents,
        'Education': Education,
        'Self_Employed': Self_Employed,
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Property_Area': Property_Area
    }

    return pd.DataFrame([data])

input_df = user_input_features()

# Encoding categorical features manually
input_df['Gender'] = input_df['Gender'].map({'Male': 1, 'Female': 0})
input_df['Married'] = input_df['Married'].map({'Yes': 1, 'No': 0})
input_df['Education'] = input_df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
input_df['Self_Employed'] = input_df['Self_Employed'].map({'Yes': 1, 'No': 0})
input_df['Property_Area'] = input_df['Property_Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
input_df['Dependents'] = input_df['Dependents'].replace('3+', 3).astype(int)

# Preprocess and predict
input_processed = preprocessor.transform(input_df)
prediction = model.predict(input_processed)

st.subheader("Prediction Result 🧠")
st.success("✅ Loan Approved!" if prediction[0] == 1 else "❌ Loan Not Approved")
