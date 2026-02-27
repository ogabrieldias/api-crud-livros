from flask import Blueprint, jsonify, request
from database import db
from models import Projeto  # <-- troque pelo Projeto correto

# Troque "nome" pelo nome da entidade (clientes, leads, etc.)
projetos_bp = Blueprint("projetos", __name__)

# Listar todos
@projetos_bp.route("/", methods=["GET"])
def listar():
    registros = Projeto.query.all()
    return jsonify([r.to_dict() for r in registros])

# Obter por ID
@projetos_bp.route("/<int:id>", methods=["GET"])
def obter(id):
    registro = Projeto.query.get_or_404(id)
    return jsonify(registro.to_dict())

# Criar novo
@projetos_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()
    novo = Projeto(**data)  # cria objeto com os dados recebidos
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

# Atualizar por ID
@projetos_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    registro = Projeto.query.get_or_404(id)
    data = request.get_json()
    for campo, valor in data.items():
        setattr(registro, campo, valor)  # atualiza dinamicamente
    db.session.commit()
    return jsonify(registro.to_dict())

# Deletar por ID
@projetos_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    registro = Projeto.query.get_or_404(id)
    db.session.delete(registro)
    db.session.commit()
    return jsonify({"msg": "Registro deletado com sucesso!"})
