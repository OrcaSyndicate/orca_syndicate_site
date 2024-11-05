import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('Model Description',divider="gray")
tennis_intro = '''
Our tennis model is one of our most advanced projects to date. The model is trained to predict each player’s service point win percentage over the course of a match. It considers both overall and surface-specific statistics for each player, and his opponent, over the trailing 12 months. 
Service point win percentage is normally distributed, which makes the model’s job a bit easier. In the end, an ensemble model comprised of a random forest and an Xtreme Gradient Boosted model produced the best performance results. In all, approximately 60 different features are analyzed. 
Our custom ELO ratings with a dynamic K factor are among the most important contributors in arriving at a final projection for each player. Perhaps the biggest challenge of tennis modeling is the relatively complicated scoring system, in which the player that wins more points and games can still lose the match. 
To combat this, several helper functions are used to convert point probabilities to game probabilities, then to set probabilities, then to match probabilities, while also making the proper adjustments for tiebreakers and the longer match format in majors.


'''
st.write(tennis_intro)
# tennis_image1 = ('C:/Users/ajaku/Downloads/tennis_intro1.png')
# tennis_image2 = ('C:/Users/ajaku/Downloads/tennis_intro2.png')
# tennis_image3 =('C:/Users/ajaku/Downloads/tennis_intro3.png')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/tennis_intro_charts.JPG?raw=true')
st.write('')
tennis_intro2 = '''
While the player service point win probabilities are robust, we have had some issues in past versions with converting those into final match outcome projections given the scoring peculiarities here. For example - if a player’s service point win percentage is projected at 68% by the algorithm, should we use that for all simulations given the high level of path dependency? Or should it be allowed to vary around the mean? And if so, in what distribution? And should the parameters be surface and/or player specific? Furthermore, past versions were also only able to generate the final win probabilities for a given match, meaning we were limited to testing in the moneyline markets.

This year, with a few model improvements, we are finally able to generate the projected final scores for each match, allowing us to expand into the game spreads market. Alongside this new match simulation engine, we are also testing a few new distribution methodologies. Testing will likely take longer than in other sports given the slower datapoint collection cadence and general lack of historical tennis spread data, but we look forward to sharing updates as they become available.

'''
st.write('')
st.write(tennis_intro2)

#st.write(tennis_intro2)
#st.header('ATP Model Testing',divider="gray")
#st.header('Moneyline')
#st.subheader('Model Test Performance Summary')
#st.write('')    
#st.subheader('All Test Datapoints')
#st.write('')
#st.divider()
#st.header('Games Spread')
#st.subheader('Model Test Performance Summary')
#st.write('')
#st.subheader('All Test Datapoints')
