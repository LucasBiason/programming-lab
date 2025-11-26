#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preparação de Dados para Fine-tuning de Modelos de IA
Script para processar e formatar dados de notícias para treinamento de modelos

Objetivo: Demonstrar preparação de dados para fine-tuning + formatação de prompts
Data: 2025
"""

import pandas as pd
import json
import os
from typing import List, Dict, Any
from datasets import load_dataset

def load_huggingface_dataset(dataset_name: str = "glnmario/news-qa-summarization") -> pd.DataFrame:
    """
    CARREGA DATASET REAL DO HUGGING FACE
    
    Esta função baixa e carrega o dataset completo do Hugging Face.
    O dataset 'glnmario/news-qa-summarization' contém mais de 10.000 registros
    de notícias da CNN com resumos e perguntas/respostas.
    
    Parâmetros:
        dataset_name (str): Nome do dataset no Hugging Face
        
    Retorna:
        pd.DataFrame: DataFrame pandas com todos os dados do dataset
    """
    try:
        print(f"📚 Baixando dataset do Hugging Face: {dataset_name}")
        print("⏳ Isso pode demorar alguns minutos na primeira vez...")
        
        # Carrega o dataset diretamente do Hugging Face
        dataset = load_dataset(dataset_name, split="train")
        
        # Converte para DataFrame pandas
        df = dataset.to_pandas()
        
        print(f"✅ Dataset baixado com sucesso: {len(df)} registros")
        print(f"📊 Colunas disponíveis: {list(df.columns)}")
        print(f"🌐 Fonte: https://huggingface.co/datasets/{dataset_name}")
        
        # Mostra algumas estatísticas
        if 'story' in df.columns:
            avg_story_length = df['story'].str.len().mean()
            print(f"📝 Comprimento médio das notícias: {avg_story_length:.0f} caracteres")
        
        if 'summary' in df.columns:
            avg_summary_length = df['summary'].str.len().mean()
            print(f"📋 Comprimento médio dos resumos: {avg_summary_length:.0f} caracteres")
        
        return df
        
    except Exception as e:
        print(f"💥 Erro ao baixar dataset: {e}")
        print("💡 Verifique sua conexão com a internet")
        print("💡 Ou use o arquivo local 'data.jsonl' como fallback")
        
        # Fallback para arquivo local se existir
        if os.path.exists("data.jsonl"):
            print("🔄 Tentando carregar arquivo local como fallback...")
            try:
                df = pd.read_json("data.jsonl", lines=True)
                print(f"✅ Arquivo local carregado: {len(df)} registros")
                return df
            except Exception as local_error:
                print(f"❌ Erro ao carregar arquivo local: {local_error}")
        
        return pd.DataFrame()

def load_local_news_data(file_path: str) -> List[Dict[str, Any]]:
    """
    CARREGA DADOS LOCAIS DE NOTÍCIAS
    
    Esta função carrega o arquivo JSON local com as notícias extraídas
    e os resumos gerados pela IA.
    
    Parâmetros:
        file_path (str): Caminho para o arquivo JSON local
        
    Retorna:
        List[Dict]: Lista com os dados das notícias
    """
    try:
        print(f"📰 Carregando dados locais: {file_path}")
        
        # Verifica se o arquivo existe
        if not os.path.exists(file_path):
            print(f"⚠️ Arquivo não encontrado: {file_path}")
            print("💡 Execute primeiro o news_scrapper.py para gerar este arquivo")
            return []
        
        # Carrega o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        
        # Extrai a lista de notícias
        if "news_summaries" in json_data:
            news_list = json_data["news_summaries"]
            print(f"✅ Dados locais carregados: {len(news_list)} notícias")
            return news_list
        else:
            print("⚠️ Estrutura do arquivo não contém 'news_summaries'")
            return []
            
    except Exception as e:
        print(f"💥 Erro ao carregar dados locais: {e}")
        return []

def format_prompt_for_finetuning(story: str, summary: str) -> str:
    """
    FORMATA PROMPT PARA FINE-TUNING
    
    Esta função cria um prompt estruturado para treinamento do modelo.
    O formato segue um padrão específico com marcadores para delimitar
    a entrada (notícia) e a saída esperada (resumo).
    
    Parâmetros:
        story (str): Texto da notícia
        summary (str): Resumo da notícia
        
    Retorna:
        str: Prompt formatado para fine-tuning
    """
    # Formato estruturado com marcadores claros
    # [|News|] e [|eNews|] delimitam a notícia
    # [|summary|] e [|esummary|] delimitam o resumo esperado
    formatted_prompt = f"""SUMMARIZE THIS NEWS.

[|News|] {story}[|eNews|]

[|summary|]{summary}[|esummary|]"""
    
    return formatted_prompt

def process_huggingface_data(df: pd.DataFrame) -> List[Dict[str, str]]:
    """
    PROCESSAR DADOS DO HUGGING FACE
    
    Esta função processa cada linha do dataset do Hugging Face,
    formatando os dados para o formato de fine-tuning.
    
    Parâmetros:
        df (pd.DataFrame): DataFrame com os dados do Hugging Face
        
    Retorna:
        List[Dict]: Lista com prompts formatados
    """
    print(f"🔄 Processando {len(df)} registros do Hugging Face...")
    
    processed_data = []
    
    for index, row in df.iterrows():
        try:
            # Verifica se as colunas necessárias existem
            if 'story' in row and 'summary' in row:
                story = str(row['story'])
                summary = str(row['summary'])
                
                # Formata o prompt
                formatted_prompt = format_prompt_for_finetuning(story, summary)
                
                # Adiciona à lista processada
                processed_data.append({
                    "input": formatted_prompt,
                    "source": "huggingface",
                    "index": index
                })
            else:
                print(f"⚠️ Linha {index} não contém colunas 'story' ou 'summary'")
                
        except Exception as e:
            print(f"💥 Erro ao processar linha {index}: {e}")
    
    print(f"✅ Processados {len(processed_data)} registros do Hugging Face")
    return processed_data

def process_local_news_data(news_list: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    PROCESSAR DADOS LOCAIS DE NOTÍCIAS
    
    Esta função processa as notícias extraídas localmente,
    formatando-as para o formato de fine-tuning.
    
    Parâmetros:
        news_list (List[Dict]): Lista com dados das notícias
        
    Retorna:
        List[Dict]: Lista com prompts formatados
    """
    print(f"🔄 Processando {len(news_list)} notícias locais...")
    
    processed_data = []
    
    for i, item in enumerate(news_list):
        try:
            # Verifica se o item tem as chaves necessárias
            if "original_content" in item and "summary" in item:
                story = item["original_content"]
                summary = item["summary"]
                
                # Formata o prompt
                formatted_prompt = format_prompt_for_finetuning(story, summary)
                
                # Adiciona à lista processada
                processed_data.append({
                    "input": formatted_prompt,
                    "source": "local_news",
                    "url": item.get("url", ""),
                    "index": i
                })
            else:
                print(f"⚠️ Item {i} não contém 'original_content' ou 'summary'")
                
        except Exception as e:
            print(f"💥 Erro ao processar item {i}: {e}")
    
    print(f"✅ Processadas {len(processed_data)} notícias locais")
    return processed_data

def save_processed_data(data: List[Dict[str, str]], filename: str) -> None:
    """
    SALVA DADOS PROCESSADOS
    
    Esta função salva todos os dados processados em um arquivo JSON
    para uso posterior no fine-tuning.
    
    Parâmetros:
        data (List[Dict]): Lista com dados processados
        filename (str): Nome do arquivo de saída
    """
    try:
        print(f"💾 Salvando dados processados em: {filename}")
        
        # Cria estrutura de dados com metadados
        output_data = {
            "metadata": {
                "total_records": len(data),
                "sources": list(set(item.get("source", "unknown") for item in data)),
                "format": "fine-tuning_prompt",
                "description": "Dados formatados para fine-tuning de modelos de resumo de notícias"
            },
            "data": data
        }
        
        # Salva em arquivo JSON
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(output_data, file, ensure_ascii=False, indent=2)
        
        print(f"✅ Dados salvos com sucesso: {len(data)} registros")
        
        # Mostra estatísticas
        sources_count = {}
        for item in data:
            source = item.get("source", "unknown")
            sources_count[source] = sources_count.get(source, 0) + 1
        
        print("\n📊 Estatísticas dos dados:")
        for source, count in sources_count.items():
            print(f"   • {source}: {count} registros")
            
    except Exception as e:
        print(f"💥 Erro ao salvar dados: {e}")

def main():
    """
    FUNÇÃO PRINCIPAL - PIPELINE DE PREPARAÇÃO DE DADOS
    
    Esta função orquestra todo o processo de preparação de dados:
    1. Carrega dataset do Hugging Face
    2. Carrega dados locais de notícias
    3. Processa e formata todos os dados
    4. Salva dados prontos para fine-tuning
    """
    print("=" * 70)
    print("🤖 PREPARAÇÃO DE DADOS PARA FINE-TUNING")
    print("=" * 70)
    
    # Lista para armazenar todos os dados processados
    all_processed_data = []
    
    # ETAPA 1: CARREGAR DATASET DO HUGGING FACE
    print("\n🚀 ETAPA 1: CARREGANDO DATASET DO HUGGING FACE")
    print("-" * 50)
    
    hf_df = load_huggingface_dataset()
    
    if not hf_df.empty:
        # Processa dados do Hugging Face
        hf_processed = process_huggingface_data(hf_df)
        all_processed_data.extend(hf_processed)
    
    # ETAPA 2: CARREGAR DADOS LOCAIS
    print("\n🚀 ETAPA 2: CARREGANDO DADOS LOCAIS")
    print("-" * 50)
    
    local_news = load_local_news_data("news_summaries.json")
    
    if local_news:
        # Processa dados locais
        local_processed = process_local_news_data(local_news)
        all_processed_data.extend(local_processed)
    
    # ETAPA 3: SALVAR DADOS PROCESSADOS
    print("\n🚀 ETAPA 3: SALVANDO DADOS PROCESSADOS")
    print("-" * 50)
    
    if all_processed_data:
        output_filename = "news_dataset_finetuning.json"
        save_processed_data(all_processed_data, output_filename)
        
        # RESUMO FINAL
        print("\n" + "=" * 70)
        print("🎉 PREPARAÇÃO DE DADOS CONCLUÍDA!")
        print("=" * 70)
        print(f"📊 RESUMO FINAL:")
        print(f"   • Total de registros processados: {len(all_processed_data)}")
        print(f"   • Dataset Hugging Face: {len([x for x in all_processed_data if x.get('source') == 'huggingface'])}")
        print(f"   • Notícias locais: {len([x for x in all_processed_data if x.get('source') == 'local_news'])}")
        print(f"   • Arquivo gerado: {output_filename}")
        
        print("\n💡 Próximos passos:")
        print("   • Use os dados para treinar seu modelo")
        print("   • Ajuste os parâmetros de fine-tuning")
        print("   • Valide o modelo com dados de teste")
        print("   • Deploy do modelo treinado")
        
    else:
        print("❌ Nenhum dado foi processado!")
        print("💡 Verifique se os arquivos de entrada existem e têm o formato correto")

if __name__ == "__main__":
    try:
        # Executa o pipeline de preparação de dados
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Script interrompido pelo usuário.")
    except Exception as e:
        print(f"\n💥 Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
