import streamlit as st
import pandas as pd

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Bleuberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled 3 Free-Range')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
My_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
My_fruit_list= My_fruit_list.set_index("Fruit")

st.multiselect("Pick some fruits:", list(My_fruit_list.index),['Avocado','Strawberries'])
st.dataframe(My_fruit_list)
