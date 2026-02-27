from flask import Blueprint, jsonify, request
from database import db
from models import Lead  # <-- troque pelo Lead correto

# Troque "nome" pelo nome da entidade (clientes, leads, etc.)
leads_bp = Blueprint("leads", __name__)

# Listar todos
@leads_bp.route("/", methods=["GET"])
def listar():
    registros = Lead.query.all()
    return jsonify([r.to_dict() for r in registros])

# Obter por ID
@leads_bp.route("/<int:id>", methods=["GET"])
def obter(id):
    registro = Lead.query.get_or_404(id)
    return jsonify(registro.to_dict())

# Criar novo
@leads_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()
    novo = Lead(**data)  # cria objeto com os dados recebidos
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

# Atualizar por ID
@leads_bp.route("/<int:id>", methods=["PUT"])
def atualizar(id):
    registro = Lead.query.get_or_404(id)
    data = request.get_json()
    for campo, valor in data.items():
        setattr(registro, campo, valor)  # atualiza dinamicamente
    db.session.commit()
    return jsonify(registro.to_dict())

# Deletar por ID
@leads_bp.route("/<int:id>", methods=["DELETE"])
def deletar(id):
    registro = Lead.query.get_or_404(id)
    db.session.delete(registro)
    db.session.commit()
    return jsonify({"msg": "Registro deletado com sucesso!"})
