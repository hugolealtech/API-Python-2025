Este guia explica como clonar, configurar e testar a aplicação CRUD Flask com SQLite em memória. Ideal para quem quer contribuir ou testar localmente.

🔧 Pré-requisitos Python 3.8+ instalado (Download aqui).

Git (Download aqui).

Postman ou Insomnia para testar a API (Postman, Insomnia).

🚀 1. Clonar o Repositório Abra o terminal e execute:

bash git clone (https://github.com/hugolealtech/API-Python-2025.git)

cd CRUD-Python-2025;

🐍 2. Configurar o Ambiente Virtual (venv) Criar e Ativar o venv No macOS/Linux: bash python3 -m venv venv # Cria o ambiente virtual source venv/bin/activate # Ativa o venv → Você verá (venv) no início da linha do terminal.

No Windows (PowerShell): bash python -m venv venv # Cria o ambiente virtual .\venv\Scripts\activate # Ativa o venv 📦 3. Instalar as Dependências Com o venv ativado, instale as bibliotecas necessárias:

bash pip install -r requirements.txt (O arquivo requirements.txt deve conter flask e flask-sqlalchemy.)

🚀 4. Executar a Aplicação bash python app.py Saída esperada:

bash


* para iniciar o ambiente source venv/bin/activate
* para para o ambiente deactivate

* Ao inserir o ip do banco de dados, não esqueça de colocar:numero da porta

Serving Flask app 'app'
Debug mode: on
Running on http://127.0.0.1:5000 👉 A API estará acessível em: http://127.0.0.1:5000/itens
🛑 5. Parar a Aplicação No terminal onde o Flask está rodando, pressione:

bash CTRL + C 🔍 6. Testar a API (Endpoints CRUD) Use Postman ou Insomnia para testar:

🔹 POST - Criar um Item URL: http://127.0.0.1:5000/itens

Método: POST

Headers:

text Content-Type: application/json Body (JSON):

json { "nome": "Notebook", "descricao": "MacBook Pro M3" } ✅ Resposta: 201 Created + dados do item criado.

🔹 GET - Listar Todos os Itens URL: http://127.0.0.1:5000/itens

Método: GET ✅ Resposta: 200 OK + lista de itens.

🔹 GET - Buscar um Item por ID URL: http://127.0.0.1:5000/itens/1 (substitua 1 pelo ID desejado)

Método: GET ✅ Resposta: 200 OK + dados do item.

🔹 PUT - Atualizar um Item URL: http://127.0.0.1:5000/itens/1 (ID do item a atualizar)

Método: PUT

Headers:

text Content-Type: application/json Body (JSON):

json { "nome": "Notebook Atualizado", "descricao": "MacBook Pro M3 2024" } ✅ Resposta: 200 OK + dados atualizados.

🔹 DELETE - Remover um Item URL: http://127.0.0.1:5000/itens/1 (ID do item a deletar)

Método: DELETE ✅ Resposta: 200 OK + mensagem de confirmação.

💡 Dicas Extras Se der erro 404: Verifique se a rota está correta (ex: /itens com "s").

Se der erro 415: Adicione o header Content-Type: application/json.

Para persistir dados: Substitua sqlite:///:memory: por sqlite:///dados.db no código.

📌 Resumo dos Comandos Úteis Ação Comando/Método Ativar venv source venv/bin/activate

-- LISTA DE ITENS PARA AJUDAR A TESTAR A APLICAÇÃO --

{ "nome": "Smart TV", "descricao": "LG OLED 55'' 4K", "quantidade": 3 }

,

{ "nome": "Impressora", "descricao": "Epson EcoTank L3250", "quantidade": 5 }

,

{ "nome": "Roteador Wi-Fi", "descricao": "TP-Link Archer AX6000", "quantidade": 9 }

{ "nome": "Mouse Gamer", "descricao": "Logitech G Pro X Superlight", "quantidade": 12 }

{ "nome": "Teclado Mecânico", "descricao": "Keychron K2", "quantidade": 7 }

{ "nome": "Monitor", "descricao": "Dell Ultrasharp U2723QE 27''", "quantidade": 4 }

{ "nome": "HD Externo", "descricao": "Seagate Expansion 2TB", "quantidade": 6 }

{ "nome": "SSD NVMe", "descricao": "Samsung 980 Pro 1TB", "quantidade": 8 }

{ "nome": "Drone", "descricao": "DJI Mavic 3", "quantidade": 3 }

{ "nome": "Fone de Ouvido", "descricao": "Sony WH-1000XM5", "quantidade": 5 }
