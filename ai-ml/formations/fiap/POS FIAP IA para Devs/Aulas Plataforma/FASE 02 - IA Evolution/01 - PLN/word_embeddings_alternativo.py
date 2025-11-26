#!/usr/bin/env python3
"""
Alternativa para Word Embeddings sem Gensim
Substitui a funcionalidade do gensim com bibliotecas básicas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import re

class WordEmbeddingsAlternativo:
    """Classe que substitui funcionalidades do gensim"""
    
    def __init__(self, vector_size=300):
        self.vector_size = vector_size
        self.word_vectors = {}
        self.vocab = []
        
    def load_from_text(self, filename):
        """Carrega embeddings de um arquivo de texto (formato simples)"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 1:
                    word = parts[0]
                    vector = [float(x) for x in parts[1:]]
                    if len(vector) == self.vector_size:
                        self.word_vectors[word] = np.array(vector)
                        self.vocab.append(word)
            
            print(f"Carregados {len(self.vocab)} vetores de {filename}")
            return True
            
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Criando embeddings de exemplo...")
            return self.create_sample_embeddings()
    
    def create_sample_embeddings(self):
        """Cria embeddings de exemplo quando arquivo não está disponível"""
        sample_words = [
            'gato', 'cachorro', 'casa', 'jardim', 'animal', 'pet', 'lugar',
            'comida', 'água', 'brincar', 'dormir', 'correr', 'pular', 'feliz',
            'triste', 'grande', 'pequeno', 'bonito', 'feio', 'rápido', 'lento'
        ]
        
        np.random.seed(42)  # Para reprodutibilidade
        
        for word in sample_words:
            # Criar vetor aleatório normalizado
            vector = np.random.normal(0, 1, self.vector_size)
            vector = vector / np.linalg.norm(vector)  # Normalizar
            self.word_vectors[word] = vector
            self.vocab.append(word)
        
        print(f"Criados {len(self.vocab)} embeddings de exemplo")
        return True
    
    def get_vector(self, word):
        """Obtém o vetor de uma palavra"""
        return self.word_vectors.get(word, None)
    
    def most_similar(self, word, topn=5):
        """Encontra palavras mais similares"""
        if word not in self.word_vectors:
            return []
        
        target_vector = self.word_vectors[word]
        similarities = []
        
        for other_word, other_vector in self.word_vectors.items():
            if other_word != word:
                similarity = cosine_similarity([target_vector], [other_vector])[0][0]
                similarities.append((other_word, similarity))
        
        # Ordenar por similaridade (decrescente)
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:topn]
    
    def similarity(self, word1, word2):
        """Calcula similaridade entre duas palavras"""
        vec1 = self.get_vector(word1)
        vec2 = self.get_vector(word2)
        
        if vec1 is None or vec2 is None:
            return 0.0
        
        return cosine_similarity([vec1], [vec2])[0][0]
    
    def visualize_embeddings(self, words=None, method='pca'):
        """Visualiza embeddings em 2D"""
        if words is None:
            words = list(self.vocab)[:20]  # Primeiras 20 palavras
        
        # Coletar vetores
        vectors = []
        valid_words = []
        
        for word in words:
            if word in self.word_vectors:
                vectors.append(self.word_vectors[word])
                valid_words.append(word)
        
        if not vectors:
            print("Nenhum vetor válido encontrado")
            return
        
        vectors = np.array(vectors)
        
        # Reduzir dimensionalidade
        if method == 'pca':
            reducer = PCA(n_components=2)
        else:
            reducer = TSNE(n_components=2, random_state=42)
        
        vectors_2d = reducer.fit_transform(vectors)
        
        # Plotar
        plt.figure(figsize=(12, 8))
        plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], alpha=0.7, s=100)
        
        for i, word in enumerate(valid_words):
            plt.annotate(word, 
                        (vectors_2d[i, 0], vectors_2d[i, 1]),
                        xytext=(5, 5), 
                        textcoords='offset points',
                        fontsize=10,
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        
        plt.title(f'Visualização dos Word Embeddings ({method.upper()})')
        plt.xlabel('Componente 1')
        plt.ylabel('Componente 2')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

def main():
    """Função principal para demonstrar o uso"""
    print("=== Alternativa para Word Embeddings sem Gensim ===\n")
    
    # Criar instância
    embeddings = WordEmbeddingsAlternativo(vector_size=300)
    
    # Tentar carregar do arquivo (se existir)
    success = embeddings.load_from_text("cbow_s300.txt")
    
    if not success:
        print("Usando embeddings de exemplo...")
    
    # Demonstrar funcionalidades
    print("\n=== Testando Funcionalidades ===\n")
    
    # 1. Buscar palavras similares
    test_words = ['gato', 'cachorro', 'casa']
    for word in test_words:
        print(f"Palavras similares a '{word}':")
        similares = embeddings.most_similar(word, topn=3)
        for sim_word, score in similares:
            print(f"  {sim_word}: {score:.4f}")
        print()
    
    # 2. Calcular similaridade entre palavras
    word_pairs = [('gato', 'cachorro'), ('casa', 'jardim'), ('animal', 'pet')]
    for word1, word2 in word_pairs:
        sim = embeddings.similarity(word1, word2)
        print(f"Similaridade entre '{word1}' e '{word2}': {sim:.4f}")
    
    # 3. Visualizar embeddings
    print("\nGerando visualização...")
    embeddings.visualize_embeddings(method='pca')
    
    print("\n=== Uso Completo ===")
    print("Para usar em seu código:")
    print("""
# Importar
from word_embeddings_alternativo import WordEmbeddingsAlternativo

# Criar instância
embeddings = WordEmbeddingsAlternativo()

# Carregar dados
embeddings.load_from_text("seu_arquivo.txt")

# Usar funcionalidades
similares = embeddings.most_similar("palavra")
similaridade = embeddings.similarity("palavra1", "palavra2")
embeddings.visualize_embeddings()
    """)

if __name__ == "__main__":
    main() 