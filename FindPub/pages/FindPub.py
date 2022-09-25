from turtle import width
import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide'
)

df = pd.read_csv('Data/open_pubs.csv')

lat = st.sidebar.number_input(
    "Latitude",
    format="%.6f")
long = st.sidebar.number_input('Longitude',
    format="%.6f")


city = df['local_authority'].unique().tolist()
option = st.sidebar.selectbox("Select option", options=city)

df_map = df.query('latitude >= @lat & longitude <= @long  & local_authority == @option')
st.map(df_map.head(10))


