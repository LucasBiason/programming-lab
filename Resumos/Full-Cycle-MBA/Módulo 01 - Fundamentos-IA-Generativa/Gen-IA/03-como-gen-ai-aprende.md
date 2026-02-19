# Como a Gen AI aprende

**Seção:** Gen IA  
**Aula:** Como a Gen AI aprende  
**Módulo:** Fundamentos de IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Objetivo central:** Aprender a distribuição de probabilidade dos dados (P(x) ou P(x_n | x_1..x_{n-1}) para sequências).
- **Treinamento:** Maximizar likelihood dos dados; minimizar loss (ex.: cross-entropy) entre predição e token/imagem real.
- **Dados:** Corpus de texto, pares imagem-legenda, código-fonte; quanto mais e mais diverso, melhor a generalização.
- **Escala:** Modelos grandes (bilhões de parâmetros) + muitos dados + muito compute = capacidades emergentes (raciocínio, seguimento de instruções).

---

## Conceitos-chave (flashcards)

- **P: O que o modelo está de fato aprendendo?**  
  R: A distribuição de probabilidade dos dados — ou seja, quais sequências/tokens/imagens são mais prováveis.

- **P: O que é "next-token prediction"?**  
  R: Dada a sequência até o momento, prever a distribuição do próximo token; o modelo aprende a fazer isso em escala.

- **P: Por que "escala" importa tanto?**  
  R: Modelos maiores com mais dados mostram capacidades emergentes (raciocínio, instruções) que não aparecem em modelos pequenos.

- **P: O que é fine-tuning?**  
  R: Ajustar um modelo pré-treinado para uma tarefa ou domínio específico, com menos dados e compute.

---

## Mapa conceitual

```
Como a Gen AI aprende
├── Objetivo
│   └── Aprender P(dados)
├── Treinamento
│   ├── Loss: cross-entropy
│   └── Maximizar likelihood
├── Dados
│   ├── Texto, código, multimodal
│   └── Volume e diversidade
└── Escala
    ├── Parâmetros (bilhões)
    ├── Tokens de treino
    └── Capacidades emergentes
```

---

## Perguntas de reforço

1. O modelo "entende" o que gera? Ele captura padrões estatísticos; "entendimento" é debatido.
2. Por que pré-treinamento + fine-tuning? Pré-treino aprende linguagem geral; fine-tune adapta a tarefa com menos custo.
3. O que é "emergent ability"? Comportamento que surge em modelos grandes e não em menores (ex.: chain-of-thought).
