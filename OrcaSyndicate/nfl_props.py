import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Model Description',divider="gray")
nfl_intro = '''
We are excited to introduce our NFL player props for the 2024 season.
Our two most important projections start at the top with quarterback passing yards and passing attempts.
Targeting these variables has the dual advantage of being relatively stable between games and normally distributed (see graphic below). 

''' 
st.write(nfl_intro)  
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_intro1.PNG?raw=true')
st.write('')
nfl_intro2 = '''
Our model utilizes an [elastic net](https://en.wikipedia.org/wiki/Elastic_net_regularization) with 31 features to generate each projection.
Both player and season variables are included, as well as game specific data such as opponent matchups and weather conditions. 
Out of sample testing suggests it is even more accurate than book lines, which is very difficult to achieve across a full 500+ game sample (model comparision and summary statistics for the final passing yards model performance shown below). 
'''
st.write(nfl_intro2)
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_intro3.PNG?raw=true')
st.write('')

nfl_intro3 = '''
Below these two core elastic nets sit a variety of simpler random forest models that are used in conjunction with season averages in a dynamic weighting scheme to project the other component values needed to arrive at all major statistical line item predictions.
For example, predicting the quarterback completions market is a function of passing attempts and the completion percentage component prediction. A receiver’s reception projection is a function of pass attempts and the target share and catch rate components, and so on.
The methods to convert the projections into probabilities vary by market, as the distributions from various stat items take a wide range of shapes.
For example, compare receptions data below, and also note the subtle differences between projecting for a wide receiver versus a running back.
'''
st.write(nfl_intro3)  
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_intro2.PNG?raw=true')
st.write('')
nfl_intro4 = '''
In total, 6 different distributions are used, and several of the models utilize an average of several different systems to arrive at a final probability.
From there, as with all our other models, the Kelly Criterion is applied to arrive at a suggested bet size.
We then test on out-of-sample data to determine the thresholds across edge, EV, and suggested bet size that maximize profitability.
Models which manage to achieve profitability levels that reach statistical significance are then rolled out for live release. 

One important thing to keep in mind for NFL prop betting purposes is that books generally shade their lines heavily toward the "over" side of a given market. 
Over a sample of over 12,000 bets across three seasons, the “under” side hit at a 56% rate despite offering slightly longer average odds. 
Thus, while our models are designed to be well-calibrated, the nature of the books’ offerings means that the suggested wagers will be on the “under” side more often than not.
Also note that due to a lack of historical odds data availability for touchdown markets, we don’t currently suggest bets for them; once we eventually collect enough of our own data for it, these will be added as well.	

'''
st.write(nfl_intro4) 

@st.cache_data  # 👈 Add the caching decorator
def load_data(url,sheet_name):
    df = pd.read_excel(url,sheet_name)
    return df

columns_to_format_as_decimal = ['Over Odds','Under Odds','BB Odds','1U Bet Result','1U Bet Profit','KC Bet Size']
columns_to_format_as_decimal4 = ['Proj. Total','Over Odds','Under Odds','BB Odds','1U Bet Result','1U Bet Profit','KC Bet Size']
columns_to_format_as_decimal1 = ['Line']
columns_to_format_as_decimal1a = ['Proj. Pass Yds.','Line']
columns_to_format_as_decimal3 = ['Over EV','Under EV','Final Over','Final Under','BB True Prob.','Best EV','BB Imp. Prob.','KC Result','KC Profit']

st.header('NFL Prop Model Testing',divider="gray")
st.header('Passing Yards')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_py_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
#df_py = load_data('site_documents/nfl_data_website.xlsx', sheet_name=0)
df_py = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=0)
df_py =df_py.dropna(subset='Season')

for column in columns_to_format_as_decimal:
    df_py[column] = df_py[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1a:
    df_py[column] = df_py[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_py[column] = df_py[column].map('{:.3f}'.format)
#players_py = sorted(df_py['Player'].unique())
#selected_player_py = st.selectbox('Player:', ['All'] + list(players_py), key='Player PY')
season_py = sorted(df_py['Season'].astype(int).unique())
season_py_str = [str(season) for season in season_py]
selected_season_py = st.selectbox('Season:', ['All'] + season_py_str, key='Season PY')

if selected_season_py != 'All':
    selected_season_py = int(selected_season_py)
# Filter the data based on the selected values
#if selected_player_py != 'All':
#    df_py = df_py[df_py['Player'] == selected_player_py]
if selected_season_py != 'All':
    df_py = df_py[df_py['Season'] == selected_season_py]

df_py[['Season','Act. Total']] = df_py[['Season','Act. Total']].astype(int)
#df_py['Act. Total'] = df_py['Act. Total'].astype(int)
st.dataframe(df_py.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)
st.write('')
st.header('Passing Attempts')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_pa_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_pa = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=1)
df_pa =df_pa.dropna(subset='Season')


for column in columns_to_format_as_decimal4:
    df_pa[column] = df_pa[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_pa[column] = df_pa[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_pa[column] = df_pa[column].map('{:.3f}'.format)
#players_pa = sorted(df_pa['Player'].unique())
#selected_player_pa = st.selectbox('Player:', ['All'] + list(players_pa), key='Player PA')
season_pa = sorted(df_pa['Season'].astype(int).unique())
season_pa_str = [str(season) for season in season_pa]
selected_season_pa = st.selectbox('Season:', ['All'] + season_pa_str, key='Season PA')

if selected_season_pa != 'All':
    selected_season_pa = int(selected_season_pa)
# Filter the data based on the selected values
#if selected_player_pa != 'All':
#    df_pa = df_pa[df_pa['Player'] == selected_player_pa]
if selected_season_pa != 'All':
    df_pa = df_pa[df_pa['Season'] == selected_season_pa]

df_pa[['Season','Act. Total']] = df_pa[['Season','Act. Total']].astype(int)
#df_pa['Act. Total'] = df_pa['Act. Total'].astype(int)
st.dataframe(df_pa.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

st.write('')
st.header('Passing TDs')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_ptd_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_ptd = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=3)
df_ptd =df_ptd.dropna(subset='Season')

for column in columns_to_format_as_decimal4:
    df_ptd[column] = df_ptd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_ptd[column] = df_ptd[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_ptd[column] = df_ptd[column].map('{:.3f}'.format)
#players_ptd = sorted(df_ptd['Player'].unique())
#selected_player_ptd = st.selectbox('Player:', ['All'] + list(players_ptd), key='Player PTD')
season_ptd = sorted(df_ptd['Season'].astype(int).unique())
season_ptd_str = [str(season) for season in season_ptd]
selected_season_ptd = st.selectbox('Season:', ['All'] + season_ptd_str, key='Season PTD')

if selected_season_ptd != 'All':
    selected_season_ptd = int(selected_season_ptd)
# Filter the data based on the selected values
#if selected_player_ptd != 'All':
#    df_ptd = df_ptd[df_ptd['Player'] == selected_player_ptd]
if selected_season_ptd != 'All':
    df_ptd = df_ptd[df_ptd['Season'] == selected_season_ptd]

df_ptd[['Season','Act. Total']] = df_ptd[['Season','Act. Total']].astype(int)
#df_ptd['Act. Total'] = df_ptd['Act. Total'].astype(int)
st.dataframe(df_ptd.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

st.write('')
st.header('Passing INTs')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_int_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_int = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=4)
df_int =df_int.dropna(subset='Season')

for column in columns_to_format_as_decimal4:
    df_int[column] = df_int[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_int[column] = df_int[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_int[column] = df_int[column].map('{:.3f}'.format)
#players_int = sorted(df_int['Player'].unique())
#selected_player_int = st.selectbox('Player:', ['All'] + list(players_int), key='Player INT')
season_int = sorted(df_int['Season'].astype(int).unique())
season_int_str = [str(season) for season in season_int]
selected_season_int = st.selectbox('Season:', ['All'] + season_int_str, key='Season INT')

if selected_season_int != 'All':
    selected_season_int = int(selected_season_int)
# Filter the data based on the selected values
#if selected_player_int != 'All':
#    df_int = df_int[df_int['Player'] == selected_player_int]
if selected_season_int != 'All':
    df_int = df_int[df_int['Season'] == selected_season_int]

df_int[['Season','Act. Total']] = df_int[['Season','Act. Total']].astype(int)
#df_int['Act. Total'] = df_int['Act. Total'].astype(int)
st.dataframe(df_int.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

st.write('')
st.header('Rushing Yards')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_rush_yd_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_rush_yd = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=5)
df_rush_yd =df_rush_yd.dropna(subset='Season')

for column in columns_to_format_as_decimal4:
    df_rush_yd[column] = df_rush_yd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_rush_yd[column] = df_rush_yd[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_rush_yd[column] = df_rush_yd[column].map('{:.3f}'.format)
#players_rush_yd = sorted(df_rush_yd['Player'].unique())
#selected_player_rush_yd = st.selectbox('Player:', ['All'] + list(players_rush_yd), key='Player RushYd')
season_rush_yd = sorted(df_rush_yd['Season'].astype(int).unique())
season_rush_yd_str = [str(season) for season in season_rush_yd]
selected_season_rush_yd = st.selectbox('Season:', ['All'] + season_rush_yd_str, key='Season RushYd')

if selected_season_rush_yd != 'All':
    selected_season_rush_yd = int(selected_season_rush_yd)
# Filter the data based on the selected values
#if selected_player_rush_yd != 'All':
#    df_rush_yd = df_rush_yd[df_rush_yd['Player'] == selected_player_rush_yd]
if selected_season_rush_yd != 'All':
    df_rush_yd = df_rush_yd[df_rush_yd['Season'] == selected_season_rush_yd]

df_rush_yd[['Season','Act. Total']] = df_rush_yd[['Season','Act. Total']].astype(int)
#df_rush_yd['Act. Total'] = df_rush_yd['Act. Total'].astype(int)
st.dataframe(df_rush_yd.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

st.write('')
st.header('Receptions')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_rec_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_rec = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=6)
df_rec =df_rec.dropna(subset='Season')

for column in columns_to_format_as_decimal4:
    df_rec[column] = df_rec[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_rec[column] = df_rec[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_rec[column] = df_rec[column].map('{:.3f}'.format)
#players_rec = sorted(df_rec['Player'].unique())
#selected_player_rec = st.selectbox('Player:', ['All'] + list(players_rec), key='Player Rec')
season_rec = sorted(df_rec['Season'].astype(int).unique())
season_rec_str = [str(season) for season in season_rec]
selected_season_rec = st.selectbox('Season:', ['All'] + season_rec_str, key='Season Rec')

if selected_season_rec != 'All':
    selected_season_rec = int(selected_season_rec)
# Filter the data based on the selected values
#if selected_player_rec != 'All':
#    df_rec = df_rec[df_rec['Player'] == selected_player_rec]
if selected_season_rec != 'All':
    df_rec = df_rec[df_rec['Season'] == selected_season_rec]

df_rec[['Season','Act. Total']] = df_rec[['Season','Act. Total']].astype(int)
#df_rec['Act. Total'] = df_rec['Act. Total'].astype(int)
st.dataframe(df_rec.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

st.write('')
st.header('Receiving Yards')
st.subheader('Model Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_prop_rec_yd_summary.PNG?raw=true')
st.write('')

st.subheader('All Test Datapoints')
df_rec_yd = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=7)
df_rec_yd =df_rec_yd.dropna(subset='Season')

for column in columns_to_format_as_decimal4:
    df_rec_yd[column] = df_rec_yd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal1:
    df_rec_yd[column] = df_rec_yd[column].map('{:.1f}'.format)
for column in columns_to_format_as_decimal3:
    df_rec_yd[column] = df_rec_yd[column].map('{:.3f}'.format)
#players_rec_yd = sorted(df_rec_yd['Player'].unique())
#selected_player_rec_yd = st.selectbox('Player:', ['All'] + list(players_rec_yd), key='Player RecYd')
season_rec_yd = sorted(df_rec_yd['Season'].astype(int).unique())
season_rec_yd_str = [str(season) for season in season_rec_yd]
selected_season_rec_yd = st.selectbox('Season:', ['All'] + season_rec_yd_str, key='Season RecYd')

if selected_season_rec_yd != 'All':
    selected_season_rec_yd = int(selected_season_rec_yd)
# Filter the data based on the selected values
#if selected_player_rec_yd != 'All':
#    df_rec_yd = df_rec_yd[df_rec_yd['Player'] == selected_player_rec_yd]
if selected_season_rec_yd != 'All':
    df_rec_yd = df_rec_yd[df_rec_yd['Season'] == selected_season_rec_yd]

df_rec_yd[['Season','Act. Total']] = df_rec_yd[['Season','Act. Total']].astype(int)
#df_rec_yd['Act. Total'] = df_rec_yd['Act. Total'].astype(int)
st.dataframe(df_rec_yd.style.format({'Season': '{:.0f}','Week': '{:.0f}',}),hide_index=True)

#st.title('Stay tuned...')
#st.markdown("### _Data collection in progress during Weeks 1-4 of 2024 season, check back later!_ :sunglasses:")
# st.header('Testing in progress during Weeks 1-4 of 2024 season :nerd_face:')
#st.write('')
#st.write('')
#st.write('')
#st.write('')
#st.write('')
#st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nfl_placeholder.png?raw=true')
