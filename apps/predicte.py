import threading
import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import requests
from streamlit_lottie import st_lottie
import json
import pickle
import numpy as np
from imp import load_module

def app (): 

  st.title('Predict')

  st.subheader("Please, fill in this with your own records")

  def load_modle () :
    with open ('clf.pkl', 'rb') as pickle_in:
     clf = pickle.load(pickle_in)
    return clf
  clf = load_modle()

  Age = st.number_input('Insert your age')

  Weight = st.number_input('Insert your weight')
 
  Cholesterol = st.number_input('Insert your Cholesterol level')

  Bmi = st.number_input('Insert body mass index (BMI)')

  Glucose = st.number_input('Insert your Glucose level')

  Hdl_chol = st.number_input('Insert high-density lipoprotein cholesterol ratio')

  Chol_hdl_ratio = st.number_input('Insert cholesterol HDL ratio ')

  Systolic_bp = st.number_input('Insert systolic blood pressure level')

  Diastolic_bp = st.number_input('Insert diastolic blood pressure level')

  Waist_hip_ratio = st.number_input('Insert waist to hip ratio')

  ok = st.button ("Start prediction")    

  #!--------main function----------

  def prediction(cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, weight, bmi, systolic_bp, diastolic_bp, waist_hip_ratio):
      prediction = clf.predict(
            [[cholesterol, glucose, hdl_chol, chol_hdl_ratio, age, weight, bmi, systolic_bp, diastolic_bp, waist_hip_ratio]])        
      return(prediction)
  if ok :
        st.subheader(f"You may have{prediction(Cholesterol,Glucose,Hdl_chol,Chol_hdl_ratio,Age,Weight,Bmi,Systolic_bp,Diastolic_bp,Waist_hip_ratio)}")



        #!------loading the animation----------
 
  def load_lottiefile (filepath: str):
     
    with open (filepath, "r") as f :
      return json.load(f) 

  lottie_doctor = load_lottiefile("lottiefiles/doctor.json")

  left_column , right_column = st.columns(2)

  with right_column:

   st_lottie(lottie_doctor, height=300, width=300, key="doctor")    
