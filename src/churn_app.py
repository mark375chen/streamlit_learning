import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import seaborn as sns
import matplotlib.pyplot as plt


def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}"download="churn_data.csv">Download CSV File</a>'

    return href


def run_app():
    st.write("""
# Churn Prediction App

Customer churn is defined as the loss of customers after a certain period of time. Companies are interested in targeting customers

who are likely to churn. They can target these customers with special deals and promotions to influence them to stay with

the company. 

This app predicts the probability of a customer churning using Telco Customer data. Here

customer churn means the customer does not make another purchase after a period of time. 
""")

    df_selected = pd.read_csv(r'C:\Users\markz\PycharmProjects\streamlit_learning\src\telco_churn.csv')

    df_selected_all = df_selected[['gender', 'Partner', 'Dependents', 'PhoneService',
                                   'tenure', 'MonthlyCharges', 'target']].copy()

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.markdown(file_download(df_selected_all), unsafe_allow_html=True)
