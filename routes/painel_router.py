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

import httpx

from datetime import datetime, timedelta

DIAS_ATRASO = 1
DIAS_URGENTE = 3
FORMATO_DATA = "%Y-%m-%d %H:%M:%S"

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
    agora = datetime.now()
    consulta_repo.atualizar_status_por_prazo(
        limite_atraso=(agora - timedelta(days=DIAS_ATRASO)).strftime(FORMATO_DATA),
        limite_urgente=(agora - timedelta(days=DIAS_URGENTE)).strftime(FORMATO_DATA),
    )
    consultas = consulta_repo.selecionar_consulta_por_status("analise")
    consultas_em_atraso = consulta_repo.selecionar_consulta_por_status("em atraso")
    consultas_urgentes = consulta_repo.selecionar_consulta_por_status("urgente")
    consultas_antigas = consultas_em_atraso + consultas_urgentes

    return templates.TemplateResponse(
        request,
        "painel.html",
        {
            "consultas": consultas,
            "consultas_antigas": consultas_antigas
        },
    )

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


N8N_WEBHOOK_URL = "https://lorenzobarbosaalves8.app.n8n.cloud/webhook/consulta-resposta"

class Decisao(BaseModel):
    decisao: Literal["aceita", "recusada"]
    data_hora_consulta: datetime | None = None

@router.post("/leads/{lead_id}/decidir")
async def decidir_lead(lead_id: int, corpo: Decisao):
    if corpo.decisao == "aceita":
        if corpo.data_hora_consulta is None:
            raise HTTPException(
                status_code=422,
                detail="Informe o horário da consultoria para validar a lead",
            )
        if corpo.data_hora_consulta <= datetime.now():
            raise HTTPException(
                status_code=422,
                detail="O horário da consultoria deve ser futuro",
            )
        data_hora_consulta = corpo.data_hora_consulta.strftime(FORMATO_DATA)
    else:
        data_hora_consulta = None

    if not consulta_repo.atualizar_status_consulta(
        lead_id, corpo.decisao, data_hora_consulta
    ):
        raise HTTPException(status_code=404, detail="Consulta não encontrada")

    consulta = consulta_repo.selecionar_consulta_por_id(lead_id)
    payload = {
        "id": lead_id,
        "decisao": corpo.decisao,
        "telefone_cliente": consulta.telefone_cliente,
        "nome_cliente": consulta.nome_cliente,
        "status": consulta.status,
        "data_hora_consulta": consulta.data_hora_consulta,
    }
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(N8N_WEBHOOK_URL, json=payload)
            r.raise_for_status()
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="Falha ao contatar o n8n")

    return {"ok": True}