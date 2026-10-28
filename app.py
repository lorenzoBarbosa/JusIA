import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('PRAGMA foreign_keys = ON')

comando_sql = """
    CREATE TABLE IF NOT EXISTS escritorios ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cnpj_registro TEXT UNIQUE,
        data_criacao TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        telefone TEXT,
        ativo INTEGER NOT NULL DEFAULT 1
            CHECK (ativo IN (0, 1))
    );

    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        escritorio_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha_hash TEXT NOT NULL,
        perfil TEXT NOT NULL
            CHECK (perfil IN ('administrador', 'advogado', 'secretario')),
        ativo INTEGER NOT NULL DEFAULT 1
            CHECK (ativo IN (0, 1)),

        FOREIGN KEY (escritorio_id)
            REFERENCES escritorios(id),

        UNIQUE (escritorio_id, email),
        UNIQUE (escritorio_id, id)
    );

    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        escritorio_id INTEGER NOT NULL,
        telefone_cliente TEXT NOT NULL,
        nome_cliente TEXT NOT NULL,
        cpf_cliente TEXT NOT NULL,
        email_cliente TEXT NOT NULL,
        area TEXT NOT NULL,
        resumo TEXT NOT NULL,

        urgencia TEXT NOT NULL DEFAULT 'media'
            CHECK (urgencia IN ('baixa', 'media', 'alta', 'urgente')),

        advogado_id INTEGER,
        processo_andamento TEXT,
        cidade_estado TEXT,
        disponibilidade TEXT,
        data_hora_consulta TEXT,

        status TEXT NOT NULL DEFAULT 'analise'
            CHECK (status IN ('analise','agendada', 'realizada', 'cancelada')),

        data_criacao TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY (escritorio_id)
            REFERENCES escritorios(id),

        FOREIGN KEY (escritorio_id, advogado_id)
            REFERENCES usuarios(escritorio_id, id)
    );

    CREATE INDEX IF NOT EXISTS idx_usuarios_escritorio
        ON usuarios(escritorio_id);

    CREATE INDEX IF NOT EXISTS idx_consultas_escritorio
        ON consultas(escritorio_id);

    CREATE INDEX IF NOT EXISTS idx_consultas_advogado
        ON consultas(escritorio_id, advogado_id);

    CREATE INDEX IF NOT EXISTS idx_consultas_status
        ON consultas(escritorio_id, status);

    CREATE INDEX IF NOT EXISTS idx_consultas_data
        ON consultas(escritorio_id, data_hora_consulta);
"""

cursor.executescript(comando_sql)
conexao.commit()
cursor.close()
conexao.close()