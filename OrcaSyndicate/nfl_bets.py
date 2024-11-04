import streamlit as st
import pandas as pd
from st_paywall import add_auth
import matplotlib.pyplot as plt
from  matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
import matplotlib.colors as mcolors
import numpy as np
import matplotlib

st.set_page_config(layout="wide")
if 'user_subscribed' not in st.session_state:
    st.session_state['user_subscribed'] = False

data_comb_py = pd.read_csv('C:/Users/ajaku/Downloads/py_all_display.csv')
data_comb_pa = pd.read_csv('C:/Users/ajaku/Downloads/pa_all_display.csv')
data_comb_pc = pd.read_csv('C:/Users/ajaku/Downloads/pc_all_display.csv')
data_comb_ptd = pd.read_csv('C:/Users/ajaku/Downloads/ptd_all_display.csv')
data_comb_int = pd.read_csv('C:/Users/ajaku/Downloads/int_all_display.csv')
data_comb_rec = pd.read_csv('C:/Users/ajaku/Downloads/rec_all_display.csv')
data_comb_rec_yd = pd.read_csv('C:/Users/ajaku/Downloads/rec_yd_all_display.csv')
data_comb_rush_yd = pd.read_csv('C:/Users/ajaku/Downloads/rush_yd_all_display.csv')
data_comb_rec_rb = pd.read_csv('C:/Users/ajaku/Downloads/rec_rb_all_display.csv')
data_comb_rec_yd_rb = pd.read_csv('C:/Users/ajaku/Downloads/rec_yd_rb_all_display.csv')
data_comb_rr_yd = pd.read_csv('C:/Users/ajaku/Downloads/rr_all_display.csv')

dfs = [data_comb_rec, data_comb_rec_yd, data_comb_rush_yd, data_comb_rec_rb,data_comb_rec_yd_rb,data_comb_rr_yd]  # List of your dataframes
new_column_names = {'week_y': 'Week','team': 'Team','position_group': 'Position','player_display_name': 'Player','market': 'Market','best over line': 'Best Over Line', 'best under line': 'Best Under Line'}  # Dictionary of column name changes

for df in dfs:
    df.rename(columns=new_column_names, inplace=True)

data_comb2 = pd.read_csv('C:/Users/ajaku/Downloads/all_qual_nfl_prop_display.csv')

data_comb_py = data_comb_py.dropna(subset=['Player'])
data_comb_py = data_comb_py[(data_comb_py['Best Over Line'] > 0)]
data_comb_pa = data_comb_pa.dropna()
data_comb_pa = data_comb_pa[(data_comb_pa['Best Over Line'] > 0)]
data_comb_pc = data_comb_pc.dropna()
data_comb_pc = data_comb_pc[(data_comb_pc['Best Over Line'] > 0)]
data_comb_ptd = data_comb_ptd.dropna()
data_comb_ptd = data_comb_ptd[(data_comb_ptd['Best Over Line'] > 0)]
data_comb_int = data_comb_int.dropna()  
data_comb_int = data_comb_int[(data_comb_int['Best Over Line'] > 0)]
data_comb_rec = data_comb_rec.dropna()
data_comb_rec = data_comb_rec[(data_comb_rec['Best Over Line'] > 0)]
data_comb_rec_yd = data_comb_rec_yd.dropna()
data_comb_rec_yd = data_comb_rec_yd[(data_comb_rec_yd['Best Over Line'] > 0)]
data_comb_rec_rb = data_comb_rec_rb.dropna()
data_comb_rec_rb = data_comb_rec_rb[(data_comb_rec_rb['Best Over Line'] > 0)]
data_comb_rec_yd_rb = data_comb_rec_yd_rb.dropna()
data_comb_rec_yd_rb = data_comb_rec_yd_rb[(data_comb_rec_yd_rb['Best Over Line'] > 0)]
data_comb_rush_yd = data_comb_rush_yd.dropna()
data_comb_rush_yd = data_comb_rush_yd[(data_comb_rush_yd['Best Over Line'] > 0)]
data_comb_rr_yd = data_comb_rr_yd.dropna()
data_comb_rr_yd = data_comb_rr_yd[(data_comb_rr_yd['Best Over Line'] > 0)]

#styled_df_py = data_comb1.style.apply(custom_background_gradient, cmap=cmap1, subset=['EV', 'Edge'])
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

data_comb_py['Week'] = data_comb_py['Week'].astype(int)
data_comb_pa['Week'] = data_comb_pa['Week'].astype(int)
data_comb_pc['Week'] = data_comb_pc['Week'].astype(int)
data_comb_ptd['Week'] = data_comb_ptd['Week'].astype(int)
data_comb_int['Week'] = data_comb_int['Week'].astype(int)
data_comb_rec['Week'] = data_comb_rec['Week'].astype(int)
data_comb_rec_yd['Week'] = data_comb_rec_yd['Week'].astype(int)
data_comb_rec_rb['Week'] = data_comb_rec_rb['Week'].astype(int)
data_comb_rec_yd_rb['Week'] = data_comb_rec_yd_rb['Week'].astype(int)
data_comb_rr_yd['Week'] = data_comb_rr_yd['Week'].astype(int)
data_comb_rush_yd['Week'] = data_comb_rush_yd['Week'].astype(int)

columns_to_format_as_decimal_py = ['Pass Yd. Proj.']
columns_to_format_as_decimal_pa = ['PA Proj.']
columns_to_format_as_decimal_pc = ['Pred. Completions']
columns_to_format_as_decimal_ptd = ['Final TD Proj.']
columns_to_format_as_decimal_int = ['Final INT Proj.']
columns_to_format_as_decimal_rec = ['Proj. Receptions']
columns_to_format_as_decimal_rec_yd = ['Proj. Receiving Yards']
columns_to_format_as_decimal_rec_rb = ['Proj. RB Receptions']
columns_to_format_as_decimal_rec_yd_rb = ['Proj. RB Receiving Yds']
columns_to_format_as_decimal_rr_yd = ['Proj. R+R Yds']
columns_to_format_as_decimal_rush_yd = ['Proj. Rush Yd']

columns_to_format_as_decimal2 = ['Final Over Prob.','Final Under Prob.']
columns_to_format_as_decimal2a = ['Over EV', 'Under EV']
columns_to_format_as_decimal3 = ['Best Over Line','Best Under Line']
columns_to_format_as_decimal4 = ['Model Proj.','Model Prob.','LV Odds-Imp. Prob.','EV','Edge']
columns_to_format_as_decimal5 = ['Sug. Units','Book Avg. Odds']
columns_to_format_as_decimal6 = ['Final Bet Total']

for column in columns_to_format_as_decimal_py:
    data_comb_py[column] = data_comb_py[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_pa:
    data_comb_pa[column] = data_comb_pa[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_pc:
    data_comb_pc[column] = data_comb_pc[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_ptd:
    data_comb_ptd[column] = data_comb_ptd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_int:
    data_comb_int[column] = data_comb_int[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rec:
    data_comb_rec[column] = data_comb_rec[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rec_yd:
    data_comb_rec_yd[column] = data_comb_rec_yd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rec_rb:
    data_comb_rec_rb[column] = data_comb_rec_rb[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rec_yd_rb:
    data_comb_rec_yd_rb[column] = data_comb_rec_yd_rb[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rr_yd:
    data_comb_rr_yd[column] = data_comb_rr_yd[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_rush_yd:
    data_comb_rush_yd[column] = data_comb_rush_yd[column].map('{:.2f}'.format)

for column in columns_to_format_as_decimal2a:
    data_comb_py[column] = data_comb_py[column].round(3)
    data_comb_pa[column] = data_comb_pa[column].round(3)
    data_comb_pc[column] = data_comb_pc[column].round(3)
    data_comb_ptd[column] = data_comb_ptd[column].round(3)
    data_comb_int[column] = data_comb_int[column].round(3)
    data_comb_rec[column] = data_comb_rec[column].round(3)
    data_comb_rec_yd[column] = data_comb_rec_yd[column].round(3)
    data_comb_rec_rb[column] = data_comb_rec_rb[column].round(3)
    data_comb_rec_yd_rb[column] = data_comb_rec_yd_rb[column].round(3)
    data_comb_rr_yd[column] = data_comb_rr_yd[column].round(3)
    data_comb_rush_yd[column] = data_comb_rush_yd[column].round(3)
for column in columns_to_format_as_decimal2:
    #data_comb_py[column] = data_comb_py[column].round(3)
    data_comb_py[column] = data_comb_py[column].map('{:.3f}'.format)
    data_comb_pa[column] = data_comb_pa[column].map('{:.3f}'.format)
    data_comb_pc[column] = data_comb_pc[column].map('{:.3f}'.format)
    data_comb_ptd[column] = data_comb_ptd[column].map('{:.3f}'.format)
    data_comb_int[column] = data_comb_int[column].map('{:.3f}'.format)
    data_comb_rec[column] = data_comb_rec[column].map('{:.3f}'.format)
    data_comb_rec_yd[column] = data_comb_rec_yd[column].map('{:.3f}'.format)
    data_comb_rec_rb[column] = data_comb_rec_rb[column].map('{:.3f}'.format)
    data_comb_rec_yd_rb[column] = data_comb_rec_yd_rb[column].map('{:.3f}'.format)
    data_comb_rr_yd[column] = data_comb_rr_yd[column].map('{:.3f}'.format)
    data_comb_rush_yd[column] = data_comb_rush_yd[column].map('{:.3f}'.format)

for column in columns_to_format_as_decimal3:
    data_comb_py[column] = data_comb_py[column].map('{:.1f}'.format)
    data_comb_pa[column] = data_comb_pa[column].map('{:.1f}'.format)
    data_comb_pc[column] = data_comb_pc[column].map('{:.1f}'.format)
    data_comb_ptd[column] = data_comb_ptd[column].map('{:.1f}'.format)
    data_comb_int[column] = data_comb_int[column].map('{:.1f}'.format)
    data_comb_rec[column] = data_comb_rec[column].map('{:.1f}'.format)
    data_comb_rec_yd[column] = data_comb_rec_yd[column].map('{:.1f}'.format)
    data_comb_rec_rb[column] = data_comb_rec_rb[column].map('{:.1f}'.format)
    data_comb_rec_yd_rb[column] = data_comb_rec_yd_rb[column].map('{:.1f}'.format)
    data_comb_rr_yd[column] = data_comb_rr_yd[column].map('{:.1f}'.format)
    data_comb_rush_yd[column] = data_comb_rush_yd[column].map('{:.1f}'.format)

styled_df_py = data_comb_py.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_py = styled_df_py.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_pa = data_comb_pa.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pa = styled_df_pa.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_pc = data_comb_pc.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pc= styled_df_pc.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_ptd = data_comb_ptd.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_ptd= styled_df_ptd.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_int = data_comb_int.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_int= styled_df_int.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rec = data_comb_rec.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rec= styled_df_rec.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rec_yd = data_comb_rec_yd.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rec_yd= styled_df_rec_yd.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rec_rb = data_comb_rec_rb.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rec_rb= styled_df_rec_rb.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rec_yd_rb = data_comb_rec_yd_rb.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rec_yd_rb= styled_df_rec_yd_rb.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rr_yd = data_comb_rr_yd.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rr_yd= styled_df_rr_yd.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_rush_yd = data_comb_rush_yd.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_rush_yd= styled_df_rush_yd.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})

def display_login_status():
    if st.session_state['user_subscribed']==True:
    #if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write('')
        st.header('NFL Player Prop Model Bets',divider="gray")
        #st.header('Suggested Bets',divider="gray")
        for column in columns_to_format_as_decimal4:
            data_comb2[column] = data_comb2[column].map('{:.3f}'.format)
        for column in columns_to_format_as_decimal5:
            data_comb2[column] = data_comb2[column].map('{:.2f}'.format)
        for column in columns_to_format_as_decimal6:
            data_comb2[column] = data_comb2[column].map('{:.1f}'.format)

        market = sorted(data_comb2['Market'].unique())
        position = sorted(data_comb2['Position'].unique())

        selected_market = st.selectbox('Market:', ['All'] + list(market), key='NFL1')
        selected_position = st.selectbox('Position:', ['All'] + list(position), key='NFL2')

        filtered_df = data_comb2

        # Apply the market filter
        if selected_market != 'All':
            filtered_df = filtered_df[filtered_df['Market'] == selected_market]

        # Apply the position filter
        if selected_position != 'All':
            filtered_df = filtered_df[filtered_df['Position'] == selected_position]
        st.dataframe(filtered_df.style.background_gradient(cmap="Greens", subset=['EV','Edge','Sug. Units']),hide_index=True) 
        st.write('')
        st.write('')

        st.header('All Prop Bets Available',divider="gray")
        st.header('Passing Yards')
        st.dataframe(styled_df_py, hide_index=True)
        st.write('')
        st.header('Passing Attempts')
        st.dataframe(styled_df_pa, hide_index=True)
        st.write('')
        st.header('Completions')
        st.dataframe(styled_df_pc, hide_index=True)
        st.write('')
        st.header('Passing TDs')
        st.dataframe(styled_df_ptd, hide_index=True)
        st.write('')
        st.header('Interceptions')
        st.dataframe(styled_df_int, hide_index=True)
        st.write('')
        st.header('Receptions - WR & TE')
        st.dataframe(styled_df_rec, hide_index=True)
        st.write('')
        st.header('Receiving Yards - WR & TE')
        st.dataframe(styled_df_rec_yd, hide_index=True)
        st.header('Rushing Yards')
        st.dataframe(styled_df_rush_yd, hide_index=True)
        st.write('')
        st.header('Receptions - RB')
        st.dataframe(styled_df_rec_rb, hide_index=True)
        st.write('')
        st.header('Receiving Yards - RB')
        st.dataframe(styled_df_rec_yd_rb, hide_index=True)
        st.write('')
        st.header('Rushing + Receiving Yards')
        st.dataframe(styled_df_rr_yd, hide_index=True)

    else:
        st.header('NFL Player Prop Model Bets',divider="gray")
        #st.header('Suggested Bets',divider="gray")
        st.write("Subscribe now for full access to all our suggested bets!")
        st.write('')
        #st.header('All Prop Bets Available',divider="gray")
        #st.dataframe(styled_df_py, hide_index=True)

        #st.dataframe(data_comb1.style.background_gradient(cmap="RdYlGn", subset=['EV','Edge']),hide_index=True) 

#st.write(st.session_state)
display_login_status()  





