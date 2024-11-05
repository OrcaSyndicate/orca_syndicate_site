import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Model Description',divider="gray")

soccer_intro = '''
Soccer presents several modeling challenges due to its low scoring, Poisson-distributed nature. There is also a significant amount of noise in terms of goals scored relative to qualitative assessments of a team’s play. To address this, we first use tree-based AI models to predict non-penalty expected goals (NPxG). Expected goals measure how many goals a team should have scored in a game given the quantity and location of its shots, and who took them. This measure is smoother than actual goals, which have much higher variance levels, 
 and also removes the impact of penalty shots, for which there is minimal evidence of ex-ante predictability.
   
Once we have a fundamental estimate of NPxG, we adjust it based on market-expected actual goals, following a method first proposed in Benter 1994.
 This adjustment allows the algo to consider game-specific factors such as team shape and relative game importance. From there, we run Monte Carlo simulations based on these results, simulating each game thousands of times, with penalty attempts and own goals also awarded according to their historical frequencies.  A key differentiator for our algorithm is that is utilizes a Skellam distribution to estimate the non-penalty goal difference between the two teams, instead of the actual scores themselves. This eliminates the correlation between team results, and does not require that the scored goals by each team are marginally Poisson distributed. Most importantly, it provides a well-calibrated estimate of game results, as depicted in the graph below.

'''
st.write(soccer_intro)
st.write('')
st.image('C:/Users/ajaku/Downloads/soccer_intro.png')
st.write('')
soccer_intro2 = '''

'''
st.write(soccer_intro2)

st.write('')
st.header('Soccer Model Testing',divider="gray")
st.subheader('Asian Handicap Model Performance Summary')
st.image('site_images/soccer_team_spreads_summary.png')

@st.cache_data  # 👈 Add the caching decorator
def load_data(url,sheet_name):
    df = pd.read_excel(url,sheet_name)
    return df

st.write('')
st.subheader('All AH Model Datapoints')
data_comb1 = load_data('site_documents/soccer_data_website.xlsx', sheet_name=0)
data_comb1 = data_comb1.dropna(subset=['Home'])
data_comb1['Date'] = pd.to_datetime(data_comb1['Date']).dt.strftime('%m-%d-%Y')

columns_to_format_as_decimal = ['AH Home Odds','AH Away Odds','KC Result 2.0','KC Profit']
for column in columns_to_format_as_decimal:
    data_comb1[column] = data_comb1[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['Final Home WW','Final Home WD','Final Away WW','Final Away WD','Biggest Edge Odds Imp. Cover Prob.','Biggest Edge True Cover Prob.']
for column in columns_to_format_as_percentage:
    data_comb1[column] = data_comb1[column].map(lambda x: '{:.1f}%'.format(x * 100))         
columns_to_format_as_percentage1 = ['KC Bet Size 2.0']
for column in columns_to_format_as_percentage1:
    data_comb1[column] = data_comb1[column].map(lambda x: '{:.2f}%'.format(x * 100))     
teams = sorted(pd.concat([data_comb1['Home'], data_comb1['Away']]).unique())
spreads = sorted(pd.concat([data_comb1['Split Bet?']]).unique())
selected_team_spread = st.selectbox('Team:', ['All'] + list(teams), key='Teams Spread')
selected_split_spread = st.selectbox('Split Spread?:', ['All'] + list(spreads), key='Teams Spread 2')

if selected_team_spread != 'All':
    filtered_df = data_comb1[(data_comb1['Home'] == selected_team_spread) | (data_comb1['Away'] == selected_team_spread)]
if selected_split_spread  != 'All':
    filtered_df = data_comb1[data_comb1['Split Bet?'] == selected_split_spread]
else:
    filtered_df = data_comb1

st.dataframe(filtered_df,hide_index=True)































