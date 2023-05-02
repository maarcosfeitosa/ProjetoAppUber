import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")

try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `ganhos_uber`;")

cursor.execute("CREATE DATABASE `ganhos_uber`;")

cursor.execute("USE `ganhos_uber`;")

# criando tabelas
TABLES = {}
TABLES['Ganhos'] = ('''
      CREATE TABLE `ganhos` (
      `data` date NOT NULL,
      `ganhos` numeric (6,2) NOT NULL,
      `km` int(4),
      `consumo` numeric (4,2),
      `combustivel` numeric (4,3),
      PRIMARY KEY (`data`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(30) NOT NULL,
      `nickname` varchar(20) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("ADMIN", "admin", generate_password_hash("123").decode('utf-8')),
      ("Marcos Feitosa", "maarcosfeitosa", generate_password_hash("123456").decode('utf-8')),
      ("Felipe Duarte", "feduco", generate_password_hash("feduco123").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from ganhos_uber.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


# inserindo jogos
ganhos_sql = 'INSERT INTO ganhos (data, ganhos, km) VALUES (%s, %s, %s)'
ganhos = [
      ('2020-10-20', 20, 10),
      ('2020-10-21', 20, 150),
      ('2020-10-22', 20, 200),
      ('2020-10-23', 50, 139)
]
cursor.executemany(ganhos_sql,ganhos)
cursor.execute('select * from ganhos_uber.ganhos')
print(' -------------  Ganhos:  -------------')
for ganho in cursor.fetchall():
    print(ganho[1])


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()