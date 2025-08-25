import os
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

llm = ChatOllama(model="gemma3:4b")


prompt_template = PromptTemplate(input_variables =["country","no_of_paras","language"],
                                 template = """You are an expert in traditional cuisines. 
                                 You provide information about a specific dish from a specific country. 
                                 Avoid givin information about fictional places. If the country is fictional
                                 or non-existent anser: I dont know.
                                 Answer The Question: What is the traditional of cuisine of {country}?
                                 Answer in {no_of_paras} short paras in {language}                        
                                 """
                                 )

st.title('Ask anything about your traditional cuisine')

contry = st.text_input("Enter the country: ")

no_of_paras = st.number_input("Enter the number of paras",min_value=1, max_value=5)

language = st.text_input("Enter the language: ")

if contry:
    response = llm.invoke(prompt_template.format(country=contry,no_of_paras=no_of_paras,language =language))
    st.write(response.content)