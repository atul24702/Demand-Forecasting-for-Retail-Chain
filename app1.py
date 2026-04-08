import streamlit as st
import pickle
import numpy as np

# 1. Load the trained model
# Make sure your .pkl file is in the same folder as this script
try:
    with open("flood_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'flood_model.pkl' is in the directory.")

# 2. Set up the User Interface
st.set_page_config(page_title="Prediction System", page_icon="🌊")
st.title("🌊 Project Prediction System")
st.write("Enter the required details below to get a prediction:")

# 3. Create Input Fields
# These must match the order and number of features the model was trained on
col1, col2 = st.columns(2)

with col1:
    val1 = st.number_input("Monthly Rainfall (mm)", min_value=0.0)
    val2 = st.number_input("Inundation Area (sqm)", min_value=0.0)
    val3 = st.number_input("Rainfall in last 7 days (mm)", min_value=0.0)
    val4 = st.number_input("Historical Count", min_value=0)

with col2:
    val5 = st.number_input("Distance to Resource (m)", min_value=0.0)
    val6 = st.number_input("Infrastructure Score (0-10)", min_value=0.0, max_value=10.0)
    val7 = st.number_input("Drainage Index (0-10)", min_value=0.0, max_value=10.0)

# 4. Prediction Logic
if st.button("Generate Prediction"):
    # Convert inputs into a 2D numpy array for the model
    input_data = np.array([[val1, val2, val3, val4, val5, val6, val7]])
    
    # Get the prediction
    prediction = model.predict(input_data)[0]

    # 5. Display the Result
    st.divider()
    st.subheader(f"Predicted Value: {prediction:.2f}")
    
    if prediction > 0.5: # Example threshold
        st.warning("High Risk/Demand Detected")
    else:
        st.success("Low Risk/Demand Detected")
