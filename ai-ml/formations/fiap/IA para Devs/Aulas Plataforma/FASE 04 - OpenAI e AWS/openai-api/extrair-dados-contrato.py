"""
API Flask para extrair dados de contratos usando OpenAI
Processa arquivos .docx e .txt e extrai informações estruturadas
"""

from flask import Flask, request, jsonify
from openai import OpenAI
from docx import Document
import chardet
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def ler_docx(arquivo):
    """Lê texto de arquivo .docx"""
    documento = Document(arquivo)
    texto = []
    for paragrafo in documento.paragraphs:
        texto.append(paragrafo.text)
    return '\n'.join(texto)


def extrair_dados_com_gpt(texto_contrato):
    """Usa GPT para extrair dados estruturados do contrato"""
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "Você é especialista em extrair dados de contratos jurídicos. Para contratos de locação, retorne: NOME_DO_LOCADOR, DOCUMENTO_DO_LOCADOR, NOME_DO_LOCATARIO, DOCUMENTO_DO_LOCATARIO, ENDERECO_DO_IMOVEL, VALOR_DO_ALUGUEL no formato JSON."
            },
            {
                "role": "user",
                "content": f"Extraia as informações deste contrato: {texto_contrato}"
            }
        ],
        max_tokens=4096
    )
    
    return json.loads(resposta.choices[0].message.content)


@app.route('/upload', methods=['POST'])
def upload_arquivo():
    """Endpoint para upload e processamento de contratos"""
    if 'file' not in request.files:
        return jsonify({"error": "Arquivo não enviado"}), 400

    arquivo = request.files.get('file')
    
    if arquivo.filename == '':
        return jsonify({"error": "Arquivo não selecionado"}), 400

    try:
        # Processar arquivo .docx
        if arquivo.filename.endswith('.docx'):
            texto = ler_docx(arquivo)
            dados = extrair_dados_com_gpt(texto)
            return jsonify(dados)
        
        # Processar arquivo de texto
        else:
            dados_brutos = arquivo.read()
            resultado_encoding = chardet.detect(dados_brutos)
            encoding = resultado_encoding['encoding']
            texto = dados_brutos.decode(encoding)
            dados = extrair_dados_com_gpt(texto)
            return jsonify(dados)
            
    except UnicodeDecodeError:
        return jsonify({"error": "Erro ao decodificar arquivo"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro ao processar: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

