import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


def sidebar(cookies):
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Quản lý tài khoản MetaTrader', ('MetaTraderProvider', 'MetaTraderAccount'))
    st.sidebar.markdown("---")  # Add a separator line
    page = st.sidebar.selectbox('Quản lý tài khoản', ('MetaTrader4', 'MetaTrader5'))
    st.sidebar.markdown("---")
    page = st.sidebar.selectbox('Quản lý danh sách lệnh', ('MetaTrader4', 'MetaTrader5'))
    st.sidebar.markdown("---")
    page = st.sidebar.selectbox('Phân tích kỹ thuật', ('MetaTrader4', 'MetaTrader5'))
    st.sidebar.markdown("---")
    if 'Username' in st.session_state:
        st.sidebar.markdown(f"Hello, {st.session_state['Username']}")

    if page != st.session_state.get('page'):
        st.session_state['page'] = page
        cookies["page"] = page
        cookies.save()

    if st.sidebar.button('Logout'):
        st.session_state['logged_in'] = False
        cookies["logged_in"] = "false"
        cookies.save()

    return st.session_state['page']