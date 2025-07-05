import streamlit as st
import os
from dotenv import load_dotenv
from agent import Agent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


st.set_page_config(layout="wide")
st.title("Bem vindo a agência de Viagem Tabajara")
st.write("Essa aplicação irá planejar sua viagem e dar dicas valiosas")


agent = Agent(api_key)

col1, col2 = st.columns(2)

with col1:
    request = st.text_area("Para onde você gostaria de viajar")
    button = st.button("Buscar dicas de viagem")

    box = st.container(height=300)
    with box:
        container = st.empty()
        container.header("Sugestão de viagem")

if button:
    if request:
        response = agent.get_tips(request)
        container.write(response)
with col2:
    col2.write("Dicas de viagem")