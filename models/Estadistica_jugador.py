from models.db import db

class Estadistica(db.models):
    __tablename__="Estadistica"
    id=db.Column(db.Integer, primary_key=True)
    goles=db.Column(db.Integer)
    asistencias=db.Colum(db.Integer)
    efectividad_pases=db.Column(db.Float)
    tarj_rojas=db.Column(db.Integer)
    tarj_amarillas=db.Column(db.Integer)

def __init__(self, goles, asistencias,efectividad_pases,tarj_rojas,tarj_amarillas):
    self.goles=goles
    self.asistencias=asistencias
    self.efectividad_pases=efectividad_pases
    self.tarj_rojas=tarj_rojas
    self.tarj_amarillas=tarj_amarillas

def serialize (self):
        return {
           "goles":self.goles,
           "asistencias":self.asistencias,
           "efectividad_pases":self.efectividad_pases,
           "tarj_rojas":self.tarj_rojas,
           "tarj_amarillas":self.tarj_amarillas
        }
