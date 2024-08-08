import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

def sidebar(cookies):
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Quản lý tài khoản MetaTrader', ('AccountMetaTrader', 'MetaTraderAccount'))
    st.sidebar.markdown("---")  # Add a separator line
    page = st.sidebar.radio('Quản lý tài khoản', ('MetaTrader4', 'MetaTrader5'))
    st.sidebar.markdown("---")
    page = st.sidebar.radio('Quản lý danh sách lệnh', ('MetaTrader4', 'MetaTrader5'))
    st.sidebar.markdown("---")

    # Check if Username exists in cookies
    username = cookies.get("Username")
    if username:
        st.sidebar.markdown(f"Hello, {username}")

    if 'page' in st.session_state:
        if cookies.get("page") != st.session_state['page']:
            cookies["page"] = st.session_state['page']
            cookies.save()
            st.rerun()  # Refresh the page only if the page state has changed

    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        cookies["logged_in"] = "false"
        cookies.save()
        st.rerun()
    return st.session_state.get('page', 'Home')