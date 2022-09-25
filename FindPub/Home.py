from ctypes import alignment
from turtle import color
import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title="LandOnPub" ,
    page_icon =':wink:',
    layout='wide'
)

df = pd.read_csv('Data/open_pubs.csv')

st.title("Hello, Welcome to LandOnPub United Kingdom")
img = Image.open("Image/pubs.jpg")
column_left, column_right = st.columns(2)
count = df.groupby(['local_authority']).size()
with column_left:
    st.image(img,width=370)
    Count1 = df['name'].count()
    Count2 = count.count()
    st.title(f' {Count1} pubs in {Count2} cities')
with column_right:
    
    st.bar_chart(count,use_container_width=True)



st.sidebar.success("select page abve")