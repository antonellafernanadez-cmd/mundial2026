from models.db import db

class Usuario(db.models):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    
def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password