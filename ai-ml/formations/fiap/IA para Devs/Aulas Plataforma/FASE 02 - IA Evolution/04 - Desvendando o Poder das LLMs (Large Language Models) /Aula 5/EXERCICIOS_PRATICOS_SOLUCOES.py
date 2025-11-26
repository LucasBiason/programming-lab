# 🍳 Exercícios Práticos - Assistente de Receitas Saudáveis
# Soluções e Implementações

import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import pandas as pd

# Carregar configurações
load_dotenv()
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Configurações
CHROMA_PATH = "chroma"
embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

## 🟢 EXERCÍCIO 1: Análise de Similaridade

def analyze_similarity(query_text):
    """
    Analisa a similaridade entre uma query e os documentos na base de dados.
    
    Args:
        query_text (str): Texto da consulta do usuário
        
    Returns:
        list: Lista de tuplas (documento, score) ordenadas por relevância
    """
    results = db.similarity_search_with_relevance_scores(query_text, k=4)
    
    print(f"🔍 Query: {query_text}")
    print(f"📊 Encontrados {len(results)} resultados")
    print("-" * 60)
    
    for i, (doc, score) in enumerate(results):
        print(f"📄 Resultado {i+1}: Score {score:.3f}")
        print(f"📝 Conteúdo: {doc.page_content[:150]}...")
        print("-" * 60)
    
    return results

# Teste da função
if __name__ == "__main__":
    queries_teste = [
        "receita de bolo de chocolate",
        "como fazer omelete",
        "salada saudável",
        "sobremesa fit"
    ]
    
    for query in queries_teste:
        analyze_similarity(query)
        print("\n" + "="*80 + "\n")

## 🟡 EXERCÍCIO 2: Otimização do Prompt

def create_enhanced_prompt_template():
    """
    Cria um template de prompt melhorado para o assistente de receitas.
    
    Returns:
        str: Template do prompt otimizado
    """
    enhanced_template = """
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
    
    return enhanced_template

def get_enhanced_response(query_text, context):
    """
    Gera resposta usando o prompt otimizado.
    
    Args:
        query_text (str): Pergunta do usuário
        context (str): Contexto das receitas encontradas
        
    Returns:
        str: Resposta gerada pelo LLM
    """
    prompt_template = create_enhanced_prompt_template()
    prompt = prompt_template.format(context=context, question=query_text)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um chef especializado em receitas saudáveis e nutritivas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

## 🔴 EXERCÍCIO 3: Sistema de Categorização

def add_recipe_metadata():
    """
    Adiciona metadados às receitas para categorização.
    
    Returns:
        dict: Dicionário com metadados das receitas
    """
    recipe_metadata = {
        "categorias": {
            "cafe_da_manha": ["panqueca", "omelete", "granola", "mingau", "pão"],
            "almoco": ["frango", "peixe", "carne", "salada", "sopa"],
            "jantar": ["jantar", "ceia", "light"],
            "snacks": ["barrinha", "cookies", "chips", "patê"],
            "sobremesas": ["bolo", "brownie", "mousse", "brigadeiro"]
        },
        "dificuldade": {
            "facil": ["simples", "fácil", "rápido"],
            "medio": ["médio", "intermediário"],
            "dificil": ["difícil", "complexo", "elaborado"]
        },
        "tempo_preparo": {
            "rapido": ["rápido", "5 min", "10 min"],
            "medio": ["médio", "30 min", "1 hora"],
            "lento": ["lento", "2 horas", "demorado"]
        }
    }
    
    return recipe_metadata

def categorize_recipe(recipe_text):
    """
    Categoriza uma receita baseada em seu conteúdo.
    
    Args:
        recipe_text (str): Texto da receita
        
    Returns:
        dict: Metadados da receita
    """
    metadata = add_recipe_metadata()
    recipe_lower = recipe_text.lower()
    
    # Determinar categoria
    categoria = "outros"
    for cat, keywords in metadata["categorias"].items():
        if any(keyword in recipe_lower for keyword in keywords):
            categoria = cat
            break
    
    # Determinar dificuldade
    dificuldade = "medio"
    for diff, keywords in metadata["dificuldade"].items():
        if any(keyword in recipe_lower for keyword in keywords):
            dificuldade = diff
            break
    
    # Determinar tempo
    tempo = "medio"
    for t, keywords in metadata["tempo_preparo"].items():
        if any(keyword in recipe_lower for keyword in keywords):
            tempo = t
            break
    
    return {
        "categoria": categoria,
        "dificuldade": dificuldade,
        "tempo_preparo": tempo
    }

def filter_recipes_by_category(category, query_text):
    """
    Filtra receitas por categoria específica.
    
    Args:
        category (str): Categoria desejada
        query_text (str): Query do usuário
        
    Returns:
        list: Receitas filtradas por categoria
    """
    # Busca geral
    results = db.similarity_search_with_relevance_scores(query_text, k=10)
    
    # Filtra por categoria
    filtered_results = []
    for doc, score in results:
        recipe_metadata = categorize_recipe(doc.page_content)
        if recipe_metadata["categoria"] == category:
            filtered_results.append((doc, score))
    
    return filtered_results[:4]  # Retorna top 4

## 🔴 EXERCÍCIO 4: Sistema de Recomendações

class RecipeRecommender:
    """
    Sistema de recomendação de receitas baseado em histórico e similaridade.
    """
    
    def __init__(self):
        self.user_history = {}
        self.recipe_similarity_cache = {}
    
    def add_to_history(self, user_id, recipe_name):
        """
        Adiciona uma receita ao histórico do usuário.
        
        Args:
            user_id (str): ID do usuário
            recipe_name (str): Nome da receita visualizada
        """
        if user_id not in self.user_history:
            self.user_history[user_id] = []
        
        self.user_history[user_id].append({
            "recipe": recipe_name,
            "timestamp": pd.Timestamp.now()
        })
    
    def get_user_preferences(self, user_id):
        """
        Analisa as preferências do usuário baseado no histórico.
        
        Args:
            user_id (str): ID do usuário
            
        Returns:
            dict: Preferências do usuário
        """
        if user_id not in self.user_history:
            return {"categorias": [], "ingredientes": []}
        
        history = self.user_history[user_id]
        categories = []
        ingredients = []
        
        for entry in history[-10:]:  # Últimas 10 receitas
            recipe_name = entry["recipe"].lower()
            
            # Categorizar receita
            metadata = categorize_recipe(recipe_name)
            categories.append(metadata["categoria"])
            
            # Extrair ingredientes comuns
            # (implementação simplificada)
            common_ingredients = ["frango", "peixe", "carne", "ovo", "aveia", "banana"]
            for ingredient in common_ingredients:
                if ingredient in recipe_name:
                    ingredients.append(ingredient)
        
        return {
            "categorias": list(set(categories)),
            "ingredientes": list(set(ingredients))
        }
    
    def recommend_similar_recipes(self, recipe_name, k=3):
        """
        Recomenda receitas similares baseadas em uma receita específica.
        
        Args:
            recipe_name (str): Nome da receita base
            k (int): Número de recomendações
            
        Returns:
            list: Lista de receitas recomendadas
        """
        # Busca por receitas similares
        results = db.similarity_search_with_relevance_scores(recipe_name, k=k+1)
        
        # Remove a própria receita se estiver nos resultados
        recommendations = []
        for doc, score in results:
            if recipe_name.lower() not in doc.page_content.lower():
                recommendations.append({
                    "nome": doc.page_content.split('\n')[0][:50],
                    "score": score,
                    "conteudo": doc.page_content[:200]
                })
        
        return recommendations[:k]

## 🔴 EXERCÍCIO 5: Análise Nutricional

def extract_nutritional_info(recipe_text):
    """
    Extrai informações nutricionais do texto da receita.
    
    Args:
        recipe_text (str): Texto da receita
        
    Returns:
        dict: Informações nutricionais extraídas
    """
    # Padrões para extrair informações nutricionais
    import re
    
    nutritional_info = {
        "calorias": None,
        "proteinas": None,
        "carboidratos": None,
        "gorduras": None,
        "fibras": None
    }
    
    # Busca por padrões de informação nutricional
    patterns = {
        "calorias": r"(\d+)\s*(?:kcal|calorias?)",
        "proteinas": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?prote[íi]nas?",
        "carboidratos": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?carboidratos?",
        "gorduras": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?gorduras?",
        "fibras": r"(\d+(?:\.\d+)?)\s*(?:g|gramas?)\s*(?:de\s+)?fibras?"
    }
    
    for nutrient, pattern in patterns.items():
        match = re.search(pattern, recipe_text.lower())
        if match:
            nutritional_info[nutrient] = float(match.group(1))
    
    return nutritional_info

def filter_by_dietary_restrictions(recipes, restrictions):
    """
    Filtra receitas por restrições alimentares.
    
    Args:
        recipes (list): Lista de receitas
        restrictions (list): Lista de restrições alimentares
        
    Returns:
        list: Receitas filtradas
    """
    filtered_recipes = []
    
    restriction_keywords = {
        "vegetariano": ["carne", "frango", "peixe", "bacon"],
        "vegano": ["leite", "queijo", "ovo", "manteiga", "mel"],
        "sem_gluten": ["trigo", "farinha", "pão", "macarrão"],
        "low_carb": ["açúcar", "farinha", "arroz", "batata"],
        "sem_lactose": ["leite", "queijo", "iogurte", "creme"]
    }
    
    for recipe in recipes:
        recipe_text = recipe.page_content.lower()
        is_suitable = True
        
        for restriction in restrictions:
            if restriction in restriction_keywords:
                excluded_ingredients = restriction_keywords[restriction]
                for ingredient in excluded_ingredients:
                    if ingredient in recipe_text:
                        is_suitable = False
                        break
        
        if is_suitable:
            filtered_recipes.append(recipe)
    
    return filtered_recipes

## 🧪 EXERCÍCIO 6: Interface Melhorada

def create_enhanced_interface():
    """
    Cria uma interface Streamlit melhorada para o assistente de receitas.
    """
    st.set_page_config(
        page_title="Assistente de Receitas Saudáveis",
        page_icon="🍳",
        layout="wide"
    )
    
    # Sidebar com filtros
    with st.sidebar:
        st.header("🔍 Filtros")
        
        # Filtro por categoria
        categories = ["Todos", "Café da manhã", "Almoço", "Jantar", "Snacks", "Sobremesas"]
        selected_category = st.selectbox("Categoria:", categories)
        
        # Filtro por dificuldade
        difficulties = ["Todas", "Fácil", "Médio", "Difícil"]
        selected_difficulty = st.selectbox("Dificuldade:", difficulties)
        
        # Filtro por restrições alimentares
        restrictions = st.multiselect(
            "Restrições alimentares:",
            ["Vegetariano", "Vegano", "Sem glúten", "Low carb", "Sem lactose"]
        )
        
        # Botão para limpar filtros
        if st.button("Limpar filtros"):
            st.session_state.clear()
    
    # Área principal
    st.title("🍳 Assistente de Receitas Saudáveis")
    st.markdown("---")
    
    # Área de chat
    chat_container = st.container()
    
    with chat_container:
        # Histórico do chat
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Exibir histórico
        for i, (user_msg, assistant_msg) in enumerate(st.session_state.chat_history):
            st.chat_message("user").write(user_msg)
            st.chat_message("assistant").write(assistant_msg)
        
        # Input do usuário
        user_input = st.chat_input("Digite sua pergunta sobre receitas...")
        
        if user_input:
            # Adicionar mensagem do usuário
            st.chat_message("user").write(user_input)
            
            # Processar com filtros
            if selected_category != "Todos":
                results = filter_recipes_by_category(selected_category.lower(), user_input)
            else:
                results = db.similarity_search_with_relevance_scores(user_input, k=4)
            
            # Aplicar filtros adicionais
            if restrictions:
                results = filter_by_dietary_restrictions([doc for doc, _ in results], restrictions)
                results = [(doc, 0.8) for doc in results]  # Score padrão para resultados filtrados
            
            # Gerar resposta
            if results:
                context = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
                response = get_enhanced_response(user_input, context)
            else:
                response = "Desculpe, não encontrei receitas que correspondam aos seus critérios."
            
            # Adicionar resposta do assistente
            st.chat_message("assistant").write(response)
            
            # Atualizar histórico
            st.session_state.chat_history.append((user_input, response))

# Função para testar todas as funcionalidades
def run_tests():
    """
    Executa testes para todas as funcionalidades implementadas.
    """
    print("🧪 Executando testes das funcionalidades...")
    
    # Teste 1: Análise de similaridade
    print("\n1. Teste de Análise de Similaridade")
    analyze_similarity("receita de bolo de chocolate")
    
    # Teste 2: Categorização
    print("\n2. Teste de Categorização")
    test_recipe = "Panqueca de aveia com banana - Receita fit e saudável"
    metadata = categorize_recipe(test_recipe)
    print(f"Receita: {test_recipe}")
    print(f"Metadados: {metadata}")
    
    # Teste 3: Sistema de recomendações
    print("\n3. Teste de Sistema de Recomendações")
    recommender = RecipeRecommender()
    recommendations = recommender.recommend_similar_recipes("bolo de chocolate", k=2)
    print(f"Recomendações para 'bolo de chocolate':")
    for i, rec in enumerate(recommendations):
        print(f"  {i+1}. {rec['nome']} (Score: {rec['score']:.3f})")
    
    # Teste 4: Análise nutricional
    print("\n4. Teste de Análise Nutricional")
    test_recipe_with_nutrition = """
    Bolo de Chocolate Fit
    Ingredientes: farinha de aveia, cacau, ovo, banana
    Informações nutricionais: 150 kcal, 8g proteínas, 20g carboidratos, 5g gorduras
    """
    nutrition = extract_nutritional_info(test_recipe_with_nutrition)
    print(f"Informações nutricionais extraídas: {nutrition}")
    
    print("\n✅ Todos os testes foram executados com sucesso!")

if __name__ == "__main__":
    # Executar testes
    run_tests()
    
    # Para executar a interface, descomente a linha abaixo:
    # create_enhanced_interface() 