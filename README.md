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

### Inteligência Artificial

* Sistema de análise automática de candidatos
* Classificação baseada em pontuação
* Processamento de texto em linguagem natural
* Recomendação automática para aprovação, reprovação ou pendência
* Estrutura preparada para futura integração com modelos de Machine Learning


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

## ☁️ Deploy no Railway

### 1. Backend

1. Criar um novo projeto no Railway.
2. Conectar o repositório GitHub.
3. Selecionar a pasta do backend.
4. Configurar as variáveis de ambiente.
5. O Railway detectará automaticamente o projeto Python.

Variáveis recomendadas:

```env
DATABASE_URL=postgresql://...
PORT=8080
```

### 2. Banco de Dados

1. Adicionar um serviço PostgreSQL no Railway.
2. Copiar a variável DATABASE_URL gerada.
3. Inserir essa variável no serviço do backend.

### 3. Frontend

1. Criar um novo serviço no Railway.
2. Conectar a pasta do frontend.
3. Configurar a URL da API:

```javascript
const API_URL = "https://seu-backend.up.railway.app";
```

4. Realizar o deploy.

### 4. Popular o Banco

Após o deploy do backend:

```bash
python popular_animais.py
```

O script enviará os animais para o banco PostgreSQL hospedado no Railway.

### 5. Atualizações

Após qualquer alteração:

```bash
git add .
git commit -m "descrição da alteração"
git push
```

O Railway realizará o redeploy automaticamente.

---

## 🎯 Objetivos do Projeto

* Incentivar a adoção responsável
* Facilitar o contato entre adotantes e ONGs
* Organizar o processo de adoção
* Reduzir o trabalho manual de análise
* Promover o bem-estar animal

---

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para estudo de desenvolvimento web, APIs REST, banco de dados e automação de processos de adoção animal.

---

## ❤️ Missão

Conectar animais que precisam de um lar a pessoas dispostas a oferecer cuidado, segurança e carinho.
