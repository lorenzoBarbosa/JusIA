from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    escritorio_id: int
    nome: str
    email: str
    senha_hash: str
    ativo: bool