import streamlit as st
from deta import Deta

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    email = st.text_input("Your email")
    county =st.text_input("Florida county you live in")
    attorney = st.text_input("Your attorney's name")
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("Connection_Streamlit")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age, "email": email, "county": county, "attorney": attorney})

"---"
"Thank you. Your electronic will is now securely stored."
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query="user.email?contains": email, limit=None, last=None).items
st.write(db_content)

st.image('./LOGO_091622.png')
