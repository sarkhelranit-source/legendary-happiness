import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage",
                   page_icon=":innocent:",
                   layout="wide")


def animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


cyber = animation(
    "https://assets8.lottiefiles.com/packages/lf20_96cnyxkh.json")

coding = animation(
    "https://assets3.lottiefiles.com/packages/lf20_jjsrh4we.json")

ai = animation(
    "https://assets7.lottiefiles.com/private_files/lf30_cmd8kh2q.json")

with st.container():
    st.subheader("Hi, I am Ranit :wave:")
    st.title("A Computer Science Student :computer:")
    st.write(
        "I am passionate about Cyber Security and like to play video games, CTF's(Capture the flag), Chess and obviously like to code"
    )

with st.container():
    st.write("----")
    left_columns, right_colums = st.columns(2)
    with left_columns:
        st.header("My Cyber Security Experience :lock:")
        st.write("##")
        st.write("""
                 - In a daily basis I used to spent my time in front of my PC... playing CTF's, solving Labs from [HackTheBox](https://app.hackthebox.com/home) and [TryHackMe](https://tryhackme.com/hacktivities?tab=practice).
                
                 - I recently Completed two Cyber Security courses from Udemy. One is for [Ethical Hacking](https://udemy-certificate.s3.amazonaws.com/image/UC-d6b90e54-3292-473c-a26c-a7b4cc25fc39.jpg?v=1670683112000) and the other one is for [Bug Hunting](https://udemy-certificate.s3.amazonaws.com/image/UC-5d10e68f-61be-4174-87ad-5c55ed954e5e.jpg?v=1670435278000)
                 
                 - I really like Red Teaming and the Offensive side of the cyber security like the Penetration testing and Bug Hunting. I also interested in exploit development and testing malwares.
                 
                 - OSINT and Social Engineering are my other two favourite topics of cyber security. gathering confidential information from the internet is a kind of topic that I can't avoid.
                 """)
    with right_colums:
        st_lottie(cyber, height=400, quality="high", key="cyber_security")

with st.container():
    st.write("----")
    left_columns, right_columns = st.columns(2)
    with right_columns:
        st.header("My Programming Journey :school:")
        st.write("##")
        st.write("""
                 - Entering into my college the only thing I was doing in a daily basis was Programming. It may sound stupid but it really felt good to run my first ever 'Hello World!' Program :sweat_smile:. The first language I learned was C++. Then I start learning Python cause It feels like C++ dosen't suits me, i don't know why :confused:.
                 
                 - After learning Python I made two console based game -> (1) Snake, Water, Gun & (2) Guess The Number and slowly building my experience on this language. Then I start working on my very own discord bot. The overall experience was really good while making the bot, I learn few things such as how to fetch data from an API endpoint and JSON objects. The Bot is now present in my Discord Server, If you want to join my Discord server click here :point_right: [RasCord](https://discord.gg/Z94r73Mx)
                 """)
    with left_columns:
        st_lottie(coding, quality="high", key="programming", height=400)

with st.container():
    st.write("----")
    left_columns, right_columns = st.columns(2)
    with left_columns:
        st.header("Other Interests :dizzy:")
        st.write("##")
        st.write("""
                 - Other than Cyber Security and Coding, Artificial Intelligence is the thing that I really like and have a lot of interests. Although I am not studying it on a regular basis but the overall concept of machine learning & artificial intelligence is quite exiting for me.
                 
                 - I spent one month learning about [Tensorflow](https://www.tensorflow.org/?gclid=CjwKCAiArY2fBhB9EiwAWqHK6hZKF0cDt21WGMB2OyCC7Yn7Yl9oCX_jWN7Ntdm5nRU78U5dvfjFZRoCzS8QAvD_BwE), building machine learning models using tensorflow and all of the basic stuffs. You can check out my Github Repository for Machine Learning here :point_right: [sarkhelranit-source](https://github.com/sarkhelranit-source/Machine-Learning)
                 """)
    with right_columns:
        st_lottie(ai, height=400, quality="high", key="artificial_intelligence")