_COLUNAS = "id, escritorio_id, nome, email, senha_hash, perfil, ativo"

INSERIR_USUARIO = """
INSERT INTO usuarios (escritorio_id, nome, email, senha_hash, perfil, ativo)
VALUES (?, ?, ?, ?, ?, ?)
"""

SELECIONAR_USUARIO_POR_ID = f"""
SELECT {_COLUNAS}
FROM usuarios
WHERE id = ?
"""

SELECIONAR_USUARIO_POR_EMAIL = f"""
SELECT {_COLUNAS}
FROM usuarios
WHERE escritorio_id = ? AND email = ?
"""

SELECIONAR_USUARIOS_POR_ESCRITORIO = f"""
SELECT {_COLUNAS}
FROM usuarios
WHERE escritorio_id = ?
ORDER BY id
"""

SELECIONAR_TODOS_USUARIOS = f"""
SELECT {_COLUNAS}
FROM usuarios
ORDER BY id
"""

SELECIONAR_USUARIO_PAGINADO = f"""
SELECT {_COLUNAS}
FROM usuarios
ORDER BY id
LIMIT ? OFFSET ?
"""

EXCLUIR_USUARIO_POR_ID = """
DELETE FROM usuarios
WHERE id = ?
"""