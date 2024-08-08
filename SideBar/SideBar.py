import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

def sidebar(cookies):
    st.sidebar.title('Navigation')

    # Sử dụng radio để chọn trang
    page = st.sidebar.radio('Điều hướng',('Home', 'About', 'Contact'))
    st.session_state['page'] = page
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