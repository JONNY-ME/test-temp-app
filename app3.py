import streamlit
import re


def clear_page():
    streamlit.empty()
    streamlit.write('You can close the tabs now.')


def main_page():
    streamlit.write(
    """
    There are many tabs in your browser. Accessing the webiste needs more resources. 
    So closing the tabs is necessary and but before closing the tabs you can store all the links in the below. 
    Add them one by one. Select the "All done" option when you finish addning all the active tabs.
    """
    )


    links_stored = False
    def check_links():
        if not stored_links:
            streamlit.write('You have not added any links.')
        else:
            streamlit.write('You have added the following links:')
            for i, link in enumerate(stored_links):
                streamlit.write(f'{i + 1}. {link}')

            global links_stored
            links_stored = True


    button = streamlit.button('All done', on_click=check_links)


    n_inputs = 0

    streamlit.write('Enter the links below:')
    link = streamlit.text_input('Link')

    stored_links = []

    while 1:
        if link:
            stored_links.append(link)
            n_inputs += 1
            link = streamlit.text_input(f'Link {n_inputs}')
        if links_stored:
            break
    
    return stored_links


if __name__ == '__main__':
    main_page()
    clear_page()
