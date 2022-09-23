import streamlit as st
from deta import Deta
# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    email = st.text_input("Your email")
    submitted = st.form_submit_button("Store in database")
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    deta.put({"name": name, "age": age, "email": email})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# deta_content is a list of dictionaries. You can do everything you want with it.
    deta_content = db.fetch().items
st.write(deta_content)
