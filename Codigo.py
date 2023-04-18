import requests
import pyodbc
from tkinter import *

def Conexao_Banco_Dados():
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
        print("login vazio")

    elif not senha:
        print("senha vazia")

    else:
        vazio = False

    return vazio

def Validacao_Login():
    global mensagem_login
    mensagem_login.destroy()
    usuario = "maarcosfeitosa"
    senha = "123456"
    resp = ""
    mensagem_login = Label(janela, text=resp, background="#fff", anchor=W)
    mensagem_login.pack()
    mensagem_login.place(x=70, y=190)



    if Validar_Texto_Vazio():
        resp = "Insira os Dados"
        mensagem_login.config(text=resp)

    else:
        if entrada_login.get() == usuario:
            if entrada_senha.get() == senha:
                resp = "Login Efetuado"
            else:
                resp = "Senha Incorreta"

        else:

            resp = "Usuario Incorreto"

    mensagem_login.config(text=resp)







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
