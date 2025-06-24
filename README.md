
# Aplicativo: Agência de Viagens com LLM
Este projeto é uma aplicação interativa desenvolvida com Streamlit, que utiliza LangChain e OpenAI GPT-4 Turbo para atuar como um agente de viagens virtual. O objetivo é oferecer sugestões detalhadas e personalizadas sobre roteiros turísticos com base em uma solicitação feita em português.

# Objetivo do Projeto
Criar um assistente virtual de viagens que:

Receba um pedido em linguagem natural (ex: "Quero viajar para Paris por 3 dias");

Utilize um modelo LLM para gerar uma resposta simpática e estruturada;

Retorne dicas organizadas como um roteiro diário;

Possua uma interface simples e funcional via Streamlit.


agencia_viagem/
│

├── agent/

│   └── agent.py           # Classe Agent com LangChain + Prompt

│

├── app.py                 # Interface Streamlit

├── .env                   # Armazena OPENAI_API_KEY

├── .gitignore             # Ignora arquivos sensíveis e ambientes

├── requirements.txt       # Dependências do projeto

└── README.md              # Instruções e documentação




### conda info --envs

C:\Users\Dell\ProjetosPython\agente_turismo\env

conda activate C:\Users\Dell\ProjetosPython\agente_turismo\env



