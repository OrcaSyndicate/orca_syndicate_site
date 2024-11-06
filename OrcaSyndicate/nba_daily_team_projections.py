import streamlit as st
import pandas as pd
import plost
import altair as alt

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

st.set_page_config(layout="wide")

st.header('Team Level Game Projections',divider="gray")
st.markdown("### _*Updated team model coming soon!_ :grin:")
st.write('')

st.header('Player Level Game Projections',divider="gray")
data_comb1 = pd.read_excel('https://www.dropbox.com/scl/fi/qgdt7f611n9nl7yt7oxdp/NBA_Prop_Projections_Raw1.xlsx?rlkey=gqnvhocov11naejwvqrdzlavs&st=u8oynrle&dl=1',usecols=list(range(28,45)))
data_comb1 = data_comb1.dropna(subset=['Home'])
data_comb1['Date'] = pd.to_datetime(data_comb1['Date']).dt.strftime('%m-%d-%Y')
#data_comb11 =  data_comb1.rename(columns={'Final Min. Est.': 'minutes_est','Pts. Est.': 'pts_proj','RA Est.':'ra_proj'})

#styled_df_plg = data_comb1.style.applymap(color_negative_red, subset=['Home Off./100','Away Off./100','Home Def./100','Away Def./100','Home Pts. Above Avg./100','Away Pts. Above Avg./100'])
columns_to_format_as_decimal = ['Fair Home Spread','Home Court Adv.']
columns_to_format_as_decimal3 = ['Home Cover Prob.','Away Rotation Deviation','Home Rotation Deviation','Pred. Pace','Home Off./100','Away Off./100','Home Def./100','Away Def./100','Home Pts. Above Avg./100','Away Pts. Above Avg./100']
columns_to_format_as_decimal1 = ['Act. Home Spread','O/U']


#   styled_df_plg1  = styled_df_plg.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal3}).format({col: '{:.2f}'.format for col in columns_to_format_as_decimal})
#styled_df_plg2  = styled_df_plg1.format({col: '{:.2f}'.format for col in columns_to_format_as_decimal})
styled_df_plg = data_comb1.style
styled_df_plg1 = (styled_df_plg.applymap(color_negative_red, subset=['Home Off./100', 'Away Off./100', 'Home Def./100', 'Away Def./100', 'Home Pts. Above Avg./100', 'Away Pts. Above Avg./100']))
styled_df_plg1 = styled_df_plg1.background_gradient(cmap="Reds", subset=['Home Rotation Deviation', 'Away Rotation Deviation'])
styled_df_plg1 = styled_df_plg1.background_gradient(cmap="YlGn", subset=['Pred. Pace'])

format_dict = {}
format_dict.update({col: '{:.2f}'.format for col in columns_to_format_as_decimal})
format_dict.update({col: '{:.3f}'.format for col in columns_to_format_as_decimal3})
format_dict.update({col: '{:.1f}'.format for col in columns_to_format_as_decimal1})

# Apply formatting to all specified columns
styled_df_plg2 = styled_df_plg1.format(format_dict)
st.dataframe(styled_df_plg2,hide_index=True)
