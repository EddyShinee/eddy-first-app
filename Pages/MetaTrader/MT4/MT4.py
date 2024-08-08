import streamlit as st

def app():
    st.title("MT4")
    st.write("Welcome to the Home page!")
    tab1, tab2 = st.tabs(["Demo Account", "Live Account"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")