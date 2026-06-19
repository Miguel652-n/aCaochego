from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class AnimaisModel(Base):

    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especie = Column(String)
    genero = Column(String)
    idade = Column(String)
    regiao = Column(String)
    ong = Column(String)
    cidade = Column(String)
    imagem = Column(String)
    # disponivel | em_adocao | adotado
    status = Column(String, default="disponivel")


class ColabModel(Base):

    __tablename__ = "colabs"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)
    email = Column(String)
    number = Column(String)
    endereco = Column(String)
    cidade = Column(String)
    cep = Column(String)
    estado = Column(String)
    descricao = Column(String)

    # animal_id refere-se a AnimaisModel.id
    animal_id = Column(Integer, nullable=True, index=True)

    # compatibilidade (legado): guarda também o nome do animal quando fornecido
    animal = Column(String, nullable=True)

    # aprovado | reprovado | pendente | adotado
    aprovado = Column(String, default="pendente")
    analise_ia = Column(String)

