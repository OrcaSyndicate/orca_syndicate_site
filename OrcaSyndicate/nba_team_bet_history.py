import streamlit as st
import pandas as pd
import re

st.set_page_config(layout="wide")

st.header('NBA Team Models - Suggested Bets History',divider="gray")
st.write('')

@st.cache_data  # 👈 Add the caching decorator
def load_data(url,sheet_name):
    df = pd.read_excel(url,sheet_name)
    return df

st.subheader('Performance Summary by Model & Market')

df_nba_result1 = load_data('site_documents/nba_data_website.xlsx', sheet_name=14)
df_nba_result2 = load_data('site_documents/nba_data_website.xlsx', sheet_name=15)
df_nba_result3 = load_data('site_documents/nba_data_website.xlsx', sheet_name=16)
df_nba_result = pd.concat([df_nba_result1,df_nba_result2,df_nba_result3])

df_nba_result = df_nba_result.dropna(subset='Model')
df_nba_result['Date'] = pd.to_datetime(df_nba_result['Date']).dt.strftime('%m-%d-%Y')
# columns_to_format_as_decimal2 = ['KC Exp. EV in Units','KC Result','KC $ Profit','KC Unit Profit','EV','Final Odds','KF Sug. Units']
# for column in columns_to_format_as_decimal2:
#     df_nba_result[column] = df_nba_result[column].map('{:.2f}'.format)
# columns_to_format_as_percentage2 = ['Model Prob.','LV MF Prob.']
# for column in columns_to_format_as_percentage2:
#     df_nba_result[column] = df_nba_result[column].map(lambda x: '{:.1f}%'.format(x * 100))  
result_helper= df_nba_result
result_helper['Sug. Units'] = result_helper['Final Amt. Units'].astype(float)
result_helper['Final Odds'] = result_helper['Final Odds'].astype(float)
result_helper['KC Unit Profit'] = result_helper['KC Unit Profit'].astype(float)
market_count = pd.DataFrame(result_helper['Model'].value_counts())
market_y_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'Y']['Model'].value_counts().reset_index())
market_n_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'N']['Model'].value_counts().reset_index())
market_units_bet = pd.DataFrame(result_helper.groupby('Model')['Sug. Units'].sum().reset_index())
est_be = pd.DataFrame(result_helper.groupby('Model')['Final Odds'].mean().reset_index())
market_ni = pd.DataFrame(result_helper.groupby('Model')['KC Unit Profit'].sum().reset_index())

dfs = [market_count, market_y_count, market_n_count, market_units_bet, est_be, market_ni]
merged_df = market_count.merge(market_y_count, on='Model').merge(market_n_count, on='Model').merge(market_units_bet, on='Model').merge(est_be, on='Model').merge(market_ni, on='Model')
merged_df['Hit Rate']= merged_df['count_y']/(merged_df['count_y']+merged_df['count']) 
merged_df['Est. BE Hit Rate']= 1 / merged_df['Final Odds']
merged_df['KC ROI']= merged_df['KC Unit Profit'] / merged_df['Sug. Units']
merged_df_display = merged_df[['Model','count_x','Hit Rate','Est. BE Hit Rate','KC Unit Profit','KC ROI']]
rename_dict = {'count_x': 'Count'}
merged_df_display.rename(columns=rename_dict, inplace=True)
total_y_count = len((result_helper[result_helper['Correct?'] == 'Y'].reset_index()))
total_n_count = len((result_helper[result_helper['Correct?'] == 'N'].reset_index()))
total_units_bet = (result_helper['Sug. Units'].sum())
total_unit_profit= (result_helper['KC Unit Profit'].sum())
avg_odds = result_helper['Final Odds'].mean()
new_row = pd.DataFrame({
    'Model': ['Total'],
    'Count': [merged_df_display['Count'].sum()],  # Sum of Column1
    'Hit Rate': total_y_count/(total_y_count+total_n_count), 
    'Est. BE Hit Rate': 1/avg_odds,
    'KC Unit Profit': [merged_df_display['KC Unit Profit'].sum()],  # A string value
    'KC ROI': [total_unit_profit/total_units_bet]})

merged_df_display = pd.concat([merged_df_display, new_row])
merged_df_display = merged_df_display.reset_index(drop=True)

result_helper= df_nba_result
result_helper['date_column'] = pd.to_datetime(result_helper['Date']).dt.date
result_helper['monthly_period'] = result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))
grouped = result_helper.groupby('monthly_period')

# Monthly count of all entries
monthly_count = grouped.size().reset_index(name='Count')

# Monthly count of 'Correct?' being 'Y'
monthly_y_count = result_helper[result_helper['Correct?'] == 'Y'].groupby('monthly_period').size().reset_index(name='Y Count')
monthly_n_count = result_helper[result_helper['Correct?'] == 'N'].groupby('monthly_period').size().reset_index(name='N Count')

# Merge the counts into one DataFrame for comparison
monthly_summary = pd.merge(monthly_count, monthly_y_count, on='monthly_period', how='left').fillna(0)
monthly_summary = pd.merge(monthly_summary, monthly_n_count, on='monthly_period', how='left').fillna(0)

monthly_units_bet = pd.DataFrame(result_helper.groupby(result_helper['monthly_period'].map(lambda x: pd.Period(x, freq='M')))['Sug. Units'].sum().reset_index())
est_be1 = pd.DataFrame(result_helper.groupby(result_helper['monthly_period'].map(lambda x: pd.Period(x, freq='M')))['Final Odds'].mean().reset_index())
monthly_ni = pd.DataFrame(result_helper.groupby(result_helper['monthly_period'].map(lambda x: pd.Period(x, freq='M')))['KC Unit Profit'].sum().reset_index())
dfs1 = [monthly_count, monthly_y_count, monthly_n_count, monthly_units_bet, est_be1, monthly_ni]
merged_df1 = monthly_count.merge(monthly_y_count, on='monthly_period').merge(monthly_n_count, on='monthly_period').merge(monthly_units_bet, on='monthly_period').merge(est_be1, on='monthly_period').merge(monthly_ni, on='monthly_period')
merged_df1['Hit Rate']= merged_df1['Y Count']/(merged_df1['Y Count']+merged_df1['N Count']) 
merged_df1['Est. BE Hit Rate']= 1 / merged_df1['Final Odds']
merged_df1['KC ROI']= merged_df1['KC Unit Profit'] / merged_df1['Sug. Units']
merged_df_display1 = merged_df1[['monthly_period','Count','Hit Rate','Est. BE Hit Rate','KC Unit Profit','KC ROI']]
rename_dict1 = {'monthly_period':'Month'}
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


summaries = st.columns(2)
summaries[0].dataframe(merged_df_display,hide_index=True)
summaries[1].dataframe(merged_df_display1,hide_index=True)
st.write('')

columns_to_format_as_decimal = ['Final Odds','Final Amt. Units' ]  #'KC Unit Result',
for column in columns_to_format_as_decimal:
    df_nba_result1[column] = df_nba_result1[column].map('{:.2f}'.format)
columns_to_format_as_decimal3 = ['Model Prob.','LV Odds-Imp. Prob.','KC Exp. EV in Units','KC Unit Profit','EV']
for column in columns_to_format_as_decimal3:
    df_nba_result1[column] = df_nba_result1[column].map('{:.3f}'.format)
    #df_nba_result1[column] = df_nba_result1[column].map(lambda x: '{:.1f}%'.format(x * 100))         
# columns_to_format_as_percentage1 = ['KF Sug. Size']
# for column in columns_to_format_as_percentage1:
#     df_nba_result1[column] = df_nba_result1[column].map(lambda x: '{:.2f}%'.format(x * 100))  
st.divider()
st.write('')
st.subheader('Team-Level Spreads - All Bets Made')
df_nba_result1['Date'] = pd.to_datetime(df_nba_result1['Date']).dt.strftime('%m-%d-%Y')
teams = sorted(pd.concat([df_nba_result1['Final Bet'], df_nba_result1['Opponent']]).unique())
selected_team_spread = st.selectbox('Team:', ['All'] + list(teams), key='Teams Spread')
# selected_split_spread = st.selectbox('Split Spread?:', ['All'] + list(spreads), key='Teams Spread 2')

if selected_team_spread != 'All':
    filtered_df = df_nba_result1[(df_nba_result1['Final Bet'] == selected_team_spread) | (df_nba_result1['Opponent'] == selected_team_spread)]
# if selected_split_spread  != 'All':
#     filtered_df = data_comb1[data_comb1['Split Bet?'] == selected_split_spread]
else:
    filtered_df = df_nba_result1

st.dataframe(filtered_df,hide_index=True)
st.write('')
st.divider()
st.subheader('Player-Level Spreads - All Bets Made')

df_nba_result2['Date'] = pd.to_datetime(df_nba_result2['Date']).dt.strftime('%m-%d-%Y')
teams1 = sorted(pd.concat([df_nba_result2['Final Bet'], df_nba_result2['Opponent']]).unique())
selected_team_spread1 = st.selectbox('Team:', ['All'] + list(teams1), key='Teams Spread 2')
# selected_split_spread = st.selectbox('Split Spread?:', ['All'] + list(spreads), key='Teams Spread 2')

if selected_team_spread1 != 'All':
    filtered_df1 = df_nba_result2[(df_nba_result2['Final Bet'] == selected_team_spread1) | (df_nba_result2['Opponent'] == selected_team_spread1)]
# if selected_split_spread  != 'All':
#     filtered_df = data_comb1[data_comb1['Split Bet?'] == selected_split_spread]
else:
    filtered_df1 = df_nba_result2

for column in columns_to_format_as_decimal:
    df_nba_result2[column] = df_nba_result2[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal3:
    #df_nba_result2[column] = df_nba_result2[column].map(lambda x: '{:.1f}%'.format(x * 100)) 
    df_nba_result2[column] = df_nba_result2[column].map('{:.3f}'.format)
st.dataframe(filtered_df1,hide_index=True)

st.write('')
st.divider()
st.subheader('Player-Level O/U - All Bets Made')
st.write('')
df_nba_result3['Date'] = pd.to_datetime(df_nba_result3['Date']).dt.strftime('%m-%d-%Y')
df_nba_result3 = df_nba_result3.dropna(subset='Home')
teams2 = sorted(pd.concat([df_nba_result3['Home'], df_nba_result3['Away']]).unique())
selected_team_spread2 = st.selectbox('Team:', ['All'] + list(teams2), key='Teams Spread 3')
# selected_split_spread = st.selectbox('Split Spread?:', ['All'] + list(spreads), key='Teams Spread 2')
if selected_team_spread2 != 'All':
    filtered_df2 = df_nba_result3[(df_nba_result3['Home'] == selected_team_spread2) | (df_nba_result3['Away'] == selected_team_spread2)]
# if selected_split_spread  != 'All':
#     filtered_df = data_comb1[data_comb1['Split Bet?'] == selected_split_spread]
else:
    filtered_df2 = df_nba_result3

for column in columns_to_format_as_decimal:
    df_nba_result3[column] = df_nba_result3[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal3:
    df_nba_result3[column] = df_nba_result3[column].map('{:.3f}'.format)

st.dataframe(filtered_df2,hide_index=True)