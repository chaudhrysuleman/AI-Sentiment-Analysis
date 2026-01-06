import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

# Ensure API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in environment.")

llm_model = "gpt-3.5-turbo"
chat_llm = ChatOpenAI(temperature=0.7, model=llm_model)
