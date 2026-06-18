import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
 
# Carrega variáveis de ambiente do arquivo .env, se existir.
load_dotenv(Path(__file__).resolve().parent / ".env")

# Use DATABASE_URL do ambiente quando disponível.
DATABASE_URL = os.environ.get("DATABASE_URL")

# Para desenvolvimento local, usa um banco SQLite simples.
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./local.db"

# O SQLAlchemy 2.x exige "postgresql://" em vez de "postgres://".
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
 
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
Base = declarative_base()