# uvicorn app.main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.colab import router as colab_router
from app.routes.animais import router as animais_router

from app.database.connection import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(colab_router)
app.include_router(animais_router)

@app.get("/")
def home():
    return {"mensagem": "Backend funcionando"}