import streamlit as st
import pandas as pd
import csv


st.header('Interested In Learning Quantitative Sports Betting For Yourself?',divider="gray")
st.write('')
intro = '''
We are currently building a course on Udemy that will provide a comprehensive introduction to algorithmic sports betting.
It will be comprised of two sections - learning how to build a model that can consistently make accurate predictions, and then learning how and when to apply them to make bets. 
A tentative outline of course material is provided below:
'''
st.write(intro)
st.markdown("### Section 1: Building a Sports Betting Model")
st.markdown("- Data Collection")
st.markdown("- Data Cleaning and Dataset Creation")
st.markdown("- Where to Build?")
st.markdown("- Dataset Partioning and Why It's Important")
st.markdown("- Exploratory Analysis & Classification/Regression Decision")
st.markdown("- Which Type of Model?")
st.markdown("- Feature Selection")
st.markdown("- Hyperparameter Tuning")
st.markdown("- Model Fitting & Testing")
st.markdown("- Model Calibration")

st.markdown("### Section 2: Using Your Model to Make Bets")
st.markdown("- Intro to +EV Wagering")
st.markdown("- Intro to the Kelly Criterion")
st.markdown("- Exploring the Potential Parameters of Your Betting System")
st.markdown("- Validation to Determine Betting Thresholds")
st.markdown("- Common Errors to Avoid When Setting Betting Thresholds")
st.markdown("- Final Out-of-Sample Model Testing")
st.markdown("- Performance Analysis of Your Out-of-Sample Testing")
st.markdown("- Implementing Model for Live Release")
st.markdown("- Live Performance Tracking & Parsing Signal vs. Noise in Your Results")

# st.markdown("### _First Lesson Coming Soon!_ :nerd_face:")

# st.write('Scientific Sports Betting')
# st.title("Get Notified of New Articles!")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
# Create a form
with st.form("email_form",clear_on_submit=True):
    st.write("Enter your email address if you'd like to be notified when the course is published.")
    
    # Email input
    email = st.text_input("Email Address")

    # Submit button
    submitted = st.form_submit_button("Submit")

    # Check if the form is submitted
    if submitted:
        if "@" in email:
            # Logic to save the email address (to a file, database, etc.)
            st.success(f"Thank you! {email} has been added to the notification list.")
        else:
            st.error("Please enter a valid email address.")

if submitted and "@" in email:
    with open('C:/Users/ajaku/Downloads/orca_syndicate_distribution_list.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email])
    