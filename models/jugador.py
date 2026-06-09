from models.db import db

class Jugador():
    def __init__(self,id,nombre, edad,nro_camiseta):
        self.id= id
        self.nombre= nombre
        self.edad= edad
        self.nro_camiseta= nro_camiseta




class Arquero(Jugador):
    def __init__(self, id, nombre, edad, nro_camiseta):
        super().__init__(id, nombre, edad, nro_camiseta)

class Defensor(Jugador):
    def __init__(self, id, nombre, edad, nro_camiseta):
        super().__init__(id, nombre, edad, nro_camiseta)

class Mediocampista(Jugador):
    def __init__(self, id, nombre, edad, nro_camiseta):
        super().__init__(id, nombre, edad, nro_camiseta)

class Delantero(Jugador):
    def __init__(self, id, nombre, edad, nro_camiseta):
        super().__init__(id, nombre, edad, nro_camiseta)

def serialize(self):
    return{
        'id': self.id,
        'nombre': self.nombre,
        'edad': self.edad,
        'nro_camiseta':self.nro_camiseta

    }

    

