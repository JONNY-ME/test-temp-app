import streamlit as st

# Streamlit app title
st.title("Translator Job Recruitment Form")
st.subheader("Arabic to English Translator Position")

# Personal Information Section
st.header("Personal Information")
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
country = st.text_input("Country of Residence")
# authorized = st.radio("Are you legally authorized to work in this country?", ("Yes", "No"))

# Language Proficiency Section
st.header("Language Proficiency")
arabic_level = st.selectbox(
    "How would you rate your Arabic language level?",
    ["Beginner", "Intermediate", "Advanced", "Native/Fluent"]
)
english_level = st.selectbox(
    "How would you rate your English language level?",
    ["Beginner", "Intermediate", "Advanced", "Native/Fluent"]
)

# Screening Notification
st.header("Screening Process Notification")
screening_ack = st.checkbox(
    "I acknowledge that further screening (e.g., translation tests, interviews) may be required."
)

# Submit Button
if st.button("Submit Application"):
    if full_name and email and phone and screening_ack:
        st.success("Thank you for your application! We will review your information and contact you for the next steps.")
    else:
        st.error("Please complete all required fields and acknowledge the screening process.")

# Optional: Display user input for confirmation (for testing)
st.write("### Your Input:")
st.write(f"Full Name: {full_name}")
st.write(f"Email: {email}")
st.write(f"Phone: {phone}")
st.write(f"Country: {country}")
st.write(f"Authorized to work: {authorized}")
st.write(f"Arabic Level: {arabic_level}")
st.write(f"English Level: {english_level}")
st.write(f"Screening Acknowledged: {'Yes' if screening_ack else 'No'}")
