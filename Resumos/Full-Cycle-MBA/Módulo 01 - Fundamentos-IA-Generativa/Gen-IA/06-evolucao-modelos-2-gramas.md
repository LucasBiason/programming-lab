# Evolução dos modelos — 2 gramas (n-gramas)

**Seção:** Gen IA  
**Aula:** Evolução dos modelos 2 gramas  
**Módulo:** Fundamentos de IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **N-gramas:** Modelos simples que estimam probabilidade da próxima palavra com base nas N–1 palavras anteriores.
- **Bigramas (2-gramas):** P(palavra_n | palavra_{n-1}) — só o par imediatamente anterior.
- **Limitações:** Contexto muito curto; explosão combinatória (vocabulário^N); não captura dependências longas.
- **Base histórica:** Usados em correção ortográfica, suavização de linguagem, modelos de linguagem simples antes das redes neurais.

---

## Conceitos-chave (flashcards)

- **P: O que é um bigrama?**  
  R: Par de palavras consecutivas; modelo que prevê P(palavra_atual | palavra_anterior).

- **P: O que é suavização (smoothing)?**  
  R: Técnica para lidar com n-gramas nunca vistos (ex.: Laplace, backoff); evita probabilidade zero.

- **P: Por que n-gramas não escalam?**  
  R: Número de combinações cresce com vocabulário^N; dados finitos não cobrem a maioria das sequências.

- **P: Qual o elo entre n-gramas e modelos modernos?**  
  R: Mesma ideia de prever próximo token dado o contexto; modelos modernos usam contexto muito maior e representações vetoriais.

---

## Mapa conceitual

```
Evolução — N-gramas (2-gramas)
├── Definição
│   └── P(x_n | x_{n-1}, ..., x_{n-N+1})
├── Bigramas
│   └── Apenas par anterior
├── Limitações
│   ├── Contexto curto
│   ├── Esparsidade (muitos zeros)
│   └── Sem dependências longas
└── Técnicas
    ├── Suavização
    └── Backoff
```

---

## Perguntas de reforço

1. Bigrama consegue capturar "O livro que João leu era interessante"? Não; "leu" depende de "livro" e "João", além da janela de 1.
2. O que vem depois dos n-gramas na evolução? Cadeias de Markov (HMMs), redes neurais, RNNs, Transformers.
3. N-gramas ainda são usados? Sim, em correção, suavização e como baseline; não para geração de texto complexa.
