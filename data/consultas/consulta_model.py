from dataclasses import dataclass

@dataclass
class Consulta:
    id: int
    escritorio_id: int
    telefone_cliente: str
    nome_cliente: str
    cpf_cliente: str
    email_cliente: str
    area: str
    resumo: str
    urgencia: str
    advogado_id: int
    processo_andamento: str
    cidade_estado: str
    disponibilidade: str
    data_hora_consulta: str
    status: str
    data_criacao: str
