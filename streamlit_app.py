import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parents new healthy diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale, spinach and rocket smoothie')
streamlit.text('🐔 hard_boiled free_range eggs')
streamlit.text('🥑🍞 avocado bread')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.

streamlit.dataframe(my_fruit_list)

#create function
def get_fruityvice_data(this_fruit_choice):
#Can You Add A Second Text Entry Box? streamlitimport requests
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
#streamlit.text(fruityvice_response.json())

        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
        return fruityvice_normalized

#New section to display fruityvise api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #streamlit.write('The user entered ', fruit_choice)
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)




except URLError as e:
  streamlit.error()



streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit load list contains:")
streamlit.dataframe(my_data_row)

#add_my_fruit = streamlit.text_input('enter second fruit')

#streamlit.write(add_my_fruit)



#streamlit.write(add_my_fruit)

#streamlit.write('thanks for adding', add_my_fruit)
#allow user to add fruit
def insert_row_snowflake(new_fruit):
        with my_cnx_cursor() as my_cur:
                my_cur.execute("insert into fruit_load_list values ('jackfruit' + 'papaya' + 'guava' + 'kiwi')")
                return "thanks for adding" + new_fruit
        
add_my_fruit = streamlit.text_input('enter seconf fruit')
if streamlit.button('add a fruit to the list'):
        my_cnx = snowflaake.connector.connect(**streamlit.secrets["snowflake"])
        back_from_function = insert_row_snowflake(add_my_fruit)
        streamlit.text(back_from_function)
