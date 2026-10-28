from data.consultas.consulta_model import Consulta
from data.consultas.consulta_sql import *
from data.db import get_connection


def _linha_para_consulta(tupla) -> Consulta:
    return Consulta(
        id = tupla["id"],
        escritorio_id = tupla["escritorio_id"],
        telefone_cliente = tupla["telefone_cliente"],
        nome_cliente = tupla["nome_cliente"],
        cpf_cliente = tupla["cpf_cliente"],
        email_cliente = tupla["email_cliente"],
        area = tupla["area"],
        resumo = tupla["resumo"],
        urgencia = tupla["urgencia"],
        advogado_id = tupla["advogado_id"],
        processo_andamento = tupla["processo_andamento"],
        cidade_estado = tupla["cidade_estado"],
        disponibilidade = tupla["disponibilidade"],
        data_hora_consulta = tupla["data_hora_consulta"],
        status = tupla["status"],
        data_criacao = tupla["data_criacao"]
    )

def inserir_consulta(consulta: Consulta) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_CONSULTA, (
            consulta.escritorio_id,
            consulta.telefone_cliente,
            consulta.nome_cliente,
            consulta.cpf_cliente,
            consulta.email_cliente,
            consulta.area,
            consulta.resumo,
            consulta.urgencia,
            consulta.advogado_id,
            consulta.processo_andamento,
            consulta.cidade_estado,
            consulta.disponibilidade,
            consulta.data_hora_consulta,
            consulta.status,
            consulta.data_criacao
        ))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return novo_id
    except Exception as e:
        print(f"Error inserting consulta: {e}")
        return -1

def selecionar_consulta_por_id(id: int) -> Consulta:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_CONSULTA_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        return _linha_para_consulta(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting consulta by ID: {e}")
        return None

def selecionar_consultas_por_cpf(cpf: str) -> list[Consulta]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_CONSULTAS_POR_CPF, (cpf,))
        consultas = [_linha_para_consulta(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return consultas
    except Exception as e:
        print(f"Error selecting consultas by CPF: {e}")
        return []

def selecionar_consultas_por_escritorio(escritorio_id: int) -> list[Consulta]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_CONSULTAS_POR_ESCRITORIO, (escritorio_id,))
        consultas = [_linha_para_consulta(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return consultas
    except Exception as e:
        print(f"Error selecting consultas by escritorio: {e}")
        return []

def selecionar_consultas_por_advogado(advogado_id: int) -> list[Consulta]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_CONSULTAS_POR_ADVOGADO, (advogado_id,))
        consultas = [_linha_para_consulta(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return consultas
    except Exception as e:
        print(f"Error selecting consultas by advogado: {e}")
        return []

def selecionar_todas_consultas() -> list[Consulta]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_TODAS_CONSULTAS)
        consultas = [_linha_para_consulta(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return consultas
    except Exception as e:
        print(f"Error selecting all consultas: {e}")
        return []

def selecionar_consulta_paginado(limite: int, offset: int) -> list[Consulta]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_CONSULTA_PAGINADO, (limite, offset))
        consultas = [_linha_para_consulta(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return consultas
    except Exception as e:
        print(f"Error selecting paginated consultas: {e}")
        return []

def excluir_consulta_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CONSULTA_POR_ID, (id,))
        conn.commit()
        excluida = cursor.rowcount > 0
        conn.close()
        return excluida
    except Exception as e:
        print(f"Error deleting consulta: {e}")
        return False