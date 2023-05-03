import locale
from datetime import date, datetime
import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash
import pyodbc
from flask import Flask, render_template
import locale
""""
def select_db(teste, password):
    return cursor.execute('SELECT usuario FROM Usuario WHERE usuario = ? AND senha = ?',
                          (teste, password)).fetchone()


dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-8J8RVEB\SQLEXPRESS;"
    "Database=GanhosUber;"
)
conexao = pyodbc.connect(dados_conexao)
usuario = "maarcosfeitosa"
senha = 123456
global cursor
cursor = conexao.cursor()
cursor.execute(f"SELECT * FROM Usuario WHERE usuario = ? AND senha = ?", usuario, senha)

teste = "maarcosfeitosa"
password = "123456"

user = select_db(teste, password)
if user:
    print('\n  Welcome to system!')

for i in cursor:
    print(i)

print("Conexao Efetuada")

locale.setlocale(locale.LC_ALL, 'pt_BR')"""

data = date.today
print(data.day)
