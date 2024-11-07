import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header('MLB Player Prop Model - Suggested Bets History',divider="gray")

df_mlb_result = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/mlb_prop_data_website.xlsx', sheet_name=4)
df_mlb_result = df_mlb_result.dropna(subset='Market')


st.markdown("###### _*We paused active wagering operations on our MLB models in June to focus resources on the significant effort involved in rolling out our NFL models in time for the beginning of the season. We plan to resume them for next season, with the cadence of updates being determined by market demand._")

st.subheader('Summary by Market & Month')
result_helper= df_mlb_result
result_helper['Sug. Units'] = result_helper['Sug. Units'].astype(float)
result_helper['Final Odds'] = result_helper['Final Odds'].astype(float)
market_count = pd.DataFrame(result_helper['Market'].value_counts())
market_y_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'Y']['Market'].value_counts().reset_index())
market_n_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'N']['Market'].value_counts().reset_index())
market_units_bet = pd.DataFrame(result_helper.groupby('Market')['Sug. Units'].sum().reset_index())
est_be = pd.DataFrame(result_helper.groupby('Market')['Final Odds'].mean().reset_index())
market_ni = pd.DataFrame(result_helper.groupby('Market')['KC Unit Profit'].sum().reset_index())

dfs = [market_count, market_y_count, market_n_count, market_units_bet, est_be, market_ni]
merged_df = market_count.merge(market_y_count, on='Market').merge(market_n_count, on='Market').merge(market_units_bet, on='Market').merge(est_be, on='Market').merge(market_ni, on='Market')
merged_df['Hit Rate']= merged_df['count_y']/(merged_df['count_y']+merged_df['count']) 
merged_df['Est. BE Hit Rate']= 1 / merged_df['Final Odds']
merged_df['KC ROI']= merged_df['KC Unit Profit'] / merged_df['Sug. Units']
merged_df_display = merged_df[['Market','count_x','Hit Rate','Est. BE Hit Rate','KC Unit Profit','KC ROI']]
rename_dict = {'count_x': 'Count'}
merged_df_display.rename(columns=rename_dict, inplace=True)

total_y_count = len((result_helper[result_helper['Correct?'] == 'Y'].value_counts().reset_index()))
total_n_count = len((result_helper[result_helper['Correct?'] == 'N'].value_counts().reset_index()))
total_units_bet = (result_helper['Sug. Units'].sum())
total_unit_profit= (result_helper['KC Unit Profit'].sum())
avg_odds = result_helper['Final Odds'].mean()

new_row = pd.DataFrame({
    'Market': ['Total'],
    'Count': [merged_df_display['Count'].sum()],  # Sum of Column1
    'Hit Rate': total_y_count/(total_y_count+total_n_count), 
    'Est. BE Hit Rate': 1/avg_odds,
    'KC Unit Profit': [merged_df_display['KC Unit Profit'].sum()],  # A string value
    'KC ROI': [total_unit_profit/total_units_bet]})

merged_df_display = pd.concat([merged_df_display, new_row])
merged_df_display = merged_df_display.reset_index(drop=True)

result_helper['date_column'] = pd.to_datetime(result_helper['Date']).dt.date
grouped = result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))
monthly_count = result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size()

monthly_count = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size())
monthly_y_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'Y'].groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size().reset_index())
monthly_n_count =  pd.DataFrame(result_helper[result_helper['Correct?'] == 'N'].groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size().reset_index())
monthly_units_bet = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['Sug. Units'].sum().reset_index())
est_be1 = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['Final Odds'].mean().reset_index())
monthly_ni = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['KC Unit Profit'].sum().reset_index())

dfs1 = [monthly_count, monthly_y_count, monthly_n_count, monthly_units_bet, est_be1, monthly_ni]
merged_df1 = monthly_count.merge(monthly_y_count, on='date_column').merge(monthly_n_count, on='date_column').merge(monthly_units_bet, on='date_column').merge(est_be1, on='date_column').merge(monthly_ni, on='date_column')
merged_df1['Hit Rate']= merged_df1['0_y']/(merged_df1['0_y']+merged_df1[0]) 
merged_df1['Est. BE Hit Rate']= 1 / merged_df1['Final Odds']
merged_df1['KC ROI']= merged_df1['KC Unit Profit'] / merged_df1['Sug. Units']
merged_df_display1 = merged_df1[['date_column','0_x','Hit Rate','Est. BE Hit Rate','KC Unit Profit','KC ROI']]
rename_dict1 = {'0_x': 'Count','date_column':'Month'}
merged_df_display1.rename(columns=rename_dict1, inplace=True)

new_row1 = pd.DataFrame({
    'Month': ['Total'],
    'Count': [merged_df_display1['Count'].sum()],  # Sum of Column1
    'Hit Rate': total_y_count/(total_y_count+total_n_count), 
    'Est. BE Hit Rate': 1/avg_odds,
    'KC Unit Profit': [merged_df_display1['KC Unit Profit'].sum()],  # A string value
    'KC ROI': [total_unit_profit/total_units_bet]})

merged_df_display1 = pd.concat([merged_df_display1, new_row1])
merged_df_display1 = merged_df_display1.reset_index(drop=True)

columns_to_format_as_decimal = ['KC Unit Profit']
for column in columns_to_format_as_decimal:
    merged_df_display[column] = merged_df_display[column].map('{:.2f}'.format)
    merged_df_display1[column] = merged_df_display1[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['Hit Rate','Est. BE Hit Rate','KC ROI' ]
for column in columns_to_format_as_percentage:
    merged_df_display[column] = merged_df_display[column].map(lambda x: '{:.1f}%'.format(x * 100)) 
    merged_df_display1[column] = merged_df_display1[column].map(lambda x: '{:.1f}%'.format(x * 100)) 

# st.dataframe(merged_df_display,hide_index=True)
summaries = st.columns(2)
summaries[0].dataframe(merged_df_display,hide_index=True)
summaries[1].dataframe(merged_df_display1,hide_index=True)
st.write('')
st.subheader('All Bets Made')
market = sorted(df_mlb_result['Market'].unique())
player = sorted(df_mlb_result['Player'].unique())
team = sorted(df_mlb_result['Team'].unique())
# selected_market_mlb = st.selectbox('Market:', ['All'] + list(market), key='Market MLB')
# selected_player_mlb = st.selectbox('Player:', ['All'] + list(player), key='Player MLB')
# selected_team_mlb = st.selectbox('Team:', ['All'] + list(team), key='Team MLB')

# if selected_market_mlb  != 'All':
#     df_mlb_result = df_mlb_result[df_mlb_result['Market'] == selected_market_mlb]
# if selected_player_mlb != 'All':
#     df_mlb_result = df_mlb_result[df_mlb_result['Player'] == selected_player_mlb]
# if selected_team_mlb != 'All':
#     df_mlb_result = df_mlb_result[df_mlb_result['Team'] == selected_team_mlb]
# Create the multiselects with 'All' as the default
# selected_markets_mlb = st.multiselect('Market:', ['All'] + list(market), default=['All'], key='Market MLB')
# selected_players_mlb = st.multiselect('Player:', ['All'] + list(player), default=['All'], key='Player MLB')
# selected_teams_mlb = st.multiselect('Team:', ['All'] + list(team), default=['All'], key='Team MLB')

# Function to handle selection logic
def handle_selection(key, options):
    all_options = ['All'] + options
    selected = st.multiselect(f'{key}:', all_options, default=['All'], key=f'{key} MLB1')
    
    if len(selected) > 1 and 'All' in selected:
        selected.remove('All')
    elif len(selected) == 0:
        selected = ['All']
    
    return selected

# Create multiselects with custom handling
selected_markets_mlb = handle_selection('Market', market)
selected_players_mlb = handle_selection('Player', player)
selected_teams_mlb = handle_selection('Team', team)

# Function to filter dataframe based on selections
def filter_dataframe(df, column, selected_values):
    if 'All' in selected_values:
        return df
    return df[df[column].isin(selected_values)]

df_mlb_result = filter_dataframe(df_mlb_result, 'Market', selected_markets_mlb)
df_mlb_result = filter_dataframe(df_mlb_result, 'Player', selected_players_mlb)
df_mlb_result = filter_dataframe(df_mlb_result, 'Team', selected_teams_mlb)

df_mlb_result.drop('date_column', axis=1, inplace=True)
df_mlb_result.drop(['KC $ Profit','KC Result'], axis=1, inplace=True) #'Imp. Amt. @ 3k bankroll', 
df_mlb_result['Date'] = pd.to_datetime(df_mlb_result['Date']).dt.strftime('%m-%d-%Y')
columns_to_format_as_decimal2 = ['Final Odds','Sug. Units']
for column in columns_to_format_as_decimal2:
    df_mlb_result[column] = df_mlb_result[column].map('{:.2f}'.format)
columns_to_format_as_decimal3 = ['KC Exp. EV in Units','KC Unit Profit','EV']
for column in columns_to_format_as_decimal3:
    df_mlb_result[column] = df_mlb_result[column].map('{:.3f}'.format)
columns_to_format_as_percentage2 = ['Model Prob.','LV Prob.']
for column in columns_to_format_as_percentage2:
    df_mlb_result[column] = df_mlb_result[column].map(lambda x: '{:.1f}%'.format(x * 100))   

st.dataframe(df_mlb_result,hide_index=True)


