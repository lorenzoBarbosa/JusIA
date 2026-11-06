from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from data.consultas import consulta_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/painel/consultas", response_class=HTMLResponse)
async def get_painel_consultas(request: Request):
    consultas = consulta_repo.selecionar_todas_consultas()
    return templates.TemplateResponse(request, "painel_consultas.html", {"consultas": consultas})