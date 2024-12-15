import streamlit as st

class Page:
    def __init__(self, title):
        self.title = title

    def page_content(self):
        raise NotImplementedError

    def run(self):
        st.title(self.title)
        self.page_content()

class Page1(Page):
    def page_content(self):
        st.write("""
                .. ..-. / -.-- --- ..- / -.-. .- -. / ..- -. -.. . .-. ... - .- -. -.. / - .... .. ... / -. .- ...- .. --. .- - . / - --- / .--. .- --. . / - .-- --- / .. -. / - .... . / ... .. -.. . / -... .- .-. -.-.--
        """)

class Page2(Page):
    def page_content(self):
        st.write("""
                 01001110 01101111 01110111 00100000 01101110 01100001 01110110 01101001 01100111 01100001 01110100 01100101 00100000 01110100 01101111 00100000 01110000 01100001 01100111 01100101 00100000 01110100 01101000 01110010 01100101 01100101 00001010
        """)

class Page3(Page):
    def page_content(self):
        st.markdown("""
                 Tl yzxp gl gsv fhvi hzbrmt "Gsv dvyhrgv rh zdvhlnv". Fhv gsrh [ormp](https://geeks-for-geeks.streamlit.app) gl tvg yzxp gl kztv lmv
                 """)

def main():
    pages = {
        "Page 1": Page1("Page 1"),
        "Page 2": Page2("Page 2"),
        "Page 3": Page3("Page 3"),
    }
    page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[page].run()

if __name__ == "__main__":
    main()









