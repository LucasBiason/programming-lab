# Aula 4 - Chatbots e Assistentes Virtuais Impulsionados por LLMs

## Resumo executivo

Esta aula trata de **chatbots e assistentes virtuais** baseados em **LLMs**: arquitetura típica com **histórico de conversa** (contexto), **system prompt** (persona e regras), **geração** (streaming ou não) e **integração** com fontes externas (RAG, APIs). Diferença entre chatbots **genéricos** (conversa aberta) e **orientados a tarefas** (formulários, fluxos, ações). Boas práticas: delimitar tema, limitar alucinações com RAG, **guardrails** (filtros de conteúdo), avaliação com usuários e métricas (satisfação, resolução). Ferramentas: APIs (OpenAI, Anthropic), frameworks (LangChain, LlamaIndex), e interfaces (web, mensageiros).

**Objetivos de aprendizagem:** Descrever arquitetura de um chatbot com LLM (contexto, system prompt, RAG); diferenciar uso genérico e orientado a tarefas; citar guardrails e avaliação.

---

## Conceitos-chave (flashcards)

1. **O que é system prompt em um chatbot?** **R:** Instrução fixa que define papel, tom e regras do assistente; enviada antes da conversa e condiciona todas as respostas.
2. **Como RAG reduz alucinações em chatbot?** **R:** O modelo responde com base em documentos recuperados (retrieval), em vez de só memória interna; reduz invenção de fatos.
3. **O que são guardrails?** **R:** Regras ou modelos que filtram entrada/saída (conteúdo inadequado, vazamento de dados, desvio de tema).

---

## Mapa conceitual

```
Chatbots e assistentes com LLM
├── Arquitetura: system prompt + histórico + geração
├── Contexto: janela de tokens (limite de histórico)
├── RAG: recuperação de documentos para fundamentar resposta
├── Guardrails: filtros de conteúdo e segurança
└── Avaliação: satisfação, resolução, testes A/B
```

---

## Perguntas para teste de reforço

1. O que é system prompt em um chatbot? **R:** Instrução fixa que define papel, tom e regras do assistente.
2. Como RAG reduz alucinações? **R:** O modelo responde com base em documentos recuperados, não só na memória interna.
3. O que são guardrails? **R:** Filtros de conteúdo e segurança na entrada/saída do chatbot.
4. Diferença entre chatbot genérico e orientado a tarefas? **R:** Genérico = conversa aberta; orientado = fluxos, formulários, ações definidas.

---

## Materiais de apoio

- LangChain – Chatbots: [python.langchain.com/docs](https://python.langchain.com/docs)
- OpenAI – GPT best practices: [platform.openai.com/docs/guides](https://platform.openai.com/docs/guides)
