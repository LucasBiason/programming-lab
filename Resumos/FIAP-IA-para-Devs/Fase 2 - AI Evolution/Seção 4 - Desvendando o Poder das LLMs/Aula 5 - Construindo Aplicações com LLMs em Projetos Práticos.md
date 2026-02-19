# Aula 5 - Construindo Aplicações com LLMs em Projetos Práticos

## Resumo executivo

Esta aula consolida a **construção de aplicações com LLMs** em projetos práticos: definição de **caso de uso** (Q&A, resumo, geração, classificação), escolha de **modelo** (API vs self-hosted; custo, latência, privacidade), **design de prompts** (instrução, contexto, exemplos, formato), **tratamento de erros** e **retry**, **avaliação** (métricas, testes, usuários) e **deploy** (API, batch, integração). Boas práticas: versionar prompts, logar entradas/saídas para análise, limitar tokens e custos, e considerar fallbacks quando o modelo falha. Exemplos: pipeline de suporte ao cliente, gerador de conteúdo, classificador de tickets.

**Objetivos de aprendizagem:** Estruturar um projeto com LLM (requisitos, modelo, prompts, avaliação, deploy); aplicar boas práticas de prompt e operação; integrar LLM em aplicação (API, front, batch).

---

## Conceitos-chave (flashcards)

1. **Quais critérios para escolher API vs modelo self-hosted?** **R:** Custo, latência, privacidade dos dados, necessidade de fine-tuning e controle de versão do modelo.
2. **Por que versionar prompts?** **R:** Reproduzibilidade, A/B testing e rollback; prompts são parte crítica do comportamento da aplicação.
3. **O que fazer em caso de falha da API do LLM?** **R:** Retry com backoff, fallback (resposta padrão ou modelo alternativo), log para análise e alertas.

---

## Receita prática

1. Definir tarefa e métricas de sucesso. 2. Escolher modelo (API ou open) e prototipar com prompts. 3. Adicionar contexto (RAG) e exemplos se necessário. 4. Implementar chamada, retry e tratamento de erros. 5. Avaliar em conjunto de teste e com usuários. 6. Fazer deploy (endpoint, batch) e monitorar custo e qualidade.

---

## Perguntas para teste de reforço

1. Que critérios usar para escolher API vs modelo self-hosted? **R:** Custo, latência, privacidade, necessidade de fine-tuning.
2. Por que versionar prompts? **R:** Reproduzibilidade, A/B testing e rollback.
3. O que fazer quando a API do LLM falha? **R:** Retry com backoff, fallback, log e alertas.
4. Cite uma boa prática ao integrar LLM em produção. **R:** Limitar tokens, logar entradas/saídas, definir fallbacks.

---

## Materiais de apoio

- OpenAI – API reference: [platform.openai.com/docs/api-reference](https://platform.openai.com/docs/api-reference)
- LangChain – Quickstart: [python.langchain.com/docs/get_started](https://python.langchain.com/docs/get_started)
