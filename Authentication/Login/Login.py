import streamlit as st
from Utils.Auth import validate_login

def login(cookies):
    st.title('Login')
    login_container = st.empty()
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    with login_container.container():
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if validate_login(username, password):
                st.session_state['logged_in'] = True
                cookies["logged_in"] = "true"
                cookies["Username"] = username
                cookies.save()
                st.rerun()  # Làm mới trang để cập nhật trạng thái
            else:
                st.error('Invalid username or password')
    st.markdown('</div>', unsafe_allow_html=True)