# Aula 4 - Feature Scaling

**Fase 1 - IA para Devs** | **Seção 3 - Machine Learning**

---

## Resumo executivo

Esta aula trata da **importância das escalas dos dados** em ML e das técnicas de **feature scaling**: **normalização (min-max)** e **padronização (z-score)**. Explica por que escalas diferentes (ex.: salário em milhares vs idade em dezenas) podem prejudicar algoritmos (redes neurais, KNN, K-means, PCA, SVM, regressão logística), apresenta as **fórmulas** (min-max: (X − min)/(max − min), resultado em [0,1]; z-score: (X − média)/desvio padrão, média 0 e variância 1), o uso no **Scikit-learn** (MinMaxScaler, StandardScaler) e a **regra crítica**: fazer **fit apenas nos dados de treino** e **transform** no treino e no teste (evitar data leakage). Inclui exemplo com base de crédito e menção ao desafio da disciplina (regressão com insurance.csv). Ao final, você saberá quando e como aplicar normalização ou padronização.

**Objetivos de aprendizagem:**
- Explicar por que escalas diferentes afetam algoritmos de ML.
- Diferenciar normalização (min-max) e padronização (z-score).
- Usar MinMaxScaler e StandardScaler no sklearn.
- Aplicar fit apenas no treino e transform no treino e no teste.

---

## Conceitos-chave (flashcards)

**P:** O que é feature scaling?  
**R:** Processo de colocar as features em uma **escala comum** (normalização ou padronização) para que o algoritmo não seja influenciado pela magnitude das variáveis.

**P:** O que faz a normalização (min-max)?  
**R:** Redimensiona os valores para um intervalo (geralmente [0, 1]): (X − min)/(max − min). No sklearn: MinMaxScaler (parâmetro feature_range permite mudar o intervalo).

**P:** O que faz a padronização (z-score)?  
**R:** Subtrai a média e divide pelo desvio padrão; resultado: média 0 e variância 1. Menos afetada por outliers que min-max. No sklearn: StandardScaler.

**P:** Por que fazer fit só no treino e transform no treino e no teste?  
**R:** Evitar **data leakage**: a base de teste deve simular dados “nunca vistos”; as estatísticas (min, max, média, desvio) devem vir apenas do treino; no teste aplicamos a **mesma** transformação aprendida no treino.

**P:** Quais algoritmos são sensíveis à escala?  
**R:** Redes neurais (normalização/padronização muitas vezes obrigatória), KNN, K-means, PCA, SVM, regressão logística (entre outros baseados em distância ou gradiente).

---

## Normalização vs padronização

| Aspecto       | Normalização (MinMaxScaler) | Padronização (StandardScaler) |
|---------------|-----------------------------|-------------------------------|
| Fórmula       | (X − min)/(max − min)       | (X − média)/desvio padrão     |
| Resultado     | Intervalo fixo (ex.: 0 a 1)| Média 0, variância 1           |
| Outliers      | Mais sensível               | Menos sensível                |
| Uso típico    | Redes neurais (entrada 0–1) | PCA, muitos modelos           |

---

## Pipeline correto

1. Dividir dados em **treino** e **teste** (ex.: train_test_split).
2. **Fit** do scaler **apenas em X_train:** `scaler = StandardScaler(); scaler.fit(X_train)`.
3. **Transform** em treino e teste: `X_train_scaled = scaler.transform(X_train)`; `X_test_scaled = scaler.transform(X_test)`.
4. Treinar e avaliar o modelo usando as features escalonadas.

---

## Mapa conceitual

```
Feature Scaling
├── Motivação (escalas diferentes, algoritmos sensíveis)
├── Normalização (min-max)
│   ├── Fórmula, intervalo [0,1]
│   └── MinMaxScaler
├── Padronização (z-score)
│   ├── Média 0, variância 1
│   └── StandardScaler
└── Boas práticas
    ├── Fit só no treino
    └── Transform treino e teste
```

---

## Receita prática

1. **Identificar necessidade:** algoritmos que usam distância, gradiente ou que exigem escala uniforme (KNN, redes neurais, PCA, SVM, etc.).
2. **Escolher técnica:** padronização (StandardScaler) é muito usada; min-max quando quiser intervalo fixo (ex.: 0–1 para redes).
3. **Aplicar:** fit no treino, transform no treino e no teste; nunca fit no teste.
4. **Treinar:** usar X_train_scaled e X_test_scaled no modelo e na avaliação.

---

## Perguntas para teste de reforço

1. Por que não fazer fit do scaler nos dados de teste? **R:** Para evitar data leakage; o teste deve representar dados novos; as estatísticas (média, min, max) devem vir só do treino.
2. Qual a diferença entre MinMaxScaler e StandardScaler? **R:** MinMax: escala para intervalo (ex.: 0–1). Standard: subtrai média e divide pelo desvio (média 0, variância 1).
3. Qual técnica é menos afetada por outliers? **R:** Padronização (z-score); min-max usa min e max, que podem ser puxados por outliers.
4. Para que tipo de algoritmo o scaling é muitas vezes obrigatório? **R:** Redes neurais (convergência e estabilidade).
5. O que é data leakage no contexto de scaling? **R:** Usar informação dos dados de teste (ex.: min/max ou média do conjunto completo) para definir a transformação; isso “vaza” informação do teste para o treino.

---

## Materiais de apoio

- Scikit-learn – Preprocessing: [scikit-learn.org/stable/modules/preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)  
- MinMaxScaler e StandardScaler na documentação sklearn.
