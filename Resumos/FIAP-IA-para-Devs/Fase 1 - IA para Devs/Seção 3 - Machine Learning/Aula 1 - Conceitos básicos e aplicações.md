# Aula 1 - Conceitos básicos e aplicações

**Fase 1 - IA para Devs** | **Seção 3 - Machine Learning**

---

## Resumo executivo

Esta aula introduz **o que é aprendizado de máquina**: definições de Arthur Samuel e Tom Mitchell (aprender sem ser explicitamente programado; desempenho em tarefa T medido por P melhora com experiência E), **benefício para negócios** (ex.: banco prevendo bons/maus pagadores), **etapas do pipeline** (estudo do problema, escolha do algoritmo, treino, validação, deploy; calibração para overfitting e underfitting) e os **três tipos principais de aprendizado**: **supervisionado** (dados rotulados; regressão e classificação; KNN, regressão linear/logística, SVM, árvores, redes neurais), **não supervisionado** (sem rótulos; agrupamento, PCA, t-SNE, sistemas de recomendação) e **por reforço** (tentativa e erro, recompensa e punição, política atualizada). Ao final, você saberá identificar o tipo de problema e o fluxo típico de um projeto de ML.

**Objetivos de aprendizagem:**
- Definir aprendizado de máquina com base em Samuel e Mitchell.
- Descrever as etapas do pipeline (problema → algoritmo → treino → validação → deploy).
- Diferenciar aprendizado supervisionado, não supervisionado e por reforço.
- Reconhecer exemplos de algoritmos de cada tipo e cenários de aplicação (finanças, saúde, marketing, etc.).
- Entender overfitting e underfitting e a necessidade de calibração.

---

## Conceitos-chave (flashcards)

**P:** O que é aprendizado de máquina segundo Arthur Samuel?  
**R:** Campo que dá aos computadores a habilidade de aprender **sem ser explicitamente programado** (padrões aprendidos dos dados por meio de funções matemáticas).

**P:** O que Tom Mitchell acrescenta à definição?  
**R:** Um programa **aprende** com experiência **E** em relação à tarefa **T** e à medida de desempenho **P** se o desempenho em T, medido por P, **melhora com E**.

**P:** O que é variável target no aprendizado supervisionado?  
**R:** A coluna (rótulo) que contém a resposta desejada; o modelo aprende a prever essa variável a partir das características (variáveis explicativas).

**P:** Qual a diferença entre regressão e classificação no supervisionado?  
**R:** Regressão: target é **numérico** (prever valor). Classificação: target é **categórico** (prever classe, ex.: spam/não spam).

**P:** No não supervisionado, o que o algoritmo faz?  
**R:** Aprende **padrões sem rótulos**; objetivos típicos: agrupar dados (clustering), reduzir dimensionalidade ou encontrar estrutura (ex.: segmentação de clientes).

**P:** Como funciona o aprendizado por reforço?  
**R:** O agente executa ações em um ambiente; recebe **recompensa** ou **punição**; atualiza a **política** e repete até convergir a uma boa estratégia (tentativa e erro).

**P:** O que é overfitting? **R:** O modelo “decora” os dados de treino e não generaliza bem para dados novos.

**P:** O que é underfitting? **R:** O modelo é fraco demais e não aprende padrões suficientes nos dados.

---

## Etapas do pipeline de ML

1. **Estudo do problema de negócio:** mapear objetivo e escolher as melhores features.
2. **Escolha do algoritmo:** conforme tipo (supervisionado/não supervisionado/reforço) e natureza do problema (regressão, classificação, agrupamento).
3. **Treinamento:** alimentar o modelo com amostra de dados para aprender padrões.
4. **Validação:** avaliar desempenho em base de teste (métricas estatísticas).
5. **Deploy:** colocar o modelo em produção. Se o modelo não generalizar, **calibrar** (ajustar complexidade, dados ou hiperparâmetros) para reduzir overfitting ou underfitting.

---

## Tipos de aprendizado e exemplos

| Tipo            | Dados      | Objetivo              | Exemplos de algoritmos / técnicas        |
|-----------------|------------|------------------------|------------------------------------------|
| **Supervisionado** | Rotulados  | Prever target          | KNN, Regressão Linear/Logística, SVM, Árvores, Random Forest, Redes Neurais |
| **Não supervisionado** | Sem rótulos | Agrupar, reduzir dimensão | K-Means, DBSCAN, Cluster hierárquico, PCA, t-SNE, Sistemas de recomendação |
| **Por reforço** | Ambiente   | Maximizar recompensa   | Política atualizada por tentativa e erro |

**Cenários de aplicação:** finanças (crédito, fraude), saúde (diagnóstico), educação, agricultura, logística, marketing, sustentabilidade, varejo, RH.

---

## Mapa conceitual

```
Conceitos básicos de ML
├── Definição (Samuel, Mitchell)
├── Benefício (modelo preditivo, decisão antecipada)
├── Pipeline
│   ├── Problema → algoritmo → treino → validação → deploy
│   └── Calibração (overfitting, underfitting)
└── Tipos
    ├── Supervisionado (rótulos, regressão, classificação)
    ├── Não supervisionado (agrupamento, PCA, t-SNE)
    └── Reforço (recompensa, punição, política)
```

---

## Receita prática

1. **Problema:** tem rótulo (target)? → Supervisionado. Não tem? → Não supervisionado ou reforço (se houver ambiente e recompensa).
2. **Target numérico ou categórico?** Numérico → regressão. Categórico → classificação.
3. **Pipeline:** definir métricas de sucesso, separar treino/teste, treinar, validar e calibrar antes do deploy.

---

## Perguntas para teste de reforço

1. Cite uma definição clássica de ML. **R:** Arthur Samuel: computadores que aprendem sem ser explicitamente programados; ou Mitchell: desempenho em T medido por P melhora com experiência E.
2. O que é variável target? **R:** A variável que o modelo deve prever (rótulo nos dados de treino).
3. Quando usar aprendizado não supervisionado? **R:** Quando não há rótulos e o objetivo é agrupar, reduzir dimensão ou descobrir estrutura.
4. O que é overfitting? **R:** Modelo que decora o treino e não generaliza para dados novos.
5. Cite dois algoritmos de aprendizado supervisionado. **R:** Ex.: KNN, regressão linear, SVM, árvore de decisão.

---

## Materiais de apoio

- Scikit-learn – Machine Learning em Python: [scikit-learn.org](https://scikit-learn.org)  
- Livros de referência em ML (ex.: Mitchell, Hastie et al.).
