import secrets
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
import os

from data.db import criar_db
from routes.index_router import router as index_router
from routes.painel_router import router as painel_router

load_dotenv()
app = FastAPI()

criar_db()

SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-secreta-aqui")
app.add_middleware(
    SessionMiddleware,
    secret_key=SECRET_KEY,
    max_age=3600,  # 1 hora
    same_site="lax",
    https_only=False  # True em produção com HTTPS
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(index_router)
app.include_router(painel_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)