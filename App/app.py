import streamlit as st
import pandas as pd
import numpy as np

st.title("Base de Dados - Casal")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['England','Germany','Italy','Spain','France'])

st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season',['2022/2021', '2021/2020', '2020/2019'])

#Webscraping Football Data



def load_data(league, season):
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)


                  
