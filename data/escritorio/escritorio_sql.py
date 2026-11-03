_COLUNAS = "id, nome, cnpj_registro, data_criacao, telefone, ativo"

INSERIR_ESCRITORIO = """
INSERT INTO escritorios (nome, cnpj_registro, data_criacao, telefone, ativo)
VALUES (?, ?, ?, ?, ?)
"""

SELECIONAR_ESCRITORIO_POR_CNPJ = f"""
SELECT {_COLUNAS}
FROM escritorios
WHERE cnpj_registro = ?
"""

SELECIONAR_ESCRITORIO_POR_ID = f"""
SELECT {_COLUNAS}
FROM escritorios
WHERE id = ?
"""

SELECIONAR_TODOS_ESCRITORIOS = f"""
SELECT {_COLUNAS}
FROM escritorios
ORDER BY id
"""

SELECIONAR_ESCRITORIO_PAGINADO = f"""
SELECT {_COLUNAS}
FROM escritorios
ORDER BY id
LIMIT ? OFFSET ?
"""

EXCLUIR_ESCRITORIO_POR_ID = """
DELETE FROM escritorios
WHERE id = ?
"""