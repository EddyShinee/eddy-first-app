import streamlit as st

def validate_login(username, password):
    return username == 'admin' and password == 'admin'