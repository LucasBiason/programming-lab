# Pythonando Bootcamp — Programação Web + IA

Projeto prático do Bootcamp de Programação Web + IA (07-08/02/2026).

## Índice geral

| Recurso                           | Descrição                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bloco 1**                       | RAG com LangChain e FAISS (PDF → embeddings → busca). Ver [Bloco 1/README.md](Bloco%201/README.md).                                                       |
| **Bloco 2**                       | Jury AI — Django, API REST, JWT, clientes, documentos, chat, WhatsApp. Ver [Bloco 2/README.md](Bloco%202/README.md).                                      |
| **CONSTRUCAO_DA_BASE**            | Roteiro da base (índice na raiz). Ver [CONSTRUCAO_DA_BASE.md](CONSTRUCAO_DA_BASE.md).                                                                     |
| **Bloco 2/CONSTRUCAO_DA_BASE.md** | Roteiro completo, mapeamento Notion ↔ URLs, decisões de paridade.                                                                                         |
| **Bloco 2/ROTEIRO.md**            | Ordem de execução (Teoria → Config → Cadastro → … → Config empresas).                                                                                     |
| **Bloco 2/docs/ARQUITETURA.md**   | Diagramas (componentes, webhook WhatsApp, chat, RAG).                                                                                                     |
| **Bloco 2/docs/apps-\*.md**       | Documentação por app (chat, clientes, whatsapp, documents).                                                                                               |
| **Amostra Dashboard**             | Django + Chart.js (vendas, relatórios), projeto separado. Ver [amostras/dashboard-django-chartjs/README.md](amostras/dashboard-django-chartjs/README.md). |

---

## Bloco 1 — Configuração (RAG/FAISS)

1. Crie o ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou: .venv\Scripts\activate  # Windows
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Copie o `.env.example` para `.env` e adicione sua chave da OpenAI:

   ```bash
   cp .env.example .env
   # Edite .env e coloque sua OPENAI_API_KEY
   ```

4. Coloque o `Perceptron.pdf` na raiz do projeto. Download: [Perceptron.pdf (Notion)](https://file.notion.so/f/f/158c4d7c-1f1a-437d-9e8e-bca83a08a555/7db74fd7-baf0-41ff-b5c3-eaadd2bebf0b/Perceptron.pdf)

## Execução

```bash
python app.py
```

## Estrutura (Bloco 1)

- **Bloco 1/** — `app.py` (pipeline RAG: PyPDFLoader, RecursiveCharacterTextSplitter, FAISS), `grafico_embeddings.py`, `visualizar_faiss.py`. Ver [Bloco 1/README.md](Bloco%201/README.md) e diagrama dados → embeddings → FAISS.

### Scripts extras

```bash
# Após rodar app.py e gerar banco_faiss/
python grafico_embeddings.py   # Salva grafico_embeddings.png
python visualizar_faiss.py     # Exibe os chunks no terminal
```

## Bloco 2 — Construção da base

Roteiro oficial: [Construção da base](https://grizzly-amaranthus-f6a.notion.site/Constru-o-da-base-2fb6cf8ea89f80b4b118cf36f5c2aa51).

Ordem: Teoria → Configurações iniciais → Cadastro - Usuários → Login - Usuários → Clientes - Usuários → Cliente - Usuários → Documentos - IA → Chat - IA → Config empresas - Usuários.

Ver **Bloco 2/ROTEIRO.md** e **Bloco 2/CONSTRUCAO_DA_BASE.md** para roteiro e mapeamento. **Códigos do período:** `Bloco 2/CODIGOS_BLOCO2.md`. Padrões de programação: ver `Infraestrutura/cursor-multiagent-system` e `.cursor/rules/padroes-programacao.mdc` no Bootcamp.

## Material

- [RAG - Arquivos da aula](https://grizzly-amaranthus-f6a.notion.site/RAG-Arquivos-da-aula-2fb6cf8ea89f80f58351d938fcf8ab05)
- Resumos em `Apostilas e Materiais de Cursos/[Pythonando] Bootcamp Programação Web + IA/`

## Notion (contexto agentes)

IDs dos cards Studies/Roadmap (Quick Wins, Bootcamp): `Infraestrutura/cursor-multiagent-system/config/studies/roadmap/NOTION_CARDS_ESTUDOS_ROADMAP.md`
