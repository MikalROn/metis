from db import db

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.String(11), primary_key=True, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    clinica = db.Column(db.String(100), nullable=False)
    cidade_clinica = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.String(11), primary_key=True, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Integer, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

