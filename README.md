🚀 1. Clonar o repositório
Abra o terminal e execute:

bash
Copiar
Editar
git clone https://github.com/hugolealtech/API-Python-2025.git
cd API-Python-2025
🐍 2. Configurar o Ambiente Virtual (venv)
macOS / Linux:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
Windows (PowerShell):

bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate
Ative o ambiente para ver (venv) no início da linha.

📦 3. Instalar Dependências
Com o venv ativado:

bash
Copiar
Editar
pip install -r requirements.txt
Esse arquivo deve incluir Flask, flask_sqlalchemy, python-dotenv, etc.

🧪 4. Executar a Aplicação
bash
Copiar
Editar
python app.py
Saída esperada:

csharp
Copiar
Editar
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
📌 API disponível em: http://127.0.0.1:5000/itens

🛑 5. Parar a Aplicação
No terminal onde o Flask está rodando, pressione:

objectivec
Copiar
Editar
CTRL + C
🔍 6. Testar os Endpoints CRUD com Postman ou Insomnia
➕ POST – Criar item
URL: POST http://127.0.0.1:5000/itens

Headers: Content-Type: application/json

Body JSON:

json
Copiar
Editar
{
  "nome": "Notebook",
  "descricao": "MacBook Pro M3"
}
Resposta esperada: 201 Created + dados do item.

📄 GET – Listar todos
URL: GET http://127.0.0.1:5000/itens

Resposta: 200 OK + lista de itens.

📄 GET – Buscar item por ID
URL: GET http://127.0.0.1:5000/itens/1

Resposta: 200 OK + dados do item.

✏️ PUT – Atualizar item
URL: PUT http://127.0.0.1:5000/itens/1

Headers: Content-Type: application/json

Body JSON:

json
Copiar
Editar
{
  "nome": "Notebook Atualizado",
  "descricao": "MacBook Pro M3 2024"
}
Resposta: 200 OK + dados atualizados.

🗑️ DELETE – Excluir item
URL: DELETE http://127.0.0.1:5000/itens/1

Resposta: 200 OK + mensagem confirmando exclusão.

💡 7. Dicas Extras
─ Persistência de dados
Alterar sqlite:///:memory: para sqlite:///dados.db no app.py para salvar no arquivo.

─ Erro 404
Verifique se a rota está bem escrita: /itens com “s”.

─ Erro 415
Adicione Content-Type: application/json no header da requisição JSON.

🧪 8. Testes Automatizados
Para criar testes com pytest + SQLite em memória:

Instale (pytest, pytest-mock) e adicione sqlite:///:memory: na config de testes.

Exemplo de fixture:

python
Copiar
Editar
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
        yield c
        with app.app_context():
            db.drop_all()
Exemplo de teste:

python
Copiar
Editar
def test_create_item(client):
    resp = client.post('/itens', json={'nome':'TV','descricao':'LG OLED'})
    assert resp.status_code == 201
Usar SQLite em memória acelera e isola os testes 
gehrcke.de
+9
codingeasypeasy.com
+9
codezup.com
+9
dzone.com
askpython.com
.

✅ 9. Resumo dos Comandos
bash
Copiar
Editar
git clone https://github.com/hugolealtech/API-Python-2025.git
cd API-Python-2025

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python app.py
# ou "flask run" se estiver configurado via FLASK_APP

# Para testes com pytest:
pytest
🗃️ 10. Exemplo de Dados para Testar
json
Copiar
Editar
[
  {"nome": "Smart TV", "descricao": "LG OLED 55'' 4K", "quantidade": 3},
  {"nome": "Impressora", "descricao": "Epson EcoTank L3250", "quantidade": 5},
  {"nome": "Roteador Wi-Fi", "descricao": "TP-Link Archer AX6000", "quantidade": 9},
  {"nome": "Mouse Gamer", "descricao": "Logitech G Pro X Superlight", "quantidade": 12},
  {"nome": "Teclado Mecânico", "descricao": "Keychron K2", "quantidade": 7},
  {"nome": "Monitor", "descricao": "Dell Ultrasharp U2723QE 27''", "quantidade": 4},
  {"nome": "HD Externo", "descricao": "Seagate Expansion 2TB", "quantidade": 6},
  {"nome": "SSD NVMe", "descricao": "Samsung 980 Pro 1TB", "quantidade": 8},
  {"nome": "Drone", "descricao": "DJI Mavic 3", "quantidade": 3},
  {"nome": "Fone de Ouvido", "descricao": "Sony WH-1000XM5", "quantidade": 5}
]
📌 11. Thread Pool no SQLite em memória
⚠️ Cuidado: bancos em memória com threads podem criar inconsistências em diferentes threads. Melhor usar persistência em arquivo ou inicializar dentro dos handlers .

✅ Conclusão
Você agora tem um guia completo e organizado para:

✅ Clonar o repositório

✅ Configurar ambiente virtual

✅ Instalar dependências

✅ Rodar a aplicação

✅ Testar seu CRUD

✅ Persistir dados se necessário

✅ Automatizar testes com pytest
