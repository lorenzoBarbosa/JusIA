from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.db import conexao


def _linha_para_usuario(tupla) -> Usuario:
    return Usuario(
        id=tupla["id"],
        escritorio_id=tupla["escritorio_id"],
        nome=tupla["nome"],
        email=tupla["email"],
        senha_hash=tupla["senha_hash"],
        perfil=tupla["perfil"],
        ativo=bool(tupla["ativo"]),
    )


def inserir_usuario(usuario: Usuario) -> int:
    try:
        with conexao() as conn:
            cursor = conn.execute(INSERIR_USUARIO, (
                usuario.escritorio_id,
                usuario.nome,
                usuario.email,
                usuario.senha_hash,
                usuario.perfil,
                int(usuario.ativo),
            ))
            return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting usuario: {e}")
        return -1


def selecionar_usuario_por_id(id: int) -> Usuario | None:
    try:
        with conexao() as conn:
            tupla = conn.execute(SELECIONAR_USUARIO_POR_ID, (id,)).fetchone()
            return _linha_para_usuario(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting usuario by ID: {e}")
        return None


def selecionar_usuario_por_email(escritorio_id: int, email: str) -> Usuario | None:
    try:
        with conexao() as conn:
            tupla = conn.execute(SELECIONAR_USUARIO_POR_EMAIL, (escritorio_id, email)).fetchone()
            return _linha_para_usuario(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting usuario by email: {e}")
        return None


def selecionar_usuarios_por_escritorio(escritorio_id: int) -> list[Usuario]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_USUARIOS_POR_ESCRITORIO, (escritorio_id,))
            return [_linha_para_usuario(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting usuarios by escritorio: {e}")
        return []


def selecionar_todos_usuarios() -> list[Usuario]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_TODOS_USUARIOS)
            return [_linha_para_usuario(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting all usuarios: {e}")
        return []


def selecionar_usuario_paginado(limite: int, offset: int) -> list[Usuario]:
    try:
        with conexao() as conn:
            cursor = conn.execute(SELECIONAR_USUARIO_PAGINADO, (limite, offset))
            return [_linha_para_usuario(t) for t in cursor.fetchall()]
    except Exception as e:
        print(f"Error selecting paginated usuarios: {e}")
        return []


def excluir_usuario_por_id(id: int) -> bool:
    try:
        with conexao() as conn:
            cursor = conn.execute(EXCLUIR_USUARIO_POR_ID, (id,))
            return cursor.rowcount > 0
    except Exception as e:
        print(f"Error deleting usuario: {e}")
        return False