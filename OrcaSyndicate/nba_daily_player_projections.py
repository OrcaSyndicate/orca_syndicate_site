import streamlit as st
import pandas as pd
import plost
import altair as alt


st.set_page_config(layout="wide")
if 'user_subscribed' not in st.session_state:
    st.session_state['user_subscribed'] = False

st.markdown("###### _*Note that players must have played in at least 5 games this season in order to qualify for the tables._")

st.header('Free Player Projections',divider="gray")
data_comb1 = pd.read_excel('C:/Users/ajaku/Downloads/NBA_Prop_Projections_RAW.xlsx',usecols=list(range(0,17)))
data_comb1 = data_comb1.dropna(subset=['player'])
data_comb1['date'] = pd.to_datetime(data_comb1['date']).dt.strftime('%m-%d-%Y')
data_comb11 =  data_comb1.rename(columns={'Final Min. Est.': 'minutes_est','Pts. Est.': 'pts_proj','RA Est.':'ra_proj'})
#data_comb1 = data_comb1.rename(columns={'Pred. Completions':'Cmp. Proj.'})
columns_to_format_as_decimal = ['Final Min. Est.','Pts. Est.','Reb. Est.','Ast. Est.','Blk Est.','Stl Est.','3PM Est.','TO Est.','SB Est.','PRA Est.','RA Est.','PA Est.','PR Est.']
for column in columns_to_format_as_decimal:
  data_comb1[column] = data_comb1[column].map('{:.2f}'.format)

team2 = sorted(data_comb1['team'].unique())
selected_team2 = st.selectbox('team:', ['All'] + list(team2), key='Players')
if selected_team2 != 'All':
    filtered_df2 = data_comb1[(data_comb1['team'] == selected_team2)]
else:
    filtered_df2 = data_comb1
st.dataframe(filtered_df2,hide_index=True)
st.write('')
st.write('')

st.header('Key Statistic Summary Charts',divider="gray")

chart = alt.Chart(data_comb11).mark_circle().encode(
    
    x=alt.X('minutes_est', sort='ascending',axis=alt.Axis(format='.1f')) ,
    y=alt.Y('pts_proj', sort='ascending',axis=alt.Axis(format='.1f')),
    tooltip=['player', 'minutes_est', 'pts_proj']
).interactive()

chart1 = alt.Chart(data_comb11).mark_circle().encode(
    
    x=alt.X('minutes_est', sort='ascending',axis=alt.Axis(format='.1f')) ,
    y=alt.Y('ra_proj', sort='ascending',axis=alt.Axis(format='.1f')),
    tooltip=['player', 'minutes_est', 'ra_proj']
).interactive()

summaries = st.columns(2)
#st.altair_chart(chart)
summaries[0].altair_chart(chart)
summaries[1].altair_chart(chart1)


st.header('Premium Player Projections',divider="gray")

def display_login_status():
    if st.session_state['user_subscribed']==True:
    #if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write('')
        data_comb2 = pd.read_excel('C:/Users/ajaku/Downloads/NBA_Prop_Projections_RAW.xlsx',usecols=[0,1,2,18,19,20,21,22])
        data_comb2 = data_comb2.dropna(subset=['player'])
        data_comb2['date'] = pd.to_datetime(data_comb2['date']).dt.strftime('%m-%d-%Y')
        #data_comb21 =  data_comb2.rename(columns={'Final Min. Est.': 'minutes_est','Pts. Est.': 'pts_proj','RA Est.':'ra_proj'})
        #columns_to_format_as_decimal = ['Final Min. Est.','Pts. Est.']
        team = sorted(data_comb2['team'].unique())
        selected_team21 = st.selectbox('team:', ['All'] + list(team), key='Players2')
        if selected_team2 != 'All':
            filtered_df = data_comb2[(data_comb2['Team'] == selected_team21)]
        else:
            filtered_df = data_comb2
        st.dataframe(filtered_df,hide_index=True)

    else:
        #st.header('Suggested Bets',divider="gray")
        st.write("Subscribe now for full access to all premium data! Includes first basket probabilities, double-double & triple double probabilities, and DFS point projections.")
        st.write('')
    
display_login_status()  

