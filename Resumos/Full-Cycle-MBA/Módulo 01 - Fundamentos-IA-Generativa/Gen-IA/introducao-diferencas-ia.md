# Introdução às diferenças de IA

**Seção:** Gen IA  
**Aula:** Introdução às diferenças de IA  
**Módulo:** Fundamentos de IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **IA simbólica vs sub-simbólica:** IA simbólica manipula símbolos e regras (expert systems); sub-simbólica aprende padrões a partir dos dados (redes neurais).
- **IA estreita (ANI) vs geral (AGI):** ANI resolve tarefas específicas; AGI (ainda hipotética) teria capacidade humana em qualquer domínio.
- **Discriminativa vs generativa:** Discriminativa classifica (ex.: spam/não spam); generativa gera (ex.: próximo token, imagem).
- **Modelos de linguagem:** Encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5) — cada um adequado a tarefas diferentes.

---

## Conceitos-chave (flashcards)

- **P: Qual a diferença entre IA simbólica e sub-simbólica?**  
  R: Simbólica usa regras e símbolos; sub-simbólica aprende representações dos dados (ex.: redes neurais).

- **P: O que é modelo discriminativo?**  
  R: Prevê rótulos ou categorias a partir de entradas (P(classe|entrada)).

- **P: O que é modelo generativo?**  
  R: Modela distribuição dos dados e gera amostras; pode também classificar via P(entrada|classe).

- **P: Encoder-only vs decoder-only: quando usar cada um?**  
  R: Encoder: tarefas de entendimento (NLI, classificação). Decoder: geração de texto (chat, código).

---

## Mapa conceitual

```
Diferenças de IA
├── Por paradigma
│   ├── Simbólica (regras, expert systems)
│   └── Sub-simbólica (redes neurais, ML)
├── Por escopo
│   ├── ANI (tarefa específica)
│   └── AGI (hipotética, geral)
├── Por objetivo
│   ├── Discriminativa (classificar)
│   └── Generativa (gerar)
└── Arquiteturas LM
    ├── Encoder-only (BERT)
    ├── Decoder-only (GPT)
    └── Encoder-decoder (T5)
```

---

## Perguntas de reforço

1. ChatGPT é ANI ou AGI? ANI — faz bem tarefas de linguagem, mas não é geral.
2. Por que "encoder" e "decoder"? Encoder compreende/representa entrada; decoder gera saída a partir dessa representação.
3. BERT gera texto longo como o GPT? Não; BERT é treinado para preencher máscaras e entender, não para gerar sequências longas autoregressivamente.
