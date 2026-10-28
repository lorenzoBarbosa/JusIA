from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.db import get_connection


def _linha_para_usuario(tupla) -> Usuario:
    return Usuario(
        id = tupla["id"],
        escritorio_id = tupla["escritorio_id"],
        nome = tupla["nome"],
        email = tupla["email"],
        senha_hash = tupla["senha_hash"],
        ativo = bool(tupla["ativo"])
    )

def inserir_usuario(usuario: Usuario) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_USUARIO, (
            usuario.escritorio_id,
            usuario.nome,
            usuario.email,
            usuario.senha_hash,
            usuario.ativo
        ))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return novo_id
    except Exception as e:
        print(f"Error inserting usuario: {e}")
        return -1

def selecionar_usuario_por_id(id: int) -> Usuario:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_USUARIO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        return _linha_para_usuario(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting usuario by ID: {e}")
        return None

def selecionar_usuario_por_email(email: str) -> Usuario:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_USUARIO_POR_EMAIL, (email,))
        tupla = cursor.fetchone()
        conn.close()
        return _linha_para_usuario(tupla) if tupla else None
    except Exception as e:
        print(f"Error selecting usuario by email: {e}")
        return None

def selecionar_usuarios_por_escritorio(escritorio_id: int) -> list[Usuario]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_USUARIOS_POR_ESCRITORIO, (escritorio_id,))
        usuarios = [_linha_para_usuario(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Error selecting usuarios by escritorio: {e}")
        return []

def selecionar_todos_usuarios() -> list[Usuario]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_TODOS_USUARIOS)
        usuarios = [_linha_para_usuario(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Error selecting all usuarios: {e}")
        return []

def selecionar_usuario_paginado(limite: int, offset: int) -> list[Usuario]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(SELECIONAR_USUARIO_PAGINADO, (limite, offset))
        usuarios = [_linha_para_usuario(tupla) for tupla in cursor.fetchall()]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Error selecting paginated usuarios: {e}")
        return []

def excluir_usuario_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_USUARIO_POR_ID, (id,))
        conn.commit()
        excluido = cursor.rowcount > 0
        conn.close()
        return excluido
    except Exception as e:
        print(f"Error deleting usuario: {e}")
        return False