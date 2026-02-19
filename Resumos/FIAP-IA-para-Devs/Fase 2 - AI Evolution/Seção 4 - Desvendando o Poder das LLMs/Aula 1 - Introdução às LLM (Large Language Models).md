# Aula 1 - Introdução às LLM (Large Language Models)

## Resumo executivo

Esta aula introduz **Large Language Models (LLMs)**: modelos de linguagem com **bilhões de parâmetros** treinados em grandes corpora de texto, capazes de **gerar**, **resumir**, **traduzir** e **responder** em linguagem natural. Arquiteturas típicas: **transformers** (attention), modelos **decoder-only** (GPT, LLaMA) ou **encoder-decoder** (T5). Treino em duas fases: **pré-treinamento** (predição de próximo token ou máscara) e **ajuste fino** (fine-tuning, RLHF, instrução). Uso via APIs (OpenAI, Anthropic, etc.) ou modelos open-source (Hugging Face). Aplicações: chatbots, assistentes, código, resumo, Q&A.

**Objetivos de aprendizagem:** Definir LLM e seu escopo (tamanho, arquitetura, capacidades); diferenciar pré-treinamento e fine-tuning; citar aplicações e formas de uso (API, open-source).

---

## Conceitos-chave (flashcards)

1. **O que é um LLM?** **R:** Modelo de linguagem de grande escala (bilhões de parâmetros), baseado em transformers, treinado em texto massivo; gera e compreende linguagem natural.
2. **O que é pré-treinamento?** **R:** Fase de treino em texto bruto (ex.: predição do próximo token); o modelo aprende gramática, fatos e padrões gerais.
3. **O que é fine-tuning?** **R:** Ajuste do modelo pré-treinado em tarefa ou domínio específico (ex.: instruções, diálogo, código) com menos dados.
4. **Decoder-only vs encoder-decoder?** **R:** Decoder-only (GPT): geração autoregressiva. Encoder-decoder (T5): mapeia entrada para saída (tradução, resumo, Q&A).

---

## Mapa conceitual

```
LLMs (Large Language Models)
├── Arquitetura: transformers, attention
├── Escala: bilhões de parâmetros
├── Treino: pré-treinamento (next-token) → fine-tuning / RLHF
├── Uso: API (OpenAI, etc.), modelos open (Hugging Face)
└── Aplicações: chatbot, código, resumo, tradução, Q&A
```

---

## Perguntas para teste de reforço

1. O que é um LLM? **R:** Modelo de linguagem em grande escala (bilhões de parâmetros), baseado em transformers, que gera e compreende texto.
2. O que é pré-treinamento? **R:** Fase de treino em texto bruto (ex.: prever próximo token) para aprender gramática e padrões gerais.
3. O que é fine-tuning? **R:** Ajuste do modelo pré-treinado para uma tarefa ou domínio específico (instruções, diálogo, código).
4. Cite duas formas de usar LLMs na prática. **R:** APIs (OpenAI, Anthropic) ou modelos open-source (Hugging Face).

---

## Materiais de apoio

- Hugging Face – Transformers: [huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)
- Vaswani et al. – Attention Is All You Need (2017)
