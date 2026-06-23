import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

# Se a variável não existir, gera um erro claro
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL não foi encontrada. Verifique se o PostgreSQL está conectado ao serviço Backend no Railway."
    )

# Compatibilidade com URLs antigas
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1
    )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()