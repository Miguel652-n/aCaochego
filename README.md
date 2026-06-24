# 🐾 AçãoChego

Sistema web para adoção responsável de animais desenvolvido com FastAPI, PostgreSQL e JavaScript.

## 📖 Sobre o Projeto

O **AçãoChego** é uma plataforma criada para conectar pessoas interessadas em adotar animais a ONGs e instituições de proteção animal.

O sistema permite visualizar animais disponíveis para adoção, enviar solicitações de interesse e acompanhar o processo de adoção de forma organizada.

Além disso, conta com um painel administrativo que auxilia na gestão dos candidatos e utiliza uma análise automatizada para apoiar a tomada de decisão durante o processo de adoção.

---

## ✨ Funcionalidades

### Usuários

* Visualização de animais disponíveis para adoção
* Filtros por espécie, idade, gênero e região
* Formulário de interesse em adoção
* Consulta de animais disponíveis em tempo real

### Administração

* Login administrativo
* Visualização de todos os candidatos
* Aprovação de solicitações
* Reprovação de solicitações
* Retorno para status pendente
* Confirmação de adoção concluída
* Exclusão de solicitações

### Controle de Status

Os animais podem possuir os seguintes status:

| Status      | Descrição                           |
| ----------- | ----------------------------------- |
| Disponível  | Animal disponível para adoção       |
| Em processo | Existe uma solicitação em andamento |
| Adotado     | Processo concluído com sucesso      |

### Análise Automatizada

O sistema realiza uma análise automática do texto informado pelo candidato durante a solicitação de adoção.

A análise gera:

* Pontuação automática
* Justificativa textual
* Recomendação de aprovação, reprovação ou pendência

A decisão final continua sendo realizada pelo administrador.

---

## 🛠 Tecnologias Utilizadas

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla JS)

### Backend

* FastAPI
* Python

### Banco de Dados

* PostgreSQL
* SQLAlchemy ORM

### Hospedagem

* Railway

---

## 📂 Estrutura do Projeto

```text
aCaochego/
│
├── back-end/
│   ├── app/
│   │   ├── database/
│   │   ├── routes/
│   │   ├── main.py
│   │   └── popular_animais.py
│   │
│   └── requirements.txt
│
├── front-end/
│   └── public/
│       ├── Assets/
│       ├── admin.html
│       ├── admin.js
│       ├── admin.css
│       └── demais páginas
│
└── README.md
```

---

## 🚀 Como Executar Localmente

### 1. Clonar o projeto

```bash
git clone <url-do-repositorio>
cd aCaochego
```

### 2. Backend

```bash
cd back-end

pip install -r requirements.txt
```

Executar:

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

---

### 3. Frontend

Abra os arquivos HTML localmente ou utilize uma extensão como Live Server.

---

## 📡 Principais Endpoints

### Animais

```http
GET /animais
```

Lista todos os animais cadastrados.

---

### Solicitações de Adoção

```http
GET /colabs
```

Lista todos os candidatos.

```http
POST /colabs
```

Cria uma nova solicitação.

```http
PATCH /colabs/{id}
```

Atualiza status da solicitação.

```http
PATCH /colabs/{id}/adotado
```

Confirma adoção concluída.

```http
DELETE /colabs/{id}
```

Remove uma solicitação.

---

## 🎯 Objetivos do Projeto

* Incentivar a adoção responsável
* Facilitar o contato entre adotantes e ONGs
* Organizar o processo de adoção
* Reduzir o trabalho manual de análise
* Promover o bem-estar animal

---

## 🔮 Melhorias Futuras

* Sistema de autenticação com JWT
* Upload de imagens pelo painel administrativo
* Histórico completo de adoções
* Dashboard com métricas
* Integração com IA generativa
* Notificações por e-mail
* Área exclusiva para ONGs

---

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para estudo de desenvolvimento web, APIs REST, banco de dados e automação de processos de adoção animal.

---

## ❤️ Missão

Conectar animais que precisam de um lar a pessoas dispostas a oferecer cuidado, segurança e carinho.
