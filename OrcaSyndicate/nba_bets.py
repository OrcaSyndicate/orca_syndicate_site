import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
if 'user_subscribed' not in st.session_state:
    st.session_state['user_subscribed'] = False
    
st.header('NBA Team Model Bets',divider="gray")
st.markdown("### _Collecting data during the first five games for each team, check back later!_")
#st.markdown("### _Currently in the offseason, check back later!_")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_team_placeholder.png?raw=true')


def display_login_status():
    if st.session_state['user_subscribed']==True:
    #if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write('')
        st.header('Suggested Bets',divider="gray")
        st.subheader('Team-Level Game Model')


        st.subheader('Player-Level Game Model')

        st.write('')

    
    
    else:
        st.header('Suggested Bets',divider="gray")
        st.subheader('Team-Level Game Model')


        st.subheader('Player-Level Game Model')
        st.write("Subscribe now for full access to all player-level model bets!")
        st.write('')
        #st.header('All Prop Bets Available',divider="gray")
        #st.dataframe(styled_df_py, hide_index=True)

        #st.dataframe(data_comb1.style.background_gradient(cmap="RdYlGn", subset=['EV','Edge']),hide_index=True) 
display_login_status()  
