from ssl import Options
from tkinter import Button
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/open_pubs.csv')

city = df['local_authority'].unique().tolist()
#st.text(len(city))
#st.text(city)

option = st.sidebar.selectbox("Select option", options=city)
st.sidebar.text(f"You selected option {option}")

df_selection = df.query(
    "local_authority == @option"
)
totalpub = len(df_selection)
st.header(f"Total number of pubs {totalpub} in selected location")

button_click = st.button('Pubs in your area')

column_left, column_right = st.columns(2)
with column_left:
    if button_click == True:
        st.map(df_selection)
with column_right:
    if button_click == True:
        st.markdown('List of pubs and its location')
        st.dataframe(df_selection)





  