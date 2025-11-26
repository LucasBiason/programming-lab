# Fase 3 - LangChain e Fine-Tuning

Conteúdo da Fase 3 do curso FIAP IA para Devs sobre LangChain, Fine-Tuning e RAG.

## Estrutura

```
FASE 03 - LangChain e Fine-Tuning/
├── langchain/          # Agentes LLM com LangChain
├── prompts/            # Otimização de prompts
├── fine-tuning/        # Fine-tuning de modelos
└── rag/                # Retrieval Augmented Generation
```

## Projetos

### LangChain

**agent-investimentos.py**
- Agente LLM para consulta de ações brasileiras
- Usa OpenAI com function calling
- Busca preços e gera gráficos de ações
- Interface Streamlit

**Como usar:**
```bash
pip install streamlit openai python-dotenv yfinance matplotlib pandas
streamlit run agent-investimentos.py
```

### RAG

**assistente-receitas.py**
- Assistente de receitas usando RAG
- LangChain + ChromaDB para busca vetorial
- OpenAI para geração de respostas
- Interface Streamlit

**Como usar:**
```bash
pip install streamlit streamlit-chat langchain langchain-openai langchain-community chromadb python-dotenv
streamlit run assistente-receitas.py
```

### Fine-Tuning

Projetos completos de fine-tuning de modelos para sumarização de notícias:
- Preparação de dados
- Fine-tuning com Unsloth
- Aplicação RAG

Ver notebooks em `fine-tuning/fine-tuning-rag-documentos-fiap-main/`

## Tecnologias

- LangChain
- OpenAI API
- ChromaDB
- Streamlit
- Unsloth (fine-tuning)
- Transformers

## Notas

- Todos os códigos foram simplificados e adaptados
- Mantém funcionalidade original
- Comentários em português
- Estrutura organizada por tema

