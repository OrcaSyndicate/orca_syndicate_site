import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("ATP Moneyline Bets")
st.write("")

file_path = 'site_documents/atp_display_ml.csv'
data = pd.read_csv(file_path)   
data['P1 ML'] = data['P1 ML'].map('{:.2f}'.format)
data['P2 ML'] = data['P2 ML'].map('{:.2f}'.format)
data['P2 MC Win Prob.'] = 1 - data['P1 MC Win Prob.'] 
data['P1 MC Win Prob.'] = data['P1 MC Win Prob.'].map(lambda x: '{:.1f}%'.format(x * 100))
data['P2 MC Win Prob.'] = data['P2 MC Win Prob.'].map(lambda x: '{:.1f}%'.format(x * 100))

st.dataframe(data,hide_index=True)
st.write('')

st.header("ATP Spread Bets")
file_path1 = 'site_documents/atp_display_spr.csv'
data1 = pd.read_csv(file_path1)   
data1['P1 Spread Odds'] = data1['P1 Spread Odds'].map('{:.2f}'.format)
data1['P2 Spread Odds'] = data1['P2 Spread Odds'].map('{:.2f}'.format)
data1['P2 MC Cover Prob.'] = 1- data1['P1 MC Cover Prob.'] 
data1['P1 MC Cover Prob.'] = data1['P1 MC Cover Prob.'].map(lambda x: '{:.1f}%'.format(x * 100))
data1['P2 MC Cover Prob.'] = data1['P2 MC Cover Prob.'].map(lambda x: '{:.1f}%'.format(x * 100))

st.dataframe(data1,hide_index=True)
