"""
Visualizar conteúdo do índice FAISS
Bootcamp Pythonando - Script extra do RAG
Lista os documentos armazenados no banco vetorial.
"""

import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Defina OPENAI_API_KEY no .env")

DB_PATH = "banco_faiss"


def main():
    if not os.path.isdir(DB_PATH):
        raise FileNotFoundError(
            f"Pasta '{DB_PATH}' não encontrada. Rode app.py antes para gerar o índice FAISS."
        )
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local(
        DB_PATH, embeddings, allow_dangerous_deserialization=True
    )

    # Recuperar todos os documentos do docstore
    docs = list(vectordb.docstore._dict.values())

    print(f"Total de chunks no FAISS: {len(docs)}\n")
    print("-" * 60)

    for i, doc in enumerate(docs, 1):
        preview = doc.page_content[:150].replace("\n", " ") + "..."
        print(f"\n[Chunk {i}]")
        print(preview)
        if hasattr(doc, "metadata") and doc.metadata:
            print(f"  metadata: {doc.metadata}")
        print("-" * 60)


if __name__ == "__main__":
    main()
