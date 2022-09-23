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
db = deta

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    deta.put({"name": name, "age": age, "email": email, "County": county})
"---"
"Thank you, your electronic Will is now safely stored"
