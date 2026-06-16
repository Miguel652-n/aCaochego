import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
 
# Railway injeta a variável DATABASE_URL automaticamente quando você
# adiciona um banco PostgreSQL ao projeto.
DATABASE_URL = "postgresql://postgres:BCYODXbIhzkvhHDepTVGuHnyrrtAnLMu@postgres.railway.internal:5432/railway"

# O Railway às vezes fornece a URL com "postgres://" (formato antigo),
# mas o SQLAlchemy 2.x exige "postgresql://". A linha abaixo corrige isso.
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
 
engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
Base = declarative_base()