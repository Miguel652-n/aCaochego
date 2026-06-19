"""
Dependências comuns do FastAPI
"""
from app.database.connection import SessionLocal
from sqlalchemy.orm import Session


def get_db():
    """
    Dependency para injetar sessão de banco de dados nos endpoints.
    Garante que a conexão seja fechada automaticamente.
    
    Uso em endpoints:
    @router.get("/items")
    def listar_items(db: Session = Depends(get_db)):
        return db.query(ItemModel).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
