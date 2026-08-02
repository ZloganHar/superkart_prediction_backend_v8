import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKart_prediction_model_v1_0")

# Section for online prediction
st.subheader("Online Prediction")

# Collect user input for property features
Product_Sugar_Content = st.selectbox("Product Sugar Content",["Low Sugar","Regular","No Sugar"])
Store_Size = st.selectbox("Store size",["Medium", "High", "Small"])
Store_Location_City_Type = st.selectbox("Store size",["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store type", ["Supermarket Type2","Supermarket Type1","Departmental Store"])
Id_Prefix = st.selectbox("ID_Prefix", ["FD", "DR", "NC"])
Product_Weight = st.number_input("Product weight", min_value=0, value=1.0, step=0.01)
Product_Allocated_Area = st.number_input("Product allocated area", min_value=0, value=1.0, step=0.01)
Product_MRP = st.number_input("Product Max Retail Price", min_value=0, value=1.0, step=0.01)
Store_Age = st.number_input("Store age", min_value=0, value=1, step=1)

input_data = pd.DataFrame([{
  "Product_Sugar_Content": Product_Sugar_Content,
  "Store_Size": Store_Size,
  "Store_Location_City_Type": Store_Location_City_Type,
  "Store_Type": Store_Type,
  "Id_Prefix": Id_Prefix,
  "Product_Weight": Product_Weight,
  "Product_Allocated_Area": Product_Allocated_Area,
  "Product_MRP": Product_MRP,
  "Store_Age": Store_Age
}])

if st.button("Predict", type="primary"):
  response = requests.post(f"{BACKEND_URL}/v1/product", json=input_data.to_dict(orient='records'[0]))
  if response.status_code == 200: 
    prediction = response.json()['Predicted_Product_Store_Sales_Total']
    st.success(f"Predicted product price": {prediction}")
  else:
    st.error("Unable to connect to the prediction API.")
