import os

from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st

from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

llm = ChatOllama(model="gemma3:4b")

host = 'localhost'
port = '5432'
username = 'root'
password = 'root'
database_schema = 'db_tes'

postgres_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_schema}"
db = SQLDatabase.from_uri(postgres_uri)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True,handle_parsing_errors=True)
response = agent.invoke("""You are an assistant that analyzes names from a database.

Important rules:
- Do NOT use SQL filters with LIKE, WHERE, or regex to find Arabic names.
- Always first run: SELECT nome FROM colaboradora;
- After retrieving all names, analyze them yourself and classify which are of Arabic origin.
- Use only your cultural and linguistic knowledge to decide. 
- Return only the names with Arabic origin as a JSON array.""")

print(response['output'])