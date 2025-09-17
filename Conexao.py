import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / "MeuBanco.db"

def criar_conexao():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )"""
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")


def inserir_registro(nome, email):
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"Erro: o email '{email}' já está cadastrado.")
    except sqlite3.Error as e:
        print(f"Erro ao inserir registro: {e}")
    else:
        print("Registro inserido com sucesso!")



def atualizar_registro(id, nome, email):
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao Atualizar Registro {e}")
    except sqlite3.IntegrityError:
        print(f"Erro, o registro '{email}' não existe!")
    else:
        print("Registro atualizado com sucesso!")



def remover_registro(id):
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
            conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro de operação no banco: {e}")
    except sqlite3.Error as e:
        print(f"Erro ao remover registro: {e}")
    else:
        print(f"Registro com id={id} removido com sucesso!")


def inserir_muitos(dados):
    with criar_conexao() as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
        conn.commit() 


def consultar_um(id):
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado
            else:
                print(f"Nenhum cliente encontrado com id={id}")
                return None
    except sqlite3.OperationalError as e:
        print(f"Erro de operação no banco: {e}")
    except sqlite3.Error as e:
        print(f"Erro ao consultar registro: {e}")
        return None       


def consultar_todos():
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            resultados = cursor.fetchall()
            return resultados
    except sqlite3.OperationalError as e:
        print(f"Erro de operação no banco: {e}")
        return []
    except sqlite3.Error as e:
        print(f"Erro ao consultar todos os registros: {e}")
        return []


def deletar_tabela():
    try:
        with criar_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS clientes")
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar a tabela: {e}")
    else:
        print("Tabela 'clientes' deletada com sucesso.")







