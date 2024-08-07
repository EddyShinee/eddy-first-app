import streamlit as st
from Utils.Auth import validate_login
import Pages.Home.Home as home
import Pages.About.About as about
import Pages.Contact.Contact as contact
from streamlit_cookies_manager import EncryptedCookieManager

# Create a cookie manager
cookies = EncryptedCookieManager(
    prefix="myapp_",  # prefix for cookie names
    password="your_password",  # this is the encryption key
)

if not cookies.ready():
    st.stop()

def main():
    if 'logged_in' not in st.session_state:
        # Check if there's a login cookie
        if cookies.get("logged_in") == "true":
            st.session_state['logged_in'] = True
            st.session_state['page'] = cookies.get("page", "Home")
        else:
            st.session_state['logged_in'] = False
            st.session_state['page'] = 'Home'

    if not st.session_state['logged_in']:
        login()
    else:
        sidebar()
        if st.session_state['page'] == 'Home':
            home.app()
        elif st.session_state['page'] == 'About':
            about.app()
        elif st.session_state['page'] == 'Contact':
            contact.app()

def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if validate_login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'Home'
            cookies["logged_in"] = "true"
            cookies["page"] = 'Home'
            cookies.save()
            # st.experimental_rerun()
        else:
            st.error('Invalid username or password')

def sidebar():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Home', 'About', 'Contact'))
    st.session_state['page'] = page
    cookies["page"] = page
    cookies.save()
    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        cookies["logged_in"] = "false"
        cookies.save()
        # st.experimental_rerun()

if __name__ == '__main__':
    main()