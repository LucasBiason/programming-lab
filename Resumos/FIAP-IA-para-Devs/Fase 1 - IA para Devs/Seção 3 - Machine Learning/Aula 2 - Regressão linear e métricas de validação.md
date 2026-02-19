# Aula 2 - Regressão linear e métricas de validação

**Fase 1 - IA para Devs** | **Seção 3 - Machine Learning**

---

## Resumo executivo

Esta aula cobre **regressão linear** (simples e múltipla) e **métricas de validação** para modelos de regressão. Inclui a **equação** da regressão (Yi = α + βXi + εi; intercepto α, declive β, resíduos ε), o método dos **mínimos quadrados** (OLS: minimizar soma dos quadrados dos resíduos), **regressão múltipla** (várias variáveis independentes), e métricas: **RMSE**, **MSE** e **MAE**, além de **R²** e interpretação do **summary** do statsmodels (coeficientes, erro padrão, valor-p, R-squared). Inclui uso de **statsmodels** (OLS, summary) e **sklearn** (métricas). Ao final, você saberá ajustar um modelo de regressão linear e avaliar com métricas adequadas.

**Objetivos de aprendizagem:**
- Interpretar a equação da regressão linear (intercepto, coeficientes, resíduos).
- Explicar o método dos mínimos quadrados (OLS).
- Diferenciar regressão simples (uma preditora) e múltipla (várias preditoras).
- Calcular e interpretar RMSE, MSE, MAE e R².
- Usar statsmodels e sklearn para ajustar e avaliar regressão.

---

## Conceitos-chave (flashcards)

**P:** O que a regressão linear estima?  
**R:** A relação entre variável(is) preditora(s) X e a variável resposta Y; a equação Yi = α + βXi + εi; α = intercepto, β = declive, ε = resíduo.

**P:** O que são os resíduos?  
**R:** Diferença entre valor observado e valor previsto pelo modelo; o OLS minimiza a soma dos quadrados dos resíduos (RSS).

**P:** O que é RMSE?  
**R:** Raiz do erro quadrático médio; mesma unidade que Y; quanto menor, melhor; mede o desvio médio das previsões em relação ao real.

**P:** O que é R² (R-squared)?  
**R:** Proporção da variabilidade de Y explicada pelo modelo; entre 0 e 1; quanto mais próximo de 1, melhor o ajuste.

**P:** O que indica o valor-p (P>|t|) no summary?  
**R:** Teste de hipótese de que o coeficiente é zero; valor-p pequeno (ex.: < 0,05) indica que o preditor é estatisticamente significativo.

---

## Regressão linear simples e múltipla

- **Simples:** uma variável preditora X; Y = α + βX + ε; ex.: vendas de sorvete em função da temperatura.
- **Múltipla:** várias preditoras (X1, X2, …); Y = α + β1X1 + β2X2 + … + ε; ex.: vendas em função de temperatura e promoção de marketing.
- **Mínimos quadrados (OLS):** encontrar α e β que minimizam a soma dos quadrados dos resíduos (RSS).

---

## Métricas de avaliação

- **MSE (Mean Squared Error):** média dos quadrados das diferenças (real − previsto).
- **RMSE:** raiz quadrada do MSE; mesma escala que Y; interpretação direta do erro médio.
- **MAE (Mean Absolute Error):** média do valor absoluto das diferenças; robusto a outliers.
- **R²:** variância explicada pelo modelo; 0 a 1; summary do statsmodels traz coef, std err, valor-p e R².

**Boas práticas:** usar dados de treino para ajustar; calcular métricas em dados de teste (ou validação) para avaliar generalização.

---

## Uso em Python (resumo)

- **statsmodels:** `sm.OLS(Y, X).fit()`; `modelo.summary()` para coeficientes, erros padrão, valor-p, R².
- **sklearn:** `mean_absolute_error`, `mean_squared_error`; RMSE = `np.sqrt(mean_squared_error(Y, y_pred))`.

---

## Mapa conceitual

```
Regressão linear
├── Equação (α, β, ε)
├── Mínimos quadrados (OLS)
├── Simples vs múltipla
├── Métricas
│   ├── MSE, RMSE, MAE
│   └── R²
└── Implementação
    ├── statsmodels (OLS, summary)
    └── sklearn (métricas)
```

---

## Receita prática

1. **Preparar X e Y:** variáveis independentes e dependente; adicionar constante (intercepto) se usar statsmodels sem intercepto automático.
2. **Ajustar:** `modelo = sm.OLS(Y, X).fit()` ou `LinearRegression().fit(X, y)`.
3. **Interpretar:** coeficientes (impacto de cada X em Y), valor-p (significância), R² (qualidade do ajuste).
4. **Avaliar:** RMSE e MAE em conjunto de teste para ver erro de previsão.

---

## Perguntas para teste de reforço

1. O que o OLS minimiza? **R:** A soma dos quadrados dos resíduos (RSS).
2. Para que serve o R²? **R:** Medir a proporção da variabilidade de Y explicada pelo modelo (0 a 1).
3. RMSE e MAE estão na mesma unidade que Y? **R:** RMSE e MAE sim; MSE está na unidade ao quadrado.
4. O que um valor-p alto para um coeficiente indica? **R:** Que não rejeitamos a hipótese de que o coeficiente é zero; o preditor pode não ser estatisticamente significativo.
5. Qual a diferença entre regressão simples e múltipla? **R:** Simples: uma variável X; múltipla: várias variáveis independentes (X1, X2, …).

---

## Materiais de apoio

- statsmodels: [statsmodels.org](https://www.statsmodels.org)  
- Scikit-learn – Linear Regression e métricas: [scikit-learn.org](https://scikit-learn.org)
