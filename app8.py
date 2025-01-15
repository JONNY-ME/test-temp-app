import streamlit as st


st.set_page_config(page_title="Textra", page_icon="📱", layout="wide")

st.sidebar.title("Textra")
page = st.sidebar.radio("Go to", ["Home", "Contact", "Newsletter"])

if page == "Home":
    st.title("Textra - Welcome to the Text Era")
    st.write("""
    ## The Future of Text Communication
    Welcome to Textra, your hub for everything related to the Text Era. 
    Explore trends, innovations, and insights in the ever-evolving world of text communication.
    """)
    st.write("""
    **Features:**
    - Latest updates in text technology
    - Expert articles and insights
    - Stay connected with the world of communication evolution
    """)

elif page == "Contact":
    st.title("Contact Us")
    st.write("""
    ## We'd Love to Hear From You
    Whether you have questions, feedback, or just want to say hello, feel free to reach out to us.
    """)
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you for reaching out! We'll get back to you soon.")

elif page == "Newsletter":
    st.title("Subscribe to Our Newsletter")
    st.write("""
    ## Stay Updated with Textra
    Subscribe to our newsletter to receive the latest updates, insights, and trends in the Text Era directly to your inbox.
    """)
    
    phone_number = st.text_input("Enter your phone number")
    if st.button("Subscribe"):
        if phone_number:
            st.success(f"Thank you for subscribing! We will keep you updated at {phone_number}.")
        else:
            st.warning("Please enter a valid phone number to subscribe.")

st.markdown("""
---
Made with ❤️ by the Textra Team
""")
