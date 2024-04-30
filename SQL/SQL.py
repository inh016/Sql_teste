import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent 

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco_de_dados.sqlite')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100), email VARCHAR(150))')

datas = ("Luis ", "inho@gmail.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", datas)
conexao.commit()



