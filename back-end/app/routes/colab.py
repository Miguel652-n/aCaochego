import os
import json
import httpx
import re

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator

from typing import Optional
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import ColabModel, AnimaisModel
from app.dependencies import get_db

router = APIRouter()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")


# =========================
# SCHEMAS
# =========================

class Colab(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    number: str = Field(..., min_length=8, max_length=20)
    endereco: str = Field(..., min_length=1, max_length=255)
    cidade: str = Field(..., min_length=1, max_length=100)
    cep: str = Field(..., min_length=8, max_length=10)
    estado: str = Field(..., min_length=2, max_length=2)
    descricao: str = Field(..., min_length=10, max_length=2000)

    # novo contrato
    animal_id: Optional[int] = Field(None)

    # compatibilidade (legado)
    animal: Optional[str] = Field(None, max_length=100)

    
    @field_validator('estado')
    def validate_estado(cls, v):

        valid_states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
                       'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
                       'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        if v.upper() not in valid_states:
            raise ValueError('Estado inválido')
        return v.upper()
    
    @field_validator('cep')
    def validate_cep(cls, v):

        if not re.match(r'^\d{5}-?\d{3}$', v):
            raise ValueError('CEP deve estar no formato XXXXX-XXX ou XXXXXXXX')
        return v


class ColabUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    number: Optional[str] = Field(None, min_length=8, max_length=20)
    endereco: Optional[str] = Field(None, min_length=1, max_length=255)
    cidade: Optional[str] = Field(None, min_length=1, max_length=100)
    cep: Optional[str] = Field(None, min_length=8, max_length=10)
    estado: Optional[str] = Field(None, min_length=2, max_length=2)
    descricao: Optional[str] = Field(None, min_length=10, max_length=2000)
    animal: Optional[str] = Field(None, max_length=100)
    aprovado: Optional[str] = Field(None, max_length=50)


# =========================
# ANÁLISE DE APTIDÃO COM IA
# =========================

def analisar_aptidao(descricao: str, nome_animal: Optional[str]) -> dict:
    """Chama a API da Anthropic para analisar se o colaborador é apto a adotar."""

    if not ANTHROPIC_API_KEY:
        return {"aprovado": "pendente", "analise": "Chave da API não configurada."}

    prompt = f"""Você é um especialista em bem-estar animal que avalia candidatos à adoção de pets.

Analise a seguinte descrição familiar de um candidato à adoção{f' do animal {nome_animal}' if nome_animal else ''}:

"{descricao}"

Com base na descrição, avalie se o candidato está APTO ou INAPTO para adotar.

Considere positivamente: espaço adequado, experiência com animais, estabilidade familiar, disponibilidade de tempo, menção a responsabilidade e cuidado.
Considere negativamente: instabilidade, falta de espaço, ausência de responsabilidade, sinais de impulsividade.

Responda SOMENTE com um JSON no formato:
{{"resultado": "aprovado" ou "reprovado", "analise": "justificativa curta em uma frase"}}

Não escreva mais nada além do JSON."""

    try:
        response = httpx.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 200,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=15.0
        )

        content = response.json()["content"][0]["text"]
        clean = content.strip().replace("```json", "").replace("```", "").strip()
        parsed = json.loads(clean)

        return {
            "aprovado": parsed.get("resultado", "pendente"),
            "analise": parsed.get("analise", "")
        }

    except Exception as e:
        return {"aprovado": "pendente", "analise": f"Erro na análise: {str(e)}"}


# =========================
# GET - LISTAR COLABS
# =========================

@router.get("/colabs")
def listar_colabs(db: Session = Depends(get_db)):
    try:
        colabs = db.query(ColabModel).all()
        return [
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email,
                "number": c.number,
                "endereco": c.endereco,
                "cidade": c.cidade,
                "cep": c.cep,
                "estado": c.estado,
                "descricao": c.descricao,
                "animal_id": c.animal_id,
                "animal": c.animal,
                "aprovado": c.aprovado or "pendente",
                "analise_ia": c.analise_ia or ""
            }
            for c in colabs
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar colaboradores: {str(e)}")


# =========================
# POST - CRIAR COLAB
# =========================

@router.post("/colabs")
def criar_colab(colab: Colab, db: Session = Depends(get_db)):
    try:
        # Análise de aptidão pela IA
        resultado = analisar_aptidao(colab.descricao, colab.animal)

        novo_colab = ColabModel(
            nome=colab.nome,
            email=colab.email,
            number=colab.number,
            endereco=colab.endereco,
            cidade=colab.cidade,
            cep=colab.cep,
            estado=colab.estado,
            descricao=colab.descricao,
            animal_id=colab.animal_id,
            animal=colab.animal,
            aprovado=resultado["aprovado"],
            analise_ia=resultado["analise"]
        )


        db.add(novo_colab)

        # Se aprovado e tem animal, muda status do animal para "em_adocao"
        if resultado["aprovado"] == "aprovado":
            # Preferir animal_id (novo contrato)
            if colab.animal_id:
                animal = db.query(AnimaisModel).filter(AnimaisModel.id == colab.animal_id).first()
            else:
                # legado
                animal = db.query(AnimaisModel).filter(AnimaisModel.nome == colab.animal).first() if colab.animal else None

            if animal:
                animal.status = "em_adocao"


        db.commit()

        return {
            "mensagem": "Colaborador adicionado",
            "aprovado": resultado["aprovado"],
            "analise_ia": resultado["analise"]
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar colaborador: {str(e)}")


# =========================
# PATCH - ATUALIZAR COLAB
# =========================

@router.patch("/colabs/{id}")
def atualizar_colab(id: int, colab: ColabUpdate, db: Session = Depends(get_db)):
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            raise HTTPException(status_code=404, detail="Colaborador não encontrado")

        animal_anterior = colab_db.animal
        aprovado_anterior = colab_db.aprovado

        for campo in ["nome", "email", "number", "endereco", "cidade", "cep", "estado", "descricao", "animal", "aprovado"]:
            valor = getattr(colab, campo)
            if valor is not None:
                setattr(colab_db, campo, valor)

        # Se o admin mudou o status de aprovação, atualiza status do animal
        if colab.aprovado is not None and colab.aprovado != aprovado_anterior:
            # Preferir animal_id (novo contrato)
            animal_id = colab.animal_id if colab.animal_id is not None else colab_db.animal_id

            if animal_id is not None:
                animal = db.query(AnimaisModel).filter(AnimaisModel.id == animal_id).first()
                if animal:
                    if colab.aprovado == "aprovado":
                        animal.status = "em_adocao"
                    elif colab.aprovado == "reprovado":
                        outros = db.query(ColabModel).filter(
                            ColabModel.animal_id == animal_id,
                            ColabModel.aprovado == "aprovado",
                            ColabModel.id != id
                        ).count()
                        if outros == 0:
                            animal.status = "disponivel"
            else:
                # legado: por nome
                nome_animal = colab.animal or animal_anterior
                if nome_animal:
                    animal = db.query(AnimaisModel).filter(AnimaisModel.nome == nome_animal).first()
                    if animal:
                        if colab.aprovado == "aprovado":
                            animal.status = "em_adocao"
                        elif colab.aprovado == "reprovado":
                            outros = db.query(ColabModel).filter(
                                ColabModel.animal == nome_animal,
                                ColabModel.aprovado == "aprovado",
                                ColabModel.id != id
                            ).count()
                            if outros == 0:
                                animal.status = "disponivel"


        db.commit()
        return {"mensagem": "colab atualizado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar colab: {str(e)}")


# =========================
# PATCH - MARCAR COMO ADOTADO
# =========================

@router.patch("/colabs/{id}/adotado")
def marcar_adotado(id: int, db: Session = Depends(get_db)):
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            raise HTTPException(status_code=404, detail="Colaborador não encontrado")

        colab_db.aprovado = "adotado"

        # Atualiza status do animal usando animal_id (novo) ou nome (legado)
        animal = None
        if colab_db.animal_id:
            animal = db.query(AnimaisModel).filter(AnimaisModel.id == colab_db.animal_id).first()
        elif colab_db.animal:
            animal = db.query(AnimaisModel).filter(AnimaisModel.nome == colab_db.animal).first()

        if animal:
            animal.status = "adotado"


        db.commit()
        return {"mensagem": "adoção confirmada com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao confirmar adoção: {str(e)}")


# =========================
# DELETE - DELETAR COLAB
# =========================

@router.delete("/colabs/{id}")
def deletar_colab(id: int, db: Session = Depends(get_db)):
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            raise HTTPException(status_code=404, detail="Colaborador não encontrado")
        db.delete(colab_db)
        db.commit()
        return {"mensagem": "colab deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao deletar colab: {str(e)}")