import requests
import Logado
import pyodbc
from tkinter import *


def Conexao_Banco_Dados(): #Conexão com SQL Server que esta no meu Computador
    global conexao
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-8J8RVEB\SQLEXPRESS;"
        "Database=GanhosUber;"
    )
    conexao = pyodbc.connect(dados_conexao)


def Validar_Texto_Vazio():
    login = entrada_login.get()
    senha = entrada_senha.get()
    vazio = True
    if not login:
        vazio = True
    elif not senha:
        vazio = True
    else:
        vazio = False
    return vazio


def Validacao_Login():
    global mensagem_login
    mensagem_login.destroy() #Usei para as label nao ficarem sobrepostas
    resp = ""
    mensagem_login = Label(janela, text=resp, background="#fff", anchor=W)
    mensagem_login.pack()
    mensagem_login.place(x=70, y=190)
    usuario = Compara_Login(entrada_login.get())
    senha = Compara_Senha(entrada_login.get(), entrada_senha.get())

    if Validar_Texto_Vazio():
        resp = "Insira os Dados"
    else:
        if usuario:
            if senha:
                janela.destroy() #Destruindo a Janela que eu estava para iniciar a janela LOGADO
                Logado.Inicio(usuario)
                #resp = "Login Efetuado"
            else:
                resp = "Senha Incorreta"
        else:
            resp = "Usuario Incorreto"

    mensagem_login.config(text=resp) #Receberei a resposta dos If e colocarei aqui qual foi


def Compara_Login(usuario): #Puxei do Banco de Dados todos os usuarios e comparei com o digitado
    cursor = conexao.cursor()
    return cursor.execute('SELECT * FROM Usuario WHERE usuario = ? ',
                          usuario).fetchone() #Preciso entender o que é fetchone


def Compara_Senha(usuario, senha):#Nao sabia puxar de uma coluna especifica de maneira mais simples
                                  #Entao usei o usuario que ja tinha sido validado e puxei a senha dele, preciso simplificar
    cursor = conexao.cursor()
    return cursor.execute('SELECT * FROM Usuario WHERE usuario = ? AND senha = ? ',
                          usuario, senha).fetchone()


Conexao_Banco_Dados()

global cursor
cursor = conexao.cursor()

janela = Tk()
janela.title("Ganhos Uber")
janela.geometry("300x300")

mensagem_login = Label(janela)

texto_Apresentacao = Label(janela, text="Faça o Login")
texto_Apresentacao.place(x=120, y=80)
Label(janela, text="Login", background="#fff", anchor=W).place(x=70, y=120)
Label(janela, text="Senha", background="#fff", anchor=W).place(x=70, y=155)

entrada_login = Entry(janela)
entrada_login.place(x=120, y=120)

entrada_senha = Entry(janela)
entrada_senha.place(x=120, y=155)

botao_login = Button(janela, text="Login", command=Validacao_Login)
botao_login.place(x=120, y=250)
janela.mainloop()


