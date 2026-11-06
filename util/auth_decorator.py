from functools import wraps
from typing import List, Optional

from fastapi import HTTPException, Request, status
from fastapi.responses import RedirectResponse

from urllib.parse import quote


def criar_sessao(request: Request, usuario: dict) -> None:
    if hasattr(request, 'session'):
        usuario_sessao = usuario.copy()
        usuario_sessao.pop('senha', None)
        request.session['usuario'] = usuario_sessao


def obter_usuario_logado(request: Request) -> Optional[dict]:
    """
    Obtém os dados do usuário logado da sessão
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        Dicionário com dados do usuário ou None se não estiver logado
    """
    if not hasattr(request, 'session'):
        return None
    return request.session.get('usuario')

def esta_logado(request: Request) -> bool:
    """
    Verifica se há um usuário logado
    
    Args:
        request: Objeto Request do FastAPI
    
    Returns:
        True se há usuário logado, False caso contrário
    """
    return obter_usuario_logado(request) is not None




def requer_autenticacao(perfis_autorizados: Optional[List[str]] = None):
    def dependencia(request: Request) -> dict:
        usuario = obter_usuario_logado(request)

        if not usuario or not usuario.get("ativo", False):
            # 303 + Location faz o navegador redirecionar para o login
            raise HTTPException(
                status_code=status.HTTP_303_SEE_OTHER,
                headers={"Location": "/login?redirect=" + quote(request.url.path)},
            )

        if perfis_autorizados and usuario.get("perfil") not in perfis_autorizados:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Você não tem permissão para acessar este recurso",
            )

        return usuario

    return dependencia