# Spacy Word2Vec Classifier

Este projeto implementa um sistema de classificação de textos usando spaCy para processamento de linguagem natural e Word2Vec para representação vetorial das palavras.

## 📋 Descrição

O sistema é treinado para classificar artigos de notícias em diferentes categorias usando:
- **spaCy**: Para processamento de linguagem natural em português
- **Word2Vec**: Para criar representações vetoriais das palavras
- **Logistic Regression**: Para classificação final

## 🚀 Instalação

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Instale o modelo spaCy para português:**
```bash
python -m spacy download pt_core_news_sm
```

## 📊 Dados

O script espera os seguintes arquivos CSV no diretório atual:
- `treino.csv`: Dados de treinamento
- `teste.csv`: Dados de teste

Cada arquivo deve conter as colunas:
- `title`: Título do artigo
- `category`: Categoria do artigo

## 🎯 Funcionalidades

### 1. Processamento de Texto
- Remoção de stopwords
- Filtragem de caracteres não alfanuméricos
- Tokenização

### 2. Modelos Word2Vec
- **CBOW (Continuous Bag of Words)**: window=2
- **Skip-gram**: window=5
- Ambos com vector_size=300

### 3. Classificação
- Regressão Logística
- Métricas: precision, recall, f1-score
- Suporte para múltiplas categorias

## 🔧 Uso

Execute o script principal:
```bash
python spacy_word2vec_classifier.py
```

## 📈 Saídas

O script gera:
1. **Modelos Word2Vec salvos:**
   - `modelo_cbow.txt`: Modelo CBOW
   - `modelo_sg.txt`: Modelo Skip-gram

2. **Relatórios de classificação** com métricas detalhadas

3. **Exemplos de similaridade** de palavras

## 📊 Estrutura do Código

- `install_spacy_model()`: Instala e carrega modelo spaCy
- `load_data()`: Carrega dados de treino e teste
- `process_text_with_spacy()`: Demonstração do spaCy
- `trata_textos()`: Pré-processamento de textos
- `train_word2vec_models()`: Treina modelos Word2Vec
- `tokenizador()`: Tokenização de textos
- `matriz_vetores()`: Cria matriz de vetores
- `classificador()`: Treina e avalia classificador

## 🎯 Resultados Esperados

O sistema deve conseguir classificar artigos com:
- **Acurácia**: ~53-54%
- **Melhor performance**: Categoria "esporte"
- **Skip-gram**: Geralmente melhor que CBOW

## 🔍 Exemplo de Uso

```python
# Carregar modelo treinado
from gensim.models import KeyedVectors
modelo = KeyedVectors.load_word2vec_format('modelo_sg.txt')

# Encontrar palavras similares
similares = modelo.most_similar('google')
print(similares)
```

## 📝 Notas

- O script requer dados em português
- O treinamento pode levar alguns minutos
- Os modelos são salvos em formato texto para compatibilidade
- O sistema usa processamento paralelo para eficiência 