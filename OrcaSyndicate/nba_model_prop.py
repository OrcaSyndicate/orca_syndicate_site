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

st.header('NBA Player Prop Model Bets',divider="gray")
#st.markdown("### _Currently in the offseason, check back later!_")
st.markdown("### _Currently collecting data during the first few games of the season, check back later!_")

data_comb_pts = pd.read_csv('https://www.dropbox.com/scl/fi/f4li33lrqog6y22nueiih/pts_all_display.csv?rlkey=gjvhwza956td1slgbdm04853t&st=wmadmwtn&dl=1')
data_comb_reb = pd.read_csv('https://www.dropbox.com/scl/fi/70zndne09ajr3qt1wlamb/reb_all_display.csv?rlkey=nnjk7wxdzvn76bh3wfyd8euam&st=u53riq53&dl=1')
data_comb_ast = pd.read_csv('https://www.dropbox.com/scl/fi/qzp83j5f4djrzlekc613x/ast_all_display.csv?rlkey=g46zjgs8gtdrb19k6n3i5itv7&st=hwnqakgv&dl=1')
data_comb_blk = pd.read_csv('https://www.dropbox.com/scl/fi/uq41a40qapjebhuuuiqk8/blk_all_display.csv?rlkey=1741lubt2upwwpdoopnfjemia&st=p8tvcv8v&dl=1')
data_comb_stl = pd.read_csv('https://www.dropbox.com/scl/fi/zah8pp18drlq9q46eulfr/stl_all_display.csv?rlkey=xlcylhg8do6p4yo17aoloeld7&st=p4nwjd06&dl=1')
data_comb_sb = pd.read_csv('https://www.dropbox.com/scl/fi/kvqq8vwks7rd2935zanm0/sb_all_display.csv?rlkey=o1yjntuemy9st7yi2o2rculfk&st=lsla63u5&dl=1')
data_comb_tpm = pd.read_csv('https://www.dropbox.com/scl/fi/cnyskvyevh19z9onvjw0i/tpm_all_display.csv?rlkey=90f9qje6tovp1kpum4m0g7myf&st=2ownuow5&dl=1')
data_comb_to = pd.read_csv('https://www.dropbox.com/scl/fi/txk045l559bsdzk3c68qq/to_all_display.csv?rlkey=uvpj0ecl1qogtswrjbe11bx8q&st=2hi378nw&dl=1')
data_comb_pra = pd.read_csv('https://www.dropbox.com/scl/fi/8e6s69pkhjt9fmvwkq5x1/pra_all_display.csv?rlkey=d2qku3np3iyziduzb31ifvlh8&st=308go46c&dl=1')
data_comb_pr = pd.read_csv('https://www.dropbox.com/scl/fi/729rolvxd6jzpohzfushs/pr_all_display.csv?rlkey=gxhigdu86kqrixb3vziid2m2z&st=6ps003jh&dl=1')
data_comb_pa = pd.read_csv('https://www.dropbox.com/scl/fi/306q81mpwr8d4meswvw95/nba_pa_all_display.csv?rlkey=nygdds1nygc5x1tjf9d1v4c16&st=in3nosu8&dl=1')
data_comb_ra= pd.read_csv('https://www.dropbox.com/scl/fi/6tujveaiv70xkmpy9e9v1/ra_all_display.csv?rlkey=ctalorsuexvzd2wswka77gs0l&st=imk1qu3b&dl=1')

dfs = [data_comb_pts, data_comb_reb, data_comb_ast, data_comb_tpm,data_comb_blk,data_comb_stl]  # List of your dataframes
new_column_names = {}  # Dictionary of column name changes

for df in dfs:
    df.rename(columns=new_column_names, inplace=True)

data_comb2 = pd.read_csv('https://www.dropbox.com/scl/fi/ey9uvgx0nyop56shu07xs/all_qual_nba_prop_display.csv?rlkey=e687c6p5nqprmk79p4bmobfh2&st=t77ccdmf&dl=1')

data_comb_pts = data_comb_pts.dropna(subset=['Player'])
data_comb_pts = data_comb_pts[(data_comb_pts['Best Over Line'] > 0)]
data_comb_reb = data_comb_reb.dropna()
data_comb_reb = data_comb_reb[(data_comb_reb['Best Over Line'] > 0)]
data_comb_ast = data_comb_ast.dropna()
data_comb_ast = data_comb_ast[(data_comb_ast['Best Over Line'] > 0)]
data_comb_stl = data_comb_stl.dropna()
data_comb_stl = data_comb_stl[(data_comb_stl['Best Over Line'] > 0)]
data_comb_blk = data_comb_blk.dropna()  
data_comb_blk = data_comb_blk[(data_comb_blk['Best Over Line'] > 0)]
data_comb_sb = data_comb_sb.dropna()
data_comb_sb = data_comb_sb[(data_comb_sb['Best Over Line'] > 0)]
data_comb_to = data_comb_to.dropna()
data_comb_to = data_comb_to[(data_comb_to['Best Over Line'] > 0)]
data_comb_tpm = data_comb_tpm.dropna()
data_comb_tpm = data_comb_tpm[(data_comb_tpm['Best Over Line'] > 0)]
data_comb_pra = data_comb_pra.dropna()
data_comb_pra = data_comb_pra[(data_comb_pra['Best Over Line'] > 0)]
data_comb_pr = data_comb_pr.dropna()
data_comb_pr = data_comb_pr[(data_comb_pr['Best Over Line'] > 0)]
data_comb_pa = data_comb_pa.dropna()
data_comb_pa = data_comb_pa[(data_comb_pa['Best Over Line'] > 0)]
data_comb_ra = data_comb_ra.dropna()
data_comb_ra = data_comb_ra[(data_comb_ra['Best Over Line'] > 0)]

#styled_df_py = data_comb1.style.apply(custom_background_gradient, cmap=cmap1, subset=['EV', 'Edge'])
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

#data_comb_py['Week'] = data_comb_py['Week'].astype(int)
#data_comb_pa['Week'] = data_comb_pa['Week'].astype(int)
#data_comb_pc['Week'] = data_comb_pc['Week'].astype(int)
#data_comb_ptd['Week'] = data_comb_ptd['Week'].astype(int)
#data_comb_int['Week'] = data_comb_int['Week'].astype(int)
#data_comb_rec['Week'] = data_comb_rec['Week'].astype(int)
#data_comb_rec_yd['Week'] = data_comb_rec_yd['Week'].astype(int)
#data_comb_rec_rb['Week'] = data_comb_rec_rb['Week'].astype(int)
#data_comb_rec_yd_rb['Week'] = data_comb_rec_yd_rb['Week'].astype(int)
#data_comb_rr_yd['Week'] = data_comb_rr_yd['Week'].astype(int)
#data_comb_rush_yd['Week'] = data_comb_rush_yd['Week'].astype(int)

columns_to_format_as_decimal = ['Pts. Proj.']
columns_to_format_as_decimal_reb = ['Reb. Proj.']
columns_to_format_as_decimal_ast = ['Ast. Proj.']
columns_to_format_as_decimal_blk = ['Blk. Proj.']
columns_to_format_as_decimal_stl = ['Stl. Proj.']
columns_to_format_as_decimal_tpm = ['3PM Proj.']
columns_to_format_as_decimal_sb = ['S+B Proj.']
columns_to_format_as_decimal_to = ['TO Proj.']
columns_to_format_as_decimal_pra = ['PRA Proj.']
columns_to_format_as_decimal_pr= ['PR Proj.']
columns_to_format_as_decimal_pa = ['PA Proj.']
columns_to_format_as_decimal_ra = ['RA Proj.']

columns_to_format_as_decimal2 = ['Final Over Prob.','Final Under Prob.']
columns_to_format_as_decimal2a = ['Over EV', 'Under EV']
columns_to_format_as_decimal3 = ['Best Over Line','Best Under Line']
columns_to_format_as_decimal4 = ['Model Proj.','Model Prob.','LV Odds-Imp. Prob.','EV','Edge']
columns_to_format_as_decimal5 = ['Sug. Units','Final Odds']  #Book Avg. Odds
columns_to_format_as_decimal6 = ['Final Bet Total']

for column in columns_to_format_as_decimal:
    data_comb_pts[column] = data_comb_pts[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_reb:
    data_comb_reb[column] = data_comb_reb[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_ast:
    data_comb_ast[column] = data_comb_ast[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_blk:
    data_comb_blk[column] = data_comb_blk[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_stl:
    data_comb_stl[column] = data_comb_stl[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_tpm:
    data_comb_tpm[column] = data_comb_tpm[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_sb:
    data_comb_sb[column] = data_comb_sb[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_to:
    data_comb_to[column] = data_comb_to[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_pra:
    data_comb_pra[column] = data_comb_pra[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_pr:
    data_comb_pr[column] = data_comb_pr[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_pa:
    data_comb_pa[column] = data_comb_pa[column].map('{:.2f}'.format)
for column in columns_to_format_as_decimal_ra:
    data_comb_ra[column] = data_comb_ra[column].map('{:.2f}'.format)

for column in columns_to_format_as_decimal2a:
    data_comb_pts[column] = data_comb_pts[column].round(3)
    data_comb_reb[column] = data_comb_reb[column].round(3)
    data_comb_ast[column] = data_comb_ast[column].round(3)
    data_comb_tpm[column] = data_comb_tpm[column].round(3)
    data_comb_stl[column] = data_comb_stl[column].round(3)
    data_comb_blk[column] = data_comb_blk[column].round(3)
    data_comb_sb[column] = data_comb_sb[column].round(3)
    data_comb_to[column] = data_comb_to[column].round(3)
    data_comb_pra[column] = data_comb_pra[column].round(3)
    data_comb_pr[column] = data_comb_pr[column].round(3)
    data_comb_pa[column] = data_comb_pa[column].round(3)
    data_comb_ra[column] = data_comb_ra[column].round(3)
for column in columns_to_format_as_decimal2:
    #data_comb_reb[column] = data_comb_reb[column].round(3)
    data_comb_pts[column] = data_comb_pts[column].map('{:.3f}'.format)
    data_comb_pa[column] = data_comb_pa[column].map('{:.3f}'.format)
    data_comb_ast[column] = data_comb_ast[column].map('{:.3f}'.format)
    data_comb_blk[column] = data_comb_blk[column].map('{:.3f}'.format)
    data_comb_stl[column] = data_comb_stl[column].map('{:.3f}'.format)
    data_comb_tpm[column] = data_comb_tpm[column].map('{:.3f}'.format)
    data_comb_pra[column] = data_comb_pra[column].map('{:.3f}'.format)
    data_comb_pr[column] = data_comb_pr[column].map('{:.3f}'.format)
    data_comb_ra[column] = data_comb_ra[column].map('{:.3f}'.format)
    data_comb_reb[column] = data_comb_reb[column].map('{:.3f}'.format)
    data_comb_sb[column] = data_comb_sb[column].map('{:.3f}'.format)
    data_comb_to[column] = data_comb_to[column].map('{:.3f}'.format)

for column in columns_to_format_as_decimal3:
    data_comb_pts[column] = data_comb_pts[column].map('{:.1f}'.format)
    data_comb_pa[column] = data_comb_pa[column].map('{:.1f}'.format)
    data_comb_reb[column] = data_comb_reb[column].map('{:.1f}'.format)
    data_comb_ast[column] = data_comb_ast[column].map('{:.1f}'.format)
    data_comb_tpm[column] = data_comb_tpm[column].map('{:.1f}'.format)
    data_comb_blk[column] = data_comb_blk[column].map('{:.1f}'.format)
    data_comb_stl[column] = data_comb_stl[column].map('{:.1f}'.format)
    data_comb_sb[column] = data_comb_sb[column].map('{:.1f}'.format)
    data_comb_to[column] = data_comb_to[column].map('{:.1f}'.format)
    data_comb_pra[column] = data_comb_pra[column].map('{:.1f}'.format)
    data_comb_pr[column] = data_comb_pr[column].map('{:.1f}'.format)
    data_comb_ra[column] = data_comb_ra[column].map('{:.1f}'.format)

styled_df_pts = data_comb_pts.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pts = styled_df_pts.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})

styled_df_pa = data_comb_pa.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pa = styled_df_pa.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_reb = data_comb_reb.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_reb= styled_df_reb.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_ast = data_comb_ast.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_ast= styled_df_ast.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_blk = data_comb_blk.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_blk= styled_df_blk.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_stl = data_comb_stl.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_stl= styled_df_stl.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_sb = data_comb_sb.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_sb= styled_df_sb.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_to = data_comb_to.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_to= styled_df_to.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_pra = data_comb_pra.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pra= styled_df_pra.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_pr = data_comb_pr.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_pr= styled_df_pr.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_ra = data_comb_ra.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_ra= styled_df_ra.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})
styled_df_tpm = data_comb_tpm.style.applymap(color_negative_red, subset=['Over EV', 'Under EV'])
styled_df_tpm= styled_df_tpm.format({col: '{:.3f}'.format for col in columns_to_format_as_decimal2a})


def display_login_status():
    if st.session_state['user_subscribed']==True:
    #if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write('')
        st.header('Suggested Bets',divider="gray")
        for column in columns_to_format_as_decimal4:
            data_comb2[column] = data_comb2[column].map('{:.3f}'.format)
        for column in columns_to_format_as_decimal5:
            data_comb2[column] = data_comb2[column].map('{:.2f}'.format)
        for column in columns_to_format_as_decimal6:
            data_comb2[column] = data_comb2[column].map('{:.1f}'.format)

        market = sorted(data_comb2['Market'].unique())
        team = sorted(data_comb2['Team'].unique())

        selected_market = st.selectbox('Market:', ['All'] + list(market), key='NBA1')
        selected_team = st.selectbox('Team:', ['All'] + list(team), key='NBA2')

        filtered_df = data_comb2

        # Apply the market filter
        if selected_market != 'All':
            filtered_df = filtered_df[filtered_df['Market'] == selected_market]

        # Apply the position filter
        if selected_team != 'All':
            filtered_df = filtered_df[filtered_df['Team'] == selected_team]
        st.dataframe(filtered_df.style.background_gradient(cmap="Greens", subset=['EV','Edge','Sug. Units']),hide_index=True) 
        st.write('')
        st.write('')

        st.header('All Prop Bets Available',divider="gray")
        st.header('Points')
        st.dataframe(styled_df_pts, hide_index=True)
        st.write('')
        st.header('Rebounds')
        st.dataframe(styled_df_reb, hide_index=True)
        st.write('')
        st.header('Assists')
        st.dataframe(styled_df_ast, hide_index=True)
        st.write('')
        st.header('TPM')
        st.dataframe(styled_df_tpm, hide_index=True)
        st.header('Blocks')
        st.dataframe(styled_df_blk, hide_index=True)
        st.write('')
        st.header('Steals')
        st.dataframe(styled_df_stl, hide_index=True)
        st.write('')
        st.header('S+B')
        st.dataframe(styled_df_sb, hide_index=True)
        st.write('')
        st.header('TO')
        st.dataframe(styled_df_to, hide_index=True)
        st.header('PRA')
        st.dataframe(styled_df_pra, hide_index=True)
        st.write('')
        st.header('PA')
        st.dataframe(styled_df_pa, hide_index=True)
        st.write('')
        st.header('PR')
        st.dataframe(styled_df_pr, hide_index=True)
        st.write('')
        st.header('RA')
        st.dataframe(styled_df_ra, hide_index=True)
    else:
        st.header('Suggested Bets',divider="gray")
        st.write("Subscribe now for full access to all our suggested prop bets!")
        st.write('')
        #st.header('All Prop Bets Available',divider="gray")
        #st.dataframe(styled_df_py, hide_index=True)

        #st.dataframe(data_comb1.style.background_gradient(cmap="RdYlGn", subset=['EV','Edge']),hide_index=True) 

display_login_status()  
st.dataframe(styled_df_pts, hide_index=True)
filtered_df=data_comb2
st.dataframe(filtered_df.style.background_gradient(cmap="Greens", subset=['EV','Edge','Sug. Units']),hide_index=True) 

#st.write('')
#st.write('')
#st.write('')
#st.write('')
#st.write('')
#st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/nba_prop_placeholder.png?raw=true')
