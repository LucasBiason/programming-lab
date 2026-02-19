# LLMs

**Seção:** Aprofundando na IA e LLM  
**Aula:** LLMs (Large Language Models)  
**Data da aula:** 12/02/2026 (18:11–18:46)  
**Material:** Fundamentos de IA Generativa (PDF p.66–67)  
**Fonte:** Transcrição da videoaula

---

## Resumo executivo

- **LLM (Large Language Model)** é o termo que descreve **modelos de linguagem em larga escala**: treinados com **bilhões de parâmetros** e grande volume de dados de texto. Não apenas memorizam padrões; entendem representação, contextualização e linguagem para tarefas que exigem fluência, coerência e adaptabilidade.
- **Base técnica:** arquitetura **Transformer** (auto-atenção, embeddings, camadas feedforward empilhadas). Cada token presta atenção em todo o resto da sequência; embeddings são a representação vetorial dos tokens; múltiplas camadas permitem processamento em paralelo.
- **Treinamento:** (1) **Pré-treinamento:** modelo exposto a bilhões de tokens (livros, sites, fóruns, código) para aprender padrões de linguagem e prever próxima palavra / preencher lacunas (autosupervisão). (2) **Fine tuning** supervisionado para tarefas específicas (classificação, resposta). (3) **RLHF (Reinforcement Learning with Human Feedback):** reforço com preferências humanas — usado no ChatGPT.
- **Capacidades:** geração de texto (conversação, livros, respostas contextualizadas, imitação de estilos); compreensão semântica (resumo, análise de sentimento, tradução, Q&A); capacidades emergentes (raciocínio, generalização, **few-shot** e **zero-shot**).
- **Modelos citados:** **GPT** (OpenAI) — autoregressivo, geração de texto e assistente; **BERT** (Google) — bidirecional, compreensão, classificação, busca; **Gemini** — multimodal (texto, imagem, código); **LLaMA** (Meta) — open source, pesquisa e desenvolvimento. Quanto mais tokens/ escala no treino, maior a performance.

---

## Conceitos-chave (flashcards)

- **P: O que é LLM?**  
  R: Large Language Model — modelos de linguagem em larga escala (bilhões de parâmetros, muito texto), com capacidade de fluência, coerência e adaptabilidade.

- **P: Quais os três blocos técnicos do LLM?**  
  R: Auto-atenção (cada token olha para os outros); embeddings (tokens em vetores); camadas feedforward empilhadas (processamento paralelo).

- **P: O que é RLHF?**  
  R: Reinforcement Learning with Human Feedback — aprendizado por reforço com feedback humano; usado no ChatGPT para alinhar respostas às preferências humanas.

- **P: GPT vs BERT?**  
  R: GPT é autoregressivo, unidirecional (esquerda→direita), focado em geração de texto. BERT é bidirecional, focado em compreensão, classificação, busca, preencher lacunas.

- **P: Por que “quanto mais tokens, melhor”?**  
  R: Mais texto permite criar e conectar mais relações e padrões; os parâmetros agem como nós de aprendizado que dependem do volume de dados.

- **P: O que é few-shot e zero-shot?**  
  R: Few-shot: realizar tarefa com poucos exemplos. Zero-shot: com pouquíssima ou nenhuma instrução; o modelo generaliza.

---

## Mapa conceitual

```
LLMs
├── Definição: modelos de linguagem em larga escala (bilhões de parâmetros)
├── Base: Transformer (atenção, embeddings, feedforward)
├── Treinamento
│   ├── Pré-treinamento (bilhões de tokens, autosupervisão)
│   ├── Fine tuning (tarefas específicas)
│   └── RLHF (preferências humanas)
├── Capacidades
│   ├── Geração (texto, estilos, respostas)
│   ├── Compreensão (resumo, sentimento, tradução, Q&A)
│   └── Emergentes (raciocínio, few-shot, zero-shot)
└── Modelos
    ├── GPT (geração, assistente)
    ├── BERT (compreensão, classificação, busca)
    ├── Gemini (multimodal)
    └── LLaMA (open source, pesquisa)
```

---

## Receita prática

1. **Entender** que LLM não é um único modelo; é uma estratégia de arquitetura e treinamento (Transformer + escala).
2. **Pré-treino:** expor a muito texto para prever próxima palavra / preencher lacunas.
3. **Refinar:** fine tuning para tarefa específica; RLHF para alinhar com humanos.
4. **Escolher modelo:** GPT para geração/assistente; BERT para compreensão/classificação; Gemini para multimodal; LLaMA para pesquisa/aberto.

---

## Perguntas de reforço

1. LLM memoriza padrões? Vai além: entende representação e contextualização para fluência e coerência.
2. O que é “autoregressivo”? Geração da esquerda para a direita, previsão da próxima palavra (ex.: GPT).
3. BERT é bom para gerar texto longo? Não; foi feito para compreensão, classificação, busca, preencher lacunas.
4. O que o RLHF faz no ChatGPT? Ajusta o modelo com reforço usando feedback humano (preferências).
5. Por que dados textuais são críticos para LLMs? Os nós de aprendizado (parâmetros) dependem do volume de texto para criar relações e padrões fiéis à realidade.
