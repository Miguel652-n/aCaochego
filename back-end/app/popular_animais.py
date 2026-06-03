from database.connection import SessionLocal
from database.models import Animal

db = SessionLocal()

animais = [

]

for animal in animais:

    novo = Animal(**animal)

    db.add(novo)

db.commit()

db.close()

print("Animais adicionados com sucesso!")