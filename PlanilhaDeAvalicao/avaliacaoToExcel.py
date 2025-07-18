import pandas as pd

# Lista de requisitos
data = [
    ["Suporte Multicloud", "Capacidade nativa da plataforma operar em ambientes Azure e GCP simultaneamente", "Alta", "Alta", "Sim", "Sim", "Evita retrabalho futuro durante e após a migração"],
    ["Conectores Nativos", "Integrações prontas com serviços como BigQuery, ADLS, Data Factory, Pub/Sub etc.", "Alta", "Alta", "Sim", "Sim", "Avaliar cobertura e profundidade da integração por serviço"],
    ["Catálogo de Dados com Busca Semântica", "Motor de busca inteligente que entende termos de negócio e relaciona com objetos técnicos", "Alta", "Média", "Sim", "Sim", "Relevante para adoção por usuários de negócio"],
    ["Glossário de Negócios e Mapeamento Técnico", "Definições de termos de negócio ligadas a tabelas, colunas e ativos de dados", "Alta", "Alta", "Sim", "Sim", "Fundamental para padronização e entendimento comum de dados"],
    ["Classificação de Dados Sensíveis", "Identificação automática/manual de dados pessoais, confidenciais e sensíveis", "Alta", "Alta", "Sim", "Sim", "Avaliar suporte à LGPD, GDPR e taxonomias customizadas"],
    ["Rastreabilidade e Linhagem de Dados", "Capacidade de identificar a origem, transformação e destino de cada ativo de dado", "Alta", "Alta", "Sim", "Sim", "Preferência por visualização gráfica e detalhamento por coluna"],
    ["Integração com Segurança e IAM", "Suporte a sistemas de identidade como Azure AD, Google IAM e políticas de acesso granular", "Alta", "Alta", "Sim", "Sim", "Avaliar suporte a OAuth, SAML, RBAC, ABAC"],
    ["Recursos de Automação e API", "APIs abertas, SDKs e suporte a automação de onboarding, curadoria e atualizações", "Média", "Média", "Sim", "Sim", "Essencial para escalabilidade e integração com pipelines DevOps"],
    ["Facilidade de Implantação e Adoção", "Facilidade para instalação, configuração e treinamento dos usuários", "Alta", "Alta", "Sim", "Sim", "Avaliar complexidade de setup e tempo médio para primeiros resultados"],
    ["Governança de IA e ML", "Suporte para catalogar modelos, metadados de experimentos, features e rastreabilidade de ML", "Média", "Baixa", "Sim", "Sim", "Diferencial importante para maturidade futura"],
    ["Conformidade (LGPD / SOX / etc.)", "Capacidade da ferramenta de apoiar obrigações regulatórias e auditorias", "Alta", "Alta", "Sim", "Sim", "Avaliar templates prontos, relatórios automatizados e evidências de auditoria"],
    ["Auditoria de Acessos e Trilhas", "Registro de ações, acessos e alterações feitas por usuários", "Alta", "Alta", "Sim", "Sim", "Suporte essencial para ambientes regulados"],
    ["Controle e Segregação de Funções", "Mecanismos de separação clara de responsabilidades (admin, steward, data owner etc.)", "Alta", "Média", "Sim", "Sim", "Fundamental para controle de permissões e accountability"],
    ["Integração com Segurança Corporativa", "Compatibilidade com SIEMs, DLP, CASB, e outras ferramentas de segurança empresarial", "Média", "Média", "Sim", "Sim", "Avaliar via conectores nativos ou via integração por API"]
]

# Cabeçalhos da tabela
columns = [
    "Requisito",
    "Descrição",
    "Importância",
    "Prioridade no curto prazo",
    "Compatibilidade com Azure",
    "Compatibilidade com GCP",
    "Observações adicionais"
]

# Criação do DataFrame
df = pd.DataFrame(data, columns=columns)

# Salvar o Excel no mesmo diretório do script
df.to_excel("Requisitos_Governanca_Dados_Multicloud.xlsx", index=False)

print("Arquivo Excel gerado com sucesso!")
