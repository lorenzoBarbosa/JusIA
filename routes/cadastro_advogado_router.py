from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from util.auth_decorator import requer_autenticacao
from util.security import criar_senha_hash


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/cadastro/advogado")
# @requer_autenticacao(perfis_autorizados=["administrador", "advogado"])
async def get_cadastro_advogado(request: Request):
    return templates.TemplateResponse(request,"cadastro.html")


@router.post("/cadastro/advogado")
# @requer_autenticacao(perfis_autorizados=["administrador", "advogado"])
async def post_cadastro_advogado(request: Request,
                                 nome: str = Form(...),
                                 email: str = Form(...),
                                 senha: str = Form(...),
                                 ativo: bool = Form(...),
                                 perfil: str = Form(...)):
    dados_formulatio={
        "nome": nome,
        "email": email,
        "senha": senha,
        "ativo": ativo,
        "perfil": perfil
    }

    if usuario_repo.selecionar_usuario_por_email(1,email):
        return templates.TemplateResponse(request, "cadastro.html", {"mensagem": "Email já cadastrado", "dados_formulario": dados_formulatio})

    try:
        usuario = Usuario(
            id=0,
            escritorio_id=1,
            nome=nome,
            email=email,
            senha_hash=criar_senha_hash(senha),
            perfil=perfil,
            ativo=ativo
        )
        usuario_id = usuario_repo.inserir_usuario(usuario)


        return templates.TemplateResponse(request, "cadastro.html", {"mensagem": "Usuário cadastrado com sucesso!", "sucesso": 1})
    except Exception as e:
        return templates.TemplateResponse(request, "cadastro.html", {"mensagem": f"Erro ao criar usuário: {str(e)}", "dados_formulario": dados_formulatio, "sucesso": 0})