"""
Agente LLM para consulta de ações brasileiras
Usa OpenAI com function calling para buscar preços e gerar gráficos
"""

import streamlit as st
import pandas as pd
from openai import OpenAI
import json
import matplotlib.pyplot as plt
import yfinance as yf
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def buscar_preco_acao(ticker):
    """Busca o preço atual de uma ação pelo ticker"""
    try:
        acao = yf.Ticker(ticker)
        historico = acao.history(period='1y')
        if not historico.empty:
            preco = historico.iloc[-1].Close
            return f"Preço atual de {ticker}: R$ {preco:.2f}"
        return f"Não foi possível obter o preço de {ticker}"
    except Exception as e:
        return f"Erro ao buscar preço: {str(e)}"


def gerar_grafico_acao(ticker):
    """Gera gráfico de cotação da ação no último ano"""
    try:
        acao = yf.Ticker(ticker)
        dados = acao.history(period='1y')
        
        plt.figure(figsize=(10, 5))
        plt.plot(dados.index, dados.Close)
        plt.title(f"{ticker} - Cotação no Último Ano")
        plt.xlabel("Data")
        plt.ylabel("Preço (R$)")
        plt.grid(True)
        
        os.makedirs('imagens', exist_ok=True)
        caminho_imagem = f'imagens/{ticker}.png'
        plt.savefig(caminho_imagem)
        plt.close()
        
        return caminho_imagem
    except Exception as e:
        return None


# Definição das funções para o OpenAI
funcoes_disponiveis = [
    {
        "type": "function",
        "function": {
            "name": "buscar_preco_acao",
            "description": "Busca o preço atual de uma ação brasileira pelo ticker (formato: VALE3.SA)",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Ticker da ação no formato Yahoo Finance (ex: VALE3.SA, PETR4.SA)"
                    }
                },
                "required": ["ticker"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "gerar_grafico_acao",
            "description": "Gera gráfico com histórico de preços de uma ação no último ano",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Ticker da ação no formato Yahoo Finance"
                    }
                },
                "required": ["ticker"]
            }
        }
    }
]

mapeamento_funcoes = {
    "buscar_preco_acao": buscar_preco_acao,
    "gerar_grafico_acao": gerar_grafico_acao
}

# Inicializar histórico de mensagens
if 'mensagens' not in st.session_state:
    st.session_state['mensagens'] = [
        {
            'role': 'system',
            'content': 'Você é um assistente de investimentos especializado em ações brasileiras.'
        }
    ]

st.title("Assistente de Investimentos")

pergunta = st.text_input("Faça sua pergunta sobre ações:")

if pergunta:
    try:
        # Adicionar pergunta do usuário
        st.session_state['mensagens'].append({
            'role': 'user',
            'content': pergunta
        })

        # Chamar OpenAI com function calling
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state['mensagens'],
            tools=funcoes_disponiveis,
            tool_choice='auto'
        )

        mensagem_resposta = resposta.choices[0].message

        # Verificar se precisa chamar alguma função
        if mensagem_resposta.tool_calls:
            nome_funcao = mensagem_resposta.tool_calls[0].function.name
            argumentos = json.loads(mensagem_resposta.tool_calls[0].function.arguments)
            tool_call_id = mensagem_resposta.tool_calls[0].id

            # Executar função
            funcao = mapeamento_funcoes[nome_funcao]
            resultado = funcao(**argumentos)

            # Se for gráfico, exibir imagem
            if nome_funcao == 'gerar_grafico_acao' and resultado:
                st.image(resultado)
            else:
                # Adicionar resultado ao histórico
                st.session_state['mensagens'].append(mensagem_resposta)
                st.session_state['mensagens'].append({
                    'role': 'tool',
                    'tool_call_id': tool_call_id,
                    'name': nome_funcao,
                    'content': str(resultado)
                })

                # Obter resposta final do GPT
                resposta_final = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state['mensagens']
                )

                texto_resposta = resposta_final.choices[0].message.content.strip()
                st.write(texto_resposta)
                
                st.session_state['mensagens'].append({
                    'role': 'assistant',
                    'content': texto_resposta
                })
        else:
            # Resposta direta sem função
            st.write(mensagem_resposta.content)
            st.session_state['mensagens'].append({
                'role': 'assistant',
                'content': mensagem_resposta.content
            })

    except Exception as e:
        st.error(f"Erro: {str(e)}")

