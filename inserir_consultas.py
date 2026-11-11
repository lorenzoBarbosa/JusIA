import sqlite3

consultas = [
    (
        1,                          # escritorio_id
        "5528999483389",          # telefone_cliente
        "Joao da Silva",            # nome_cliente
        "111.222.333-44",           # cpf_cliente
        "joaoo@email.com",            # email_cliente
        "Trabalhista",              # area
        "Duvidas sobre rescisao contratual",
        "alta",                     # urgencia
        1,                          # advogado_id
        "Nao informado",            # processo_andamento
        "Sao Paulo - SP",           # cidade_estado
        "Manha",                    # disponibilidade
        None,                       # data_hora_consulta
        "analise",                  # status
        "2026-11-01 10:00:00",               # data_criacao
    ),
    (
        1,
        "5528999483389",
        "Maria Oliveira",
        "555.666.777-88",
        "mariaa@email.com",
        "Civil",
        "Problema com contrato de aluguel",
        "normal",
        1,
        None,
        "Campinas - SP",
        "Tarde",
        None,
        "analise",
        "2026-11-01 10:00:00",
    ),
    (
        1,
        "5528999483389",
        "Maria Oliveira",
        "555.676.777-88",
        "mariaaeadf@email.com",
        "Civil",
        "Problema com contrato de aluguel",
        "normal",
        1,
        None,
        "Campinas - SP",
        "Tarde",
        None,
        "analise",
        "2026-11-01 10:00:00",
    ),
    (
        1,
        "5528999483389",
        "Maria Oliveira",
        "555.676.727-88",
        "mariaaefdadf@email.com",
        "Civil",
        "Problema com contrato de aluguel",
        "normal",
        1,
        None,
        "Campinas - SP",
        "Tarde",
        None,
        "analise",
        "2026-11-01 10:00:00",
    ),
    (
        1,
        "5528999483389",
        "Maria Oliveira",
        "555.676.707-88",
        "mariaaeadf@email.com",
        "Civil",
        "Problema com contrato de aluguel",
        "normal",
        1,
        None,
        "Campinas - SP",
        "Tarde",
        None,
        "analise",
        "2026-11-01 10:00:00",
    ),
]

sql = """
INSERT INTO consultas (
    escritorio_id, telefone_cliente, nome_cliente, cpf_cliente,
    email_cliente, area, resumo, urgencia, advogado_id,
    processo_andamento, cidade_estado, disponibilidade,
    data_hora_consulta, status, data_criacao
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

with sqlite3.connect("dados.db") as conexao:
    conexao.execute("PRAGMA foreign_keys = ON")
    conexao.executemany(sql, consultas)
    print(f"{len(consultas)} consultas inseridas com sucesso.")