import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# initialize Flask app
superkart_api = Flask("SuperKart Product Store Sales Total")

# load the model
model = joblib.load("backend_files/SuperKart_prediction_model_v1_0.joblib")

@superkart_api.get("/")
def home():
  return "Welcome to the SuperKart product store sales total prediction API."

# define an endpoint to predict the product store sales total for a single product
@superkart_api.post('/v1/product')
def predict_product_store_sales_total():
  # get JSON data
  product_data = request.get_json()

  # extract relevant product details
  sample = {
    'Product_Weight': product_data['Product_Weight'],
    'Product_Allocated_Area': product_data['Product_Allocated_Area'],
    'Product_MRP': product_data['Product_MRP'],
    'Store_Age': product_data['Store_Age'],
    'Product_Sugar_Content': product_data['Product_Sugar_Content'],
    'Store_Size': product_data['Store_Size'],
    'Store_Location_City_Type': product_data['Store_Location_City_Type'],
    'Store_Type': product_data['Store_Type'],
    'Id_Prefix': product_data['Id_Prefix']
  }

  # extract to dataframe
  input_data = pd.DataFrame([sample])

  # predict using the trained model
  prediction = model.predict(input_data).tolist()[0]

  # return the prediction as a JSON response
  return jsonify({'Predicted_Product_Store_Sales_Total': prediction})

# run in debug mode
if __name__ == '__main__':
  superkart_api.run(debug=True)
