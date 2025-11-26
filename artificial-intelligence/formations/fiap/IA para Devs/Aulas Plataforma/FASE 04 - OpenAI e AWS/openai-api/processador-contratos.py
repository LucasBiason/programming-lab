"""
Sistema para processar contratos e extrair informações usando OpenAI
Processa arquivos Word e texto, extraindo dados estruturados
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
cliente_openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def extrair_texto_word(arquivo_docx):
    """Extrai todo o texto de um arquivo Word"""
    doc = Document(arquivo_docx)
    paragrafos = [p.text for p in doc.paragraphs if p.text.strip()]
    return '\n'.join(paragrafos)


def processar_arquivo_texto(arquivo):
    """Processa arquivo de texto detectando encoding automaticamente"""
    dados_brutos = arquivo.read()
    deteccao = chardet.detect(dados_brutos)
    encoding = deteccao.get('encoding', 'utf-8')
    return dados_brutos.decode(encoding)


def chamar_openai_para_extrair(texto_contrato):
    """Usa GPT para extrair dados estruturados do contrato"""
    prompt_sistema = (
        "Você é um especialista em análise de contratos jurídicos. "
        "Para contratos de locação, extraia as seguintes informações em formato JSON: "
        "NOME_DO_LOCADOR, DOCUMENTO_DO_LOCADOR, NOME_DO_LOCATARIO, "
        "DOCUMENTO_DO_LOCATARIO, ENDERECO_DO_IMOVEL, VALOR_DO_ALUGUEL"
    )
    
    resposta = cliente_openai.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": f"Extraia as informações deste contrato:\n\n{texto_contrato}"}
        ],
        max_tokens=4096
    )
    
    return json.loads(resposta.choices[0].message.content)


@app.route('/processar', methods=['POST'])
def processar_contrato():
    """Endpoint principal para processar contratos"""
    if 'arquivo' not in request.files:
        return jsonify({"erro": "Nenhum arquivo foi enviado"}), 400

    arquivo = request.files.get('arquivo')
    
    if not arquivo or arquivo.filename == '':
        return jsonify({"erro": "Arquivo não foi selecionado"}), 400

    try:
        # Processar arquivo Word
        if arquivo.filename.lower().endswith('.docx'):
            texto = extrair_texto_word(arquivo)
            dados_extraidos = chamar_openai_para_extrair(texto)
            return jsonify(dados_extraidos)
        
        # Processar arquivo de texto
        else:
            texto = processar_arquivo_texto(arquivo)
            dados_extraidos = chamar_openai_para_extrair(texto)
            return jsonify(dados_extraidos)
            
    except UnicodeDecodeError:
        return jsonify({"erro": "Não foi possível decodificar o arquivo"}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro ao processar: {str(e)}"}), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Verifica se a API está funcionando"""
    return jsonify({"status": "ok", "servico": "processador de contratos"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

