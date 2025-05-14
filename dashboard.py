import streamlit as st

st.title("Hacker Instagram Bot Dashboard")
st.write("Monitor bot activity and manage settings here.")

with open("bot.log", "r") as log_file:
    logs = log_file.read()

st.text_area("Bot Logs", logs, height=400)