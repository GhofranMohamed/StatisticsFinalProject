from operator import index
from turtle import width
from randomforestmodified import X
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import requests
from streamlit_lottie import st_lottie
import json
import matplotlib.pyplot as plt
import seaborn as sns 
import altair as alt



def app():


  #!-------loading the animation---------

  def load_lottiefile (filepath: str):
     
    with open (filepath, "r") as f :
      return json.load(f) 

  lottie_robot = load_lottiefile("lottiefiles/robot.json")

  left_column , right_column = st.columns(2)

  with right_column:

    st_lottie(lottie_robot, height=300, width=300, key="doctor")

  st.title('Explore')

  st.subheader("This page shows diabetes distrubtion among different catogries in our data")  

  def load_Data ():
    data = pd.read_csv(r'C:\users\gufran\desktop\data\diabetes1.csv')

    data['chol_hdl_ratio']=data['chol_hdl_ratio'].str.replace('"', ' ', 2)

    data['bmi']=data['bmi'].str.replace('"', ' ', 2)

    data['waist_hip_ratio']= data['waist_hip_ratio'].str.replace('"', ' ', 2)

    data['chol_hdl_ratio']= pd.to_numeric(data['chol_hdl_ratio'].str.replace(',', '.'))

    data['bmi']= pd.to_numeric(data['bmi'].str.replace(',', '.'))
  
    data['waist_hip_ratio']= pd.to_numeric(data['waist_hip_ratio'].str.replace(',', '.'))

    data['diabetes']= data['diabetes'].str.replace('No diabetes' ,'1')

    data['diabetes']= data['diabetes'].str.replace('Diabetes' ,'0')

    data['diabetes']= pd.to_numeric(data['diabetes'])
    return data

  data = load_Data()

  st.write("diabetes withing differnet ages")
  DATA = data.groupby(['age'])['diabetes'].mean().sort_values(ascending=True)
  st.bar_chart(DATA)

  st.write("diabetes withing differnet cholesterol levels")
  DATA1 = data.groupby(['cholesterol'])['diabetes'].mean().sort_values(ascending=True)
  st.line_chart(DATA1)

  st.write("diabetes withing differnet weights")
  DATA2 = data.groupby(['weight'])['diabetes'].mean().sort_values(ascending=True)
  st.bar_chart(DATA2)

  st.write("diabetes withing differnet glucose levels")
  DATA3 = data.groupby(['glucose'])['diabetes'].mean().sort_values(ascending=True)
  st.line_chart(DATA3)

  DATA4 = data['glucose'].value_counts()
  fig1, ax1 = plt.subplots()
  ax1.pie(DATA4, labels=DATA4.index, autopct="%0.00000000000000000001f%%", shadow=True , startangle=0)
  ax1.axis("equal")

  st.pyplot(fig1)
  