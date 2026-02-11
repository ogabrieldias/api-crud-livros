from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco (SQLite local)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/livros'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




# Modelo Livro
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor}

# Criar tabelas
with app.app_context():
    db.create_all()

# ------------------- ENDPOINTS -------------------

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = Livro.query.all()
    return jsonify([livro.to_dict() for livro in livros])

# Consultar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = Livro.query.get_or_404(id)
    return jsonify(livro.to_dict())

# Criar novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    data = request.get_json()
    novo_livro = Livro(titulo=data['titulo'], autor=data['autor'])
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify(novo_livro.to_dict()), 201

# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro = Livro.query.get_or_404(id)
    data = request.get_json()
    livro.titulo = data.get('titulo', livro.titulo)
    livro.autor = data.get('autor', livro.autor)
    db.session.commit()
    return jsonify(livro.to_dict())

# Excluir livro por ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return jsonify({"msg": "Livro deletado com sucesso!"})

# Rodar servidor
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
