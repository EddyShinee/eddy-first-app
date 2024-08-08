import streamlit as st
from Utils.Auth import validate_login
import Pages.Home.Home as home
import Pages.About.About as about
import Pages.Contact.Contact as contact
import Pages.AccountMetaTrader.AccountMetaTrader as accountmt
import Pages.Dashboard.Dashboard as db
import Pages.MetaTrader.MT4.MT4 as MT4
import Pages.MetaTrader.MT5.MT5 as MT5
from streamlit_cookies_manager import EncryptedCookieManager
from SideBar.SideBar import sidebar

# Set page configuration to use the full width
st.set_page_config(page_title="Eddy Shinee", layout="wide")
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
        page = sidebar(cookies)
        print(page)
        # Use a dictionary to switch between pages
        pages = {
            'Home': home.app,
            'About': about.app,
            'Contact': contact.app,
            'AccountMetaTrader': accountmt.app,
            'Dashboard': db.app,
            'MetaTrader4': MT4.app,
            'MetaTrader5': MT5.app
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
            cookies["Username"] = username
            cookies.save()
            st.rerun()
            # Refresh the page to update the state
            # st.experimental_rerun()
        else:
            st.error('Invalid username or password')

if __name__ == '__main__':
    main()