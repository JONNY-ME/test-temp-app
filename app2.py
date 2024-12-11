import streamlit as st
import re 

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

if str(num).isnumeric():
    st.sidebar.write('You entered a number')
else:
    raise ValueError('You did not enter a number')

# Name
st.sidebar.write('checking name input')
name = st.sidebar.text_input('Enter a random name')

if name:
    st.sidebar.write('You entered a name')
else:
    raise ValueError('You did not enter a name')

# Email
st.sidebar.write('checking email input')
email = st.sidebar.text_input('Enter a valid email')

mail = re.compile(r'[^@]+@[^@]+\.[^@]+')
if mail.match(email) and email.endswith('@oaisb.info'):
    st.sidebar.write('You entered an email')
else:
    if mail.match(email):
        st.sidebar.write('only oaisb.info email is allowed')
    else:
        st.sidebar.write('Please enter a valid email')
    raise ValueError('You did not enter an email')