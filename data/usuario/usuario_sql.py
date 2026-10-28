INSERIR_USUARIO="""
INSERT INTO usuarios (escritorio_id, nome, email, senha_hash, ativo)
VALUES (?, ?, ?, ?, ?)
"""

SELECIONAR_USUARIO_POR_ID="""
SELECT
    id, escritorio_id, nome, email, senha_hash, ativo
FROM usuarios
WHERE id = ?
"""

SELECIONAR_USUARIO_POR_EMAIL="""
SELECT
    id, escritorio_id, nome, email, senha_hash, ativo
FROM usuarios
WHERE email = ?
"""

SELECIONAR_USUARIOS_POR_ESCRITORIO="""
SELECT
    id, escritorio_id, nome, email, senha_hash, ativo
FROM usuarios
WHERE escritorio_id = ?
ORDER BY id
"""

SELECIONAR_TODOS_USUARIOS="""
SELECT
    id, escritorio_id, nome, email, senha_hash, ativo
FROM usuarios
ORDER BY id
"""

SELECIONAR_USUARIO_PAGINADO="""
SELECT
    id, escritorio_id, nome, email, senha_hash, ativo
FROM usuarios
ORDER BY id
LIMIT ? OFFSET ?
"""

EXCLUIR_USUARIO_POR_ID="""
DELETE FROM usuarios
WHERE id = ?
"""