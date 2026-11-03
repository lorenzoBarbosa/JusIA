import os
import secrets
import unicodedata
from typing import Literal

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, field_validator

from data.consultas import consulta_repo
from data.consultas.consulta_model import Consulta

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# N8N_SENHA = os.getenv("N8N_SENHA", "")


class Consulta_n8n(BaseModel):
    escritorio_id: int
    telefone_cliente: str
    nome_cliente: str
    cpf_cliente: str
    email_cliente: EmailStr
    area: str
    resumo: str
    urgencia: str
    advogado_id: int | None = None
    processo_andamento: str | None = None
    cidade_estado: str | None = None
    disponibilidade: str | None = None
    data_hora_consulta: str | None = None
    status: str
    data_criacao: str | None = None


# def exigir_senha_n8n(x_api_key: str | None = Header(default=None)):
#     if not N8N_SENHA or not x_api_key or not secrets.compare_digest(x_api_key, N8N_SENHA):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")


@router.get("/painel", response_class=HTMLResponse)
async def get_painel(request: Request):
    consultas = consulta_repo.selecionar_consulta_por_status("analise")
    return templates.TemplateResponse(request, "painel.html", {"consultas": consultas})


@router.post("/painel",status_code=status.HTTP_201_CREATED)
async def get_n8n_data(dados: Consulta_n8n):
    consulta = Consulta(
        id=0,
        escritorio_id=1,
        telefone_cliente=dados.telefone_cliente,
        nome_cliente=dados.nome_cliente,
        cpf_cliente=dados.cpf_cliente,
        email_cliente=str(dados.email_cliente),
        area=dados.area,
        resumo=dados.resumo,
        urgencia=dados.urgencia,
        advogado_id=1,
        processo_andamento=dados.processo_andamento,
        cidade_estado=dados.cidade_estado,
        disponibilidade=dados.disponibilidade,
        data_hora_consulta=dados.data_hora_consulta,
        status="analise",
        data_criacao=dados.data_criacao
    )

    id_consulta = consulta_repo.inserir_consulta(consulta)

    if id_consulta == -1:
        raise HTTPException(status_code=500, detail="Erro ao salvar consulta")

    return {"ok": True, "id": id_consulta}