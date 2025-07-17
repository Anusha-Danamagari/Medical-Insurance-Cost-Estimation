import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('insurance_rf_model.pkl')

st.title("Medical Insurance Cost Estimator")

age = st.slider('Age', 18, 100, 30)
sex = st.selectbox('Sex', ['male', 'female'])
bmi = st.slider('BMI', 10.0, 50.0, 25.0)
children = st.slider('Number of Children', 0, 10, 0)
smoker = st.selectbox('Smoker', ['yes', 'no'])
region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

# Encode categorical inputs
sex_val = 1 if sex == 'male' else 0
smoker_val = 1 if smoker == 'yes' else 0

region_northwest = 1 if region == 'northwest' else 0
region_southeast = 1 if region == 'southeast' else 0
region_southwest = 1 if region == 'southwest' else 0

features = np.array([age, sex_val, bmi, children, smoker_val,
                     region_northwest, region_southeast, region_southwest]).reshape(1, -1)

if st.button('Estimate Insurance Cost'):
    prediction = model.predict(features)[0]
    st.success(f'Estimated Medical Insurance Charges: ${prediction:,.2f}')
