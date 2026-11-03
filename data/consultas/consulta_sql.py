_COLUNAS = """
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
"""

INSERIR_CONSULTA = """
INSERT INTO consultas (
    escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SELECIONAR_CONSULTA_POR_ID = f"""
SELECT {_COLUNAS}
FROM consultas
WHERE id = ?
"""

SELECIONAR_CONSULTAS_POR_STATUS = f"""
SELECT {_COLUNAS}
FROM consultas
WHERE status = ?
ORDER BY id DESC
"""

SELECIONAR_CONSULTAS_POR_CPF = f"""
SELECT {_COLUNAS}
FROM consultas
WHERE cpf_cliente = ?
ORDER BY id
"""

SELECIONAR_CONSULTAS_POR_ESCRITORIO = f"""
SELECT {_COLUNAS}
FROM consultas
WHERE escritorio_id = ?
ORDER BY id
"""

SELECIONAR_CONSULTAS_POR_ADVOGADO = f"""
SELECT {_COLUNAS}
FROM consultas
WHERE advogado_id = ?
ORDER BY id
"""

SELECIONAR_TODAS_CONSULTAS = f"""
SELECT {_COLUNAS}
FROM consultas
ORDER BY id
"""

SELECIONAR_CONSULTA_PAGINADO = f"""
SELECT {_COLUNAS}
FROM consultas
ORDER BY id
LIMIT ? OFFSET ?
"""

ATUALIZAR_STATUS_CONSULTA = """
UPDATE consultas
SET status = ?
WHERE id = ?
"""

EXCLUIR_CONSULTA_POR_ID = """
DELETE FROM consultas
WHERE id = ?
"""