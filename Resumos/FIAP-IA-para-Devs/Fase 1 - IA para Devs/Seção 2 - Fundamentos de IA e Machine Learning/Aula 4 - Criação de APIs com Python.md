# Aula 4 - Criação de APIs com Python

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula aborda a **criação de APIs (interfaces de programação de aplicações)** em Python com os dois frameworks mais usados: **Flask** e **FastAPI**. Inclui extensões do Flask (ex.: **Flask-SQLAlchemy** para integração com banco de dados), **Blueprints** para organização de rotas em projetos maiores, e no FastAPI o uso de **Pydantic** (validação automática de dados com `BaseModel`), **dependências** (Depends) e **autenticação OAuth2** (OAuth2PasswordBearer, rotas protegidas). Ao final, você saberá escolher entre Flask e FastAPI e implementar endpoints, validação e autenticação básica.

**Objetivos de aprendizagem:**
- Entender o papel de uma API na conexão entre sistemas e serviços.
- Criar aplicação Flask com extensões (ex.: SQLAlchemy) e Blueprints.
- Criar aplicação FastAPI com modelos Pydantic e validação automática.
- Usar dependências e autenticação por token (OAuth2) no FastAPI.

---

## Conceitos-chave (flashcards)

**P:** O que é uma API no contexto desta aula?  
**R:** Interface de programação de aplicações: conjunto de endpoints (rotas) que permitem que sistemas se comuniquem (ex.: cliente consome dados ou envia comandos) sem precisar conhecer a implementação interna.

**P:** O que o Flask-SQLAlchemy oferece?  
**R:** Integração do SQLAlchemy com o Flask; configuração do banco via `app.config['SQLALCHEMY_DATABASE_URI']`; objeto `db` para modelos (db.Model) e operações (db.create_all, sessões).

**P:** Para que servem os Blueprints no Flask?  
**R:** Agrupar rotas e views relacionadas (ex.: autenticação); registrar no app com `url_prefix`; organizar projetos grandes (ex.: `/auth/login` via blueprint `auth_bp`).

**P:** O que é o Pydantic no FastAPI?  
**R:** Biblioteca de validação de dados; modelos herdando de `BaseModel` definem a estrutura esperada da requisição/resposta; FastAPI valida automaticamente e gera documentação (OpenAPI).

**P:** Como proteger uma rota no FastAPI com token? **R:** Usar `OAuth2PasswordBearer` e uma dependência (ex.: `get_current_user`) que valida o token e retorna o usuário; declarar a dependência no endpoint com `Depends(get_current_user)`.

---

## Flask: pontos principais

- **Simplicidade e flexibilidade:** microframework; rotas com `@app.route()`; retorno de JSON ou templates.
- **Extensões:** Flask-SQLAlchemy (ORM e configuração do DB), Flask-JWT, Flask-CORS etc.
- **Configuração:** `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'`; criação do objeto `db = SQLAlchemy(app)`.
- **Modelos:** classes herdando de `db.Model` (colunas id, username, etc.); representam tabelas.
- **Blueprints:** criar `Blueprint('auth_bp', __name__)`; definir rotas no blueprint; registrar com `app.register_blueprint(auth_bp, url_prefix='/auth')`.

---

## FastAPI: pontos principais

- **Modernidade:** construído sobre Starlette; assíncrono; documentação automática (Swagger/OpenAPI).
- **Pydantic:** classes que herdam de `BaseModel`; atributos com tipo (name: str, price: float, description: str | None = None); validação automática de entrada e saída.
- **Dependências:** `Depends(função)` injeta resultado da função nos parâmetros do endpoint (ex.: usuário atual, sessão de DB).
- **OAuth2:** `OAuth2PasswordBearer(tokenUrl="token")`; dependência que lê o token do header, valida e retorna o usuário; rotas que precisam de login usam `Depends(get_current_user)`.
- **HTTPException:** para retornar códigos de erro (401, 404, 422) e mensagens padronizadas.

---

## Comparação rápida

| Aspecto        | Flask              | FastAPI                    |
|----------------|--------------------|----------------------------|
| Estilo         | Síncrono, minimal  | Assíncrono, orientado a API|
| Validação      | Manual ou libs     | Pydantic nativo            |
| Documentação   | Opcional           | OpenAPI automática         |
| Performance    | Boa                | Muito boa (async)          |
| Uso típico     | Web full, APIs simples | APIs REST modernas, ML   |

---

## Mapa conceitual

```
APIs com Python
├── Flask
│   ├── Rotas, app.config
│   ├── Extensões (Flask-SQLAlchemy)
│   ├── Modelos db.Model
│   └── Blueprints (organização)
└── FastAPI
    ├── BaseModel (Pydantic)
    ├── Depends (dependências)
    ├── OAuth2PasswordBearer
    └── HTTPException
```

---

## Receita prática

1. **Escolher framework:** Flask para apps web tradicionais ou APIs simples; FastAPI para APIs REST com validação forte e documentação automática.
2. **Flask:** instalar Flask e extensões; definir modelos se usar DB; usar Blueprints se o projeto crescer.
3. **FastAPI:** definir modelos Pydantic para request/response; usar `Depends` para autenticação e injeção; testar via `/docs`.
4. **Segurança:** nunca deixar credenciais no código; usar variáveis de ambiente e tokens para OAuth2.

---

## Perguntas para teste de reforço

1. O que é um Blueprint no Flask? **R:** Mecanismo para agrupar rotas e views em módulos; permite prefixo de URL (ex.: /auth) e organização em projetos grandes.
2. Para que o Pydantic é usado no FastAPI? **R:** Definir e validar a estrutura dos dados de entrada e saída (request/response); gera documentação e erros de validação automáticos.
3. Como uma rota no FastAPI sabe quem é o usuário autenticado? **R:** Através de uma dependência (ex.: get_current_user) que lê o token OAuth2 e retorna o usuário; o endpoint declara `Depends(get_current_user)`.
4. Cite uma vantagem do FastAPI em relação ao Flask para APIs. **R:** Validação automática com Pydantic; documentação OpenAPI/Swagger gerada automaticamente; suporte nativo a async.
5. O que o Flask-SQLAlchemy simplifica? **R:** A integração do SQLAlchemy com o app Flask (configuração do DB, criação de modelos e sessões vinculadas ao app).

---

## Materiais de apoio

- Flask: [flask.palletsprojects.com](https://flask.palletsprojects.com)  
- FastAPI: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)  
- Pydantic: [docs.pydantic.dev](https://docs.pydantic.dev)  
- OAuth2 em FastAPI: documentação oficial (Security).
