from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from database.connection import SessionLocal
from database.models import AnimaisModel

router = APIRouter()


# =========================
# SCHEMAS
# =========================

class Animal(BaseModel):
    nome: str
    especie: str
    genero: str
    idade: str
    regiao: str
    ong: str
    cidade: str
    imagem: str
    status: Optional[str] = "disponivel"


class AnimalUpdate(BaseModel):
    nome: Optional[str] = None
    especie: Optional[str] = None
    genero: Optional[str] = None
    idade: Optional[str] = None
    regiao: Optional[str] = None
    ong: Optional[str] = None
    cidade: Optional[str] = None
    imagem: Optional[str] = None
    status: Optional[str] = None


# =========================
# GET - LISTAR ANIMAIS
# =========================

@router.get("/animais")
def listar_animais():
    db = SessionLocal()
    try:
        animais = db.query(AnimaisModel).all()
        return [
            {
                "id": animal.id,
                "nome": animal.nome,
                "especie": animal.especie,
                "genero": animal.genero,
                "idade": animal.idade,
                "regiao": animal.regiao,
                "ong": animal.ong,
                "cidade": animal.cidade,
                "imagem": animal.imagem,
                "status": animal.status or "disponivel"
            }
            for animal in animais
        ]
    finally:
        db.close()


# =========================
# POST - CRIAR ANIMAL
# =========================

@router.post("/animais")
def criar_animal(animal: Animal):
    db = SessionLocal()
    try:
        novo_animal = AnimaisModel(
            nome=animal.nome,
            especie=animal.especie,
            genero=animal.genero,
            ong=animal.ong,
            idade=animal.idade,
            regiao=animal.regiao,
            cidade=animal.cidade,
            imagem=animal.imagem,
            status=animal.status or "disponivel"
        )
        db.add(novo_animal)
        db.commit()
        db.refresh(novo_animal)
        return {"mensagem": "animal criado com sucesso", "animal": {"id": novo_animal.id, "nome": novo_animal.nome}}
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


# =========================
# PATCH - EDITAR ANIMAL
# =========================

@router.patch("/animais/{id}")
def atualizar_animal(id: int, animal: AnimalUpdate):
    db = SessionLocal()
    animal_db = db.query(AnimaisModel).filter(AnimaisModel.id == id).first()
    if not animal_db:
        return {"erro": "animal não encontrado"}

    for campo in ["nome", "especie", "genero", "idade", "regiao", "ong", "cidade", "imagem", "status"]:
        valor = getattr(animal, campo)
        if valor is not None:
            setattr(animal_db, campo, valor)

    db.commit()
    db.refresh(animal_db)
    return {"mensagem": "animal atualizado com sucesso"}


# =========================
# DELETE - DELETAR ANIMAL
# =========================

@router.delete("/animais/{id}")
def deletar_animal(id: int):
    db = SessionLocal()
    animal_db = db.query(AnimaisModel).filter(AnimaisModel.id == id).first()
    if not animal_db:
        return {"erro": "animal não encontrado"}
    db.delete(animal_db)
    db.commit()
    return {"mensagem": "animal deletado com sucesso"}