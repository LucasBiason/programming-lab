# Aula 3 - Tokenização com NLTK e remoção de stop words

## Resumo executivo

Esta aula trata de **tokenização** (dividir texto em unidades menores: palavras, sentenças ou subpalavras) e **remoção de stop words** (palavras muito frequentes e pouco informativas, como artigos e preposições). A **NLTK** (Natural Language Toolkit) oferece `word_tokenize`, `sent_tokenize`, listas de stop words por idioma e ferramentas de pré-processamento. Tokenização é etapa fundamental antes de BoW, TF-IDF ou embeddings; a remoção de stop words reduz ruído e dimensão, mas pode remover informação em alguns contextos (ex.: negação).

**Objetivos de aprendizagem:** Aplicar tokenização em palavras e sentenças com NLTK; usar e customizar listas de stop words; integrar tokenização e remoção de stop words em um pipeline de PLN.

---

## Conceitos-chave (flashcards)

1. **O que é tokenização?** **R:** Divisão do texto em unidades (tokens): palavras, sentenças ou subpalavras, para análise e representação numérica.
2. **O que são stop words?** **R:** Palavras muito comuns (ex.: "o", "a", "de", "em") geralmente removidas para reduzir ruído e dimensionalidade; em português há listas em NLTK e em bibliotecas como spaCy.
3. **Para que serve nltk.word_tokenize?** **R:** Dividir uma string em lista de palavras (tokens), considerando pontuação e contrações.
4. **Quando não remover stop words?** **R:** Em tarefas onde negociação ou contexto gramatical importam (ex.: "não é bom"); em perguntas/respostas onde "o", "a" podem ser relevantes.

---

## Exemplos práticos

```python
import nltk
nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

texto = "O PLN processa texto. Tokenização e stop words são fundamentais."
palavras = word_tokenize(texto)
sentencas = sent_tokenize(texto)

stop_pt = set(stopwords.words("portuguese"))
tokens_limpos = [w for w in palavras if w.lower() not in stop_pt]
```

---

## Mapa conceitual

```
Tokenização e stop words
├── Tokenização: palavras (word_tokenize), sentenças (sent_tokenize)
├── NLTK: punkt, stopwords (portuguese)
├── Stop words: remoção para BoW/TF-IDF; cuidado com negação
└── Pipeline: texto → tokenize → filtrar stop words → representação
```

---

## Receita prática

1. Baixar recursos NLTK: `punkt_tab`, `stopwords`. 2. Tokenizar com `word_tokenize` (ou `sent_tokenize`). 3. Carregar stop words: `stopwords.words("portuguese")`. 4. Filtrar: `[t for t in tokens if t.lower() not in stop_pt]`. 5. Usar lista de tokens em CountVectorizer ou TF-IDF.

---

## Perguntas para teste de reforço

1. Qual a diferença entre word_tokenize e sent_tokenize? **R:** word_tokenize retorna lista de palavras; sent_tokenize retorna lista de sentenças.
2. Por que usar set para stop words? **R:** Busca O(1); mais rápido que lista em filtros grandes.
3. O que é punkt no NLTK? **R:** Modelo usado para tokenização de sentenças (e palavras em alguns idiomas).

---

## Materiais de apoio

- NLTK – Tokenization: [nltk.org/api/nltk.tokenize.html](https://www.nltk.org/api/nltk.tokenize.html)
- NLTK – Stopwords: [nltk.org/corpus/words](https://www.nltk.org/nltk_data/)
