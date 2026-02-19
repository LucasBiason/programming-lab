# Aula 3 - Aplicações Práticas de LLMs em Tradução Automática e Localização

## Resumo executivo

Esta aula aborda **aplicações práticas** de LLMs em **tradução automática e localização**: fluxos de **tradução em lote** (documentos, catálogos), **tradução sob demanda** (chat, UI), **pós-edição** (MT + revisor humano), **geração de conteúdo localizado** (marketing, suporte) e **manutenção de glossários** (termos técnicos, marca). Uso de **APIs** (OpenAI, Google, Azure) ou modelos locais; **prompts** estruturados (idioma fonte/alvo, estilo, restrições); **avaliação** (BLEU, COMET, revisão humana). Integração com ferramentas CAT e TMS quando aplicável.

**Objetivos de aprendizagem:** Montar pipeline de tradução com LLM (prompt, API, pós-edição); aplicar glossários e instruções de estilo; avaliar qualidade (métricas e amostragem).

---

## Conceitos-chave (flashcards)

1. **O que é pós-edição (PE)?** **R:** Revisão humana da saída da tradução automática; combina produtividade da MT com qualidade do revisor.
2. **Como usar glossário com LLM para tradução?** **R:** Incluir no prompt lista de termos (origem → alvo) ou instruções para preferir certas traduções; alguns APIs suportam glossário nativo.
3. **BLEU e COMET?** **R:** BLEU: métrica baseada em n-grams entre hipótese e referência. COMET: modelo neural que avalia qualidade de tradução (mais correlacionado com humano).

---

## Perguntas para teste de reforço

1. O que é pós-edição em tradução? **R:** Revisão humana da saída da tradução automática.
2. Como aplicar glossário com LLM na tradução? **R:** Incluir no prompt termos origem→alvo ou instruções de preferência.
3. Para que serve BLEU? **R:** Métrica automática que compara hipótese com referência (n-grams).
4. Cite um fluxo prático de tradução com LLM. **R:** Tradução em lote, sob demanda, ou pós-edição (MT + revisor).

---

## Materiais de apoio

- OpenAI – Best practices for translation: [platform.openai.com/docs](https://platform.openai.com/docs)
- COMET – [unbabel.com/COMET](https://unbabel.com/COMET)
