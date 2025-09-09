# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 13:36:11 2025

@author: urmilesh
"""
import numpy as np
import pickle
import streamlit as st
#loading the saved model
loaded_model=pickle.load(open('C:/Users/urmil/OneDrive/Documents/ml-deployment/trained_model.sav','rb'))

# creating a prediction function

def diabetes_prediction(input_data):
    input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

def main():
    # giving a title
    st.title("Diabetes Prediction Web App")
    
    #getting the input data from user					
    Pregnancies=st.text_input("Number of pregnancies")
    Glucose=st.text_input("Glucose level")
    BloodPressure=st.text_input("BP value")
    SkinThickness=st.text_input("skin thickness value")
    Insulin=st.text_input("insulin level")
    BMI=st.text_input("bmi value")
    DiabetesPedigreeFunction=st.text_input("dpf value")
    Age	=st.text_input("age of the person")
    
    #code for prediction
    diagnosis=""
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()

