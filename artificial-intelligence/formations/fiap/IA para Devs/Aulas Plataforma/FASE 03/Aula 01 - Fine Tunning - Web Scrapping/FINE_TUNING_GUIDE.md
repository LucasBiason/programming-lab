# 🎯 Guia de Fine-tuning para Modelos de IA

## 📋 **Visão Geral**

Este guia explica como usar os scripts para preparar dados e realizar fine-tuning de modelos de IA para resumo de notícias.

## 🚀 **Pipeline Completo**

### **1. Web Scraping + Geração de Resumos**
```bash
python3 news_scrapper.py
```
- Extrai notícias da CNN
- Gera resumos com GPT
- Cria `news_summaries.json`

### **2. Preparação para Fine-tuning**
```bash
python3 finetunning_news.py
```
- Processa dados do Hugging Face
- Combina com dados locais
- Gera `news_dataset_finetuning.json`

## 📊 **Formato dos Dados**

### **Estrutura do Prompt**
```
SUMMARIZE THIS NEWS.

[|News|] {texto_da_noticia}[|eNews|]

[|summary|]{resumo_esperado}[|esummary|]
```

### **Arquivo de Saída**
```json
{
  "metadata": {
    "total_records": 3,
    "sources": ["huggingface", "local_news"],
    "format": "fine-tuning_prompt"
  },
  "data": [
    {
      "input": "prompt_formatado_aqui",
      "source": "huggingface",
      "index": 0
    }
  ]
}
```

## 🔧 **Configuração**

### **Arquivo .env**
```bash
OPENAI_API_KEY=sua_chave_aqui
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=150
TEMPERATURE=0.3
```

### **Dependências**
```bash
pip install -r requirements.txt
```

## 📁 **Arquivos Necessários**

### **Para Web Scraping**
- `news_scrapper.py` - Script principal
- `.env` - Configuração da API

### **Para Fine-tuning**
- `finetunning_news.py` - Preparação de dados
- `data.jsonl` - Dataset do Hugging Face (opcional)
- `news_summaries.json` - Dados locais (gerado pelo scraper)

## 🎯 **Próximos Passos**

### **1. Treinamento do Modelo**
- Use `news_dataset_finetuning.json` para treinar
- Ajuste hiperparâmetros conforme necessário
- Valide com dados de teste

### **2. Deploy**
- Exporte o modelo treinado
- Integre em sua aplicação
- Monitore performance

## 💡 **Dicas Importantes**

### **Qualidade dos Dados**
- Verifique a qualidade dos resumos gerados
- Limpe dados duplicados ou de baixa qualidade
- Balanceie diferentes tipos de notícias

### **Formato dos Prompts**
- Mantenha consistência nos marcadores
- Teste diferentes formatos de prompt
- Valide com exemplos reais

### **Performance**
- Monitore o tempo de processamento
- Otimize para grandes volumes de dados
- Use cache quando apropriado

## 🚨 **Troubleshooting**

### **Erro: Arquivo não encontrado**
```bash
# Verifique se os arquivos existem
ls -la *.json *.jsonl

# Execute o scraper primeiro
python3 news_scrapper.py
```

### **Erro: API OpenAI**
```bash
# Verifique o arquivo .env
cat .env

# Teste a conexão
python3 -c "import openai; print('OK')"
```

### **Erro: Formato de dados**
```bash
# Verifique a estrutura do JSON
python3 -c "import json; data=json.load(open('news_summaries.json')); print(data.keys())"
```

## 📚 **Recursos Adicionais**

- [OpenAI Fine-tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [JSON Lines Format](https://jsonlines.org/)

## 🎓 **Conceitos Aplicados**

- **Web Scraping**: Extração automática de dados
- **NLP**: Processamento de linguagem natural
- **Prompt Engineering**: Formatação de instruções para IA
- **Data Pipeline**: Fluxo automatizado de processamento
- **Fine-tuning**: Adaptação de modelos pré-treinados




