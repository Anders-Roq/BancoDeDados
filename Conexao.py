import sqlite3
from pathlib import Path

# ROOT_PATH = Path(__file__).parent #mostra o caminho para a raiz da pasta.

# conexao = sqlite3.connect(ROOT_PATH / "MeuBanco.db") # cria a conexão com o banco de dados e seu nome.

# #cur = conexao.cursor() #objeto para executar comandos.

ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / "MeuBanco.db"

def criar_conexao():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )"""
        )
        conn.commit()

def inserir_registro(nome, email):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()


def atualizar_registro(id, nome, email):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
        conn.commit()

def remover_registro(id):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
        conn.commit()

def inserir_muitos(dados):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
        conn.commit()

def consultar_um(id):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        return cursor.fetchone()

def consultar_todos():
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

##inserir_registro(conexao, cur, "Diego", "DiegoFG@gmail.com")
#atualizar_registro(conexao, cur, "Eloisa", "Elo.Isa@gmail.com", 2)
#remover_registro(conexao,cur, 2)
#inserir_muitos(conexao,cur, dados)
#consultar_um(conexao, cur, 1)
#consultar_todos(cur)






