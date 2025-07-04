from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env

app = Flask(__name__)

# Configuração do SQLite em memória
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://flask_user:{os.getenv('DB_PASSWORD')}@192.168.1.3/crud_flask"
# Altere a configuração do banco de dados para:
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://flask_user:{os.getenv('DB_PASSWORD')}@192.168.1.44:3306/crud_flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Modelo de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    quantidade = db.Column(db.Integer, default=1)

    def to_dict(self): #está ligado ao flask e cria recebe os dados e retorna em JSON para a API
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'quantidade': self.quantidade
        }


# Cria as tabelas no banco de dados em memória
with app.app_context():
    db.create_all()


# Rotas da API

# POST - Criar um novo item
@app.route('/itens', methods=['POST'])
def criar_item():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'erro': 'Dados inválidos ou nome não fornecido'}), 400

    # Verifica se o item já existe (com mesmo nome E descrição)
    item_existente = Item.query.filter_by(
        nome=dados['nome'],
        descricao=dados.get('descricao', '')
    ).first()

    if item_existente:
        # Item existe: incrementa a quantidade
        nova_quantidade = item_existente.quantidade + dados.get('quantidade', 1)
        item_existente.quantidade = nova_quantidade
        db.session.commit()
        return jsonify(item_existente.to_dict()), 200
    else:
        # Item não existe: cria novo
        novo_item = Item(
            nome=dados['nome'],
            descricao=dados.get('descricao', ''),
            quantidade=dados.get('quantidade', 1)
        )
        db.session.add(novo_item)
        db.session.commit()
        return jsonify(novo_item.to_dict()), 201


@app.route('/itens/decrementar', methods=['POST'])
def decrementar_item():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'erro': 'Dados inválidos ou nome não fornecido'}), 400

    item = Item.query.filter_by(
        nome=dados['nome'],
        descricao=dados.get('descricao', '')
    ).first()

    if not item:
        return jsonify({'erro': 'Item não encontrado'}), 404

    # Verifica se a quantidade não fica negativa
    nova_quantidade = item.quantidade - dados.get('quantidade', 1)
    if nova_quantidade < 0:
        return jsonify({'erro': 'Quantidade não pode ser negativa'}), 400

    item.quantidade = nova_quantidade
    db.session.commit()
    return jsonify(item.to_dict()), 200

# GET - Listar todos os itens
@app.route('/itens', methods=['GET'])
def listar_itens():
    itens = Item.query.all()
    return jsonify([item.to_dict() for item in itens]), 200


# GET - Obter um item específico
@app.route('/itens/<int:item_id>', methods=['GET'])
def obter_item(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return jsonify({'erro': 'Item não encontrado'}), 404

    return jsonify(item.to_dict()), 200


# PUT - Atualizar um item
@app.route('/itens/<int:item_id>', methods=['PUT'])
def atualizar_item(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return jsonify({'erro': 'Item não encontrado'}), 404

    dados = request.get_json()

    if 'nome' in dados:
        item.nome = dados['nome']
    if 'descricao' in dados:
        item.descricao = dados['descricao']
    if 'quantidade' in dados:
        item.quantidade = dados['quantidade']

    db.session.commit()

    return jsonify(item.to_dict()), 200


# DELETE - Remover um item
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def remover_item(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return jsonify({'erro': 'Item não encontrado'}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({'mensagem': 'Item removido com sucesso'}), 200


if __name__ == '__main__':
    app.run(debug=True)