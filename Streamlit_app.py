import streamlit
streamlit.title('My parents healthy diner')

streamlit.title('Breakfast menu')
streamlit.title('omega3 and oate meal')
streamlit.title('kale , spinach Rocket smoothie')
streamlit.title('Hard-Boiled egg, free-range egg')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado and Toast ')
streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
