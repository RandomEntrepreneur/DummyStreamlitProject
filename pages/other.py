import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"

try:
    st.text(f"Hello, {st.session_state['name']}")
    message = requests.get(f"{BACKEND}/get_message").json()["response"]
    st.success("I could access the backend just fine :)")
except:
    st.image(
        "https://i.imgflip.com/84siwz.jpg?a480648",
        use_column_width=True
    )