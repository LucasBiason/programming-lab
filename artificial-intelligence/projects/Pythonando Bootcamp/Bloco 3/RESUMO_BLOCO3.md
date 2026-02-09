# Bloco 3 — Funcionalidades com IA (Dia 2 manhã)

Resumo do bloco: integração de IA no projeto Jury AI (chat, RAG, análise jurisprudencial, ver referências).

## Objetivos do bloco

- Revisar e praticar **Chat** com streaming e análise jurisprudencial.
- **RAG** e base de conhecimento (LanceDB, documentos, embeddings).
- Endpoint **Ver referências** e fluxo de respostas baseadas em contexto.
- Testes (pytest, E2E com Playwright) e validação das funcionalidades.

## Principais endpoints (Jury AI)

| Área                    | Endpoint / URL                           | Uso                                                |
| ----------------------- | ---------------------------------------- | -------------------------------------------------- |
| Chat                    | `POST /api/chat/`                        | Cria pergunta; stream e análise em views separadas |
| Análise jurisprudencial | `POST /api/chat/analise-jurisprudencia/` | Processar análise com classificação Médio/Crítico  |
| Ver referências         | `/ver-referencias/<pergunta_id>/`        | Exibe fontes e trechos recuperados                 |
| Documentos (OCR)        | `POST /api/documents/ocr/`               | Upload e processamento de documentos               |

## RAG e base de conhecimento

O agente **SecretariaAI** usa LanceDB e base `knowledge`; é necessário garantir que a base está populada (documentos/embedding) para respostas baseadas em conhecimento. O conceito de RAG foi praticado no Bloco 1 (LangChain + FAISS) e reutilizado no Jury AI.

## Status e observações

- Bloco 3 corresponde ao **Dia 2 manhã** do bootcamp (09:00–12:00).
- Conteúdo alinhado ao roteiro Notion (Construção da base + Funcionalidades com IA).
