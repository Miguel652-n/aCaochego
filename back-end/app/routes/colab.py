import os
import json
import httpx

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.database.connection import SessionLocal
from app.database.models import ColabModel, AnimaisModel

router = APIRouter()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1
    )


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
    aprovado: Optional[str] = None


# =========================
# ANÁLISE DE APTIDÃO COM IA
# =========================

def analisar_aptidao(descricao: str, nome_animal: Optional[str]) -> dict:
    """Chama a API da Anthropic para analisar se o colaborador é apto a adotar."""

    if not DATABASE_URL:
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
                "x-api-key": DATABASE_URL,
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
def listar_colabs():
    db = SessionLocal()
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
                "animal": c.animal,
                "aprovado": c.aprovado or "pendente",
                "analise_ia": c.analise_ia or ""
            }
            for c in colabs
        ]
    finally:
        db.close()


# =========================
# POST - CRIAR COLAB
# =========================

@router.post("/colabs")
def criar_colab(colab: Colab):
    db = SessionLocal()
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
            animal=colab.animal,
            aprovado=resultado["aprovado"],
            analise_ia=resultado["analise"]
        )

        db.add(novo_colab)

        # Se aprovado e tem animal, muda status do animal para "em_adocao"
        if resultado["aprovado"] == "aprovado" and colab.animal:
            animal = db.query(AnimaisModel).filter(
                AnimaisModel.nome == colab.animal
            ).first()
            if animal:
                animal.status = "em_adocao"

        db.commit()

        return {
            "mensagem": "Colaborador adicionado",
            "aprovado": resultado["aprovado"],
            "analise_ia": resultado["analise"]
        }

    finally:
        db.close()


# =========================
# PATCH - ATUALIZAR COLAB
# =========================

@router.patch("/colabs/{id}")
def atualizar_colab(id: int, colab: ColabUpdate):
    db = SessionLocal()
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            return {"erro": "colab não encontrado"}

        animal_anterior = colab_db.animal
        aprovado_anterior = colab_db.aprovado

        for campo in ["nome", "email", "number", "endereco", "cidade", "cep", "estado", "descricao", "animal", "aprovado"]:
            valor = getattr(colab, campo)
            if valor is not None:
                setattr(colab_db, campo, valor)

        # Se o admin mudou o status de aprovação, atualiza status do animal
        if colab.aprovado is not None and colab.aprovado != aprovado_anterior:
            nome_animal = colab.animal or animal_anterior
            if nome_animal:
                animal = db.query(AnimaisModel).filter(AnimaisModel.nome == nome_animal).first()
                if animal:
                    if colab.aprovado == "aprovado":
                        animal.status = "em_adocao"
                    elif colab.aprovado == "reprovado":
                        # Verifica se ainda tem outro colab aprovado para esse animal
                        outros = db.query(ColabModel).filter(
                            ColabModel.animal == nome_animal,
                            ColabModel.aprovado == "aprovado",
                            ColabModel.id != id
                        ).count()
                        if outros == 0:
                            animal.status = "disponivel"

        db.commit()
        return {"mensagem": "colab atualizado"}

    finally:
        db.close()


# =========================
# PATCH - MARCAR COMO ADOTADO
# =========================

@router.patch("/colabs/{id}/adotado")
def marcar_adotado(id: int):
    db = SessionLocal()
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            return {"erro": "colab não encontrado"}

        colab_db.aprovado = "adotado"

        if colab_db.animal:
            animal = db.query(AnimaisModel).filter(AnimaisModel.nome == colab_db.animal).first()
            if animal:
                animal.status = "adotado"

        db.commit()
        return {"mensagem": "adoção confirmada"}

    finally:
        db.close()


# =========================
# DELETE - DELETAR COLAB
# =========================

@router.delete("/colabs/{id}")
def deletar_colab(id: int):
    db = SessionLocal()
    try:
        colab_db = db.query(ColabModel).filter(ColabModel.id == id).first()
        if not colab_db:
            return {"erro": "colab não encontrado"}
        db.delete(colab_db)
        db.commit()
        return {"mensagem": "colab deletado com sucesso"}
    finally:
        db.close()