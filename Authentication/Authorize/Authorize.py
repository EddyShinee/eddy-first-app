import streamlit as st
from SideBar.SideBar import sidebar

def authorize_user(cookies):
    if 'logged_in' not in st.session_state:
        # Kiểm tra nếu đã có cookie đăng nhập
        if cookies.get("logged_in") == "true":
            st.session_state['logged_in'] = True
            st.session_state['page'] = cookies.get("page", "Home")
        else:
            st.session_state['logged_in'] = False
            st.session_state['page'] = 'Home'

    if st.session_state['logged_in']:
        page = sidebar(cookies)
        return page
    else:
        return None