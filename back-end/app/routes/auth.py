import os
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Credenciais do admin (armazene em variáveis de ambiente em produção)
ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "acaochego2025")

# Em produção, use um sistema de tokens JWT real
# Por enquanto usaremos um token simples
ADMIN_TOKEN = "admin_session_token_acaochego_2024"


class LoginRequest(BaseModel):
    usuario: str
    senha: str


class LoginResponse(BaseModel):
    token: str
    mensagem: str


@router.post("/auth/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """
    Autentica o administrador e retorna um token de sessão.
    
    Em produção, considere:
    - Usar JWT tokens
    - Implementar hash de senhas
    - Adicionar rate limiting
    - Usar HTTPS obrigatório
    """
    if request.usuario == ADMIN_USER and request.senha == ADMIN_PASSWORD:
        return {
            "token": ADMIN_TOKEN,
            "mensagem": "Login realizado com sucesso"
        }
    else:
        return {
            "token": "",
            "mensagem": "Credenciais inválidas"
        }, 401
