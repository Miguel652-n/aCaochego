from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from database.connection import SessionLocal
from database.models import ColabModel

router = APIRouter()

# =========================
# SCHEMAS
# =========================

class Colab(BaseModel):
    nome: str
    email: str
    number: str
    endereco: str
    cidade: str
    cep: str
    estado: str
    descricao: str
    animal: Optional[str] = None


class ColabUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    number: Optional[str] = None
    endereco: Optional[str] = None
    cidade: Optional[str] = None
    cep: Optional[str] = None
    estado: Optional[str] = None
    descricao: Optional[str] = None
    animal: Optional[str] = None

# =========================
# ROTA GET - LISTAR COLABS
# =========================

@router.get("/colabs")
def listar_colabs():

    db = SessionLocal()

    try:
        colabs = db.query(ColabModel).all()

        return [
            {
                "id": colab.id,
                "nome": colab.nome,
                "email": colab.email,
                "number": colab.number,
                "endereco": colab.endereco,
                "cidade": colab.cidade,
                "cep": colab.cep,
                "estado": colab.estado,
                "descricao": colab.descricao,
                "animal": colab.animal
            }
            for colab in colabs
        ]

    finally:
        db.close()


# =========================
# ROTA POST - CRIAR COLAB
# =========================

@router.post("/colabs")
def criar_colab(colab: Colab):

    db = SessionLocal()

    try:
        novo_colab = ColabModel(
            nome=colab.nome,
            email=colab.email,
            number=colab.number,
            endereco=colab.endereco,
            cidade=colab.cidade,
            cep=colab.cep,
            estado=colab.estado,
            descricao=colab.descricao,
            animal=colab.animal
        )

        db.add(novo_colab)
        db.commit()

        return {
            "mensagem": "Colaborador adicionado"
        }

    finally:
        db.close()


# =========================
# ROTA PATCH
# =========================

@router.patch("/colabs/{id}")
def atualizar_colab(id: int, colab: ColabUpdate):

    db = SessionLocal()

    colab_db = db.query(ColabModel).filter(
        ColabModel.id == id
    ).first()

    if not colab_db:
        return {"erro": "colab não encontrado"}

    if colab.nome is not None:
        colab_db.nome = colab.nome

    if colab.email is not None:
        colab_db.email = colab.email

    if colab.number is not None:
        colab_db.number = colab.number

    if colab.endereco is not None:
        colab_db.endereco = colab.endereco

    if colab.cidade is not None:
        colab_db.cidade = colab.cidade

    if colab.cep is not None:
        colab_db.cep = colab.cep

    if colab.estado is not None:
        colab_db.estado = colab.estado

    if colab.descricao is not None:
        colab_db.descricao = colab.descricao
        
    if colab.animal is not None:
        colab_db.animal = colab.animal

    db.commit()

    return {
        "mensagem": "colab atualizado"
    }


# =========================
# ROTA DELETE
# =========================

@router.delete("/colabs/{id}")
def deletar_colab(id: int):

    db = SessionLocal()

    colab_db = db.query(ColabModel).filter(
        ColabModel.id == id
    ).first()

    if not colab_db:
        return {"erro": "colab não encontrado"}

    db.delete(colab_db)

    db.commit()

    return {
        "mensagem": "colab deletado com sucesso"
    }