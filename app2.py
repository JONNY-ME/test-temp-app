import streamlit as st
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
num = st.sidebar.number_input('Enter first number')

if str(num).isdigit():
    st.sidebar.write('You entered 0')
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
email = st.sidebar.text_input('Enter a random email')

if '@' in email:
    st.sidebar.write('You entered an email')
else:
    raise ValueError('You did not enter an email')