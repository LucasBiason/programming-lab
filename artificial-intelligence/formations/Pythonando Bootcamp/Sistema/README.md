# Bloco 2 — Construção da base (Jury AI)

Projeto **Jury AI** — base do sistema em Django, seguindo o roteiro do Notion _Construção da base_.

## Roteiro

Ver **ROTEIRO.md** para a ordem de execução.

**Links Notion (tutoriais):** [Construção da base](https://grizzly-amaranthus-f6a.notion.site/Constru-o-da-base-2fb6cf8ea89f80b4b118cf36f5c2aa51) · [Funcionalidades com IA](https://grizzly-amaranthus-f6a.notion.site/Funcionalidades-com-IA-2fc6cf8ea89f80d18000dfac39b15b46) · [RAG — Arquivos da aula](https://www.notion.so/RAG-Arquivos-da-aula-300962a7693c81a69264ed1c73e4ac5d). Para o Notion MCP extrair conteúdo: compartilhe as páginas com a integração — ver **[docs/NOTION_BOOTCAMP.md](./docs/NOTION_BOOTCAMP.md)**. Cópia local: **[docs/FUNCIONALIDADES_COM_IA.md](./docs/FUNCIONALIDADES_COM_IA.md)**. **Conferência transcrição vs implementação:** [docs/CONFERENCIA_TRANSCRICAO_BLOCO2.md](./docs/CONFERENCIA_TRANSCRICAO_BLOCO2.md).

**Figma (design Arcane-3):** [Arcane-3](https://www.figma.com/design/4IF8seRuIodeRCwlzJg8GO/Arcane-3?node-id=0-1). Screenshots para referência em **[docs/figma_captures/](./docs/figma_captures/)** (capturados via Playwright — `python3 scripts/capture_figma_playwright.py`).

### Análise e resumo (transcrição 07/02)

- **[ANALISE_BLOCO2_PARTE1.md](./ANALISE_BLOCO2_PARTE1.md)** — Primeira análise: o que a transcrição do Dia 1 traz sobre o Jury AI, cronograma, stack e ligação Bloco 1 (RAG) → Bloco 2.
- **[RESUMO_BLOCO2_PARTE1.md](./RESUMO_BLOCO2_PARTE1.md)** — Primeira parte do resumo study-summary-rich (Resumo Executivo, Conceitos-Chave, Mapa, Receita, Diagrama Mermaid, Perguntas de Reforço).
- **[CODIGOS_BLOCO2.md](./CODIGOS_BLOCO2.md)** — Códigos do período: `config/urls.py`, `settings/base.py`, apps `users` e `clientes` (models, views, serializers, urls), `core/views.py`, `requirements.txt` e tabela de endpoints.

## Estrutura

- `jury_ai/` — projeto Django (config, apps: users, clientes, documents, chat, whatsapp, core)
- `jury_ai/static/jury_ai/images/` — imagens do roteiro (logo JURI.AI, banner, assistente virtual, avatar)
- **CONSTRUCAO_DA_BASE.md** — roteiro e checklist do Notion (mapeamento URLs, imagens)
- **ROTEIRO.md** — ordem de execução (Teoria → Config → Cadastro → … → Config empresas)
- **docs/ARQUITETURA.md** — diagramas (componentes, fluxo WhatsApp, chat, RAG)
- **docs/apps-\*.md** — documentação por app (chat, clientes, whatsapp, documents)

O código do Bloco 2 tem as mesmas funcionalidades do **arcabe3-completo**, revisado pelos padrões do **cursor-multiagent-system** (Ruff, uma classe por arquivo, CHANGELOG, migrations intocadas). Ver `.cursor/rules/padroes-programacao.mdc` na raiz do Bootcamp.

## Setup

```bash
cd "Bloco 2"
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env       # Ajuste SECRET_KEY, OPENAI_API_KEY
cd jury_ai
python manage.py migrate
python manage.py createsuperuser   # opcional
python manage.py runserver
```

Abra **http://127.0.0.1:8000/** no navegador para ver o **frontend** do roteiro:

- **/** — Início (Entrar / Criar conta)
- **/login/** — Login - Usuários
- **/cadastro/** — Cadastro - Usuários
- **/clientes/** — Clientes - Usuários (lista, novo, editar, excluir)
- **/clientes/<id>/** — Cliente - Usuários (detalhe/edição)
- **/documentos/** — Documentos - IA (OCR na API)
- **/chat/** — Chat - IA (agente geral + análise jurisprudência na API)
- **/config-empresas/** — Config empresas (placeholder)

**APIs — Funcionalidades com IA:** [docs/FUNCIONALIDADES_COM_IA.md](./docs/FUNCIONALIDADES_COM_IA.md). Resumo: `POST /api/documents/ocr/`, `POST /api/chat/`, `POST /api/chat/analise-jurisprudencia/`, `POST /api/whatsapp/webhook/`.

## Como executar (testes rápidos)

Com o servidor rodando (`python manage.py runserver` em `jury_ai/`):

**1. Cadastro**

```bash
curl -X POST http://127.0.0.1:8000/api/auth/cadastro/ \
  -H "Content-Type: application/json" \
  -d '{"email":"seu@email.com","username":"seuuser","first_name":"Nome","last_name":"Sobrenome","password":"senha1234","password_confirm":"senha1234"}'
```

**2. Login** (retorna `access` e `refresh` para usar nas próximas requisições)

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"seu@email.com","password":"senha1234"}'
```

**3. Listar / criar clientes** (use o token em `Authorization: Bearer <access>`)

```bash
curl http://127.0.0.1:8000/api/clientes/ -H "Authorization: Bearer SEU_ACCESS_TOKEN"
curl -X POST http://127.0.0.1:8000/api/clientes/ -H "Authorization: Bearer SEU_ACCESS_TOKEN" \
  -H "Content-Type: application/json" -d '{"nome":"Cliente Exemplo","email":"cliente@exemplo.com"}'
```

## Apps

| App         | Descrição                                                              |
| ----------- | ---------------------------------------------------------------------- |
| `users`     | Cadastro, login, custom user (email como USERNAME_FIELD)               |
| `clientes`  | CRUD de clientes, Documentos, DadosEmpresa                             |
| `documents` | Upload, OCR (Docling), conteúdo para RAG e análise jurisprudencial     |
| `chat`      | Pergunta, ContextRag, AnaliseJurisprudencia; agente agno, streaming    |
| `whatsapp`  | Webhook Evolution API, SecretariaAI, envio de resposta                 |
| `core`      | Views de páginas (index, login, cadastro, clientes, documentos, chat…) |

## Documentação Postman

A API está documentada em **Postman** para importação e testes.

| Arquivo                    | Descrição                                                                   |
| -------------------------- | --------------------------------------------------------------------------- |
| `postman/collection.json`  | Collection com todos os endpoints (Auth, Clientes, Documentos, Chat)        |
| `postman/environment.json` | Environment local (`base_url`, `user_email`, `user_password`, `cliente_id`) |

**Importar no Postman:** File → Import → escolha `postman/collection.json` e `postman/environment.json`. Selecione o environment "Jury AI - Local" e use as variáveis `base_url`, `user_email`, `user_password`.

**Executar testes (Newman):** Com o servidor rodando (`python manage.py runserver` em `jury_ai/`):

```bash
./scripts/run_newman.sh
# ou: npx newman run postman/collection.json -e postman/environment.json --reporters cli
```

Relatórios (quando usar `run_newman.sh` com reporters html/junit): `reports/postman/report.html` e `reports/postman/junit-results.xml`.

## Atualizar conteúdo do Notion (Funcionalidades com IA)

Se a página do Notion for alterada e você quiser atualizar a cópia local sem depender do navegador (evita bloqueio por extensões):

```bash
pip install playwright
playwright install chromium
python3 scripts/fetch_notion_with_playwright.py
```

O conteúdo é salvo em **docs/FUNCIONALIDADES_COM_IA.md** (possíveis API keys são redactadas).

## Lint e verificação

```bash
cd jury_ai
python manage.py check          # Django system check
ruff check .                   # Lint (instale ruff: pip install ruff)
ruff format .                  # Formato (opcional: ruff format .)
```

## Próximos passos (após a base)

- Documentos: upload, transcrição, RAG (reuso do Bloco 1).
- Chat: integração com LLM/agente.
- Config empresas: dados do escritório.
- Integrações: DataJude, Evolution API (WhatsApp), Google Calendar.
