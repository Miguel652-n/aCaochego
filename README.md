# 🐾 aCãochego

O **aCãochego** é uma plataforma web desenvolvida para conectar pessoas interessadas em adoção de animais com ONGs e protetores independentes. O projeto busca facilitar o processo de adoção responsável, além de incentivar a colaboração da comunidade em causas animais.

---

## 📋 Funcionalidades

### Para visitantes
- Visualização de animais disponíveis para adoção;
- Filtro e busca de animais;
- Informações sobre ONGs parceiras;
- Formulário para colaboração e ajuda à causa;
- Interface responsiva para desktop e dispositivos móveis.

### Para administração
- Cadastro de animais para adoção;
- Edição de informações dos animais;
- Remoção de animais cadastrados;
- Gerenciamento de colaboradores.

---

## 🛠️ Tecnologias Utilizadas

### Front-end
- HTML5
- CSS3
- JavaScript

### Back-end
- Python
- FastAPI

### Banco de Dados
- SQLite
- SQLAlchemy

---

## 📂 Estrutura do Projeto

```bash
aCaochego/
│
├── front-end/
│   └── public/
│       ├── index.html
│       ├── admin.html
│       ├── formulario.html
│       ├── ONGs.html
│       ├── script.js
│       ├── admin.js
│       ├── form.js
│       └── Assets/
│
├── back-end/
│   └── app/
│       ├── main.py
│       ├── routes/
│       │   ├── animais.py
│       │   └── colab.py
│       ├── database/
│       │   ├── connection.py
│       │   └── models.py
│       └── requirements.txt
│
└── README.md
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/aCaochego.git
```

### 2. Acessar a pasta do backend

```bash
cd aCaochego/back-end/app
```

### 3. Criar ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Iniciar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```bash
http://localhost:8000
```

Documentação automática:

```bash
http://localhost:8000/docs
```

---

## 🔗 Principais Rotas da API

### Animais

| Método | Rota | Descrição |
|----------|----------|----------|
| GET | /animais | Listar animais |
| POST | /animais | Cadastrar animal |
| PATCH | /animais/{id} | Atualizar animal |
| DELETE | /animais/{id} | Remover animal |

### Colaboradores

| Método | Rota | Descrição |
|----------|----------|----------|
| GET | /colabs | Listar colaboradores |
| POST | /colabs | Cadastrar colaborador |
| PATCH | /colabs/{id} | Atualizar colaborador |
| DELETE | /colabs/{id} | Remover colaborador |

---

## 🎯 Objetivo do Projeto

O projeto foi desenvolvido com o propósito de:

- Incentivar a adoção responsável;
- Dar visibilidade a animais que procuram um lar;
- Facilitar a comunicação entre ONGs e adotantes;
- Centralizar informações sobre adoção e colaboração.

---

## 👨‍💻 Equipe

Projeto desenvolvido para fins acadêmicos e de aprendizado em desenvolvimento web Full Stack.

---

## 📄 Licença

Este projeto é destinado para fins educacionais.
