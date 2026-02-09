"""
Geração de gráfico dos embeddings
Bootcamp Pythonando - Script extra do RAG
Reduz os vetores de embedding para 2D (PCA) e gera visualização.
"""

import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Defina OPENAI_API_KEY no .env")

DB_PATH = "banco_faiss"
OUTPUT = "grafico_embeddings.png"


def main():
    if not os.path.isdir(DB_PATH):
        raise FileNotFoundError(
            f"Pasta '{DB_PATH}' não encontrada. Rode app.py antes para gerar o índice FAISS."
        )
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local(
        DB_PATH, embeddings, allow_dangerous_deserialization=True
    )

    # Extrair vetores do índice FAISS (compatível com diferentes versões)
    import numpy as np

    index = vectordb.index
    n = index.ntotal
    vectors = np.array([index.reconstruct(i) for i in range(n)], dtype=np.float32)

    # Reduzir para 2D com PCA
    pca = PCA(n_components=2, random_state=42)
    coords_2d = pca.fit_transform(vectors)

    plt.figure(figsize=(10, 8))
    plt.scatter(coords_2d[:, 0], coords_2d[:, 1], alpha=0.6, s=30)
    plt.title("Embeddings do FAISS (redução PCA 2D)")
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    plt.tight_layout()
    plt.savefig(OUTPUT, dpi=150)
    plt.close()
    print(f"Gráfico salvo em: {OUTPUT}")


if __name__ == "__main__":
    main()
