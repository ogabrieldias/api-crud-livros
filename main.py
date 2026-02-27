from flask import Flask
from flask_cors import CORS
from database import db
from routes.leads import leads_bp
from routes.clientes import clientes_bp
from routes.projetos import projetos_bp
from routes.pagamentos import pagamentos_bp
from routes.planos import planos_bp
from routes.interacoes import interacoes_bp

app = Flask(__name__)
CORS(app)

# Configuração do banco MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345678@localhost/techdias"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Registrar rotas
app.register_blueprint(leads_bp, url_prefix="/leads")
app.register_blueprint(clientes_bp, url_prefix="/clientes")
app.register_blueprint(projetos_bp, url_prefix="/projetos")
app.register_blueprint(pagamentos_bp, url_prefix="/pagamentos")
app.register_blueprint(planos_bp, url_prefix="/planos")
app.register_blueprint(interacoes_bp, url_prefix="/interacoes")

if __name__ == "__main__":
    app.run(port=8000, host="localhost", debug=True)
