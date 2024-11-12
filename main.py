import streamlit as st

st.title("Hi, this is a test project")
name = st.text_input("So, who are you?")

if st.button("Go to next page"):
    st.session_state["name"] = name
    st.switch_page("pages/other.py")