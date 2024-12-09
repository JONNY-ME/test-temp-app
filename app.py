import streamlit as st

'''
App that simulates an interactive calculator
'''

# Title
st.title('Interactive Calculator')

# Sidebar
st.sidebar.title('Calculator')
# any input not only number 
num1 = st.sidebar.text_input('Enter first number')
num2 = st.sidebar.text_input('Enter second number')

# Operations
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Other']
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
else:
    result = 'None'

# submit button
st.sidebar.button('Calculate')

# Display result
st.write(f'Result: {result}')
