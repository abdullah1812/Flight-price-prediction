

import joblib
import pandas as pd
import numpy as np
import streamlit as st
import datetime

Model = joblib.load("flight_model.pkl")
Inputs = joblib.load("inputs.pkl")

def prediction(Airline, Source, Destination, Duration ,Total_Stops, Additional_Info, Day, Month):
    df = pd.DataFrame(columns=Inputs)
    df.at[0,"Airline"] = Airline
    df.at[0,"Source"] = Source
    df.at[0,"Destination"] = Destination
    df.at[0,"Duration(m)"] = Duration
    df.at[0,"Total_Stops"] = Total_Stops
    df.at[0,"Additional_Info  "] = Additional_Info
    df.at[0,"Day"] = Day
    df.at[0,"Month"] = Month
    
    
    result = Model.predict(df)[0]
    return result

def Main():
    Airline_list=['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers',
     'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business','Multiple carriers Premium economy', 'Trujet']

    Additional_Info_list = ['No info', 'In-flight meal not included',
       'No check-in baggage included', '1 Short layover', 'No Info',
       '1 Long layover', 'Change airports', 'Business class',
       'Red-eye flight', '2 Long layover']

    st.title("Flight Price Prediction")
    Airline = st.selectbox("Airline Name",Airline_list)
    Source = st.selectbox("Source",['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination",['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
   
    Duration_time = st.text_input("Duration Time (e.g., 2h 50m)", value="2h 40m", max_chars=10)
    h =  Duration_time.replace('h', '*60').replace(' ', '+').replace('m', '') 
    Duration = eval(h)

    Total_Stops = st.slider("Flight Stops",min_value = 0.0, max_value = 4.0, step = 1.0, value = 1.0)
    Additional_Info = st.selectbox("Info About Flight",Additional_Info_list)
   

    d = st.date_input("Date_of_Journey", datetime.date(2019, 7, 6))
    Day = d.day
    Month = d.month

    
    h =  Duration_time.replace('h', '*60').replace(' ', '+').replace('m', '') 

    Duration = eval(h)
    
    if st.button("Predict"):
        
        result = prediction(Airline, Source, Destination, Duration ,Total_Stops, Additional_Info, Day, Month)
        st.text(f"The Flight price is: {result}")
Main()
