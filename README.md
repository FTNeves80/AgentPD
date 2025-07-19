
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



## Instruções para execução local
Clone o repositório:

git clone <INSIRA AQUI O LINK DO SEU REPOSITÓRIO>
cd agencia_viagem
Crie um ambiente Conda ou virtualenv (exemplo com Conda):

conda create -n agente_viagem python=3.11
conda activate agente_viagem
Instale as dependências:

pip install -r requirements.txt
Crie o arquivo .env com sua chave da OpenAI:

OPENAI_API_KEY=sk-xxxxxxx

Execute o aplicativo:
streamlit run app.py


Acesse o navegador:
O Streamlit abrirá automaticamente, ou você pode acessar manualmente:
http://localhost:8501



