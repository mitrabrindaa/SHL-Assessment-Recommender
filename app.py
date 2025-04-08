import streamlit as st
import requests

st.title("SHL Recommender 🔍")
query = st.text_input("Search assessments", value="")
max_dur = st.slider("Max duration (mins)", 0, 120, 60)

if st.button("Search"):
    if not query:
        st.warning("Please enter a search term")
    else:
        try:
            response = requests.post(
                "http://localhost:8000/recommend",
                json={"text": query, "max_duration": max_dur}
            )
            st.table(response.json())
        except Exception as e:
            st.error(f"Start the backend first! Run: python main.py")