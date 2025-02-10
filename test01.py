import streamlit as st
import random

# Initialize variables
if "field_order" not in st.session_state:
    st.session_state.field_order = ["name", "email", "grade"]
    random.shuffle(st.session_state.field_order)
if "button_position" not in st.session_state:
    st.session_state.button_position = random.randint(0, len(st.session_state.field_order) - 1)

# Header
st.title("Form Filling Error Handling Test")

# Display the form
with st.form("test_form"):
    st.subheader("User Registration")
    
    form_data = {}
    submitted = None  # Initialize the submit button variable
    
    for index, field in enumerate(st.session_state.field_order):
        if field == "name":
            form_data["name"] = st.text_input("Name", key="name")
        elif field == "email":
            form_data["email"] = st.text_input("Email", key="email")
        elif field == "grade":
            form_data["grade"] = st.slider("Grade", 0, 100, 0, 1)
        
        # Randomly insert the submit button in different positions
        if index == st.session_state.button_position:
            submitted = st.form_submit_button("Submit")
    
    # Ensure submit button is placed if it was not inserted in the loop
    if submitted is None:
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        if any(value is None or value.strip() == "" for value in form_data.values()):
            st.error("Form submission failed due to missing fields.")
        else:
            st.success(f"Form submitted successfully! Name: {form_data['name']}, Email: {form_data['email']}")
