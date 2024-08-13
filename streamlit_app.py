import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from Authentication.Login.Login import login  # Import hàm login từ file Login.py
from Authentication.Authorize.Authorize import authorize_user  # Import hàm authorize từ file Authorize.py

import Pages.Home.Home as home
import Pages.About.About as about
import Pages.Contact.Contact as contact
import Pages.AccountMetaTrader.AccountMetaTrader as accountmt
import Pages.Dashboard.Dashboard as db
import Pages.MetaTrader.MT4.MT4 as MT4
import Pages.MetaTrader.MT5.MT5 as MT5

# Set page configuration to use the full width
st.set_page_config(
    page_title="Eddy - Adam Project",
    page_icon=":shark:",  # Can be an emoji or a URL to an image
    layout="wide",  # Options: "centered", "wide"
    initial_sidebar_state="auto",  # Options: "auto", "expanded", "collapsed"
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://www.extremelycoolapp.com/bug',
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Create a cookie manager
cookies = EncryptedCookieManager(
    prefix="myapp_",  # prefix for cookie names
    password="your_password",  # this is the encryption key
)

if not cookies.ready():
    st.stop()

# Main function to control the app flow
def main():
    page = authorize_user(cookies)

    if page is None:
        login(cookies)  # Gọi hàm login từ file Login.py
    else:
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

if __name__ == '__main__':
    main()