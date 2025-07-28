import streamlit as st
import requests

def get_groq_response(input_text):
        response=requests.post("http://localhost:8000/essay/invoke",
                               json={'input':{'topic':input_text}})
        return response.json()['output']['content']


# streamlit framework

st.title('Langchain Demo with Groq')
input_text=st.text_input("Search what you want your essay")

if input_text:
    st.write(get_groq_response(input_text))

