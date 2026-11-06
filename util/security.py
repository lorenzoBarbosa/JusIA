from passlib.context import CryptContext


pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criar_senha_hash(senha: str) -> str:
    return pwd_content.hash(senha)