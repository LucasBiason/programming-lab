"""
RAG (Retrieval-Augmented Generation) com LangChain
Bootcamp Pythonando - Programação Web + IA
Usa OPENAI_API_KEY do .env (sua chave, não a do instrutor)
"""

import os
import warnings

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

warnings.filterwarnings("ignore")
load_dotenv()

# Chave da OpenAI vem do .env
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Defina OPENAI_API_KEY no arquivo .env")

# Carregar PDF
caminho_pdf = "Perceptron.pdf"
loader = PyPDFLoader(caminho_pdf)
documentos = loader.load()


def train():
    """Prepara o vectorstore FAISS: carrega se existir, adiciona chunks, ou cria do zero."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documentos)

    embeddings = OpenAIEmbeddings()
    db_path = "banco_faiss"

    if os.path.exists(db_path):
        vectordb = FAISS.load_local(
            db_path, embeddings, allow_dangerous_deserialization=True
        )
        vectordb.add_documents(chunks)
    else:
        vectordb = FAISS.from_documents(chunks, embeddings)

    vectordb.save_local(db_path)
    return vectordb


def retrieval(pergunta):
    """Carrega o FAISS e retorna os documentos mais similares à pergunta."""
    embeddings = OpenAIEmbeddings()
    db_path = "banco_faiss"
    vectordb = FAISS.load_local(
        db_path, embeddings, allow_dangerous_deserialization=True
    )
    docs = vectordb.similarity_search(pergunta, k=4)
    contexto = "\n\n".join([f"Material: {doc.page_content}" for doc in docs])

    # Template do prompt
    template = """Você é um assistente que responde com base no contexto fornecido.
    Use APENAS o contexto abaixo para responder. Se não souber, diga que não encontrou a informação.

    Contexto:
    {context}

    Pergunta: {question}

    Resposta:"""

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": contexto, "question": pergunta})


if __name__ == "__main__":
    if not os.path.isfile(caminho_pdf):
        raise FileNotFoundError(
            f"Coloque o arquivo {caminho_pdf} na raiz do projeto. "
            "Download: link no README (Notion RAG - Arquivos da aula)."
        )
    train()
    print(retrieval("O que é o Perceptron e como funciona?"))
    print(retrieval("O que é o Youtube?"))
