import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-8J8RVEB\SQLEXPRESS;"
    "Database=GanhosUber;"
)
conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()
cursor.execute('SELECT * FROM Usuario')

for i in cursor:
    print(i)

print("Conexao Efetuada")
