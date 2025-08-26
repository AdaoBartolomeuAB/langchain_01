import os

import json
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st


llm = ChatOllama(model="gemma3:4b")

title_promt = PromptTemplate(input_variables =["topic"],
                                 template = """You are an experienced speech writer. 
                                 
                                 You need to craft an impactful title fir a speech 
                                 on the following topic: {topic} 
                                 Answer exactly with one title.
                                 """)

speech_promt =  PromptTemplate(input_variables =["title", "emotion"],
                                 template = """You need to write a powerful speech of 350 words
                                 for the following topic: {title}
                                 Format the output with 2 keys: 'title', 'speech' and fill them
                                 with the respective values
                                 """)


first_chain = title_promt | llm | StrOutputParser() | (lambda title: (st.write(title),title)[1])
second_chain = speech_promt | llm
final_chain = first_chain | second_chain


st.title('Speech Generator')
topic = st.text_input("Enter the topic")


if topic:
    response = final_chain.invoke({"topic":topic})
    st.write(response.content.title())