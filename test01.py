import streamlit as st
import random

# Initialize variables
if "hidden_field" not in st.session_state:
    st.session_state.hidden_field = None
    st.session_state.changed_labels = {
        "name": "Name",
        "email": "Email",
        "grade": "Grade",
    }

# Header
st.title("Summer School Registration")

# Display the form
with st.form("test_form"):
    st.subheader("Student Registration Form")
    
    if st.session_state.hidden_field != "name":
        name = st.text_input(st.session_state.changed_labels["name"], key="name")
    else:
        name = None
        st.warning("Name field is missing!")
    
    # Email field is intentionally missing to trigger the error
    st.text("Email")
    email = None  # Email field is missing
    
    if st.session_state.hidden_field != "grade":
        grade = st.slider(st.session_state.changed_labels["grade"], 0, 100, 50, 1)
    else:
        grade = None
        st.warning("Grade field is missing!")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        missing = []
        if name is None:
            missing.append("Name")
        if email is None:
            missing.append("Email")
        if grade is None:
            missing.append("Grade")
        if missing:
            st.error(f"Form submission failed due to missing fields: {', '.join(missing)}")
        else:
            st.success(f"Form submitted successfully! Name: {name}, Email: {email}")