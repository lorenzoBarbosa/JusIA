from data.escritorio.escritorio_model import Escritorio
from data.escritorio.escritorio_sql import *
from data.db import conexao, agora


def _linha_para_escritorio(tupla) -> Escritorio:
    return Escritorio(
        id=tupla["id"],
        nome=tupla["nome"],
        cnpj_registro=tupla["cnpj_registro"],
        data_criacao=tupla["data_criacao"],
        telefone=tupla["telefone"],
        ativo=bool(tupla["ativo"]),
    )


def inserir_escritorio(escritorio: Escritorio) -> int:
    try:
        with conexao() as conn:
            cursor = conn.execute(INSERIR_ESCRITORIO, (
                escritorio.nome,
                escritorio.cnpj_registro,
                escritorio.data_criacao or agora(),
                escritorio.telefone,
                int(escritorio.ativo),
            ))
            return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting escritorio: {e}")
        return -1


def selecionar_escritorio_por_id(id: int) -> Escritorio | None:
    try:
        with conexao() as conn:
            tupla = conn.execute(SELECIONAR_ESCRITORIO_POR_ID, (id,)).fetchone()
            return _linha_para_escritorio(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting escritorio by ID: {e}")
        return None


def selecionar_escritorio_por_cnpj(cnpj: str) -> Escritorio | None:
    try:
        with conexao() as conn:
            tupla = conn.execute(SELECIONAR_ESCRITORIO_POR_CNPJ, (cnpj,)).fetchone()
            return _linha_para_escritorio(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting escritorio by CNPJ: {e}")
        return None


def selecionar_todos_escritorios() -> list[Escritorio]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_TODOS_ESCRITORIOS)
            return [_linha_para_escritorio(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting all escritorios: {e}")
        return []


def selecionar_escritorio_paginado(limite: int, offset: int) -> list[Escritorio]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_ESCRITORIO_PAGINADO, (limite, offset))
            return [_linha_para_escritorio(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting paginated escritorios: {e}")
        return []


def excluir_escritorio_por_id(id: int) -> bool:
    try:
        with conexao() as conn:
            cursor = conn.execute(EXCLUIR_ESCRITORIO_POR_ID, (id,))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting escritorio: {e}")
        return False