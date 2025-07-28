from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# calling environment variables

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# initializing model
llm=init_chat_model("groq:llama-3.1-8b-instant")


# Langsmith Tracinhg
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

# creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries."),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("Langchain Demo with Groq")
input_text=st.text_input("Search the topic you want")

# Groq llm call
output_parser=StrOutputParser()

# chain 
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))


