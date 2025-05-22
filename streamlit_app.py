import streamlit as st
import requests

st.title('Hello, FastAPI + Streamlit!')
st.write('This is a simple Streamlit Application')


# Create text input fields for user data
email = st.text_input("Email", value="")
password = st.text_input("Password", value="", type="password")

# Create a button to send the POST request when clicked
if st.button("Create User"):
    # Define the new user data
    new_user = {
        "email": email,
        "password": password
    }

    # Make the POST request
    response = requests.post('http://localhost:8000/create-user', json=new_user)

    # Check if the request was successful
    if response.status_code == 201:
        data = response.json()
        st.success("User created successfully!")
        st.write(data)
    else:
        st.error("Failed to create user")

