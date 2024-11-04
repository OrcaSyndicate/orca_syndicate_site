import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Soccer Team Models - Suggested Bets History',divider="gray")
st.write('')
st.subheader('Performance Summary')

data_comb1 = pd.read_excel('C:/Users/ajaku/Downloads/soccer_data_website.xlsx', sheet_name=1)
data_comb1 = data_comb1.dropna(subset=['Final Bet'])
data_comb1['Date'] = pd.to_datetime(data_comb1['Date']).dt.strftime('%m-%d-%Y')
result_helper= data_comb1
# result_helper['Sug. Units'] = result_helper['Sug. Units'].astype(float)
# result_helper['Final Odds'] = result_helper['Final Odds'].astype(float)
# result_helper['KC Unit Profit'] = result_helper['KC Unit Profit'].astype(float)

total_y_count = len((result_helper[result_helper['Correct?'] == 'WW'].value_counts().reset_index()))
total_n_count = len((result_helper[result_helper['Correct?'] == 'LL'].value_counts().reset_index()))
total_units_bet = (result_helper['Sug. Units'].sum())
total_unit_profit= (result_helper['KC Unit Profit'].sum())
avg_odds = result_helper['Book Odds'].mean()

result_helper['date_column'] = pd.to_datetime(result_helper['Date']).dt.date
grouped = result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))
monthly_count = result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size()

monthly_count = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size())
monthly_y_count = pd.DataFrame(result_helper[result_helper['Correct?'] == 'WW'].groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size().reset_index())
monthly_n_count =  pd.DataFrame(result_helper[result_helper['Correct?'] == 'LL'].groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M'))).size().reset_index())
monthly_units_bet = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['Sug. Units'].sum().reset_index())
est_be1 = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['Book Odds'].mean().reset_index())
monthly_ni = pd.DataFrame(result_helper.groupby(result_helper['date_column'].map(lambda x: pd.Period(x, freq='M')))['KC Unit Profit'].sum().reset_index())

dfs1 = [monthly_count, monthly_y_count, monthly_n_count, monthly_units_bet, est_be1, monthly_ni]
merged_df1 = monthly_count.merge(monthly_y_count, on='date_column').merge(monthly_n_count, on='date_column').merge(monthly_units_bet, on='date_column').merge(est_be1, on='date_column').merge(monthly_ni, on='date_column')
merged_df1['Hit Rate']= merged_df1['0_y']/(merged_df1['0_y']+merged_df1[0]) 
merged_df1['Est. BE Hit Rate']= 1 / merged_df1['Book Odds']
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
    merged_df_display1[column] = merged_df_display1[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['Hit Rate','Est. BE Hit Rate','KC ROI' ]
for column in columns_to_format_as_percentage:
    merged_df_display1[column] = merged_df_display1[column].map(lambda x: '{:.1f}%'.format(x * 100)) 
summaries = st.columns(2)
summaries[0].dataframe(merged_df_display1,hide_index=True)
st.divider()
st.write('')
st.subheader('All Bets Made')

columns_to_format_as_decimal = ['Book Odds','KC Unit Profit','KC Result','KC $ Profit']
for column in columns_to_format_as_decimal:
    data_comb1[column] = data_comb1[column].map('{:.2f}'.format)
columns_to_format_as_percentage = ['Model Prob.','LV MF Prob.']
for column in columns_to_format_as_percentage:
    data_comb1[column] = data_comb1[column].map(lambda x: '{:.1f}%'.format(x * 100))         
columns_to_format_as_percentage1 = ['KF Size']
for column in columns_to_format_as_percentage1:
    data_comb1[column] = data_comb1[column].map(lambda x: '{:.2f}%'.format(x * 100))   
#   
teams = sorted(pd.concat([data_comb1['Final Bet'], data_comb1['Opponent']]).unique())
spreads = sorted(pd.concat([data_comb1['Split Bet?']]).unique())
selected_team_spread = st.selectbox('Team:', ['All'] + list(teams), key='Teams Spread')
selected_split_spread = st.selectbox('Split Spread?:', ['All'] + list(spreads), key='Teams Spread 2')

if selected_team_spread != 'All':
    filtered_df = data_comb1[(data_comb1['Home'] == selected_team_spread) | (data_comb1['Away'] == selected_team_spread)]
if selected_split_spread  != 'All':
    filtered_df = data_comb1[data_comb1['Split Bet?'] == selected_split_spread]
else:
    filtered_df = data_comb1
data_comb1['Book Odds'] = data_comb1['Book Odds'].astype(float)
st.dataframe(filtered_df,hide_index=True)