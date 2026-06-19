from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import AnimaisModel
from app.dependencies import get_db

router = APIRouter()


# =========================
# SCHEMAS
# =========================

class Animal(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    especie: str = Field(..., min_length=1, max_length=50)
    genero: str = Field(..., min_length=1, max_length=50)
    idade: str = Field(..., min_length=1, max_length=50)
    regiao: str = Field(..., min_length=1, max_length=2)
    ong: str = Field(..., min_length=1, max_length=100)
    cidade: str = Field(..., min_length=1, max_length=100)
    imagem: str = Field(..., min_length=1, max_length=255)
    status: Optional[str] = Field("disponivel", max_length=50)


class AnimalUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    especie: Optional[str] = Field(None, min_length=1, max_length=50)
    genero: Optional[str] = Field(None, min_length=1, max_length=50)
    idade: Optional[str] = Field(None, min_length=1, max_length=50)
    regiao: Optional[str] = Field(None, min_length=1, max_length=2)
    ong: Optional[str] = Field(None, min_length=1, max_length=100)
    cidade: Optional[str] = Field(None, min_length=1, max_length=100)
    imagem: Optional[str] = Field(None, min_length=1, max_length=255)
    status: Optional[str] = Field(None, max_length=50)


# =========================
# GET - LISTAR ANIMAIS
# =========================

@router.get("/animais")
def listar_animais(db: Session = Depends(get_db)):
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar animais: {str(e)}")


# =========================
# POST - CRIAR ANIMAL
# =========================

@router.post("/animais")
def criar_animal(animal: Animal, db: Session = Depends(get_db)):
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
        raise HTTPException(status_code=500, detail=f"Erro ao criar animal: {str(e)}")


# =========================
# PATCH - EDITAR ANIMAL
# =========================

@router.patch("/animais/{id}")
def atualizar_animal(id: int, animal: AnimalUpdate, db: Session = Depends(get_db)):
    try:
        animal_db = db.query(AnimaisModel).filter(AnimaisModel.id == id).first()
        if not animal_db:
            raise HTTPException(status_code=404, detail="Animal não encontrado")

        for campo in ["nome", "especie", "genero", "idade", "regiao", "ong", "cidade", "imagem", "status"]:
            valor = getattr(animal, campo)
            if valor is not None:
                setattr(animal_db, campo, valor)

        db.commit()
        db.refresh(animal_db)
        return {"mensagem": "animal atualizado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar animal: {str(e)}")


# =========================
# DELETE - DELETAR ANIMAL
# =========================

@router.delete("/animais/{id}")
def deletar_animal(id: int, db: Session = Depends(get_db)):
    try:
        animal_db = db.query(AnimaisModel).filter(AnimaisModel.id == id).first()
        if not animal_db:
            raise HTTPException(status_code=404, detail="Animal não encontrado")
        db.delete(animal_db)
        db.commit()
        return {"mensagem": "animal deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao deletar animal: {str(e)}")