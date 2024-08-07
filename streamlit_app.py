import streamlit as st
from Utils.Auth import validate_login
import Pages.Home.Home as home
import Pages.About.About as about
import Pages.Contact.Contact as contact

def main():
    if 'logged_in' not in st.session_state:
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
            # st.set_query_params['logged_in']=True  # Refresh the page
        else:
            st.error('Invalid username or password')

def sidebar():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Home', 'About', 'Contact'))
    st.session_state['page'] = page
    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        # st.set_query_params['logged_in']=False  # Refresh the page

if __name__ == '__main__':
    main()