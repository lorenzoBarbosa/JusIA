INSERIR_ESCRITORIO="""
INSERT INTO escritorios (nome, cnpj_registro, data_criacao, telefone, ativo)
VALUES (?, ?, ?, ?, ?)
"""

SELECIONAR_ESCRITORIO_POR_CNPJ="""
SELECT
    id, nome, cnpj_registro, data_criacao, telefone, ativo 
FROM escritorios
WHERE cnpj_registro LIKE ?
"""

SELECIONAR_ESCRITORIO_POR_ID="""
SELECT
    id, nome, cnpj_registro, data_criacao, telefone, ativo 
FROM escritorios
WHERE id LIKE ?
"""

SELECIONAR_TODOS_ESCRITORIOS="""
SELECT 
    id, nome, cnpj_registro, data_criacao, telefone, ativo 
FROM escritorios
ORDER BY id 
"""

SELECIONAR_ESCRITORIO_PAGINADO="""
SELECT
    id, nome, cnpj_registro, data_criacao, telefone, ativo 
FROM escritorios
ORDER BY id
LIMIT ? OFFSET ?    
"""

EXLUIR_ESCRITORIO_POR_ID="""
DELETE FROM escritorios
WHERE id = ?
"""
