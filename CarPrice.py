import numpy as np
import pandas as pd
import datetime
import streamlit as st
import pickle

cars_df = pd.read_csv("./cars24.csv")
st.write('''
          # Cars 24 : Used Car Prediction App :sunglasses: ''')
st.dataframe(cars_df.head())
col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type", ["Diesel", "Petrol", "Electric","CNG", "LPG"])
engine = st.slider("Set the Engine Power", 500,5000, step = 100)
transmission_type = col2.selectbox("Select the Transmission type", ["Manual", "Automatic"])
seats = st.selectbox("Number of seats you need" , [4,5,6,7,8,9,11])

encode_dict = {
    "fuel_type" : {"Diesel" : 1, "Petrol" : 2, "Electric":3,"CNG":4, "LPG":5},
    "seller_type" : {"Dealer": 1, "Individual" : 2, "Trustmark Dealer" : 3},
    "transmission_type" : {"Manual" :0, "Automatic" : 1}
}

def model_pred(fuel_type, engine, trasnmission_type, seats):
    # load the model
    with open('car_pred.pkl', 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30 , seats]]
        return reg_model.predict(input_features)

if (st.button("Predict Price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, engine, transmission_type, seats)

    st.text(f"The price of the car is {price[0].round(2)} lakh rupees.")

