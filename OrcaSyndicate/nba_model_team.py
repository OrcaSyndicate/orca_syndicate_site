import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Model Descriptions',divider="gray")
st.write('')
st.markdown("### _NBA Team-Level Spread Model_")

nba_intro = '''
Our NBA team models are our oldest ongoing implementation, and we continue to iterate on them each year.
 For the 21/22 and 22/23 seasons, we utilized classification models based on team-level performance metrics and betting market data to arrive at the final win and cover probability estimates.
   For the 23/24 season, we moved our team-level algorithm to a regression-based approach centered around fundamental play-by-play data, and fit separate models for the two components of team points scored - game pace and points per possession (PpP).
     A few performance metrics for both approaches are shown below.
     '''
st.write(nba_intro)  
st.write('')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_intro_1.PNG?raw=true')
nba_intro2 = '''
We hoped that the switch to a regression model in 23/24 with two independent variables would allow for more robust simulations that would more accurately capture the full range of outcomes possible for each game.
 However, the algorithm’s prioritization of [RMSE minimization](https://arize.com/blog-course/root-mean-square-error-rmse-what-you-need-to-know/) reduced its prediction variance to a greater extent than anticipated. This had the effect of generally biasing the model toward large underdogs, as the model did not sufficiently discount the expected PpP from the inferior team or enhance it for the superior one.
   While the model still provided enough of a signal to generate betting opportunities, profitability was lower than in past years. Given the significant work involved in overhauling and and then re-testing an active model, doing so was impractical in the middle of a season, and so we instead continued to utilize the existing implementation with more conservative bet sizing.
     But for the upcoming year, we will be modifying the implementation to ensure better calibration across all splits (Fav/UG, Home/Away, etc.). We are testing both classification and regression approaches and will have further updates later this year closer to the start of the season.
 ''' 
st.write('')
st.write(nba_intro2)   
st.write('')
st.markdown("### _NBA Player-Level Spread & O/U Models_")
nba_intro3 = '''
Our introduction of player prop models as well as game pace estimates allowed us to generate an entirely new set of team predictions based on player-level data for the first time in 23/24.
The NBA player model takes each player's net contribution per 100 possessions on both offense and defense, weights it for his minutes, and then sums the total to get an idea of each team's overall strength on both offense and defense.
 An example from a typical night during the season is shown below (left table), with each team’s offensive and defensive points scored/allowed above the league average per 100 possessions. The higher the values for each, the better, hence the teams with the best record tend to have the highest total values across offense and defense. 
     
The contributions per 100 possessions are then scaled based on the projected pace of the game that day. To arrive at a point total estimate, Team A's offensive strength (measured in points scored above the league average per 100 possessions) is netted against Team B's defensive strength (measured in points allowed below the league average per 100 possessions).
The same process is applied to Team B's offense and Team A's defensive totals. From there, we can infer a fair points spread on a neutral court. We then give the home team a points boost vs the spread based on 25,000 games to see how much they outperform vs a baseline expectation when playing at home. We then re-center each team's advantage to the league average to account for the relative decline in home court advantages in recent years.
The long-term and current HCAs for each team are shown below in the center table. This is not a perfect method, as a city's interest can ebb and flow based on how good or bad their team is, but it is the best we can do without inserting discretionary judgments. Unsurprisingly, the high altitude teams have had the biggest advantage over 10+ years of games.

Once we have point totals and a home-court advantage estimate, we can make a final fair home spread estimate of (away proj. score - home proj. score - home court adv.). The final step is to convert these values to a probability to compare them with the odds-implied probabilites.
Fortunately for us, spreads vs final results are normally distributed, making the calculation trivia (see right chart). By simply comparing the fair spread to the actual spread and providing the long-term standard deviation between projected spreads and outcomes, we can arrive at a solid estimate of a team's cover probability using the Gaussian CDF.
The same process (with the home court advantage removed) is used to calculate over/under edges. 
'''
st.write('')
st.write(nba_intro3)   
st.write('')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_intro_2.PNG?raw=true')
st.header('NBA Model Testing',divider="gray",help="Games Used to Determine Betting Thresholds")
st.subheader('Team-Level Model Spread Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_team_spreads_summary.PNG?raw=true')
st.write('')
st.subheader('All Team-Level Model Spread Datapoints')


@st.cache_data  # 👈 Add the caching decorator
def load_data(url,sheet_name):
    df = pd.read_excel(url,sheet_name)
    return df

data_comb1 = load_data('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nba_data_website.xlsx', sheet_name=11)
# data_comb1 = pd.read_excel('C:/Users/ajaku/Downloads/nba_data_website.xlsx', sheet_name=11)
data_comb1 = data_comb1.dropna(subset=['Home'])
data_comb1['Date'] = pd.to_datetime(data_comb1['Date']).dt.strftime('%m-%d-%Y')

columns_to_format_as_decimal = ['KC Unit Profit'] #'KC Unit Result',
for column in columns_to_format_as_decimal:
    data_comb1[column] = data_comb1[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['Home Odds Imp. Cover Prob.','Home Model Cover Prob.','Biggest Edge Odds Imp. Cover Prob.','Biggest Edge True Cover Prob.']
for column in columns_to_format_as_percentage:
    data_comb1[column] = data_comb1[column].map('{:.3f}'.format)
    #data_comb1[column] = data_comb1[column].map(lambda x: '{:.1f}%'.format(x * 100))         
columns_to_format_as_percentage1 = []
for column in columns_to_format_as_percentage1:
    data_comb1[column] = data_comb1[column].map(lambda x: '{:.2f}%'.format(x * 100))     
teams = sorted(pd.concat([data_comb1['Home'], data_comb1['Away']]).unique())
selected_team_spread = st.selectbox('Team:', ['All'] + list(teams), key='Teams Spread')

if selected_team_spread != 'All':
    filtered_df = data_comb1[(data_comb1['Home'] == selected_team_spread) | (data_comb1['Away'] == selected_team_spread)]
else:
    filtered_df = data_comb1

st.dataframe(filtered_df,hide_index=True)
st.write('')
st.divider()
st.subheader('Player-Level Model Spread Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_team_spreads_summary.PNG?raw=true')
st.write('')
st.subheader('All Player-Level Model Spread Datapoints')
data_comb2 = load_data('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nba_data_website.xlsx', sheet_name=12)
data_comb2 = data_comb2.dropna(subset=['Home']) 
data_comb2['Date'] = pd.to_datetime(data_comb2['Date']).dt.strftime('%m-%d-%Y')
for column in columns_to_format_as_percentage:
    data_comb2[column] = data_comb2[column].map(lambda x: '{:.1f}%'.format(x * 100))   
for column in columns_to_format_as_percentage1:
    data_comb2[column] = data_comb2[column].map(lambda x: '{:.2f}%'.format(x * 100))  
for column in columns_to_format_as_decimal:
    data_comb2[column] = data_comb2[column].map('{:.2f}'.format)      
teams1 = sorted(pd.concat([data_comb2['Home'], data_comb2['Away']]).unique())
selected_team_spread2 = st.selectbox('Team:', ['All'] + list(teams1), key='Teams Spread 2')

if selected_team_spread2 != 'All':
    filtered_df1 = data_comb2[(data_comb2['Home'] == selected_team_spread2) | (data_comb2['Away'] == selected_team_spread2)]
else:
    filtered_df1 = data_comb2

st.dataframe(filtered_df1,use_container_width=True,hide_index=True)
st.write('')
st.divider()
st.subheader('Player-Level Model O/U Performance Summary')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_player_ou_summary.PNG?raw=true')
st.write('')
st.subheader('All Player-Level Model O/U Datapoints')
data_comb3 = load_data('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nba_data_website.xlsx', sheet_name=13)
data_comb3 = data_comb3.dropna(subset=['Home'])
data_comb3['Date'] = pd.to_datetime(data_comb3['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_percentage2 = ['Over Odds Imp. Cover Prob.','Over Model Cover Prob.','Biggest Edge Odds Imp. Cover Prob.','Biggest Edge True Cover Prob.','KC Unit Bet Size']
columns_to_format_as_percentage3 = []  #'KC Unit Result'
for column in columns_to_format_as_percentage2:
    data_comb3[column] = data_comb3[column].map('{:.3}'.format)
    #data_comb3[column] = data_comb3[column].map(lambda x: '{:.1f}%'.format(x * 100))   
for column in columns_to_format_as_percentage3:
    data_comb3[column] = data_comb3[column].map(lambda x: '{:.2f}%'.format(x * 100))
for column in columns_to_format_as_decimal:
    data_comb3[column] = data_comb3[column].map('{:.2f}'.format)        
teams2 = sorted(pd.concat([data_comb3['Home'], data_comb3['Away']]).unique())
selected_team_spread3 = st.selectbox('Team:', ['All'] + list(teams1), key='Teams Spread 3')

if selected_team_spread3 != 'All':
    filtered_df2 = data_comb3[(data_comb3['Home'] == selected_team_spread3) | (data_comb3['Away'] == selected_team_spread3)]
else:
    filtered_df2 = data_comb3
st.dataframe(filtered_df2,hide_index=True)

st.write('')
