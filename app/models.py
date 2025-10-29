from datetime import datetime
from .database import db

class HabitoAlimentar(db.Model):
    __tablename__ = "habitos_alimentares"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    refeicoes_dia = db.Column(db.Integer, nullable=False)
    consume_frutas = db.Column(db.Boolean, nullable=False)
    consome_agua_litros = db.Column(db.Float, nullable=False)
    horario_jantar = db.Column(db.String(10), nullable=False)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)