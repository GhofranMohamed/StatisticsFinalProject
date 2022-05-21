import streamlit as st
from multiapp import MultiApp
from apps import welcome, explore, predicte # import your app modules here

app = MultiApp()


st.markdown("""
    # Diabetes Prediction """)

# Add all your application here
app.add_app("Welcome", welcome.app)
app.add_app("Explore", explore.app)
app.add_app("Predict", predicte.app)
# The main app
app.run()
