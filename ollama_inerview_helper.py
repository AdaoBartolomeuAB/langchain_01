import os
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st


llm = ChatOllama(model="gemma3:1b")


prompt_template = PromptTemplate(input_variables =["company","position","strengths","weaknesses"],
                                 template = """
                                 You are career coach. Provide tailored interview tips for the position of {position} at {company}
                                 Highligth your strengths in {strengths} and prepare for questions about your weaknessessuch as {weaknesses}.                 
                                 """
                                 )

st.title('Ask anything about your traditional cuisine')

company = st.text_input("Company Name")
position = st.text_input("Position Title")
strengths = st.text_area("Your Strengths", height=100)
weaknesses = st.text_area("Your Weaknesses", height=100)

if company and position and strengths and weaknesses:
    response = llm.invoke(prompt_template.format(company=company,position=position,strengths=strengths,weaknesses=weaknesses))
    st.write(response.content)