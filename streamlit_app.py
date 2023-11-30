import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header("Breakfast Menu")

streamlit.text('Broccoli,asparagus,oats')

 
streamlit.title("Breakfast FAvorites")
streamlit.text('🥣Omega3 and blueberry oat meal')
streamlit.text(' 🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔hard boiled free cage egg')
streamlit.text('🥑🍞avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
