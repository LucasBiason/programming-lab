# Aula 1 - Modelos de classificação

**Fase 1 - IA para Devs** | **Seção 4 - Machine Learning Avançado**

---

## Resumo executivo

Esta aula aborda **modelos de classificação** (aprendizado supervisionado): identificação de problemas de classificação (ex.: spam vs não spam), **variáveis explicativas** (features) e **classe alvo** (target categórico), **pré-processamento** para classificação — **Label Encoding** e **One Hot Encoding** para variáveis categóricas (evitar ordem falsa; One Hot aumenta dimensão) — e **feature scaling** em colunas numéricas (MinMaxScaler, StandardScaler). Inclui o **fluxo de treino e teste**: separação treino (~70–80%) e teste (~20–30%), uso de **train_test_split** no sklearn (test_size, random_state, stratify), e representação **X** (features) e **y** (target). Ao final, você saberá preparar dados e dividir base para treinar um classificador com Scikit-learn.

**Objetivos de aprendizagem:**

- Identificar um problema de classificação (target categórico; ex.: spam/não spam).
- Aplicar Label Encoding e One Hot Encoding em variáveis categóricas e saber quando usar cada um.
- Relembrar feature scaling (MinMaxScaler, StandardScaler) para variáveis numéricas.
- Separar dados em treino e teste com train_test_split (test_size, random_state, stratify).
- Entender a representação X (independentes) e y (dependente/target).

---

## Exemplo do material: classificação de spam

No curso, o modelo supervisionado é ilustrado com o exemplo **spam vs não spam**:

- **Variáveis explicativas (features):** presença de propaganda no corpo do e-mail, remetente na agenda, quantidade de caracteres etc.
- **Classe alvo:** tipo de e-mail (spam ou não spam).
- **Padrão dos “não spam” no exemplo:** sem propaganda no corpo; remetentes já na agenda; total de caracteres ≥ 1000.
  O classificador aprende com base em **padrões ou similaridade** nos dados; na classificação buscamos as melhores features que descrevem cada classe (diferente da regressão, que busca linearidade).

---

## Conceitos-chave (flashcards)

**P:** O que é um modelo de classificação?  
**R:** Modelo supervisionado que **prevê uma classe** (categórica), ou seja, uma variável target no formato de categoria (ex.: spam/não spam), com base em variáveis explicativas (features).

**P:** Por que o computador precisa de variáveis numéricas?  
**R:** A maioria dos algoritmos trabalha com números; variáveis categóricas (texto) precisam ser transformadas (Label Encoding ou One Hot Encoding).

**P:** O que é Label Encoding?  
**R:** Atribuir um número inteiro a cada categoria (ex.: maçã=0, banana=1). Cuidado: pode introduzir ordem falsa (o modelo pode interpretar que uma categoria é “maior” que outra).

**P:** O que é One Hot Encoding?  
**R:** Criar **uma coluna binária por categoria** (1 se a amostra pertence àquela categoria, 0 caso contrário); evita ordem entre categorias, mas **aumenta a dimensionalidade** (muitas colunas).

**P:** Para que serve o stratify no train_test_split?  
**R:** Manter a **proporção das classes** (target) igual no treino e no teste; evita conjuntos desbalanceados (ex.: uma classe só no treino ou só no teste).

**P:** Por que separar treino e teste?  
**R:** Treino: modelo aprende padrões. Teste: simular dados “nunca vistos” para avaliar se o modelo **generaliza**; evitar avaliar só nos dados em que foi treinado.

---

## Pré-processamento para classificação

**Categóricas:**

- **Label Encoding:** categorias → inteiros (sklearn: LabelEncoder; pandas: map). Use quando não há ordem natural e o modelo não interpreta ordem (ex.: árvores).
- **One Hot Encoding:** uma coluna por categoria, valores 0/1 (pandas: get_dummies; sklearn: OneHotEncoder). Use quando a ordem seria enganosa (ex.: regressão logística). Atenção: aumento de colunas (maldição da dimensionalidade); pode exigir redução de dimensionalidade depois.

**Numéricas:**

- **Feature scaling:** MinMaxScaler (normalização 0–1) ou StandardScaler (padronização z-score) para que escalas diferentes não dominem o modelo (fit no treino, transform no treino e teste).

---

## Treino e teste

- **Proporção típica:** 70–80% treino, 20–30% teste.
- **train_test_split(X, y, test_size=0.2, random_state=42, stratify=y):**
  - X: variáveis independentes (features).
  - y: variável dependente (target).
  - test_size: fração (ex.: 0.2 = 20%) ou inteiro para tamanho do teste.
  - random_state: reprodutibilidade da divisão.
  - stratify=y: manter proporção das classes em treino e teste.
- Resultado: X_train, X_test, y_train, y_test.

---

## Scikit-learn e código (referência do material)

- **Biblioteca:** Scikit-learn — aprendizado supervisionado e não supervisionado, pré-processamento, seleção e avaliação de modelos.
- **Categóricas:** `LabelEncoder` (sklearn.preprocessing); One Hot com `pd.get_dummies` (pandas). Exemplo da aula: base _Frutas.xlsx_.
- **Treino/teste:** `train_test_split` em `sklearn.model_selection`; uso típico com `test_size=0.2` (20% teste), `random_state` para reprodutibilidade e `stratify=y` para manter proporção das classes.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

---

## Mapa conceitual

```
Modelos de classificação
├── Definição (target categórico, features)
├── Pré-processamento
│   ├── Categóricas: Label Encoding, One Hot
│   └── Numéricas: MinMaxScaler, StandardScaler
├── Treino e teste
│   ├── train_test_split (X, y, test_size, stratify)
│   └── X_train, X_test, y_train, y_test
└── Scikit-learn (classificadores, pipelines)
```

---

## Receita prática

1. **Identificar target:** é categórico? → problema de classificação.
2. **Categóricas:** sem ordem → One Hot (ou Label se o algoritmo não sofrer com ordem). Com muitas categorias, considerar agrupamento ou redução depois.
3. **Numéricas:** aplicar scaling (fit no treino, transform no treino e teste).
4. **Dividir:** train_test_split com stratify=y se as classes forem desbalanceadas.
5. **Treinar:** usar classificadores do sklearn (ex.: LogisticRegression, RandomForest) em X_train, y_train; avaliar em X_test, y_test.

---

## Perguntas para teste de reforço

1. Qual a diferença entre Label Encoding e One Hot Encoding? **R:** Label: uma categoria = um número (pode sugerir ordem). One Hot: uma coluna binária por categoria (1/0), sem ordem; aumenta o número de colunas.
2. Para que serve o parâmetro stratify em train_test_split? **R:** Manter a mesma proporção das classes (y) nos conjuntos de treino e teste.
3. Por que não treinar e avaliar no mesmo conjunto? **R:** Avaliar no mesmo conjunto que treinou superestima o desempenho; o teste deve simular dados novos para medir generalização.
4. O que são X e y na notação de ML? **R:** X = variáveis independentes (features); y = variável dependente (target).
5. One Hot Encoding aumenta a dimensionalidade? **R:** Sim; cada categoria vira uma coluna; com muitas categorias, o número de features cresce (pode exigir redução depois).

---

## Materiais de apoio

- Scikit-learn – Preprocessing (LabelEncoder, OneHotEncoder, scalers): [scikit-learn.org/stable/modules/preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- Scikit-learn – model_selection (train_test_split): [scikit-learn.org/stable/modules/model_selection](https://scikit-learn.org/stable/modules/model_selection.html#splitter-functions)
- Scikit-learn – Supervised learning (classificadores): [scikit-learn.org/stable/supervised_learning](https://scikit-learn.org/stable/supervised_learning.html)
