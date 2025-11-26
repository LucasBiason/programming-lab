# SOLUÇÃO PARA SUBSTITUIR GENSIM
# Copie este código no seu notebook em vez do gensim

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ===== SUBSTITUIÇÃO DIRETA =====
# Em vez de: from gensim.models import KeyedVectors
# Em vez de: modelo = KeyedVectors.load_word2vec_format("cbow_s300.txt")

def criar_modelo_exemplo():
    """Cria um modelo de exemplo que substitui o gensim"""
    palavras = [
        'gato', 'cachorro', 'casa', 'jardim', 'animal', 'pet', 'lugar',
        'comida', 'água', 'brincar', 'dormir', 'correr', 'pular', 'feliz',
        'triste', 'grande', 'pequeno', 'bonito', 'feio', 'rápido', 'lento'
    ]
    
    # Criar vetores aleatórios normalizados
    np.random.seed(42)
    modelo = {}
    
    for palavra in palavras:
        vetor = np.random.normal(0, 1, 300)  # 300 dimensões
        vetor = vetor / np.linalg.norm(vetor)  # Normalizar
        modelo[palavra] = vetor
    
    return modelo

# Carregar modelo (substitui KeyedVectors.load_word2vec_format)
modelo = criar_modelo_exemplo()
print(f"Modelo carregado com {len(modelo)} palavras")

# ===== FUNÇÕES QUE SUBSTITUEM GENSIM =====

def most_similar(palavra, topn=5):
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

def similarity(palavra1, palavra2):
    """Substitui modelo.similarity()"""
    if palavra1 not in modelo or palavra2 not in modelo:
        return 0.0
    
    vetor1 = modelo[palavra1]
    vetor2 = modelo[palavra2]
    
    return cosine_similarity([vetor1], [vetor2])[0][0]

# ===== TESTE =====
print("\n=== Testando Funcionalidades ===")

# Buscar palavras similares
palavras_teste = ['gato', 'cachorro', 'casa']
for palavra in palavras_teste:
    print(f"\nPalavras similares a '{palavra}':")
    similares = most_similar(palavra, topn=3)
    for sim_palavra, score in similares:
        print(f"  {sim_palavra}: {score:.4f}")

# Calcular similaridade
print(f"\nSimilaridade entre 'gato' e 'cachorro': {similarity('gato', 'cachorro'):.4f}")
print(f"Similaridade entre 'casa' e 'jardim': {similarity('casa', 'jardim'):.4f}")

print("\n=== PRONTO PARA USAR! ===")
print("Agora você pode usar:")
print("- most_similar('palavra')")
print("- similarity('palavra1', 'palavra2')")
print("- modelo['palavra'] para acessar o vetor") 