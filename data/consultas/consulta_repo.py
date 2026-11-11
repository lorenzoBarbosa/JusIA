from data.consultas.consulta_model import Consulta
from data.consultas.consulta_sql import *
from data.db import conexao, agora


def _linha_para_consulta(tupla) -> Consulta:
    return Consulta(
        id=tupla["id"],
        escritorio_id=tupla["escritorio_id"],
        telefone_cliente=tupla["telefone_cliente"],
        nome_cliente=tupla["nome_cliente"],
        cpf_cliente=tupla["cpf_cliente"],
        email_cliente=tupla["email_cliente"],
        area=tupla["area"],
        resumo=tupla["resumo"],
        urgencia=tupla["urgencia"],
        advogado_id=tupla["advogado_id"],
        processo_andamento=tupla["processo_andamento"],
        cidade_estado=tupla["cidade_estado"],
        disponibilidade=tupla["disponibilidade"],
        data_hora_consulta=tupla["data_hora_consulta"],
        status=tupla["status"],
        data_criacao=tupla["data_criacao"],
    )


def inserir_consulta(consulta: Consulta) -> int:
    try:
        with conexao() as conn:
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
                consulta.data_criacao or agora(),
            ))
            return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting consulta: {e}")
        return -1


def selecionar_consulta_por_id(id: int) -> Consulta | None:
    try:
        with conexao() as conn:
            tupla = conn.execute(SELECIONAR_CONSULTA_POR_ID, (id,)).fetchone()
            return _linha_para_consulta(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting consulta by ID: {e}")
        return None


def selecionar_consulta_por_status(status: str) -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_CONSULTAS_POR_STATUS, (status,))
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting consultas by status: {e}")
        return []


def selecionar_consultas_por_cpf(cpf: str) -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_CONSULTAS_POR_CPF, (cpf,))
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting consultas by CPF: {e}")
        return []


def selecionar_consultas_por_escritorio(escritorio_id: int) -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_CONSULTAS_POR_ESCRITORIO, (escritorio_id,))
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting consultas by escritorio: {e}")
        return []


def selecionar_consultas_por_advogado(advogado_id: int) -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_CONSULTAS_POR_ADVOGADO, (advogado_id,))
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting consultas by advogado: {e}")
        return []


def selecionar_todas_consultas() -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_TODAS_CONSULTAS)
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting all consultas: {e}")
        return []


def selecionar_consulta_paginado(limite: int, offset: int) -> list[Consulta]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_CONSULTA_PAGINADO, (limite, offset))
            return [_linha_para_consulta(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting paginated consultas: {e}")
        return []

def atualizar_status_consulta(
    id: int, status: str, data_hora_consulta: str | None = None
) -> bool:
    try:
        with conexao() as conn:
            cursor = conn.execute(
                ATUALIZAR_STATUS_CONSULTA, (status, data_hora_consulta, id)
            )
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error updating consulta status: {e}")
        return False

def atualizar_status_por_prazo(limite_atraso: str, limite_urgente: str) -> int:
    try:
        with conexao() as conn:
            urgentes = conn.execute(MARCAR_URGENTES, (limite_urgente,)).rowcount
            atrasadas = conn.execute(MARCAR_EM_ATRASO, (limite_atraso,)).rowcount
            return urgentes + atrasadas
    except Exception as e:
        print(f"Error updating status by deadline: {e}")
        return 0



def excluir_consulta_por_id(id: int) -> bool:
    try:
        with conexao() as conn:
            cursor = conn.execute(EXCLUIR_CONSULTA_POR_ID, (id,))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting consulta: {e}")
        return False