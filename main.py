import os
import secrets

from dotenv import load_dotenv

from data.consultas.consulta_model import Consulta
from data.usuario.usuario_model import Usuario

load_dotenv()

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from data.db import criar_db
from routes.index_router import router as index_router
from routes.painel_router import router as painel_router
from data.escritorio import escritorio_repo
from data.escritorio.escritorio_model import Escritorio
from data.usuario import usuario_repo
from data.consultas import consulta_repo

app = FastAPI()

escritorio= Escritorio(
    id=0,
    nome="Escritório Exemplo",
    cnpj_registro="12.345.678/0001-90",
    data_criacao=None,
    telefone="(11) 1234-5678",
    ativo=True
)
admin = Usuario(
    id=0,
    escritorio_id = 1,
    nome="Advogado Exemplo",
    email="advogado@example.com",
    senha_hash="senha123",
    perfil="administrador",
    ativo=1
)
consulta_teste= Consulta(
    id=0,
    escritorio_id= 1,
    telefone_cliente= "282828282",
    nome_cliente= "claudio",
    cpf_cliente="124215345",
    email_cliente="wmkldgfmkl",
    area="civil",
    resumo="lomsklfdmvlaskmfvlkamdvkl",
    urgencia="sfkjadskv",
    advogado_id=1,
    processo_andamento="maklsdc",
    cidade_estado="cachoeiro ES",
    disponibilidade="smdklc",
    data_hora_consulta="dsf",
    status="teste",
    data_criacao="jsdfhaj"
)

criar_db()
escritorio_repo.inserir_escritorio(escritorio)
usuario_repo.inserir_usuario(admin)
consulta_repo.inserir_consulta(consulta_teste)


# Em produção, defina SECRET_KEY no ambiente.
# Em desenvolvimento, uma chave aleatória é gerada (sessões expiram a cada reinício).
SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_urlsafe(32)

app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    max_age=3600,  # 1 hora
    same_site="lax",
    https_only=os.getenv("ENV") == "production",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(index_router)
app.include_router(painel_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)