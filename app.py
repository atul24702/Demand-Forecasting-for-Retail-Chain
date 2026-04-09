import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("demand_model.pkl", "rb"))

st.title("📦 Demand Forecasting for Retail Chain")

st.write("Enter details to predict demand")

# 5 Inputs (IMPORTANT)
store = st.number_input("Store ID", value=1)
item = st.number_input("Item ID", value=101)
temperature = st.number_input("Temperature", value=25.0)
fuel_price = st.number_input("Fuel Price", value=3.5)
cpi = st.number_input("CPI", value=200.0)

# Convert into array (5 features)
input_data = np.array([[store, item, temperature, fuel_price, cpi]])

if st.button("Predict Demand"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Demand: {prediction[0]}")