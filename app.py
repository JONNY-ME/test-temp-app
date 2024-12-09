import streamlit as st

'''
App that simulates an interactive calculator
'''

# Title
st.title('Interactive Calculator')

# Sidebar
st.sidebar.title('Calculator')
num1 = st.sidebar.number_input('Enter first number', value=0)
num2 = st.sidebar.number_input('Enter second number', value=0)

# Operations
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
operation = st.sidebar.selectbox('Select operation', operations)

# Calculate
if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 == 0:
        result = 'Cannot divide by zero'
    else:
        result = num1 / num2