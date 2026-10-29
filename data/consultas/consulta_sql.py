INSERIR_CONSULTA="""
INSERT INTO consultas (
    escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SELECIONAR_CONSULTA_POR_ID="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
WHERE id = ?
"""

SELECIONAR_CONSULTAS_POR_CPF="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
WHERE cpf_cliente = ?
ORDER BY id
"""

SELECIONAR_CONSULTAS_POR_ESCRITORIO="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
WHERE escritorio_id = ?
ORDER BY id
"""

SELECIONAR_CONSULTAS_POR_ADVOGADO="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
WHERE advogado_id = ?
ORDER BY id
"""

SELECIONAR_CONSULTAS_POR_STATUS="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
WHERE status = ?
ORDER BY id
"""

SELECIONAR_TODAS_CONSULTAS="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
ORDER BY id
"""

SELECIONAR_CONSULTA_PAGINADO="""
SELECT
    id, escritorio_id, telefone_cliente, nome_cliente, cpf_cliente, email_cliente,
    area, resumo, urgencia, advogado_id, processo_andamento, cidade_estado,
    disponibilidade, data_hora_consulta, status, data_criacao
FROM consultas
ORDER BY id
LIMIT ? OFFSET ?
"""

EXCLUIR_CONSULTA_POR_ID="""
DELETE FROM consultas
WHERE id = ?
"""