from jogoteca import db
from datetime import datetime
from sqlalchemy import extract

class Ganhos(db.Model):
    data = db.Column(db.Date, primary_key=True, nullable=False)
    ganhos = db.Column(db.Numeric(6,2), nullable=False)
    km = db.Column(db.Integer, nullable=True)
    consumo = db.Column(db.Numeric(4,2), nullable=True)
    combustivel = db.Column(db.Numeric(4,3), nullable=True)

    def __repr__(self):
        return '<Data %r>' % self.data


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Conversor_Data:

    def __init__(self, format):
        self.format = format

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)

class Verifica_Nulo():
    def __init__(self, km, consumo, combustivel):
        self.km = km
        self.consumo = consumo
        self.combustivel = combustivel
        if  self.km == None:
            self.km = 0
            
        if  self.consumo == None:
            self.consumo = 0
            
        if  self.combustivel == None:
            self.combustivel = 0

    
    
    """ def __repr__(self):
        return '<Data %r>' % self.data"""