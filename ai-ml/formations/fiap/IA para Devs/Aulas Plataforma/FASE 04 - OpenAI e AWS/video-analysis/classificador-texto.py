"""
Classificador de texto usando aprendizado supervisionado
Classifica textos em categorias usando Naive Bayes
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics


def preparar_dados():
    """Prepara dados de exemplo para treinamento"""
    textos = [
        "Python é uma linguagem excelente para programação",
        "Minha geladeira parou de funcionar ontem",
        "Adoro comer pizza nos finais de semana",
        "Estou aprendendo machine learning com Python",
        "Preciso chamar um técnico para consertar o fogão",
        "A pizza margherita é minha favorita",
        "Programação em Python é muito produtiva",
        "O ar condicionado quebrou na semana passada",
        "Vou pedir uma pizza para o jantar",
        "Python tem uma comunidade muito ativa",
        "A máquina de lavar precisa de reparo",
        "Pizza de calabresa é deliciosa",
        "Estou fazendo um curso de Python avançado",
        "O micro-ondas não está esquentando direito"
    ]
    
    categorias = [
        "tecnologia", "domestico", "comida",
        "tecnologia", "domestico", "comida",
        "tecnologia", "domestico", "comida",
        "tecnologia", "domestico", "comida",
        "tecnologia", "domestico"
    ]
    
    return textos, categorias


def treinar_modelo(textos, categorias):
    """Treina modelo de classificação"""
    # Dividir em treino e teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        textos,
        categorias,
        test_size=0.25,
        random_state=42
    )
    
    # Criar pipeline: vetorização + classificação
    modelo = Pipeline([
        ('vetorizador', TfidfVectorizer()),
        ('classificador', MultinomialNB())
    ])
    
    # Treinar
    modelo.fit(X_treino, y_treino)
    
    # Avaliar
    predicoes = modelo.predict(X_teste)
    print("Relatório de Classificação:")
    print(metrics.classification_report(y_teste, predicoes, zero_division=0))
    
    return modelo


def classificar_novos_textos(modelo, textos_novos):
    """Classifica novos textos usando modelo treinado"""
    predicoes = modelo.predict(textos_novos)
    return predicoes


def main():
    """Função principal"""
    print("Preparando dados...")
    textos, categorias = preparar_dados()
    
    print("Treinando modelo...")
    modelo = treinar_modelo(textos, categorias)
    
    print("\nClassificando novos textos:")
    textos_teste = [
        "Estou estudando Python para projetos de IA",
        "A pizza chegou quentinha"
    ]
    
    resultados = classificar_novos_textos(modelo, textos_teste)
    
    for texto, categoria in zip(textos_teste, resultados):
        print(f"  '{texto}' -> {categoria}")


if __name__ == "__main__":
    main()

