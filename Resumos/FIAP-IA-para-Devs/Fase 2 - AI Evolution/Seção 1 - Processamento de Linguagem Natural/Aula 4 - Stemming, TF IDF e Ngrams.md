# Aula 4 - Stemming, TF IDF e Ngrams

## Resumo executivo

Esta aula aborda **stemming** (reduzir palavras ao radical/tronco, ex.: "correndo" → "corr"), **TF-IDF** (Term Frequency – Inverse Document Frequency: pondera termos pela frequência no documento e pela raridade no corpus, destacando termos discriminativos) e **N-grams** (sequências de N tokens, ex.: bigramas, trigramas), que preservam contexto local. Stemming reduz variabilidade morfológica; TF-IDF substitui ou complementa a contagem bruta do BoW; N-grams enriquecem a representação com frases. Implementação típica: sklearn `TfidfVectorizer`, NLTK ou Snowball stemmer, e `ngram_range` no vetorizador.

**Objetivos de aprendizagem:** Aplicar stemming (ex.: Porter, Snowball); explicar TF e IDF e o produto TF-IDF; usar TfidfVectorizer com ngram_range; interpretar o efeito de N-grams na representação.

---

## Conceitos-chave (flashcards)

1. **O que é stemming?** **R:** Redução de palavras ao tronco/radical (ex.: "correr", "correndo" → "corr") para agrupar variantes e reduzir dimensionalidade.
2. **O que é TF-IDF?** **R:** TF = frequência do termo no documento; IDF = log(N/doc_freq); TF-IDF = TF × IDF; termos raros no corpus e frequentes no documento ganham peso alto.
3. **O que são N-grams?** **R:** Sequências de N tokens consecutivos (bigramas N=2, trigramas N=3); capturam expressões como "machine learning" ou "não recomendo".
4. **Para que serve ngram_range em TfidfVectorizer?** **R:** Definir intervalo de N para n-grams (ex.: (1,2) = unigramas + bigramas).

---

## Exemplos práticos

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ["PLN processa linguagem natural.", "Linguagem natural e texto."]
vec = TfidfVectorizer(ngram_range=(1, 2))
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
```

```python
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("portuguese")
print(stemmer.stem("correndo"))  # corr
print(stemmer.stem("belíssimo")) # bel
```

---

## Mapa conceitual

```
Stemming, TF-IDF e N-grams
├── Stemming: tronco comum (Porter, Snowball); reduz variantes
├── TF-IDF: TF × IDF; termos discriminativos; TfidfVectorizer
├── N-grams: bigramas, trigramas; ngram_range(1,2) ou (1,3)
└── Pipeline: tokenize → stem (opcional) → TfidfVectorizer(ngram_range=...)
```

---

## Receita prática

1. Pré-processar texto (tokenizar, stop words). 2. Opcional: aplicar stemmer aos tokens. 3. TfidfVectorizer(ngram_range=(1,2), max_features=...) para unigramas + bigramas. 4. fit_transform nos documentos; usar matriz resultante em classificador ou similaridade.

---

## Perguntas para teste de reforço

1. Por que um termo com IDF alto? **R:** Aparece em poucos documentos; é mais discriminativo.
2. Qual a diferença entre stemming e lematização? **R:** Stemming corta sufixos (pode gerar "radical" não dicionarizado); lematização retorna forma de dicionário (ex.: "correndo" → "correr").
3. Para que bigramas ajudam em análise de sentimento? **R:** Capturam expressões como "não bom", "muito ruim", que unigramas perdem.

---

## Materiais de apoio

- Scikit-learn – TfidfVectorizer: [sklearn.feature_extraction.text.TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- NLTK Stemmers: [nltk.org/api/nltk.stem.html](https://www.nltk.org/api/nltk.stem.html)
