import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('NFL Player Props - Suggested Bets History',divider="gray")
df_nfl_result = pd.read_excel('https://github.com/OrcaSyndicate/orca_syndicate_site/raw/refs/heads/main/OrcaSyndicate/site_documents/nfl_data_website.xlsx', sheet_name=8)
df_nfl_result = df_nfl_result.dropna(subset='Market')

columns_to_format_as_decimal2 = ['KC Exp. EV in Units','KC Unit Profit','Edge','EV','Final Odds','Sug. Units','KC Unit Result']  #,''
for column in columns_to_format_as_decimal2:
    df_nfl_result[column] = df_nfl_result[column].round(2)         #.map('{:.2f}'.format)
columns_to_format_as_percentage2 = ['Model Prob.','LV Prob.','Model Proj.']
for column in columns_to_format_as_percentage2:
    #df_nfl_result[column] = df_nfl_result[column].map(lambda x: '{:.1f}%'.format(x * 100))
    df_nfl_result[column] = df_nfl_result[column].round(3)         #map('{:.3f}'.format)
st.subheader('Summary by Market & Week')
result_helper= df_nfl_result
result_helper['Sug. Units'] = result_helper['Sug. Units'].astype(float)
result_helper['Final Odds'] = result_helper['Final Odds'].astype(float)
result_helper['KC Unit Profit'] = result_helper['KC Unit Profit'].astype(float)
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

result_helper['Week'] = pd.to_datetime(result_helper['Week']).astype(int)
grouped = result_helper.groupby('Week')
count_by_integer = result_helper.groupby('Week').size()

week_count = pd.DataFrame(result_helper['Week'].value_counts())
week_y_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'Y']['Week'].value_counts().reset_index())
week_n_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'N']['Week'].value_counts().reset_index())
week_units_bet = pd.DataFrame(result_helper.groupby('Week')['Sug. Units'].sum().reset_index())
est_be1 = pd.DataFrame(result_helper.groupby('Week')['Final Odds'].mean().reset_index())
week_ni = pd.DataFrame(result_helper.groupby('Week')['KC Unit Profit'].sum().reset_index())

dfs1 = [week_count, week_y_count, week_n_count, week_units_bet, est_be1, week_ni]
merged_df1 = week_count.merge(week_y_count, on='Week').merge(week_n_count, on='Week').merge(week_units_bet, on='Week').merge(est_be1, on='Week').merge(week_ni, on='Week')
merged_df1['Hit Rate']= merged_df1['count_y']/(merged_df1['count_y']+merged_df1['count']) 
merged_df1['Est. BE Hit Rate']= 1 / merged_df1['Final Odds']
merged_df1['KC ROI']= merged_df1['KC Unit Profit'] / merged_df1['Sug. Units']
merged_df_display1 = merged_df1[['Week','count_x','Hit Rate','Est. BE Hit Rate','KC Unit Profit','KC ROI']]
rename_dict1 = {'count_x': 'Count','date_column':'Month'}
merged_df_display1.rename(columns=rename_dict1, inplace=True)
new_row1 = pd.DataFrame({
    'Week': ['Total'],
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
columns_to_format_as_percentage = ['Hit Rate','Est. BE Hit Rate','KC ROI']
for column in columns_to_format_as_percentage:
    merged_df_display[column] = merged_df_display[column].map(lambda x: '{:.1f}%'.format(x * 100)) 
    merged_df_display1[column] = merged_df_display1[column].map(lambda x: '{:.1f}%'.format(x * 100)) 
    #merged_df_display[column] = merged_df_display[column].map('{:.3f}'.format)
    #merged_df_display1[column] = merged_df_display1[column].map('{:.3f}'.format)
# titles = st.columns(2)
# titles[0]= st.markdown("Market")
# titles[1] = st.markdown("Month")
summaries = st.columns(2)
summaries[0].dataframe(merged_df_display,hide_index=True)
summaries[1].dataframe(merged_df_display1,hide_index=True)
st.write('')

def handle_selection(key, options):
    all_options = ['All'] + options
    selected = st.multiselect(f'{key}:', all_options, default=['All'], key=f'{key} NFL1')
    
    if len(selected) > 1 and 'All' in selected:
        selected.remove('All')
    elif len(selected) == 0:
        selected = ['All']
    
    return selected
st.divider()

st.subheader('All Bets Made')
market = sorted(df_nfl_result['Market'].unique())
player = sorted(df_nfl_result['Player'].unique())
team = sorted(df_nfl_result['Team'].unique())

# Create multiselects with custom handling
selected_markets_nfl = handle_selection('Market', market)
selected_players_nfl = handle_selection('Player', player)
selected_teams_nfl = handle_selection('Team', team)

# Function to filter dataframe based on selections
def filter_dataframe(df, column, selected_values):
    if 'All' in selected_values:
        return df
    return df[df[column].isin(selected_values)]

df_nfl_result = filter_dataframe(df_nfl_result, 'Market', selected_markets_nfl)
df_nfl_result = filter_dataframe(df_nfl_result, 'Player', selected_players_nfl)
df_nfl_result = filter_dataframe(df_nfl_result, 'Team', selected_teams_nfl)

#df_nfl_result.drop('date_column', axis=1, inplace=True)

st.dataframe(df_nfl_result,hide_index=True)

