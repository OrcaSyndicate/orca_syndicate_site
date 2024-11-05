import streamlit as st
from st_paywall import add_auth


def custom_add_auth(**kwargs):
    result = add_auth(**kwargs)
    	
    st.markdown(""" div.stButton > button:first-child {
	background-color: #00cc00;color:white;font-size:20px;border-radius:10px 10px 10px 10px;
	}
	“”", unsafe_allow_html=True)
    
    return result


#st.title('Orca Syndicate')
#st.header('Scientific Sports Betting')
# st.set_page_config(layout="wide")



current_page = st.navigation({ 
    "Home": [
    st.Page("about.py", title="About Orca Syndicate", icon=":material/star:"),
    #st.Page("my_account.py", title="My Account", icon=":material/account_circle:")
        # ...
    ],  

    "NFL - Player Prop Models": [
    st.Page("nfl_props.py", title="Model Intro & Test Data", icon=":material/sports_football:"),
    st.Page("nfl_weekly_projections.py", title="Weekly Projections", icon=":material/sports_football:"),
    #st.Page("nfl_bets.py", title="Suggested Bets - Upcoming Games", icon=":material/sports_football:"),
    #st.Page("nfl_prop_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_football:"),
    ],     
    "NBA - Game Projection Models": [
    st.Page("nba_model_team.py", title="Model Intro & Test Data", icon=":material/sports_basketball:"),
    st.Page("nba_daily_team_projections.py", title="Daily Game Projections", icon=":material/sports_basketball:"),
    #st.Page("nba_bets.py", title="Suggested Bets - Upcoming Games", icon=":material/sports_basketball:"),
    #st.Page("nba_team_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_basketball:"),
],
    "NBA - Player Prop Models": [
    st.Page("nba_player_props.py", title="Model Intro & Test Data", icon=":material/sports_basketball:"),
    st.Page("nba_daily_player_projections.py", title="Daily Player Projections", icon=":material/sports_basketball:"),
    #st.Page("nba_model_prop.py", title="Suggested Bets - Upcoming Games", icon=":material/sports_basketball:"),
    #st.Page("nba_prop_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_basketball:"),
], 
    "MLB - Player Prop Models": [
    st.Page("mlb_model_prop.py", title="Model Intro & Test Data", icon=":material/sports_baseball:"),
    #st.Page("mlb_bets.py", title="Suggested Bets - Upcoming Games", icon=":material/sports_baseball:"),
    #st.Page("mlb_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_baseball:"),
],
 # "European Soccer": [ 
 # st.Page("soccer_model.py", title="Model Intro", icon=":material/sports_soccer:"),   # & Test Data
  #  st.Page("soccer_bets.py", title="Suggested Bets - Upcoming Games", icon=":material/sports_soccer:"),
  #  st.Page("soccer_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_soccer:"),
  # ],           
    "Tennis": [
    st.Page("tennis_model.py", title="Model Intro", icon=":material/sports_tennis:"),  # & Test Data
    #st.Page("tennis_bets.py", title="Suggested Bets - Upcoming Matches", icon=":material/sports_tennis:"),
    #st.Page("tennis_bet_history.py", title="Suggested Bet Tracker", icon=":material/sports_tennis:"),
    ],

"More Information": [
    #st.Page("FAQ.py", title="FAQ", icon=":material/question_mark:"),
    st.Page("blog.py", title="Blog", icon=":material/edit_note:"),    
    #st.Page("learning.py", title="Learning Algorithmic Sports Betting", icon=":material/school:"),
    st.Page("contact.py", title="Contact", icon=":material/contact_page:"),    
    ],
})

# call run() to execute the current page
current_page.run()
st.markdown("""
<style>
    [alt=Logo] {
        height: 72px;
    }
</style>
""",unsafe_allow_html=True)


st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #000000;
    color: white;
    border: none;
    border-radius: 4px;
    margin: 0px;
    line-height: 1.6;
    width: auto;
    user-select: none;
    background-image: none;
}
div.stButton > button:hover {
    border: none;
    color: #000000;
    background-color: #000000;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}
</style>""",

unsafe_allow_html=True)
add_auth(required=True, login_button_text="Login with Google")
    
