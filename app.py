import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="parth''s website", page_icon=":tada:", layout="wide")
st.subheader("hi i am parth")
st.write("---")
st.header("what do i do")
st.write("i'am an python devloper and i  will make a python tutorial to make this website and deploy it to streamlit.com/cloud ")

lottie_codeing = "https://lottie.host/e0f22623-d29c-4c40-93be-8854fe89b613/JIW1POmVxB.json"

def load_lottieurl():
    r = Requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
st_lottie(lottie_codeing, height = 300, key="coding")