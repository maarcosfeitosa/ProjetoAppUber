import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, DateField, DecimalField, IntegerField
from wtforms import *
import locale

class FormularioGanhos(FlaskForm):
    data_ganho = DateField('Data', [validators.DataRequired()])
    ganhos = DecimalField('Ganhos', [
            validators.DataRequired(),
            validators.NumberRange(max=2000, message="Valor deve ser menor ou igual a 1000")
        ])
    km = IntegerField('Km', [])
    consumo = DecimalField('Consumo', [])
    combustivel = DecimalField('Preço Gasolina', [])
    salvar = SubmitField('Salvar')
       

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

