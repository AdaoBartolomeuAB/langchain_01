import os
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st


llm = ChatOllama(model="gemma3:4b")

prompt_template = PromptTemplate(input_variables =["city","month","language","budget"],
                                 template = """You are an expert in traditional cuisines. 
                                 Welcome to {city} travel guide!
                                 If you're visiting in {month}, here's what you can do:
                                 1. Must-visit attractions.
                                 2. Local cuisine you must try.
                                 3. Useful pharases in {language}.
                                 4. Tips for traveling on a {budget} budget.
                                 Enjoy your trip!                  
                                 """
                                 )

st.title('Travel Guide')

city = st.text_input("Enter the city")
month = st.text_input("Enter the month")
language = st.text_input("Enter the language")
budget = st.selectbox("Travel Budget",["Low","Medion","High"])


if city and month and language and budget:
    response = llm.invoke(prompt_template.format(city=city,
                                                 month=month,
                                                 language =language,
                                                 budget =budget))
    st.write(response.content)