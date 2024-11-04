import streamlit as st

st.header('Frequently Asked Questions',divider="gray")
st.write('')
st.subheader('What sports/markets do you cover?')
faq1 = '''
We currently have production models (meaning that we're actively betting them) for NFL player props, NBA spreads/totals, NBA player props, and MLB player props.
We are actively building and testing multiple others, including NHL player props, ATP tennis game spreads, and European soccer moneylines/spreads/totals. 

We have developed systems for a wide variety of other sports and markets, including MLB moneylines/run-lines/totals, NFL moneylines/spreads/totals, WTA tennis moneylines,
college basketball moneylines/spreads/totals, and Hong Kong horse racing.
However, these projects currently are either incomplete or have not met profitability thresholds to graduate to production models and active betting implementations. More data may be released on them even without an active betting implementation if there's a sufficent level of public interest.
'''
st.write(faq1)
st.write('')
# st.subheader('How often is site data updated?')
# faq6 = '''
# NBA data will be available daily with very limited exceptions, although we do not bet on the first 10 games of each team's season while the model collects data. NFL data will be available weekly upon 

# '''

# st.write(faq6)
# st.write('')
st.subheader('Who might this site be good for?')
faq2 = '''
Data-driven sports bettors - those that think about wagering in terms of probabilities and prices, instead of based on gut feelings or recent streaks.
Sports fans who enjoy analytics and the numbers behind the games. People that would like to learn more about building, testing, and then applying machine learning models.
'''
st.write(faq2)
st.write('')
st.subheader('What makes you different than other people selling picks?')
faq3 = '''
We don’t do gimmicks like lottery parlays and ladder challenges.
 We won’t tout hot streaks over an arbitrarily determined last number of picks.
   We provide performance histories that you can go back and verify yourself, unlike most “trust me bro” touts.
     And when we say we use AI, we aren’t just using a buzzword for marketing - we have actual models and discuss many aspects of their creation and implementation here.
'''
st.write(faq3)
st.write('')
st.subheader('Why bother making a website when most cappers just use Twitter and Discord?')
faq4 = '''
After spending a few years on those sites, it became very clear that the vast majority of sports betting accounts on these sites have no actual edge - they either coast off some positive run of variance, focus solely on entertainment value, or outlight lie to their followers. We aren’t looking to play any of those games and would rather not be lumped into the same general category as the ":fire::fire::fire:" engagement farmers. While we will still maintain our accounts there, we wanted to build a place where our process and IP can stand on its own.

On top of these issues, the formats of both Twitter and Discord do not lend themselves to serious analysis and in-depth discussion of building and implementing AI sports betting models. Simply posting a bullet point list of plays isn’t sufficient for us. Having the ability to post entire datasets as well as in-depth reviews is a huge upgrade over the quick chat nature of most alternatives.

'''
st.write(faq4)
st.write('')
st.subheader('Where did the name "Orca Syndicate" come from?')
faq5 = '''
I used to be a fairly high-level poker player, a game whose success requires a lot of the same elements as sports betting. In poker, good players are referred to as “sharks”. And in the wild, sharks have only one known predator - the killer whale. 
We approach sports betting in the same manner - we know that the sportsbooks set good lines and beat the vast majority of bettors, but that our data, models, and betting processes will still allow us to profit against them in the long run. 
'''
st.write(faq5)