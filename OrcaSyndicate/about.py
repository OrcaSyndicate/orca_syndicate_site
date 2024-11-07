import streamlit as st
from st_paywall import add_auth
from pathlib import Path


st.set_page_config(layout="wide")
st.title('Welcome to the Orca Syndicate!')
st.divider()
intro = '''
The Orca Syndicate was created to combine advanced data analysis with scientific wagering principles to create successful sports betting systems.
Since the legalization of sports betting in the United States in 2018, we have devoted a significant amount of time and effort into building advanced AI models that are capable of generating sustainable edges for betting purposes.
'''

intro2 = '''
It is estimated that only 3-5% of sports bettors end up profitable in the long term, as they have to overcome both the very sharp lines of sportsbooks and their overround.
Aside from a few lottery-winner equivalents, those that manage to do so must be able to consistently make accurate probability estimates of event outcomes. But how do you come up with an accurate probability estimate?
It is [virtually impossible](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1132168/full#h7) for a human to consistently and accurately differentiate whether some novel event has a 60% or 65% chance of occurring, but that 5% delta can be the difference between winning and losing money in the long-term.
Thus, much like the only way to scratch a diamond is with another diamond, we believe that in most betting markets today the only way to beat the sportsbooks’ algorithms is by applying an algorithm of your own. To that end, we build and rigorously test models across a wide range of markets to give us the best chance of beating the odds.

'''
intro3 = '''
Quantitative betting groups tend to guard their source code closely, and we are no different in that regard. However, by sharing some of our data and model outputs, we can produce interesting and useful content while still preserving our IP.
Doing so also helps differentiate us from the myriad of sports betting “gurus” who offer no unique insight and zero sustainable edge. We want people to be able to see the basis on which the wagering suggestions are generated, rather than blindly trusting the recommendations.
We hope the data provided here will help those who want to be among the few who make money from their passion, or who want a source of funding for their other “lottery-ticket” plays. 
Even those who don’t have the time and/or inclination to bet but enjoy data and sports analytics will find something to interest them here. 
'''

#often essentially amount to a [confidence game](https://www.merriam-webster.com/dictionary/confidence%20game)
st.write(intro)
st.write('')
image2 = st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/home_page2.PNG?raw=true')
#summaries[0].image(image1)
#summaries[1].image(image2)
#st.write('')
st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/home_page4.PNG?raw=true')
#st.write('')

st.write(intro2)
st.write('')

st.image('https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/home_page3.PNG?raw=true')

st.write(intro3)
# st.markdown("#### The Orca Syndicate was created to combine advanced data analysis with scientific wagering principles to create successful sports betting systems. Since the legalization of sports betting in the United States in 2018, we have devoted a significant amount of time and effort into building advanced AI models that are capable of generating sustainable edges for betting purposes.")
st.write('')
st.markdown("""
<style>
    [alt=Logo] {
        height: 4.5rem;
    }
</style>
""",unsafe_allow_html=True)

st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}
</style>""",

unsafe_allow_html=True)

#add_auth(required=True, login_button_text="Login with Google")

#st.image("https://github.com/OrcaSyndicate/orca_syndicate_site/blob/main/OrcaSyndicate/site_images/logo1.JPG?raw=true")
