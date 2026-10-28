from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/painel", response_class=HTMLResponse)
async def get_painel(request: Request):
    return templates.TemplateResponse(request, "painel.html")


