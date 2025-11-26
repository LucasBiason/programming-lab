"""
Sumarização de documentos usando transformers
Lê arquivo .docx e gera resumo do texto
"""

from docx import Document
from transformers import pipeline
import os


def ler_docx(caminho_arquivo):
    """Lê texto completo de arquivo .docx"""
    documento = Document(caminho_arquivo)
    texto_completo = []
    
    for paragrafo in documento.paragraphs:
        texto_completo.append(paragrafo.text)
    
    return "\n".join(texto_completo)


def sumarizar_texto(texto, max_tamanho=130, min_tamanho=30):
    """Gera resumo do texto usando modelo de sumarização"""
    sumarizador = pipeline("summarization")
    
    resumo = sumarizador(
        texto,
        max_length=max_tamanho,
        min_length=min_tamanho,
        do_sample=False
    )
    
    return resumo[0]['summary_text']


def salvar_resumo(texto_resumo, caminho_saida):
    """Salva resumo em arquivo .txt"""
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write(texto_resumo)


def main():
    """Função principal"""
    arquivo_docx = 'documento.docx'
    arquivo_saida = 'resumo.txt'

    # Ler documento
    texto_completo = ler_docx(arquivo_docx)
    
    # Gerar resumo
    resumo = sumarizar_texto(texto_completo, max_tamanho=200, min_tamanho=50)
    
    # Salvar resumo
    salvar_resumo(resumo, arquivo_saida)
    
    print(f"Resumo salvo em {arquivo_saida}")


if __name__ == "__main__":
    main()

