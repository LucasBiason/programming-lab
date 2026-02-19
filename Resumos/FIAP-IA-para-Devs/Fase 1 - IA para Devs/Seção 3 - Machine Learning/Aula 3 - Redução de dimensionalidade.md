# Aula 3 - Redução de dimensionalidade

**Fase 1 - IA para Devs** | **Seção 3 - Machine Learning**

---

## Resumo executivo

Esta aula aborda o **problema da alta dimensionalidade** (muitas features; dados esparsos, risco de overfitting) e a **redução de dimensionalidade** como solução. Foco na **PCA (Análise de Componentes Principais)**: objetivo (reduzir complexidade mantendo a maior parte da variância), **funcionamento** (combinações lineares das variáveis originais em componentes principais; autovetores e autovalores), **padronização** obrigatória (PCA sensível à escala; StandardScaler), **variância explicada** (explained_variance_ratio_) para decidir quantos componentes manter, e **aplicação em Python** (sklearn: StandardScaler, PCA, fit_transform). Menção a outras técnicas: t-SNE, Autoencoders, Kernel PCA, LDA, LLE, Isomap. Ao final, você saberá quando e como usar PCA e como avaliar a qualidade da redução.

**Objetivos de aprendizagem:**
- Explicar o problema da alta dimensionalidade e a maldição da dimensionalidade.
- Descrever o objetivo e o funcionamento da PCA (componentes principais, variância).
- Aplicar padronização antes do PCA (StandardScaler).
- Interpretar variância explicada (explained_variance_ratio_) e escolher o número de componentes.
- Usar sklearn para aplicar PCA em um dataset (ex.: Iris).

---

## Conceitos-chave (flashcards)

**P:** O que é a maldição da alta dimensionalidade?  
**R:** Muitas features (colunas) tornam os dados esparsos e aumentam o risco de overfitting; o modelo pode “decorar” o treino e não generalizar.

**P:** O que a PCA faz?  
**R:** Reduz o número de dimensões criando **componentes principais** (combinações lineares das variáveis originais) que capturam a maior parte da **variância** dos dados.

**P:** Por que padronizar antes do PCA?  
**R:** PCA é sensível à escala; variáveis com amplitude maior dominariam a variância; padronização (média 0, desvio 1) coloca todas em pé de igualdade.

**P:** O que é variância explicada (explained variance ratio)?  
**R:** Proporção da variância total dos dados explicada por cada componente principal; usada para decidir quantos componentes manter (ex.: 95% ou 99% da variância).

**P:** O que são autovetores e autovalores no PCA?  
**R:** Autovetores definem as direções dos componentes principais; autovalores indicam a quantidade de variância (informação) capturada em cada direção.

---

## PCA: funcionamento

- **Ideia:** projetar os dados em novas direções (componentes) que maximizam a variância; primeiro componente = direção de maior variância; segundo = maior variância perpendicular ao primeiro; e assim por diante.
- **Resultado:** menos colunas (dimensões) mantendo a maior parte da informação; útil para visualização (ex.: 2 componentes), redução de ruído e evitar overfitting.
- **Técnicas alternativas:** t-SNE (visualização), Autoencoders (não linear), Kernel PCA, LDA (supervisionado), LLE, Isomap.

---

## Pipeline típico em Python

1. Separar features (X) e target (y).
2. **Padronizar:** `StandardScaler().fit_transform(X)` (só com dados de treino; aplicar mesma transformação no teste).
3. **PCA:** `PCA(n_components=2).fit_transform(X)` (ou número que acumule ~95% da variância).
4. **Avaliar:** `pca.explained_variance_ratio_` e soma para ver variância total explicada.

Quantos componentes: equilibrar simplificação e retenção de informação (ex.: 95% ou 99% da variância); depende do objetivo do projeto.

---

## Mapa conceitual

```
Redução de dimensionalidade
├── Problema (alta dimensionalidade, overfitting)
├── PCA
│   ├── Componentes principais (combinações lineares)
│   ├── Autovetores e autovalores
│   ├── Padronização (obrigatória)
│   └── Variância explicada
├── Outras técnicas (t-SNE, LDA, Kernel PCA, etc.)
└── Prática (StandardScaler → PCA, n_components, explained_variance_ratio_)
```

---

## Receita prática

1. **Verificar necessidade:** muitas features ou risco de overfitting? Considerar redução.
2. **Padronizar:** sempre antes do PCA (fit no treino, transform no treino e no teste).
3. **Aplicar PCA:** escolher n_components (fixo ou por variância acumulada); fit no treino, transform no treino e teste.
4. **Interpretar:** explained_variance_ratio_ para justificar quantos componentes manter.

---

## Perguntas para teste de reforço

1. Por que padronizar antes do PCA? **R:** PCA é sensível à escala; variáveis com unidades/amplitude maiores dominariam; padronização coloca todas em escala comparável.
2. O que o primeiro componente principal representa? **R:** A direção em que os dados têm maior variância (maior “espalhamento”).
3. Como decidir quantos componentes manter? **R:** Usar variância explicada acumulada (ex.: manter componentes até 95% ou 99% da variância total).
4. A soma das variâncias explicadas de todos os componentes é 100%? **R:** Sim; cada componente explica uma fração; os que não são usados explicam o restante.
5. Cite uma técnica alternativa à PCA. **R:** Ex.: t-SNE, LDA, Kernel PCA, Autoencoders.

---

## Materiais de apoio

- Scikit-learn – Decomposition (PCA): [scikit-learn.org/stable/modules/decomposition](https://scikit-learn.org/stable/modules/decomposition.html#pca)  
- Scikit-learn – Preprocessing (StandardScaler): [scikit-learn.org/stable/modules/preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
