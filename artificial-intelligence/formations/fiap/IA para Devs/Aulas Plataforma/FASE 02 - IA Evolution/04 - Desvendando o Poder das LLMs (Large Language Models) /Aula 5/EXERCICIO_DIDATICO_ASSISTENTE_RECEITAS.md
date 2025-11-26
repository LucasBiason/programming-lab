# 🍳 Exercício Didático: Assistente de Receitas Saudáveis com RAG

## 📚 Contexto Teórico

### O que é RAG (Retrieval Augmented Generation)?
RAG é uma técnica que combina **recuperação de informações** com **geração de texto** usando LLMs. Em vez de o modelo gerar respostas apenas com seu conhecimento pré-treinado, o RAG:

1. **Recupera** documentos relevantes de uma base de dados
2. **Usa** esses documentos como contexto
3. **Gera** respostas baseadas no contexto recuperado

### Por que usar RAG para receitas?
- ✅ **Precisão**: Respostas baseadas em receitas reais e testadas
- ✅ **Especialização**: Conhecimento específico sobre culinária saudável
- ✅ **Atualização**: Fácil adição de novas receitas
- ✅ **Controle**: Evita "alucinações" do modelo

## 🎯 Objetivos do Exercício

1. **Compreender** o funcionamento do RAG
2. **Implementar** um sistema de busca vetorial
3. **Integrar** LLMs com bases de dados especializadas
4. **Otimizar** a qualidade das respostas

## 🛠️ Componentes do Sistema

### 1. Base de Dados de Receitas
- **Formato**: Documentos Word (.docx) com receitas saudáveis
- **Estrutura**: 80+ receitas organizadas por categoria
- **Conteúdo**: Ingredientes, modo de preparo, informações nutricionais

### 2. Pipeline de Processamento
```python
# Fluxo de processamento
Documentos → Chunks → Embeddings → VectorDB → Busca → Contexto → LLM → Resposta
```

### 3. Interface de Usuário
- **Streamlit**: Interface web interativa
- **Chat**: Conversação natural com o assistente
- **Histórico**: Manutenção do contexto da conversa

## 📋 Exercícios Práticos

### 🟢 Nível Básico: Configuração e Teste

#### Exercício 1.1: Configuração do Ambiente
**Objetivo**: Preparar o ambiente de desenvolvimento

**Tarefas**:
1. Criar ambiente virtual: `python -m venv venv`
2. Ativar ambiente: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
3. Instalar dependências: `pip install -r requirements.txt`
4. Configurar arquivo `.env` com sua chave da OpenAI

**Código de teste**:
```python
import os
from dotenv import load_dotenv

load_dotenv()
print(f"API Key configurada: {'Sim' if os.getenv('OPENAI_API_KEY') else 'Não'}")
```

#### Exercício 1.2: Criação da Base de Dados Vetorial
**Objetivo**: Processar documentos e criar embeddings

**Tarefas**:
1. Executar `python chroma_db.py`
2. Verificar se a pasta `chroma/` foi criada
3. Analisar os logs de processamento

**Perguntas para reflexão**:
- Quantos documentos foram processados?
- Quantos chunks foram criados?
- Por que dividimos os documentos em chunks?

### 🟡 Nível Intermediário: Otimização e Análise

#### Exercício 2.1: Análise de Similaridade
**Objetivo**: Compreender como funciona a busca vetorial

**Tarefas**:
1. Modificar o código para mostrar os scores de similaridade
2. Testar diferentes queries e analisar os resultados
3. Ajustar o threshold de similaridade (0.7)

**Código para análise**:
```python
def analyze_similarity(query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=4)
    print(f"Query: {query_text}")
    for i, (doc, score) in enumerate(results):
        print(f"Resultado {i+1}: Score {score:.3f}")
        print(f"Conteúdo: {doc.page_content[:100]}...")
        print("-" * 50)
```

#### Exercício 2.2: Otimização do Prompt
**Objetivo**: Melhorar a qualidade das respostas

**Tarefas**:
1. Analisar o template atual do prompt
2. Propor melhorias para incluir:
   - Informações nutricionais
   - Tempo de preparo
   - Dificuldade da receita
   - Substituições possíveis

**Template melhorado**:
```python
PROMPT_TEMPLATE = """
Você é um assistente de receitas saudáveis especializado.

Contexto das receitas disponíveis:
{context}

Instruções:
- Forneça receitas completas com ingredientes e modo de preparo
- Inclua informações nutricionais quando disponíveis
- Sugira substituições para ingredientes
- Mantenha o foco em opções saudáveis e nutritivas

Pergunta do usuário: {question}

Resposta:
"""
```

### 🔴 Nível Avançado: Funcionalidades Extras

#### Exercício 3.1: Sistema de Categorização
**Objetivo**: Implementar filtros por categoria de receita

**Tarefas**:
1. Adicionar metadados aos documentos (categoria, tempo, dificuldade)
2. Implementar busca filtrada por categoria
3. Criar interface para seleção de filtros

**Implementação**:
```python
def get_recipes_by_category(category, query_text):
    """Busca receitas por categoria específica"""
    # Implementar lógica de filtro por categoria
    pass

def add_category_filter():
    """Interface para filtros de categoria"""
    categories = ["Café da manhã", "Almoço", "Jantar", "Snacks", "Sobremesas"]
    selected = st.selectbox("Categoria:", categories)
    return selected
```

#### Exercício 3.2: Sistema de Recomendações
**Objetivo**: Implementar recomendações baseadas em histórico

**Tarefas**:
1. Armazenar histórico de receitas visualizadas
2. Implementar algoritmo de recomendação
3. Sugerir receitas similares

**Algoritmo de recomendação**:
```python
def recommend_similar_recipes(recipe_name, k=3):
    """Recomenda receitas similares baseadas em uma receita"""
    # Buscar receita no banco
    # Encontrar receitas com ingredientes similares
    # Retornar top-k recomendações
    pass
```

#### Exercício 3.3: Análise Nutricional
**Objetivo**: Adicionar informações nutricionais às receitas

**Tarefas**:
1. Extrair informações nutricionais dos documentos
2. Calcular valores nutricionais por porção
3. Implementar filtros por restrições alimentares

**Implementação**:
```python
def extract_nutritional_info(recipe_text):
    """Extrai informações nutricionais do texto da receita"""
    # Usar regex ou NLP para extrair valores
    # Calorias, proteínas, carboidratos, gorduras
    pass

def filter_by_dietary_restrictions(recipes, restrictions):
    """Filtra receitas por restrições alimentares"""
    # Vegetariano, vegano, sem glúten, low-carb
    pass
```

## 🧪 Desafios Especiais

### Desafio 1: Multi-modalidade
**Objetivo**: Integrar imagens das receitas

**Tarefas**:
1. Adicionar imagens às receitas
2. Implementar busca por similaridade visual
3. Gerar descrições de imagens com IA

### Desafio 2: Personalização
**Objetivo**: Adaptar receitas às preferências do usuário

**Tarefas**:
1. Criar perfil de usuário (preferências, alergias)
2. Adaptar receitas automaticamente
3. Sugerir substituições personalizadas

### Desafio 3: Integração com APIs
**Objetivo**: Conectar com serviços externos

**Tarefas**:
1. Integrar com API de supermercados para lista de compras
2. Conectar com aplicativos de fitness para tracking
3. Integrar com redes sociais para compartilhamento

## 📊 Métricas de Avaliação

### Qualidade das Respostas
- **Precisão**: A receita corresponde à pergunta?
- **Completude**: Todos os passos estão incluídos?
- **Clareza**: As instruções são claras?

### Performance do Sistema
- **Velocidade**: Tempo de resposta < 3 segundos
- **Relevância**: Score de similaridade > 0.7
- **Cobertura**: % de perguntas respondidas com sucesso

### Experiência do Usuário
- **Facilidade de uso**: Interface intuitiva
- **Satisfação**: Feedback positivo dos usuários
- **Engajamento**: Frequência de uso

## 🎓 Conclusão

Este exercício demonstra como construir um sistema RAG completo, desde o processamento de dados até a interface de usuário. Os conceitos aprendidos podem ser aplicados a qualquer domínio que necessite de conhecimento especializado.

### Próximos Passos
1. **Expandir** a base de dados com mais receitas
2. **Otimizar** os embeddings para melhor performance
3. **Implementar** funcionalidades avançadas
4. **Deploy** em produção com monitoramento

### Recursos Adicionais
- [Documentação LangChain](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

*Este exercício foi desenvolvido para o curso de IA da FIAP, demonstrando aplicações práticas de LLMs e RAG.* 