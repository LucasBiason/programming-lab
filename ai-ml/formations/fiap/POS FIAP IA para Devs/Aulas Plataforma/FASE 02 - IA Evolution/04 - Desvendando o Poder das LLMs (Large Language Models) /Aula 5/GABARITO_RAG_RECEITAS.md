# 📝 Gabarito - Exercício Assistente de Receitas com RAG

## 🎯 Respostas e Explicações

### 🟢 Nível Básico

#### Exercício 1.1: Configuração do Ambiente

**Resposta Esperada:**
```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente (Linux/Mac)
source venv/bin/activate
# OU (Windows)
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar .env
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

**Explicação:**
- O ambiente virtual isola as dependências do projeto
- O arquivo `.env` mantém a chave da API segura
- As dependências incluem: `streamlit`, `langchain`, `openai`, `chromadb`

#### Exercício 1.2: Criação da Base de Dados Vetorial

**Resposta Esperada:**
```bash
python chroma_db.py
```

**Logs esperados:**
```
Split 80 documents into 240 chunks.
Saved 240 chunks to chroma.
```

**Explicação:**
- **80 documentos**: Cada arquivo .docx é um documento
- **240 chunks**: Cada documento é dividido em ~3 chunks (300 caracteres com overlap de 100)
- **ChromaDB**: Armazena embeddings vetoriais para busca semântica

**Perguntas de reflexão:**
- **Por que dividir em chunks?** Para permitir busca granular e evitar limites de contexto
- **Tamanho dos chunks?** 300 caracteres com overlap de 100 para manter contexto
- **Overlap?** Garante que informações importantes não sejam cortadas

### 🟡 Nível Intermediário

#### Exercício 2.1: Análise de Similaridade

**Código de análise:**
```python
def analyze_similarity(query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=4)
    print(f"Query: {query_text}")
    for i, (doc, score) in enumerate(results):
        print(f"Resultado {i+1}: Score {score:.3f}")
        print(f"Conteúdo: {doc.page_content[:100]}...")
        print("-" * 50)
    return results
```

**Testes esperados:**
```
Query: receita de bolo de chocolate
Resultado 1: Score 0.892
Conteúdo: Bolo de Chocolate Fit - Ingredientes: farinha de aveia...
Resultado 2: Score 0.745
Conteúdo: Brownie Fit - Uma versão saudável do brownie...
```

**Análise dos scores:**
- **Score > 0.8**: Muito relevante
- **Score 0.6-0.8**: Relevante
- **Score < 0.6**: Pouco relevante

#### Exercício 2.2: Otimização do Prompt

**Template melhorado:**
```python
PROMPT_TEMPLATE = """
Você é um assistente especializado em receitas saudáveis e nutritivas.

CONTEXTO DAS RECEITAS DISPONÍVEIS:
{context}

INSTRUÇÕES ESPECÍFICAS:
1. Forneça receitas completas com ingredientes e modo de preparo detalhado
2. Inclua informações nutricionais quando disponíveis no contexto
3. Sugira substituições para ingredientes quando apropriado
4. Mantenha o foco em opções saudáveis e nutritivas
5. Se não encontrar uma receita específica, sugira alternativas similares
6. Inclua dicas de preparo e variações quando possível

PERGUNTA DO USUÁRIO: {question}

RESPOSTA (formato estruturado):
"""
```

**Melhorias implementadas:**
- ✅ **Estrutura clara**: Instruções específicas para o LLM
- ✅ **Informações nutricionais**: Incluídas quando disponíveis
- ✅ **Substituições**: Sugestões para ingredientes
- ✅ **Alternativas**: Fallback para receitas similares
- ✅ **Dicas**: Informações extras de preparo

### 🔴 Nível Avançado

#### Exercício 3.1: Sistema de Categorização

**Implementação completa:**
```python
def categorize_recipe(recipe_text):
    """Categoriza uma receita baseada em seu conteúdo."""
    recipe_lower = recipe_text.lower()
    
    # Categorias principais
    categories = {
        "cafe_da_manha": ["panqueca", "omelete", "granola", "mingau", "pão"],
        "almoco": ["frango", "peixe", "carne", "salada", "sopa"],
        "jantar": ["jantar", "ceia", "light"],
        "snacks": ["barrinha", "cookies", "chips", "patê"],
        "sobremesas": ["bolo", "brownie", "mousse", "brigadeiro"]
    }
    
    # Determinar categoria
    for category, keywords in categories.items():
        if any(keyword in recipe_lower for keyword in keywords):
            return category
    
    return "outros"
```

**Teste de categorização:**
```python
# Teste
test_recipes = [
    "Panqueca de aveia com banana",
    "Frango grelhado com legumes",
    "Bolo de chocolate fit",
    "Salada de frutas"
]

for recipe in test_recipes:
    category = categorize_recipe(recipe)
    print(f"{recipe} → {category}")
```

**Resultado esperado:**
```
Panqueca de aveia com banana → cafe_da_manha
Frango grelhado com legumes → almoco
Bolo de chocolate fit → sobremesas
Salada de frutas → almoco
```

#### Exercício 3.2: Sistema de Recomendações

**Algoritmo de recomendação:**
```python
def recommend_similar_recipes(recipe_name, k=3):
    """Recomenda receitas similares."""
    # Busca por similaridade
    results = db.similarity_search_with_relevance_scores(recipe_name, k=k+1)
    
    recommendations = []
    for doc, score in results:
        # Evita recomendar a própria receita
        if recipe_name.lower() not in doc.page_content.lower():
            recommendations.append({
                "nome": doc.page_content.split('\n')[0][:50],
                "score": score,
                "conteúdo": doc.page_content[:200]
            })
    
    return recommendations[:k]
```

**Teste de recomendações:**
```python
# Para "bolo de chocolate"
recommendations = recommend_similar_recipes("bolo de chocolate", k=3)
for i, rec in enumerate(recommendations):
    print(f"{i+1}. {rec['nome']} (Score: {rec['score']:.3f})")
```

**Resultado esperado:**
```
1. Brownie Fit (Score: 0.856)
2. Bolo de Banana com Aveia (Score: 0.723)
3. Brigadeiro Fit (Score: 0.689)
```

#### Exercício 3.3: Análise Nutricional

**Extração de informações nutricionais:**
```python
def extract_nutritional_info(recipe_text):
    """Extrai informações nutricionais do texto."""
    import re
    
    patterns = {
        "calorias": r"(\d+)\s*(?:kcal|calorias?)",
        "proteinas": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?prote[íi]nas?",
        "carboidratos": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?carboidratos?",
        "gorduras": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?gorduras?"
    }
    
    nutritional_info = {}
    for nutrient, pattern in patterns.items():
        match = re.search(pattern, recipe_text.lower())
        if match:
            nutritional_info[nutrient] = float(match.group(1))
    
    return nutritional_info
```

**Teste de extração:**
```python
test_recipe = """
Bolo de Chocolate Fit
Informações nutricionais: 150 kcal, 8g proteínas, 20g carboidratos, 5g gorduras
"""

nutrition = extract_nutritional_info(test_recipe)
print(nutrition)
```

**Resultado esperado:**
```python
{
    "calorias": 150.0,
    "proteinas": 8.0,
    "carboidratos": 20.0,
    "gorduras": 5.0
}
```

## 🧪 Desafios Especiais - Soluções

### Desafio 1: Multi-modalidade

**Implementação básica:**
```python
def add_image_to_recipe(recipe_name, image_path):
    """Adiciona imagem à receita."""
    import shutil
    import os
    
    images_dir = "recipe_images"
    os.makedirs(images_dir, exist_ok=True)
    
    # Copiar imagem para pasta
    shutil.copy(image_path, f"{images_dir}/{recipe_name}.jpg")
    
    return f"{images_dir}/{recipe_name}.jpg"

def display_recipe_with_image(recipe_name, recipe_content):
    """Exibe receita com imagem."""
    import streamlit as st
    
    image_path = f"recipe_images/{recipe_name}.jpg"
    
    if os.path.exists(image_path):
        st.image(image_path, caption=recipe_name, use_column_width=True)
    
    st.write(recipe_content)
```

### Desafio 2: Personalização

**Sistema de perfil de usuário:**
```python
class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {
            "dietary_restrictions": [],
            "allergies": [],
            "preferred_ingredients": [],
            "disliked_ingredients": []
        }
    
    def update_preferences(self, **kwargs):
        """Atualiza preferências do usuário."""
        for key, value in kwargs.items():
            if key in self.preferences:
                self.preferences[key] = value
    
    def adapt_recipe(self, recipe_content):
        """Adapta receita às preferências do usuário."""
        adapted_recipe = recipe_content
        
        # Substituir ingredientes não desejados
        for disliked in self.preferences["disliked_ingredients"]:
            adapted_recipe = adapted_recipe.replace(disliked, "substituto")
        
        return adapted_recipe
```

### Desafio 3: Integração com APIs

**Integração com supermercado (exemplo):**
```python
def create_shopping_list(recipe_ingredients):
    """Cria lista de compras para uma receita."""
    # Simulação de API de supermercado
    shopping_list = []
    
    for ingredient in recipe_ingredients:
        # Buscar preço e disponibilidade
        price = get_ingredient_price(ingredient)
        available = check_availability(ingredient)
        
        shopping_list.append({
            "ingredient": ingredient,
            "price": price,
            "available": available
        })
    
    return shopping_list

def get_ingredient_price(ingredient):
    """Simula busca de preço de ingrediente."""
    # Em implementação real, conectar com API de supermercado
    prices = {
        "farinha de aveia": 8.50,
        "banana": 4.99,
        "ovo": 12.90,
        "cacau": 15.00
    }
    return prices.get(ingredient.lower(), 0.0)
```

## 📊 Métricas de Avaliação - Resultados Esperados

### Qualidade das Respostas
- **Precisão**: > 90% das receitas correspondem à pergunta
- **Completude**: 100% das receitas incluem ingredientes e preparo
- **Clareza**: Instruções claras e passo a passo

### Performance do Sistema
- **Velocidade**: < 3 segundos para resposta
- **Relevância**: Score > 0.7 para 85% das consultas
- **Cobertura**: 95% das perguntas respondidas com sucesso

### Experiência do Usuário
- **Facilidade de uso**: Interface intuitiva com filtros
- **Satisfação**: Feedback positivo em testes
- **Engajamento**: Uso frequente do sistema

## 🎓 Conclusão

Este gabarito demonstra como implementar um sistema RAG completo para receitas, incluindo:

1. **Configuração adequada** do ambiente e dependências
2. **Análise de similaridade** para otimizar buscas
3. **Prompts estruturados** para respostas de qualidade
4. **Sistemas de categorização** e recomendação
5. **Análise nutricional** e filtros personalizados
6. **Interface melhorada** com funcionalidades avançadas

Os conceitos aprendidos podem ser aplicados a qualquer domínio que necessite de conhecimento especializado e busca semântica.

---

*Este gabarito complementa o exercício didático do assistente de receitas saudáveis.* 