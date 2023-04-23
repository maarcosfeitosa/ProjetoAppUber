import requests
import pyodbc
from datetime import datetime
import locale
from tkinter import *

locale.setlocale(locale.LC_ALL, 'pt_BR')
"""class Testando():
    def __int__(self,usuario):
        self.usuario = usuario
        self.janela = Tk()
        self.janela.title("Ganhos Uber")
        self.janela.geometry("800x800")

        mensagem_login = Label(self.janela)

        texto_Apresentacao = Label(self.janela, text=f"Bem Vindo {usuario[1]}")
        texto_Apresentacao.place(x=120, y=80)
        Label(self.janela, text="O que deseja fazer?", anchor=W).place(x=100, y=110)



        botao_inserir_dados = Button(self.janela, text="Login", command=usuario())
        botao_inserir_dados.place(x=70, y=145)

        self.janela.mainloop()

    def usuario(self):
        print("oi")
        pass

    def Inserir_Dados(self):
        #print(self)
        pass




#Testando().__int__("maarcosfeitosa")"""
def Conexao_Banco_Dados(): #Conexão com SQL Server que esta no meu Computador
    global conexao
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-8J8RVEB\SQLEXPRESS;"
        "Database=GanhosUber;"
    )
    conexao = pyodbc.connect(dados_conexao)

def Validar_Os_Dados_Inseridos(id_user, data, valor, km, consumo):
    Validar_Data(id_user, data)

def Validar_Data(id_user, data):
    global mensagem_data
    mensagem_data.destroy()
    resp = ""
    mensagem_data = Label(janela, text=resp, fg="Red", font=("Arial", 8), anchor=W)
    mensagem_data.pack()
    mensagem_data.place(x=245, y=150)
    data_valida = False
    try:
        datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        resp = "Data Inválida"
        mensagem_data = Label(janela, text=resp, fg="Red", font=("Arial", 8), anchor=W)
        mensagem_data.pack()
        mensagem_data.place(x=245, y=150)
        return None
    else:
        resp = "aiskdjnasijdjasidiasoijda"
        mensagem_data = Label(janela, text=resp, fg="Red", font=("Arial", 8), anchor=W)
        mensagem_data.pack()
        mensagem_data.place(x=245, y=150)
        data_datetime = datetime.strptime(data, '%d/%m/%Y')
        data_valida = True
        return datetime.strftime(data_datetime, '%d de %B de %Y')

    """if data_valida:
        cursor = conexao.cursor()
        comdando ="""


def Confirmar_Incersao(id_user, data, valor, km, consumo):
    print(id_user)
    print(data)
    print(valor)
    print(km)
    print(consumo)
    cursor = conexao.cursor()
    comando = F"""INSERT INTO Ganhos(id_user,data_ganhos, valor, km_rodado, consumo)
                    VALUES 
                    ({id_user}, '{data}', {valor}, {km}, {consumo})"""
    cursor.execute(comando)
    cursor.commit()

def Inserir_Dados():
    print("Botao")
    botao_inserir_dados.destroy()
    texto_Apresentacao.destroy()
    texto_Mensagem.config(text="Inserindo dados ")
    entrada_data = Entry(janela)
    entrada_data.place(x=120, y=150)
    entrada_valor = Entry(janela)
    entrada_valor.place(x=120, y=175)
    entrada_km_rodado = Entry(janela)
    entrada_km_rodado.place(x=120, y=200)
    entrada_consumo = Entry(janela)
    entrada_consumo.place(x=120, y=225)


    Label(janela, text="Data", background="#fff", anchor=W).place(x=50, y=150)
    Label(janela, text="Valor", background="#fff", anchor=W).place(x=50, y=175)
    Label(janela, text="Km", background="#fff", anchor=W).place(x=50, y=200)
    Label(janela, text="Consumo", background="#fff", anchor=W).place(x=50, y=225)

    botao_confirmar_dados = Button(janela, text="Confirmar", command=lambda: Validar_Os_Dados_Inseridos(usuario[0], entrada_data.get(),entrada_valor.get(),entrada_km_rodado.get(),entrada_consumo.get()))
    #Esse Lambda foi como consegui enviar parametros para minha funcao, ainda preciso entender o que realmente significa
    botao_confirmar_dados.place(x=70, y=250)

def Inicio(user):
    #Criei tudo global pq senao nao conseguia usar nos outros def, e se eu deixasse solto quando puxava
    #da outra pagina ele ja iniciava o codigo todoo mesmo sem configurar
    #preciso entender se o import ja executa o programa

    Conexao_Banco_Dados()

    global usuario
    global janela
    global botao_inserir_dados
    global texto_Apresentacao
    global texto_Mensagem
    usuario = user
    janela = Tk()
    janela.title("Ganhos Uber")
    janela.geometry("800x800")

    mensagem_login = Label(janela)

    texto_Apresentacao = Label(janela, text=f"Bem Vindo {usuario[1]}")
    texto_Apresentacao.place(x=120, y=80)
    texto_Mensagem = Label(janela, text="O que deseja fazer?", anchor=W)
    texto_Mensagem.place(x=100, y=110)


    botao_inserir_dados = Button(janela, text="Inserir Dados", command=Inserir_Dados)
    botao_inserir_dados.place(x=70, y=145)

    janela.mainloop()


global mensagem_data