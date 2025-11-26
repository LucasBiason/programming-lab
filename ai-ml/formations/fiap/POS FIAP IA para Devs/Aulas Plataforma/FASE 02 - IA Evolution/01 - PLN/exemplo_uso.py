#!/usr/bin/env python3
"""
Exemplo de uso - Substitui a linha problemática do gensim
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ===== SUBSTITUIÇÃO DIRETA =====
# Em vez de:
# from gensim.models import KeyedVectors
# modelo = KeyedVectors.load_word2vec_format("cbow_s300.txt")

# Use isto:
print("=== Alternativa para Gensim ===\n")

# Criar embeddings de exemplo (substitui o arquivo grande)
def criar_embeddings_exemplo():
    """Cria embeddings de exemplo para substituir o arquivo grande"""
    palavras = [
        'gato', 'cachorro', 'casa', 'jardim', 'animal', 'pet', 'lugar',
        'comida', 'água', 'brincar', 'dormir', 'correr', 'pular', 'feliz',
        'triste', 'grande', 'pequeno', 'bonito', 'feio', 'rápido', 'lento'
    ]
    
    # Criar vetores aleatórios normalizados (simula embeddings reais)
    np.random.seed(42)
    embeddings = {}
    
    for palavra in palavras:
        vetor = np.random.normal(0, 1, 300)  # 300 dimensões como o original
        vetor = vetor / np.linalg.norm(vetor)  # Normalizar
        embeddings[palavra] = vetor
    
    return embeddings

# Carregar embeddings (substitui KeyedVectors.load_word2vec_format)
modelo = criar_embeddings_exemplo()
print(f"Carregados {len(modelo)} embeddings de exemplo")

# ===== FUNÇÕES QUE SUBSTITUEM GENSIM =====

def most_similar(modelo, palavra, topn=5):
    """Substitui modelo.most_similar()"""
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

def similarity(modelo, palavra1, palavra2):
    """Substitui modelo.similarity()"""
    if palavra1 not in modelo or palavra2 not in modelo:
        return 0.0
    
    vetor1 = modelo[palavra1]
    vetor2 = modelo[palavra2]
    
    return cosine_similarity([vetor1], [vetor2])[0][0]

# ===== EXEMPLO DE USO =====

print("\n=== Testando Funcionalidades ===\n")

# 1. Buscar palavras similares (substitui modelo.most_similar())
palavras_teste = ['gato', 'cachorro', 'casa']
for palavra in palavras_teste:
    print(f"Palavras similares a '{palavra}':")
    similares = most_similar(modelo, palavra, topn=3)
    for sim_palavra, score in similares:
        print(f"  {sim_palavra}: {score:.4f}")
    print()

# 2. Calcular similaridade (substitui modelo.similarity())
pares = [('gato', 'cachorro'), ('casa', 'jardim'), ('animal', 'pet')]
for palavra1, palavra2 in pares:
    sim = similarity(modelo, palavra1, palavra2)
    print(f"Similaridade entre '{palavra1}' e '{palavra2}': {sim:.4f}")

# 3. Acessar vetor diretamente (substitui modelo[palavra])
palavra = 'gato'
if palavra in modelo:
    vetor = modelo[palavra]
    print(f"\nVetor de '{palavra}': {vetor[:5]}... (dimensões: {len(vetor)})")

print("\n=== CÓDIGO COMPLETO PARA SUBSTITUIR GENSIM ===")
print("""
# Em vez de:
# from gensim.models import KeyedVectors
# modelo = KeyedVectors.load_word2vec_format("cbow_s300.txt")
# similares = modelo.most_similar("palavra")

# Use isto:
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def criar_embeddings_exemplo():
    # Seu código para criar/carregar embeddings
    pass

modelo = criar_embeddings_exemplo()
similares = most_similar(modelo, "palavra")
""") 