import streamlit as st


st.set_page_config(page_title= "growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("Welcome to Your Growth Mindset Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build  a growth mindset with reflection, challenges, and achievements! ❀")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

st.header("What's Your challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f" you re facing: {user_input}. Keep pushing forward! toward your goal!")
else:
    st.warning("Tell us about your challenge to get started!")   

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflectin on past experience help you grow! Share your difficulties")


#achievement

st.header("Celebrate your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")


if achievement:
    st.success(f"✨ Amazing! You achieved: {achievement}")
else: 
    st.info("Big or small , every achievement counts! Share one now 😊")

#footer
st.write("---")    
st.write(" Keep believing in yourself. Growth is a journey, not a destination!")
st.write("**⛔ Create by Zainub Nazish** ")
