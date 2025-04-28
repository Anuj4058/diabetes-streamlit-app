import streamlit as st
import pandas as pd
import numpy as np
from llm_helper import get_llm_response
import pickle

# Load the trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

st.title('Diabetes Prediction App')
st.write('Enter the following details to predict whether you are diabetic:')

# Collect user input
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
glucose = st.number_input('Glucose Level', min_value=0, max_value=200, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=80)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
insulin = st.number_input('Insulin Level', min_value=0, max_value=800, value=85)
BMI = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input('Age', min_value=0, max_value=120, value=30)

# Make prediction
if st.button('Predict'):
    user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, diabetes_pedigree, age]])
    prediction = model.predict(user_data)
    result = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'
    st.success(f'Prediction: {result}')

    # Get explanation from LLM
    prompt = f"Explain why a person with glucose level {glucose}, BMI {BMI}, and age {age} might be {result}."
    explanation = get_llm_response(prompt)
    st.write('LLM Explanation:')
    st.write(explanation)

st.write('---')
st.write('Powered by Google Gemini & Streamlit')


