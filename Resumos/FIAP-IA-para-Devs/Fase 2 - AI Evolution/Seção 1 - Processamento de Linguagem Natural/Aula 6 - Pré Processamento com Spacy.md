# Aula 6 - Pré Processamento com Spacy

## Resumo executivo

Esta aula aborda **pré-processamento de texto com spaCy**: biblioteca industrial para NLP que oferece **tokenização**, **lematização**, **POS tagging** (part-of-speech), **NER** (reconhecimento de entidades nomeadas), **dependency parsing** e pipelines em mais de 60 idiomas. O objeto **Doc** contém tokens (**Token**) com atributos como `lemma_`, `pos_`, `dep_`. Modelos pré-treinados (ex.: `pt_core_news_sm`) fornecem pipeline completo. Uso típico: substituir ou complementar NLTK em pipelines que precisam de lematização de qualidade e análise linguística mais rica.

**Objetivos de aprendizagem:** Carregar modelo spaCy (pt_core_news_*); tokenizar e acessar lemma, POS e dependências; usar spaCy em pipeline de pré-processamento (lematização, filtro por POS, remoção de stop words).

---

## Conceitos-chave (flashcards)

1. **O que é spaCy?** **R:** Biblioteca de NLP com pipelines eficientes: tokenização, lematização, POS, NER, dependency parsing; modelos pré-treinados por idioma.
2. **Lematização vs stemming?** **R:** Lematização retorna forma de dicionário (ex.: "correndo" → "correr"); stemming retorna tronco que pode não ser palavra válida ("corr").
3. **O que é POS tagging?** **R:** Atribuição de classe gramatical (substantivo, verbo, adjetivo, etc.) a cada token.
4. **Para que serve doc[0].lemma_?** **R:** Obter a forma lematizada do primeiro token do documento.

---

## Exemplos práticos

```python
import spacy
nlp = spacy.load("pt_core_news_sm")

doc = nlp("O processamento de linguagem natural está evoluindo.")
for token in doc:
    print(token.text, token.lemma_, token.pos_)

# Apenas substantivos e verbos
tokens_relevantes = [t.lemma_ for t in doc if t.pos_ in ("NOUN", "VERB")]
```

```python
# Remover stop words e pontuação
tokens_limpos = [t.lemma_ for t in doc if not t.is_stop and not t.is_punct]
```

---

## Mapa conceitual

```
Pré-processamento com spaCy
├── Pipeline: nlp(texto) → Doc → Tokens
├── Token: text, lemma_, pos_, dep_, is_stop, is_punct
├── Modelos: pt_core_news_sm, pt_core_news_lg
├── Operações: lematização, POS, NER, dependency parsing
└── Uso em PLN: limpar texto, filtrar por POS, extrair entidades
```

---

## Receita prática

1. Instalar spaCy e modelo: `python -m spacy download pt_core_news_sm`. 2. nlp = spacy.load("pt_core_news_sm"); doc = nlp(texto). 3. Iterar doc: usar token.lemma_, token.pos_, token.is_stop. 4. Montar lista de lemas (ex.: filtrando stop words e pontuação) para BoW, TF-IDF ou embeddings.

---

## Perguntas para teste de reforço

1. Qual a diferença entre pt_core_news_sm e pt_core_news_lg? **R:** sm = menor e mais rápido; lg = maior e em geral mais preciso.
2. O que é NER em spaCy? **R:** Named Entity Recognition: identificar entidades como pessoas, lugares, organizações (doc.ents).
3. Para que dependency parsing serve? **R:** Analisar relações sintáticas entre palavras (sujeito, objeto, etc.); útil para extração de relações e compreensão de estrutura.

---

## Materiais de apoio

- spaCy – Documentação: [spacy.io/usage](https://spacy.io/usage)
- spaCy – Modelos em português: [spacy.io/models/pt](https://spacy.io/models/pt)
