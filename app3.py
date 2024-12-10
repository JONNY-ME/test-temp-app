import streamlit

"""Portfolio"""

streamlit.title('Portfolio')

# all in the main area
streamlit.write('''
## Welcome to my portfolio
''')

streamlit.write('''
### About Me
I am a software developer with experience in Python, JavaScript, and SQL.
''')

streamlit.write('''
### Projects
- [Project 1](
- [Project 2](
- [Project 3](
''')

streamlit.write('''
### Contact
- [Email](mailto:
- [LinkedIn](https://www.linkedin.com/in/)
''')

streamlit.write('''
### Resume
- [Download](https://test-temp-app-nefurdi3fh4f4x3jymgskm.streamlit.app/)
''')


# set footer with an input
footer = """<style>
a:link , a:visited{
color: #0078E7;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #FF0000;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #f1f1f1;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Created with Love</p>
</div>
"""
streamlit.markdown(footer,unsafe_allow_html=True)