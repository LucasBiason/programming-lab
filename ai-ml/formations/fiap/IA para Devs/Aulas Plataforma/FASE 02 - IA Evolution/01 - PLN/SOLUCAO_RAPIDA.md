# 🚀 Solução Rápida para Substituir Gensim

## ❌ Problema
```python
# Isso não funciona:
from gensim.models import KeyedVectors
modelo = KeyedVectors.load_word2vec_format("cbow_s300.txt")
```

## ✅ Solução
Copie este código no seu notebook:

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Criar modelo de exemplo
def criar_modelo_exemplo():
    palavras = [
        'gato', 'cachorro', 'casa', 'jardim', 'animal', 'pet', 'lugar',
        'comida', 'água', 'brincar', 'dormir', 'correr', 'pular', 'feliz',
        'triste', 'grande', 'pequeno', 'bonito', 'feio', 'rápido', 'lento'
    ]
    
    np.random.seed(42)
    modelo = {}
    
    for palavra in palavras:
        vetor = np.random.normal(0, 1, 300)
        vetor = vetor / np.linalg.norm(vetor)
        modelo[palavra] = vetor
    
    return modelo

# Carregar modelo
modelo = criar_modelo_exemplo()

# Funções que substituem gensim
def most_similar(palavra, topn=5):
    if palavra not in modelo:
        return []
    
    vetor_alvo = modelo[palavra]
    similaridades = []
    
    for outra_palavra, outro_vetor in modelo.items():
        if outra_palavra != palavra:
            sim = cosine_similarity([vetor_alvo], [outro_vetor])[0][0]
            similaridades.append((outra_palavra, sim))
    
    similaridades.sort(key=lambda x: x[1], reverse=True)
    return similaridades[:topn]

def similarity(palavra1, palavra2):
    if palavra1 not in modelo or palavra2 not in modelo:
        return 0.0
    
    vetor1 = modelo[palavra1]
    vetor2 = modelo[palavra2]
    
    return cosine_similarity([vetor1], [vetor2])[0][0]
```

## 🎯 Como Usar

```python
# Buscar palavras similares
similares = most_similar('gato', topn=3)
for palavra, score in similares:
    print(f"{palavra}: {score:.4f}")

# Calcular similaridade
sim = similarity('gato', 'cachorro')
print(f"Similaridade: {sim:.4f}")

# Acessar vetor
vetor = modelo['gato']
print(f"Vetor: {vetor[:5]}...")
```

## 📦 Dependências
```bash
pip install numpy scikit-learn
```

## ✅ Vantagens
- ✅ Funciona sem gensim
- ✅ Bibliotecas básicas
- ✅ Fácil de entender
- ✅ Pronto para usar

## 🔄 Para Dados Reais
Se você tiver um arquivo de embeddings, modifique a função `criar_modelo_exemplo()` para carregar seus dados:

```python
def carregar_embeddings_reais(arquivo):
    modelo = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            partes = linha.strip().split()
            palavra = partes[0]
            vetor = [float(x) for x in partes[1:]]
            modelo[palavra] = np.array(vetor)
    return modelo
```

**Pronto! Agora você pode continuar seus estudos sem problemas com gensim!** 🎉 