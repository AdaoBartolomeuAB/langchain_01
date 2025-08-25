import os

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

llm = ChatOllama(model="qwen2.5-coder:7b")


prompt_template = PromptTemplate(input_variables =["country"],
                                 template = """You are an expert in traditional cuisines. 
                                 You provide information about a specific dish from a specific country. 
                                 Answer The Question: What is the traditional of cuisine of {country}"""
                                 )

question = input("Enter the question: ")
respone = llm.invoke(question)
print(respone.content)