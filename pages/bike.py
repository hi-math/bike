import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "Noname"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f"{ID}님 안녕하세요.")
    
data = pd.read_csv("공공자전거.csv")
data = data.copy().fillna(0)
data['total']= 5*(data["LCD"]+data["QR"])+6

color = {'QR':'#09d99a',
         'LCD':'#ebbb37'}
data['color'] = data.copy()['운영방식'].map(color)

data 
st.map(data,
       latitude="위도",
       longitude="경도",
       size = "total",
       color = "color")
