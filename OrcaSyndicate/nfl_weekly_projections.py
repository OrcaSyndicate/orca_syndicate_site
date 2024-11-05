import streamlit as st
import pandas as pd
import plost
import altair as alt


st.set_page_config(layout="wide")

st.markdown("###### _*Note that players must have played in at least 4 games this season (started, for QBs) in order to qualify for the tables. For pass catchers, their QB must have started at least 4 games as well._")

st.header('QB Projections',divider="gray")
data_comb1 = pd.read_csv('https://www.dropbox.com/scl/fi/s059a0nzlk4wre3r4kdqo/qb_site_display.csv?rlkey=9hhp34jfzhzy6alzgu2eewadm&st=4gourw9w&dl=0')
data_comb1 = data_comb1.dropna(subset=['Player'])
data_comb1 = data_comb1.rename(columns={'Pred. Completions':'Cmp. Proj.'})
columns_to_format_as_decimal = ['Pass Yd. Proj.','PA Proj.','Cmp. Proj.','Final TD Proj.','Final INT Proj.',]
for column in columns_to_format_as_decimal:
  data_comb1[column] = data_comb1[column].map('{:.2f}'.format)

data_comb11 =  data_comb1.rename(columns={'Pass Yd. Proj.': 'py_proj','PA Proj.': 'pa_proj'})
#qb_chart =st.image('C:/Users/ajaku/Downloads/qb_chart.png')


chart = alt.Chart(data_comb11).mark_circle().encode(
    
    x=alt.X('pa_proj', sort='ascending',axis=alt.Axis(format='.1f')) ,
    y=alt.Y('py_proj', sort='descending',axis=alt.Axis(format='.1f')),
    tooltip=['Player', 'pa_proj', 'py_proj']
).interactive()
#st.altair_chart(chart)

#st.dataframe(data_comb11,hide_index=True)
summaries = st.columns(2)
summaries[0].dataframe(data_comb1,hide_index=True)
summaries[1].altair_chart(chart)
st.write('')

st.header('RB Projections',divider="gray")
data_comb2 = pd.read_csv('C:/Users/ajaku/Downloads/rb_site_display.csv')
data_comb2 = data_comb2.dropna(subset=['Player'])
columns_to_format_as_decimal1 =   ['Final Carries', 'Final YpC','Proj. Rush Yd', 'Proj. RB Receptions', 'Final YpR','Proj. RB Receiving Yds', 'Proj. RushTDs', 'Proj. RB RecTDs','ATTD Prob. %', 'Standard Fantasy Score', 'PPR Fantasy Score']
for column in columns_to_format_as_decimal1:
    data_comb2[column] = data_comb2[column].map('{:.2f}'.format)

team2 = sorted(data_comb2['Team'].unique())
selected_team2 = st.selectbox('Team:', ['All'] + list(team2), key='RB Players')
if selected_team2 != 'All':
    filtered_df2 = data_comb2[(data_comb2['Team'] == selected_team2)]
else:
    filtered_df2 = data_comb2
st.dataframe(filtered_df2,hide_index=True)
st.write('')

st.header('WR & TE Projections',divider="gray")
data_comb3 = pd.read_csv('C:/Users/ajaku/Downloads/wr_site_display.csv')
data_comb3 = data_comb3.dropna(subset=['Player'])
columns_to_format_as_decimal2 = ['Proj. Receptions', 'Final YpC', 'Proj. Receiving Yards','Proj. RecTDs', 'ATTD Prob. %', 'Standard Fantasy Score','PPR Fantasy Score']
columns_to_format_as_decimal3 = ['Target Share','Catch Rate']

for column in columns_to_format_as_decimal2:
    data_comb3[column] = data_comb3[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal3:
    data_comb3[column] = data_comb3[column].map('{:.3f}'.format)

team3 = sorted(data_comb3['Team'].unique())
selected_team3 = st.selectbox('Team:', ['All'] + list(team3), key='WR Players')
if selected_team3 != 'All':
    filtered_df3 = data_comb3[(data_comb3['Team'] == selected_team3)]
else:
    filtered_df3 = data_comb3
st.dataframe(filtered_df3,hide_index=True)
st.write('')

st.header('Anytime TD Probabilities',divider="gray")
data_comb4 = pd.read_csv('C:/Users/ajaku/Downloads/td_site_display.csv')
data_comb4a = data_comb4
data_comb4 = data_comb4.dropna(subset=['Player'])
data_comb4['ATTD Prob. %'] = data_comb4['ATTD Prob. %'].map('{:.2f}'.format)
data_comb4.drop(['Proj. Touches', 'Proj. TDs/Proj. Touches'], axis=1, inplace=True)

team4 = sorted(data_comb4['Team'].unique())
selected_team4 = st.selectbox('Team:', ['All'] + list(team4), key='ATTD Players')
if selected_team4 != 'All':
    filtered_df4 = data_comb4[(data_comb4['Team'] == selected_team4)]
else:
    filtered_df4 = data_comb4

columns_to_format_as_decimal_attd = ['Proj. Touches','Proj. TDs/Proj. Touches']
for column in columns_to_format_as_decimal_attd:
  data_comb4a[column] = data_comb4a[column].round(3)

data_comb41 =  data_comb4a.rename(columns={'Proj. Touches': 'proj_touches','Proj. TDs/Proj. Touches': 'proj_tds_per_touch'})
#td_chart =st.image('C:/Users/ajaku/Downloads/td_chart.png')


chart1 = alt.Chart(data_comb41).mark_circle().encode(
    
    x=alt.X('proj_tds_per_touch', sort='ascending',axis=alt.Axis(format='.2f')) ,
    y=alt.Y('proj_touches', sort='ascending',axis=alt.Axis(format='.1f')),
    tooltip=['Player','Position', 'proj_tds_per_touch', 'proj_touches']
).interactive()
#st.altair_chart(chart)

summaries = st.columns(2)
summaries[0].dataframe(filtered_df4,hide_index=True)
summaries[1].altair_chart(chart1)

#st.dataframe(filtered_df4,hide_index=True)
