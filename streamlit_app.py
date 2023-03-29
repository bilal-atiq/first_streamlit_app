import streamlit
import pandas

streamlit.title('my parents new healthy diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale, spinach and rocket smoothie')
streamlit.text('🐔 hard_boiled free_range eggs')
streamlit.text('🥑🍞 avocado bread')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
