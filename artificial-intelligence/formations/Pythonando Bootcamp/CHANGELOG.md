# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Arquivos de contexto (plano bootcamp):** `CONSTRUCAO_DA_BASE.md` na raiz (índice); `Bloco 2/NOTION_CARD_BOOTCAMP.md` e `Bloco 2/VERIFICACAO_CURSOS_E_NOTION.md` para Notion e checklist de validação.
- **Decisões de paridade** em `Bloco 2/CONSTRUCAO_DA_BASE.md`: webhook WhatsApp (não replicar bug do arcabe3), Martor opcional, Evolution API via env.
- **Validação:** Seção "Validação Notion/Figma vs código" em CONSTRUCAO_DA_BASE; referência a VERIFICACAO_CURSOS_E_NOTION.md.
- **Bloco 1:** `Bloco 1/README.md` com descrição do pipeline (app.py, FAISS, scripts) e diagrama Mermaid (dados → embeddings → FAISS → busca).
- **Bloco 2/docs:** `docs/apps-documents.md` (responsabilidade, OCR, endpoints, fluxo).
- **README raiz:** Índice geral com links para Bloco 1, Bloco 2, CONSTRUCAO_DA_BASE, ROTEIRO, docs, amostra Dashboard.
- **Comentários no código:** config/urls.py (estrutura de rotas), apps/clientes/models/documentos.py (conteúdo e paridade Martor).
- **Amostra Dashboard:** Diagrama Mermaid no README (dados → views JSON → Chart.js); link no README raiz.

- Alinhamento do Bloco 2 (jury_ai) com referência arcabe3-completo: mesmas funcionalidades (cadastro, login, clientes, documentos, chat com streaming, análise jurisprudencial, ver referências, webhook WhatsApp), com revisão pelos padrões do cursor-multiagent-system (Ruff, uma classe por arquivo, CHANGELOG, sem emojis em código).
- Configuração Ruff em `Bloco 2/jury_ai/pyproject.toml`.
- Arquivos de contexto: `CONSTRUCAO_DA_BASE.md`, `ROTEIRO.md` em Bloco 2 (a partir do Notion e extracted_content_temp).
- Documentação de arquitetura e por app em `Bloco 2/docs/` (ARQUITETURA.md com diagramas Mermaid, apps-chat.md, apps-clientes.md, apps-whatsapp.md).
- Regra `.cursor/rules/padroes-programacao.mdc` na raiz do Bootcamp referenciando cursor-multiagent-system.
- Projeto de amostra `amostras/dashboard-django-chartjs/`: Django + Chart.js (vendas, relatórios JSON), independente do Jury AI.

### Changed

- README raiz e Bloco 2 atualizados com referência aos padrões (Infraestrutura/cursor-multiagent-system) e aos arquivos de contexto.
- Correções Ruff em `apps/chat/services/agent_langchain.py` (import settings) e `apps/core/management/commands/seed.py` (formato de string).
