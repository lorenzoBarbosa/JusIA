from dataclasses import dataclass

@dataclass
class Escritorio:
    id: int
    nome: str
    cnpj_registro: str
    data_criacao: str
    telefone: str
    ativo: bool


