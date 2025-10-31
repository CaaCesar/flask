from estudo import db
from datetime import datetime
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    assunto = db.Column(db.String(150), nullable=True)
    mensagem = db.Column(db.String(500), nullable=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    respondido = db.Column(db.Integer, default=0)


    