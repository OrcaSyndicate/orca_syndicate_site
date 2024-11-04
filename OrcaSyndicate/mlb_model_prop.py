import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Model Description',divider="gray")
mlb_intro = '''
Our MLB player props combine player-specific projections and success rates with market-based adjustments for team stat totals to derive estimates for each box score item.
 Player consistency in these stat totals can vary widely based on things like their typical place in the batting order or how quick the manager is to give a struggling pitcher the hook, so each measure is calculated for each unique player-stat item combination (see examples below).
   To account for the [significant randomness in baseball](https://blogs.fangraphs.com/is-baseball-the-least-random-sport/), as well for the relatively few datapoints per season for pitchers, these calculations are then regressed to league averages with a dynamic weighting system based on games played.  
''' 
st.write(mlb_intro)  
st.image('site_images/mlb_intro_1.png')
st.write('')
mlb_intro2 = '''
Given the [Markovian](https://en.wikipedia.org/wiki/Markov_chain) and [zero-inflated](https://en.wikipedia.org/wiki/Zero-inflated_model) nature of many baseball stat items, converting these raw projections into probabilities for wagering purposes is particularly tricky here.
 To illustrate, see the significant difference in shape between the K and ER distributions below - they obviously require different conversion methods. A variety of both discrete and continuous distributions are tested for each market to determine which produces the best accuracy and calibration.
   Once these final probability estimates are generated, we compare them to the odds-implied probabilities in the same manner as with other models in order to identify plus-EV wagering opportunities. Given this model family was introduced this year, we currently only cover 4 markets, but hope to expand into additional ones in the years ahead.
'''      
st.write(mlb_intro2)  
st.image('site_images/mlb_intro_2.png')

st.header('MLB Prop Model Testing',divider="gray")
st.header('Total Bases')
st.subheader('Model Performance Summary')
st.image('site_images/mlb_prop_tb_summary.png')
st.write('')

@st.cache_data  # 👈 Add the caching decorator
def load_data(url,sheet_name):
    df = pd.read_excel(url,sheet_name)
    return df

st.subheader('All Test Datapoints')
df_tb = load_data('site_documents/mlb_prop_data_website.xlsx', sheet_name=0)
df_tb['Date'] = pd.to_datetime(df_tb['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_decimal = ['Over Odds','Under Odds','Proj. AB','Proj. TB','BB Odds']
for column in columns_to_format_as_decimal:
    df_tb[column] = df_tb[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['P1 MC Win Prob.']
# for column in columns_to_format_as_percentage:
#     df_tb[column] = df_tb[column].map(lambda x: '{:.2f}%'.format(x * 100))    
players_tb = sorted(df_tb['Player'].unique())
teams = sorted(df_tb['Team'].unique())
selected_player_tb = st.selectbox('Player:', ['All'] + list(players_tb), key='Player TB')
selected_team_tb = st.selectbox('Team:', ['All'] + list(teams), key='Teams TB')

# Filter the data based on the selected values
if selected_player_tb != 'All':
    df_tb = df_tb[df_tb['Player'] == selected_player_tb]
if selected_team_tb != 'All':
    df_tb = df_tb[df_tb['Team'] == selected_team_tb]
st.dataframe(df_tb,hide_index=True)

st.write('')
'---'
st.header('Runs Scored')
st.subheader('Model Performance Summary')
st.image('site_images/mlb_prop_r_summary.png')
st.write('')
st.subheader('All Test Datapoints')
df_r = load_data('site_documents/mlb_prop_data_website.xlsx', sheet_name=1)
df_r['Date'] = pd.to_datetime(df_r['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_decimal = ['Over Odds','Under Odds','Proj. AB','Proj. Runs','BB Odds']
for column in columns_to_format_as_decimal:
    df_r[column] = df_r[column].map('{:.2f}'.format)
    # for column in columns_to_format_as_percentage:
#     df_r[column] = df_r[column].map(lambda x: '{:.2f}%'.format(x * 100))
players_r = sorted(df_r['Player'].unique())
selected_player_r = st.selectbox('Player:', ['All'] + list(players_r), key='Player R')
selected_team_r = st.selectbox('Team:', ['All'] + list(teams), key='Teams R')
# Filter the data based on the selected values
if selected_player_r != 'All':
    df_r = df_r[df_r['Player'] == selected_player_r]
if selected_team_r != 'All':
    df_r = df_r[df_r['Team'] == selected_team_r]
st.dataframe(df_r,hide_index=True)
st.write('')
st.header('Strikeouts')
st.subheader('Model Performance Summary')
st.image('site_images/mlb_prop_k_summary.png')
st.write('')
st.subheader('All Test Datapoints')
df_k = load_data('site_documents/mlb_prop_data_website.xlsx', sheet_name=2)
df_k = df_k.dropna(subset='Player')
df_k['Date'] = pd.to_datetime(df_k['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_decimal = ['Over Odds','Under Odds','Proj. SO','Proj. IP','BB Odds']
for column in columns_to_format_as_decimal:   
    df_k[column] = df_k[column].map('{:.2f}'.format)
players_k = sorted(df_k['Player'].unique())
selected_player_k = st.selectbox('Player:', ['All'] + list(players_k), key='Player K')
selected_team_k = st.selectbox('Team:', ['All'] + list(teams), key='Team K')
# Filter the data based on the selected values
if selected_player_k != 'All':
    df_k = df_k[df_k['Player'] == selected_player_k]
if selected_team_k != 'All':
    df_k = df_k[df_k['Team'] == selected_team_k]
st.dataframe(df_k,hide_index=True)
st.write('')
'---'
st.header('Earned Runs Allowed')
st.subheader('Model Performance Summary')
st.image('site_images/mlb_prop_er_summary.png')
st.write('')
st.subheader('All Test Datapoints')  
df_er = load_data('site_documents/mlb_prop_data_website.xlsx', sheet_name=3)
df_er = df_er.dropna(subset='Player')
df_er['Date'] = pd.to_datetime(df_er['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_decimal = ['Over Odds','Under Odds','Proj. ER','Proj. IP','BB Odds']
for column in columns_to_format_as_decimal:
    df_er[column] = df_er[column].map('{:.2f}'.format)    
players_er = sorted(df_er['Player'].unique())
selected_player_er = st.selectbox('Player:', ['All'] + list(players_er), key='Player ER')
selected_team_er = st.selectbox('Team:', ['All'] + list(teams), key='Team ER')
# Filter the data based on the selected values
if selected_player_er != 'All':
    df_er = df_er[df_er['Player'] == selected_player_er]
if selected_team_er != 'All':
    df_er = df_er[df_er['Team'] == selected_team_er]    
st.dataframe(df_er,hide_index=True)
