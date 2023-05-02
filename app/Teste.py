import locale
from datetime import datetime
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

locale.setlocale(locale.LC_ALL, 'pt_BR')


def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválido, deve ser DD/MM/AAAA")
        return None
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')

        dia = datetime.strftime(data_datetime, '%d')
        mes = datetime.strftime(data_datetime, '%B')
        ano = datetime.strftime(data_datetime, '%Y')
        #return dia + " de " + mes[0].upper() + mes[1:] + " de " + ano
        # return dia + " de " + mes.capitalize() + " de " + ano


data = input("Digite uma data no formato DD/MM/AAAA:")
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)
"""
"""<figure class="img thumbnail col-md-4 formularioImagem">
          <img class="img-fluid" src="{{ url_for('imagem', nome_arquivo='capa_padrao.jpg') }}">
          <figcaption>
            <label class="fileContainer">
              Mudar Capa
              <input type="file" name="arquivo" accept=".jpg">
            </label>
          </figcaption>
        </figure>
        
        


                        ""
