# Aula 5 - Word Embedings com Word2Vec

## Resumo executivo

Esta aula trata de **word embeddings**: representações **densas** e **vetoriais** de palavras em um espaço contínuo, onde palavras semanticamente próximas ficam próximas no espaço. **Word2Vec** (Mikolov et al.) aprende esses vetores a partir de grandes corpora usando arquiteturas **CBOW** (Continuous Bag of Words: prediz a palavra central a partir do contexto) ou **Skip-gram** (prediz o contexto a partir da palavra central). Os vetores capturam relações semânticas (ex.: rei − homem + mulher ≈ rainha). Uso típico: gensim ou sklearn-compatible; representação de documento por média dos vetores das palavras (ou combinações mais sofisticadas).

**Objetivos de aprendizagem:** Diferenciar BoW/TF-IDF de embeddings; explicar CBOW e Skip-gram; treinar ou carregar Word2Vec (gensim); obter vetor de palavra e representação de documento (média); interpretar similaridade e analogias.

---

## Conceitos-chave (flashcards)

1. **O que é word embedding?** **R:** Representação vetorial densa da palavra em espaço contínuo; palavras com significado parecido têm vetores próximos.
2. **O que é Word2Vec?** **R:** Modelo que aprende embeddings a partir de co-ocorrência de palavras no texto; arquiteturas CBOW e Skip-gram.
3. **CBOW vs Skip-gram?** **R:** CBOW prediz a palavra central dado o contexto; Skip-gram prediz o contexto dado a palavra central; Skip-gram costuma funcionar melhor com pouco dado.
4. **Como obter vetor de um documento a partir de Word2Vec?** **R:** Média (ou soma) dos vetores das palavras do documento (ignorando palavras fora do vocabulário).

---

## Exemplos práticos

```python
from gensim.models import Word2Vec

sentencas = [["pln", "processa", "texto"], ["texto", "e", "linguagem", "natural"]]
modelo = Word2Vec(sentences=sentencas, vector_size=50, window=2, min_count=1)

vetor = modelo.wv["texto"]
similares = modelo.wv.most_similar("texto", topn=3)
# Analogia: rei - homem + mulher
analogia = modelo.wv.most_similar(positive=["rei", "mulher"], negative=["homem"])
```

---

## Mapa conceitual

```
Word Embedings e Word2Vec
├── Embedings: vetores densos; similaridade semântica
├── Word2Vec: CBOW (contexto → palavra), Skip-gram (palavra → contexto)
├── Hiperparâmetros: vector_size, window, min_count
├── Uso: vetor de palavra, similaridade, analogias
└── Documento: média dos vetores das palavras
```

---

## Receita prática

1. Tokenizar corpus (lista de listas de palavras). 2. Word2Vec(sentences=..., vector_size=100, window=5, min_count=2). 3. wv["palavra"] para vetor; most_similar para similares; most_similar(positive=[...], negative=[...]) para analogias. 4. Para documento: média dos vetores das palavras presentes no vocabulário.

---

## Perguntas para teste de reforço

1. Por que embeddings são melhores que BoW para semântica? **R:** BoW ignora significado e similaridade; embeddings colocam palavras com sentido próximo em vetores próximos.
2. O que é window no Word2Vec? **R:** Tamanho do contexto (quantas palavras à esquerda e à direita) usadas para previsão.
3. O que é min_count? **R:** Mínimo de ocorrências da palavra no corpus para entrar no vocabulário; reduz ruído.

---

## Materiais de apoio

- Gensim – Word2Vec: [radimrehurek.com/gensim/models/word2vec.html](https://radimrehurek.com/gensim/models/word2vec.html)
- Mikolov et al. – Efficient Estimation of Word Representations (2013)
