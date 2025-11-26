# 🍳 Exercícios Didáticos - Assistente de Receitas Saudáveis

## 📋 Visão Geral

Este conjunto de exercícios foi desenvolvido para demonstrar a implementação prática de um sistema **RAG (Retrieval Augmented Generation)** usando LLMs. O projeto foca na criação de um assistente de receitas saudáveis que combina busca vetorial com geração de texto.

## 🎯 Objetivos de Aprendizado

1. **Compreender** o funcionamento do RAG
2. **Implementar** um sistema de busca vetorial com ChromaDB
3. **Integrar** LLMs com bases de dados especializadas
4. **Otimizar** prompts para melhor qualidade de respostas
5. **Desenvolver** funcionalidades avançadas como categorização e recomendações

## 📁 Estrutura dos Arquivos

```
Aula 5/
├── README_EXERCICIOS.md                    # Este arquivo
├── EXERCICIO_DIDATICO_ASSISTENTE_RECEITAS.md  # Exercício principal
├── EXERCICIOS_PRATICOS_SOLUCOES.py         # Implementações práticas
├── GABARITO_EXERCICIOS.md                  # Respostas e explicações
├── Assistente de Receitas Saudáveis.py     # Aplicação original
├── chroma_db.py                           # Script de processamento
├── requirements.txt                        # Dependências
└── receitas/                              # Base de dados de receitas
    ├── Bolo de chocolate fit.docx
    ├── Panqueca de aveia.docx
    └── ... (80+ receitas)
```

## 🚀 Como Usar

### 1. Configuração Inicial

```bash
# 1. Navegar para o diretório
cd "Aula 5"

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Configurar arquivo .env
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

### 2. Executar o Sistema Básico

```bash
# 1. Processar documentos e criar base vetorial
python chroma_db.py

# 2. Executar aplicação Streamlit
streamlit run "Assistente de Receitas Saudáveis.py"
```

### 3. Executar Exercícios Práticos

```bash
# Executar implementações dos exercícios
python EXERCICIOS_PRATICOS_SOLUCOES.py
```

## 📚 Progression dos Exercícios

### 🟢 Nível Básico
**Foco**: Configuração e compreensão básica

1. **Configuração do Ambiente**
   - Criar ambiente virtual
   - Instalar dependências
   - Configurar API keys

2. **Criação da Base de Dados Vetorial**
   - Processar documentos
   - Entender chunks e embeddings
   - Analisar logs de processamento

### 🟡 Nível Intermediário
**Foco**: Otimização e análise

1. **Análise de Similaridade**
   - Implementar função de análise
   - Testar diferentes queries
   - Ajustar thresholds

2. **Otimização do Prompt**
   - Melhorar template do prompt
   - Adicionar instruções específicas
   - Testar qualidade das respostas

### 🔴 Nível Avançado
**Foco**: Funcionalidades avançadas

1. **Sistema de Categorização**
   - Implementar metadados
   - Criar filtros por categoria
   - Desenvolver interface de filtros

2. **Sistema de Recomendações**
   - Criar algoritmo de recomendação
   - Implementar histórico de usuário
   - Desenvolver análise de preferências

3. **Análise Nutricional**
   - Extrair informações nutricionais
   - Implementar filtros por restrições
   - Criar sistema de substituições

## 🧪 Desafios Especiais

### Desafio 1: Multi-modalidade
- Integrar imagens às receitas
- Implementar busca por similaridade visual
- Gerar descrições de imagens com IA

### Desafio 2: Personalização
- Criar perfil de usuário
- Adaptar receitas automaticamente
- Sugerir substituições personalizadas

### Desafio 3: Integração com APIs
- Conectar com APIs de supermercado
- Integrar com aplicativos de fitness
- Conectar com redes sociais

## 📊 Avaliação

### Critérios de Avaliação

1. **Funcionalidade** (40%)
   - Sistema funciona corretamente
   - Respostas são relevantes
   - Interface é intuitiva

2. **Qualidade do Código** (30%)
   - Código bem estruturado
   - Documentação adequada
   - Tratamento de erros

3. **Inovação** (20%)
   - Funcionalidades extras implementadas
   - Melhorias no sistema original
   - Otimizações criativas

4. **Apresentação** (10%)
   - Documentação clara
   - Explicações técnicas
   - Demonstração funcional

### Métricas de Performance

- **Velocidade**: < 3 segundos para resposta
- **Precisão**: > 90% de respostas relevantes
- **Cobertura**: 95% de perguntas respondidas
- **Usabilidade**: Interface intuitiva e responsiva

## 🛠️ Tecnologias Utilizadas

### Core Technologies
- **Python 3.8+**: Linguagem principal
- **Streamlit**: Interface web
- **LangChain**: Framework para LLMs
- **ChromaDB**: Base de dados vetorial
- **OpenAI API**: LLM para geração de texto

### Dependências Principais
```
streamlit>=1.28.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-openai>=0.0.5
openai>=1.0.0
chromadb>=0.4.0
python-dotenv>=1.0.0
unstructured>=0.10.0
```

## 🎓 Conceitos Aprendidos

### RAG (Retrieval Augmented Generation)
- **Recuperação**: Busca semântica em base de dados
- **Geração**: Uso de LLMs para criar respostas
- **Contexto**: Combinação de dados recuperados com prompts

### Vector Databases
- **Embeddings**: Representações numéricas de texto
- **Similaridade**: Cálculo de relevância entre queries
- **Indexação**: Organização eficiente de dados vetoriais

### LLM Integration
- **Prompts**: Estruturação de instruções para LLMs
- **Contexto**: Uso de informações externas
- **Fine-tuning**: Otimização de respostas

## 🔧 Troubleshooting

### Problemas Comuns

1. **Erro de API Key**
   ```
   Error: OPENAI_API_KEY not found
   Solução: Verificar arquivo .env
   ```

2. **Erro de dependências**
   ```
   ModuleNotFoundError: No module named 'langchain'
   Solução: pip install -r requirements.txt
   ```

3. **Erro de ChromaDB**
   ```
   Error: ChromaDB not found
   Solução: Executar python chroma_db.py primeiro
   ```

4. **Respostas irrelevantes**
   ```
   Problema: Score de similaridade baixo
   Solução: Ajustar threshold ou melhorar base de dados
   ```

### Dicas de Debug

1. **Verificar logs**: Analisar saída do `chroma_db.py`
2. **Testar queries**: Usar função `analyze_similarity()`
3. **Validar prompts**: Verificar template do prompt
4. **Monitorar performance**: Medir tempo de resposta

## 📖 Recursos Adicionais

### Documentação
- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### Artigos e Tutoriais
- [RAG: Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)
- [Vector Databases for AI](https://www.pinecone.io/learn/vector-database/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Projetos Relacionados
- [LangChain Cookbook](https://github.com/langchain-ai/langchain)
- [ChromaDB Examples](https://github.com/chroma-core/chroma)
- [Streamlit Gallery](https://streamlit.io/gallery)

## 🤝 Contribuição

Para contribuir com melhorias nos exercícios:

1. **Fork** o repositório
2. **Crie** uma branch para sua feature
3. **Implemente** as melhorias
4. **Teste** todas as funcionalidades
5. **Documente** as mudanças
6. **Submeta** um pull request

## 📄 Licença

Este material é parte do curso de IA da FIAP e está disponível para uso educacional.

---

**Desenvolvido para o curso de IA da FIAP - Demonstrando aplicações práticas de LLMs e RAG** 