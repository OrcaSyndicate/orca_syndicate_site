import streamlit as st
import pandas as pd
from st_paywall import add_auth

st.set_page_config(layout="wide")

st.header('MLB Model Bets',divider="gray")

def display_login_status():
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write('')
    else:
        st.write("Subscribe now for full access to all our suggested bets!")

display_login_status()
