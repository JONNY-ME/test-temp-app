import streamlit as st
import re 
import random

'''
App that simulates an interactive different types of user input
'''

# Title
st.title('Interactive Different Types of User Input')

# Sidebar
st.sidebar.title('User Input Types')

# Number
st.sidebar.write('checking number input')
num = st.sidebar.text_input('Enter any number')

if num:
    if str(num).isnumeric():
        st.sidebar.write('You entered a number')
    else:
        raise ValueError('You did not enter a number')

    # Name
    st.sidebar.write('checking name input')
    name = st.sidebar.text_input('Enter a random name')

    if name:
        if name.isalpha():
            st.sidebar.write('You entered a name')
        else:
            raise ValueError('You did not enter a name')

        def check_for_fake(email):
            if not email.endswith('@oaisb.info') or not email.startswith('paexternal'):
                return False

            return True

        samples = [
            "try to come up with a valid email with oaisb.info",
            "only paexternal email is allowed",
            "wrong! try user's email",
        ]


        # Email
        st.sidebar.write('checking email input')
        email = st.sidebar.text_input('Enter a valid email')

        if email:
            mail = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if mail.match(email) and check_for_fake(email):
                st.sidebar.write('You entered an email')
            else:
                if mail.match(email):
                    st.sidebar.write(random.choice(samples))
                else:
                    st.sidebar.write('Please enter a valid email')
                raise ValueError('You did not enter an email')