"""Script para limpar e repopular o banco de dados com animais com imagens"""
from database.connection import SessionLocal
from database.models import AnimaisModel
from sqlalchemy import text

ANIMAIS_PADRAO = [
    {"nome":"Ben","especie":"cachorro","genero":"macho","idade":"Idoso","regiao":"MG","ong":"Amparo pet","cidade":"Uberlândia","imagem":"Assets/Doguinhos/Machos/Ben_I.png"},
    {"nome":"Babi","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"MG","ong":"Cão Viver","cidade":"Contagem","imagem":"Assets/Doguinhos/Femeas/Babi_F.png"},
    {"nome":"Beto","especie":"cachorro","genero":"macho","idade":"Idoso","regiao":"MG","ong":"Amparo pet","cidade":"Uberlândia","imagem":"Assets/Doguinhos/Machos/Beto_I.png"},
    {"nome":"Bebel","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"RJ","ong":"Ação animal","cidade":"Rio de Janeiro","imagem":"Assets/Doguinhos/Femeas/Bebel_A.png"},
    {"nome":"Bob","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"RJ","ong":"Distrito Animal","cidade":"Rio de Janeiro","imagem":"Assets/Doguinhos/Machos/Bob_A.png"},
    {"nome":"Bella","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"MG","ong":"Apa","cidade":"Uberlândia","imagem":"Assets/Doguinhos/Femeas/Bella_A.png"},
    {"nome":"Caos","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Doguinhos/Machos/Caos_A.png"},
    {"nome":"Collie","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Doguinhos/Femeas/Collie_F.png"},
    {"nome":"Chocolate","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"RJ","ong":"Adote um Bichinho","cidade":"Itaguaí","imagem":"Assets/Doguinhos/Machos/Chocolate_A.png"},
    {"nome":"Jade","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"RJ","ong":"Adote um Bichinho","cidade":"Itaguaí","imagem":"Assets/Doguinhos/Femeas/Jade_F.png"},
    {"nome":"Cirius","especie":"cachorro","genero":"macho","idade":"Filhote","regiao":"SP","ong":"Alianima","cidade":"Bela vista","imagem":"Assets/Doguinhos/Machos/Cirius_F.png"},
    {"nome":"Lindinha","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"SP","ong":"Amor animal","cidade":"Marília","imagem":"Assets/Doguinhos/Femeas/Lindinha_F.png"},
    {"nome":"Dante","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"SP","ong":"Amor animal","cidade":"Marília","imagem":"Assets/Doguinhos/Machos/Dante_A.png"},
    {"nome":"Luna","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"MG","ong":"Apa","cidade":"Uberlândia","imagem":"Assets/Doguinhos/Femeas/Luna_F.png"},
    {"nome":"Fred","especie":"cachorro","genero":"macho","idade":"Filhote","regiao":"RJ","ong":"Adote um Bichinho","cidade":"Itaguaí","imagem":"Assets/Doguinhos/Machos/Fred_F.png"},
    {"nome":"Malu","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"SP","ong":"Alianima","cidade":"Bela vista","imagem":"Assets/Doguinhos/Femeas/Malu_F.png"},
    {"nome":"Hamlet","especie":"cachorro","genero":"macho","idade":"Filhote","regiao":"SP","ong":"Alianima","cidade":"Bela vista","imagem":"Assets/Doguinhos/Machos/Hamelet_F.png"},
    {"nome":"Mel","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"GO","ong":"Anjos da rua","cidade":"Goiânia","imagem":"Assets/Doguinhos/Femeas/Mel_A.png"},
    {"nome":"Kratus","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"GO","ong":"Anjos da rua","cidade":"Goiânia","imagem":"Assets/Doguinhos/Machos/Kratus_A.png"},
    {"nome":"Panqueca","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"RJ","ong":"Fazenda Modelo","cidade":"Guaratiba","imagem":"Assets/Doguinhos/Femeas/Panqueca_A.png"},
    {"nome":"Nacho","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"GO","ong":"Lar dos animais","cidade":"Goiânia","imagem":"Assets/Doguinhos/Machos/Nacho_A.png"},
    {"nome":"Tamires","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"GO","ong":"Anjos da rua","cidade":"Goiânia","imagem":"Assets/Doguinhos/Femeas/Tamires_A.png"},
    {"nome":"Thor","especie":"cachorro","genero":"macho","idade":"Adulto","regiao":"GO","ong":"Anjos da rua","cidade":"Goiânia","imagem":"Assets/Doguinhos/Machos/Thor_A.png"},
    {"nome":"Zoe","especie":"cachorro","genero":"femea","idade":"Filhote","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Doguinhos/Femeas/Zoe_F.png"},
    {"nome":"Zeus","especie":"cachorro","genero":"macho","idade":"Filhote","regiao":"SP","ong":"Amor animal","cidade":"Marília","imagem":"Assets/Doguinhos/Machos/Zeus_F.png"},
    {"nome":"Paçoca","especie":"cachorro","genero":"femea","idade":"Adulto","regiao":"SP","ong":"Amor Animal","cidade":"Marília","imagem":"Assets/Doguinhos/Femeas/Paçoca_A.png"},
    {"nome":"Cookie","especie":"gato","genero":"macho","idade":"Filhote","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Miaus/Machos/Cookie_F.png"},
    {"nome":"Café","especie":"gato","genero":"femea","idade":"Adulto","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Miaus/Femeas/Cafe_A.png"},
    {"nome":"Coxinha","especie":"gato","genero":"macho","idade":"Idoso","regiao":"MG","ong":"Apa","cidade":"Uberlândia","imagem":"Assets/Miaus/Machos/Coxinha_I.png"},
    {"nome":"Faisca","especie":"gato","genero":"femea","idade":"Adulto","regiao":"SP","ong":"Amor animal","cidade":"Marília","imagem":"Assets/Miaus/Femeas/Faisca_A.png"},
    {"nome":"Felix","especie":"gato","genero":"macho","idade":"Filhote","regiao":"SP","ong":"Alianima","cidade":"Bela vista","imagem":"Assets/Miaus/Machos/Felix_F.png"},
    {"nome":"Flora","especie":"gato","genero":"femea","idade":"Adulto","regiao":"MG","ong":"Bichos Gerais","cidade":"Belo Horizonte","imagem":"Assets/Miaus/Femeas/Flora_A.png"},
    {"nome":"Garfield","especie":"gato","genero":"macho","idade":"Adulto","regiao":"RJ","ong":"Fazenda Modelo","cidade":"Guaratiba","imagem":"Assets/Miaus/Machos/Garfield_A.png"},
    {"nome":"Kitty","especie":"gato","genero":"femea","idade":"Adulto","regiao":"RJ","ong":"Fazenda modelo","cidade":"Guaratiba","imagem":"Assets/Miaus/Femeas/Kitty_A.png"},
    {"nome":"Gatito","especie":"gato","genero":"macho","idade":"Filhote","regiao":"RJ","ong":"Cãodominio","cidade":"Resende","imagem":"Assets/Miaus/Machos/Gatito_F.png"},
    {"nome":"Luz","especie":"gato","genero":"femea","idade":"Adulto","regiao":"SP","ong":"Ong SOS","cidade":"São Caetano do Sul","imagem":"Assets/Miaus/Femeas/Luz_A.png"},
    {"nome":"Mingau","especie":"gato","genero":"macho","idade":"Filhote","regiao":"MG","ong":"Apa","cidade":"Uberlândia","imagem":"Assets/Miaus/Machos/Mingau_F.png"},
    {"nome":"Maya","especie":"gato","genero":"femea","idade":"Adulto","regiao":"MG","ong":"Bichos gerais","cidade":"Belo Horizonte","imagem":"Assets/Miaus/Femeas/Maya_A.png"},
    {"nome":"Nico","especie":"gato","genero":"macho","idade":"Adulto","regiao":"GO","ong":"Anjos da rua","cidade":"Goiânia","imagem":"Assets/Miaus/Machos/Nico_A.png"},
    {"nome":"Moon","especie":"gato","genero":"femea","idade":"Adulto","regiao":"SP","ong":"Ong SOS","cidade":"São Caetano do Sul","imagem":"Assets/Miaus/Femeas/Moon_A.png"},
    {"nome":"Ozzy","especie":"gato","genero":"macho","idade":"Filhote","regiao":"SP","ong":"Alianima","cidade":"Bela vista","imagem":"Assets/Miaus/Machos/Ozzy_F.png"},
    {"nome":"Pixie","especie":"gato","genero":"femea","idade":"Adulto","regiao":"SP","ong":"Amor animal","cidade":"Marília","imagem":"Assets/Miaus/Femeas/Pixie_A.png"},
    {"nome":"Zoe","especie":"gato","genero":"femea","idade":"Adulto","regiao":"GO","ong":"Lar dos animais","cidade":"Goiânia","imagem":"Assets/Miaus/Femeas/Zoe_A.png"},
]

db = SessionLocal()
try:
    # Deletar todos os animais
    db.execute(text("DELETE FROM animais"))
    db.commit()
    print("✓ Tabela de animais limpa")
    
    # Inserir novos
    for animal in ANIMAIS_PADRAO:
        novo = AnimaisModel(**animal, status="disponivel")
        db.add(novo)
    db.commit()
    print(f"✓ {len(ANIMAIS_PADRAO)} animais adicionados")
    
    # Verificar
    count = db.query(AnimaisModel).count()
    primeira = db.query(AnimaisModel).first()
    print(f"\n📊 Total: {count} animais")
    print(f"🖼️  Primeira imagem: {primeira.imagem}")
finally:
    db.close()
