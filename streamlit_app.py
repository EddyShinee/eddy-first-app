import streamlit as st
from Utils.Auth import validate_login
import Pages.Home.Home as home
import Pages.About.About as about
import Pages.Contact.Contact as contact
import Pages.MetaTraderAccount.MetaTraderAccount as mtaccount  # Import the MetaTraderAccount module
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
        # Use a dictionary to switch between pages
        page = st.session_state['page']
        pages = {
            'Home': home.app,
            'About': about.app,
            'Contact': contact.app,
            'MetaTraderAccount': mtaccount.app
        }
        # Call the function corresponding to the current page
        if page in pages:
            pages[page]()

def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if validate_login(username, password):
            st.session_state['logged_in'] = True
            cookies["logged_in"] = "true"
            cookies.save()
            # st.session_state['page'] = 'Home'
            # cookies["page"] = 'Home'
            # st.experimental_set_query_params(logged_in='true', page='Home')
            # st.stop()  # Stop execution to refresh the UI
        else:
            st.error('Invalid username or password')

def sidebar():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Home', 'About', 'Contact', 'MetaTraderAccount'))
    if page != st.session_state['page']:
        st.session_state['page'] = page
        cookies["page"] = page
        cookies.save()

    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        cookies["logged_in"] = "false"
        cookies.save()

if __name__ == '__main__':
    main()