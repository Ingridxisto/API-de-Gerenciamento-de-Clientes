🩺 API de Gerenciamento de Clientes — Health Risk API
Esta é uma API REST desenvolvida em Python 3.11+, utilizando FastAPI, que permite cadastrar, editar, listar e calcular o risco de saúde de clientes com base em seus problemas de saúde. O projeto foi desenvolvido com foco em boas práticas de SOLID, TDD e DDD.

🚀 Funcionalidades
✅ Cadastro de cliente com nome, idade e problemas de saúde

🛠️ Edição de clientes existentes

📄 Listagem de todos os clientes

🧠 Cálculo de risco de saúde baseado em condições pré-definidas

🔍 Consulta de cliente por ID

🔬 Classificação dos "Top 10" clientes com maior risco

📦 Tecnologias Utilizadas
Python 3
FastAPI
Uvicorn
Pydantic
Pytest
HTTPie ou Insomnia/Postman para testes manuais

📁 Estrutura de Diretórios
´´´.
├── app/
│   ├── main.py
│   ├── models/
│   │   └── client.py
│   ├── schemas/
│   │   └── client_schema.py
│   ├── services/
│   │   └── client_service.py
│   ├── repositories/
│   │   └── client_repository.py
│   └── routes/
│       └── client_route.py
├── tests/
│   └── test_client.py
├── requirements.txt
└── README.md
´´´  

🛠️ Instalação   
# Clone o repositório
git clone https://github.com/seu-usuario/health-risk-api.git
cd health-risk-api

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

▶️ Executando a API
´´´uvicorn app.main:app --reload´´´  
Acesse a documentação interativa em:  
📄 http://127.0.0.1:8000/docs

📈 Cálculo de Risco
A pontuação de risco é calculada com base na gravidade de cada problema de saúde.
Quanto maior a soma das severidades, maior o risco do paciente.

🧪 Rodando os Testes
´´´ pytest tests/ ´´´
