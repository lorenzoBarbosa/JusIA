from data.escritorio.escritorio_model import Escritorio
from data.escritorio.escritorio_sql import *
from data.db import get_connection

def inserir_escritorio(escritorio: Escritorio) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_ESCRITORIO, (
            escritorio.nome,
            escritorio.cnpj_registro,
            escritorio.data_criacao,
            escritorio.telefone,
            escritorio.ativo
        ))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting escritorio: {e}")
        return -1

def selecionar_escritorio_por_cnpj(id: int) -> Escritorio:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_ESCRITORIO_POR_CNPJ, (id,))
        tupla = cursor.fetchone()
        conn.close()
        return Escritorio(
            id = tupla["id"],
            cnpj_registro = tupla["cnpj_registro"],
            data_criacao = tupla["data_criacao"],
            telefone = tupla["telefone"],
            ativo = tupla["ativo"]
        )
    except Exception as e:
        print(f"Error selecting escritorio by CNPJ: {e}")
        return None

def selecionar_escritorio_por_cnpj(cnpj: str) -> Escritorio:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_ESCRITORIO_POR_CNPJ, (cnpj,))
        tupla = cursor.fetchone()
        conn.close()
        return Escritorio(
            id = tupla["id"],
            cnpj_registro = tupla["cnpj_registro"],
            data_criacao = tupla["data_criacao"],
            telefone = tupla["telefone"],
            ativo = tupla["ativo"]
        )
    except Exception as e:
        print(f"Error selecting escritorio by CNPJ: {e}")
        return None

def selecionar_todos_escritorios():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_TODOS_ESCRITORIOS)
        escritorios = []
        for tupla in cursor.fetchall():
            escritorios.append(Escritorio(
                id = tupla["id"],
                nome = tupla["nome"],
                cnpj_registro = tupla["cnpj_registro"],
                data_criacao = tupla["data_criacao"],
                telefone = tupla["telefone"],
                ativo = tupla["ativo"]
            ))
        conn.close()
        return escritorios
    except Exception as e:
        print(f"Error selecting all escritorios: {e}")
        return []

