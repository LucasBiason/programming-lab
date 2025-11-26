"""
Assistente de receitas saudáveis usando RAG (Retrieval Augmented Generation)
Usa LangChain com ChromaDB para buscar receitas e OpenAI para gerar respostas
"""

import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
import random

CHROMA_PATH = "chroma"

TEMPLATE_PROMPT = """
Responda com uma receita para a solicitação abaixo:

{context}

---

Responda com base no contexto acima: {question}
"""

load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Preparar banco de dados vetorial
embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)


def gerar_resposta_gpt(pergunta, contexto):
    """Gera resposta usando GPT com contexto das receitas"""
    prompt_template = ChatPromptTemplate.from_template(TEMPLATE_PROMPT)
    prompt = prompt_template.format(context=contexto, question=pergunta)
    
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente de receitas saudáveis que fornece cardápios variados para café da manhã, almoço e jantar."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content.strip()


def buscar_receita(pergunta):
    """Busca receitas similares no banco de dados"""
    resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)
    
    # Verificar se encontrou resultados relevantes
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        return "Não encontrei receitas correspondentes.", []
    
    # Embaralhar resultados para variar
    random.shuffle(resultados)

    # Montar contexto com as receitas encontradas
    contexto = "\n\n---\n\n".join([doc.page_content for doc, _score in resultados])
    resposta = gerar_resposta_gpt(pergunta, contexto)

    return resposta


def ao_digitar():
    """Callback quando usuário digita mensagem"""
    pergunta = st.session_state.user_input
    resposta = buscar_receita(pergunta)
    
    st.session_state.past.append(pergunta)
    st.session_state.generated.append({"type": "normal", "data": resposta})


def limpar_historico():
    """Limpa histórico de conversa"""
    del st.session_state.past[:]
    del st.session_state.generated[:]


# Inicializar estado da sessão
st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])

st.title("Chat de Receitas Saudáveis")

# Área de chat
chat_container = st.empty()

with chat_container.container():
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'],
            key=f"{i}",
            allow_html=True,
            is_table=True if st.session_state['generated'][i].get('type') == 'table' else False
        )
    
    st.button("Limpar histórico", on_click=limpar_historico)

# Campo de input
with st.container():
    st.text_input("Mensagem:", on_change=ao_digitar, key="user_input")

