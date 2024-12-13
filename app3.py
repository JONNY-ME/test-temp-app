import streamlit

streamlit.title('Streamlit App')

def clear_page():
    streamlit.empty()
    streamlit.write('You can close the tabs now.')


def main_page():



    streamlit.write(
    """
    There are many tabs in your browser. Accessing the website needs more resources.  So closing the tabs is necessary. You may re-open them after accessing the website. But before closing the tabs you have to store all the U-R-Ls in the below.  Add them one by one. Select the "All done" option when you finish adding all the active tabs.
    """, unsafe_allow_html=True, 
    )


    links_stored = False
    def check_links():
        if not stored_links:
            streamlit.write('You have not added any U-R-Ls.')
        else:
            streamlit.write('You have added the following U-R-Ls:')
            for i, link in enumerate(stored_links):
                streamlit.write(f'{i + 1}. {link}')

            global links_stored
            links_stored = True


    button = streamlit.button('All done', on_click=check_links)


    n_inputs = 0

    streamlit.write('Enter the U-R-Ls below:')
    link = streamlit.text_input('U-R-Ls')

    stored_links = []

    while 1:
        if link:
            stored_links.append(link)
            n_inputs += 1
            link = streamlit.text_input(f'U-R-Ls {n_inputs}')
        if links_stored:
            break
    
    return stored_links


if __name__ == '__main__':
    main_page()
    clear_page()
