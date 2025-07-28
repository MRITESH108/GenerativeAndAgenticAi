from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
llm=init_chat_model("groq:llama-3.1-8b-instant")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    init_chat_model(),
    path="/groq"
)

prompt=ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words")

add_routes(
    app,
    prompt|llm,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
    