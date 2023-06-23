import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥗Idli Dosa')
streamlit.text('🍞Pancake')
streamlit.text('🥣Orange Juice')
streamlit.text('🐔Eggs')
   
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lime'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()


streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list();
with my_cnx.cursor() as my_cur
my_cur.execute("SELECT * from fruit_load_list")
return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit Load List');
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows= get_fruit_load_list()
streamlit.dataframe(my_data_rows)

streamlit.write("what fruit you would like to add?")
fruit_choice1 = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding', fruit_choice1)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
