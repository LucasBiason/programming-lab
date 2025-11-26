# News Scraper CNN + IA - Pipeline Completo

Script Python para extrair links e conteúdo de notícias da CNN e gerar resumos automáticos com Inteligência Artificial (GPT).

## 🎯 **Objetivo Educacional**

Este projeto demonstra um pipeline completo de **Data Science** e **Inteligência Artificial**:
1. **Web Scraping** - Extração automática de dados da web
2. **Processamento de Linguagem Natural** - Análise e limpeza de texto
3. **IA Generativa** - Geração de resumos com GPT
4. **Pipeline de Dados** - Fluxo automatizado de processamento

## Problemas Corrigidos

1. **Filtro muito restritivo**: O filtro original `href.startswith('/') and href.endswith('.html')` era muito específico
2. **Seletores CSS desatualizados**: Adicionados múltiplos seletores para capturar conteúdo
3. **Falta de headers**: Adicionados headers para simular navegador real
4. **Tratamento de erros**: Melhorado o tratamento de exceções
5. **Debugging**: Adicionadas funções para debugar problemas

## 🚀 **Instalação e Configuração**

### 1. **Instalar Dependências**
```bash
pip install -r requirements.txt
```

### 2. **Configurar API da OpenAI**
1. Crie uma conta em [OpenAI Platform](https://platform.openai.com/)
2. Obtenha sua chave de API em [API Keys](https://platform.openai.com/api-keys)
3. Copie o arquivo de exemplo:
   ```bash
   cp env.example .env
   ```
4. Edite o arquivo `.env` e adicione sua chave:
   ```
   OPENAI_API_KEY=sua_chave_real_aqui
   ```

### 3. **Executar o Script**
```bash
python3 news_scrapper.py
```

## 🔧 **Funcionalidades**

### 1. **Extração de Links (Web Scraping)**
- 🔍 Busca automática por links de notícias na CNN
- 🎯 Filtro inteligente para capturar URLs relevantes
- 💾 Salva links em `CNN_Links.txt`

### 2. **Extração de Conteúdo (NLP)**
- 📰 Múltiplos seletores CSS para máxima compatibilidade
- 🔄 Sistema de fallback automático
- 💾 Salva conteúdo em `news_contents.json`

### 3. **Geração de Resumos com IA**
- 🤖 Integração com API da OpenAI (GPT-3.5-turbo)
- 📝 Resumos automáticos e inteligentes
- 💾 Salva resumos em `news_summaries.json`

### 4. **Pipeline Automatizado**
- ⚡ Execução completa sem intervenção manual
- 📊 Relatórios detalhados de cada etapa
- 🎯 Processamento otimizado e eficiente

### 5. **Preparação para Fine-tuning**
- 📚 Processamento de datasets do Hugging Face
- 🔄 Formatação automática de prompts
- 💾 Geração de dados estruturados para treinamento

## Seletores CSS Utilizados

1. `div.article__content` - Seletor original
2. `p` - Todos os parágrafos (filtrados por tamanho)
3. `div.zn-body__paragraph` - Classe específica da CNN
4. `div.l-container` - Container principal
5. `article` - Tag article
6. Seletores com wildcard para classes contendo "article" ou "content"

## 📁 **Arquivos Gerados**

### **Web Scraping**
- `CNN_Links.txt` - Lista de URLs encontradas
- `news_contents.json` - Conteúdo extraído das notícias
- `news_summaries.json` - Resumos gerados pela IA

### **Fine-tuning**
- `news_dataset_finetuning.json` - Dados formatados para treinamento
- `data_example.jsonl` - Exemplo de formato JSON Lines

## 🎮 **Uso**

### **Execução Automática (Recomendado)**
```bash
python3 news_scrapper.py
```

O script executa automaticamente todas as etapas:
1. 🔍 **Extração de Links** - Busca notícias na CNN
2. 📰 **Extração de Conteúdo** - Captura texto das notícias  
3. 🤖 **Geração de Resumos** - Cria resumos com IA
4. 📊 **Relatório Final** - Mostra estatísticas completas

### **Preparação para Fine-tuning**
```bash
python3 finetunning_news.py
```

Este script prepara os dados para treinamento:
1. 📚 **Carrega Dataset** - Hugging Face + dados locais
2. 🔄 **Processa Dados** - Formata prompts para fine-tuning
3. 💾 **Gera Arquivo** - Dados prontos para treinamento

## 🚀 **Melhorias Implementadas**

### **Web Scraping Robusto**
- 🌐 Headers de navegador para evitar bloqueios
- ⏱️ Timeout nas requisições
- 🕐 Pausa entre requisições (ética)
- 🎯 Múltiplos seletores CSS como fallback

### **Processamento Inteligente**
- 🤖 Integração com API da OpenAI
- 📝 Geração automática de resumos
- 🔄 Sistema de fallback robusto
- 💾 Armazenamento em formato JSON

### **Pipeline Otimizado**
- ⚡ Execução automática completa
- 📊 Relatórios detalhados
- 🎯 Tratamento robusto de erros
- 📚 Comentários educativos no código

## 🧠 **Conceitos de IA Aplicados**

### **Prompt Engineering**
- 🎯 Instruções claras e específicas para a IA
- 🔧 Formato de resposta estruturado (JSON)
- ⚙️ Parâmetros otimizados (temperature, max_tokens)

### **Processamento de Linguagem Natural**
- 📰 Análise e limpeza de texto
- 🔍 Extração de conteúdo relevante
- 📝 Geração de resumos inteligentes

### **Integração de APIs**
- 🔑 Gerenciamento seguro de chaves
- 🌐 Comunicação com serviços externos
- 📊 Processamento de respostas estruturadas

## 🎓 **Aprendizados**

Este projeto demonstra conceitos fundamentais de:
- **Data Engineering**: Pipeline de dados automatizado
- **Web Scraping**: Extração ética de dados da web
- **NLP**: Processamento de texto em português
- **IA Generativa**: Uso prático de modelos de linguagem
- **DevOps**: Gerenciamento de dependências e configurações
