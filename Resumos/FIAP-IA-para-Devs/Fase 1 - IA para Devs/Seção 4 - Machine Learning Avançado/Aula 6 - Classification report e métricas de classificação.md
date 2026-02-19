# Aula 6 - Classification report e métricas de classificação

**Fase 1 - IA para Devs** | **Seção 4 - Machine Learning Avançado**

---

## Resumo executivo

Esta aula trata das **métricas de validação para classificadores**: **matriz de confusão**, **Accuracy**, **Precision**, **Recall** e **F1 Score**. A **matriz de confusão** compara valores reais (linhas) com preditos (colunas); dela derivam **Verdadeiro Positivo (TP)**, **Verdadeiro Negativo (TN)**, **Falso Positivo (FP)** e **Falso Negativo (FN)**. **Accuracy** = acertos totais / total. **Precision** = TP/(TP+FP) (dos que predisse como positivos, quantos eram). **Recall** = TP/(TP+FN) (dos positivos reais, quantos capturou). **F1 Score** é a média harmônica entre precisão e recall. No Sklearn: **confusion_matrix**, **ConfusionMatrixDisplay** e **classification_report** para um relatório por classe.

**Objetivos de aprendizagem:**

- Construir e interpretar a matriz de confusão (True Label vs Predicted Label); identificar TP, TN, FP, FN por classe.
- Calcular e interpretar Accuracy, Precision, Recall e F1; saber quando cada uma é mais relevante (ex.: classes desbalanceadas).
- Usar confusion_matrix, ConfusionMatrixDisplay e classification_report no Sklearn.
- Entender que um modelo pode ter boa acurácia geral mas desempenho ruim em uma classe (validar por classe).

---

## Conceitos-chave (flashcards)

**P:** O que é a matriz de confusão?  
**R:** Tabela que cruza **classe real** (linhas) com **classe predita** (colunas); cada célula é a contagem; a diagonal são os acertos (TP por classe); fora da diagonal são erros (FP/FN).

**P:** O que é Precision (precisão)?  
**R:** Dos exemplos que o modelo **predisse como positivos**, quantos eram realmente positivos: **TP / (TP + FP)**. Alta precisão = poucos falsos positivos.

**P:** O que é Recall (revocação)?  
**R:** Dos exemplos **realmente positivos**, quantos o modelo **encontrou**: **TP / (TP + FN)**. Alto recall = poucos falsos negativos (não deixar escapar positivos).

**P:** O que é F1 Score?  
**R:** **Média harmônica** entre Precision e Recall: 2·(P·R)/(P+R); equilibra precisão e revocação; útil quando uma única métrica é necessária (ex.: classes desbalanceadas).

**P:** Por que só Accuracy pode enganar? **R:** Em dados desbalanceados (ex.: 95% classe A, 5% B), um modelo que sempre prediz A tem 95% de acurácia mas recall da classe B zero; é preciso olhar Precision, Recall e F1 por classe.

---

## Exemplos práticos

```python
# Matriz de confusão (exemplo da aula: doenças ortopédicas)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

matriz_confusao = confusion_matrix(
    y_true=y_test, y_pred=y_predito,
    labels=['Disk Hernia', 'Normal', 'Spondylolisthesis']
)
fig, ax = plt.subplots(figsize=(15, 5))
disp = ConfusionMatrixDisplay(
    confusion_matrix=matriz_confusao,
    display_labels=['Disk Hernia', 'Normal', 'Spondylolisthesis']
)
disp.plot(values_format='d', ax=ax)
plt.show()
```

```python
# Relatório completo de métricas por classe
from sklearn.metrics import classification_report

print(classification_report(y_test, y_predito))
# Mostra precision, recall, f1-score e support por classe + médias
```

---

## Mapa conceitual

```
Métricas de classificação
├── Matriz de confusão
│   ├── Linhas: real; colunas: predito
│   └── TP, TN, FP, FN (por classe)
├── Métricas derivadas
│   ├── Accuracy: (TP+TN)/total
│   ├── Precision: TP/(TP+FP)
│   ├── Recall: TP/(TP+FN)
│   └── F1: 2·P·R/(P+R)
└── Sklearn: confusion_matrix, ConfusionMatrixDisplay, classification_report
```

---

## Receita prática

1. **Obter predições:** y_pred = modelo.predict(X_test).
2. **Matriz de confusão:** confusion_matrix(y_test, y_pred, labels=...) e ConfusionMatrixDisplay para visualizar.
3. **Relatório:** classification_report(y_test, y_pred) para Precision, Recall, F1 por classe.
4. **Interpretar:** em classes desbalanceadas, priorizar Recall da classe minoritária (ex.: fraude) ou F1; não confiar só em Accuracy.

---

## Diagrama (Mermaid)

```mermaid
flowchart LR
  subgraph Matriz
    A[Real \n Predito] --> B[TP]
    A --> C[FP]
    A --> D[FN]
    A --> E[TN]
  end
  B --> P[Precision = TP/(TP+FP)]
  B --> R[Recall = TP/(TP+FN)]
  P --> F1[F1 = 2*P*R/(P+R)]
  R --> F1
```

---

## Perguntas para teste de reforço

1. Na matriz de confusão, o que são as linhas e as colunas? **R:** Linhas = classe real (True Label); colunas = classe predita (Predicted Label).
2. O que é um Falso Negativo? **R:** Exemplo que é da classe positiva mas foi **predito como negativo** (o modelo “perdeu” esse positivo).
3. Quando usar Recall em vez de Precision? **R:** Quando não queremos **perder** positivos (ex.: diagnóstico de doença – Recall alto = capturar os doentes); Precision quando o custo de falsos positivos é alto.
4. O que classification_report do Sklearn retorna? **R:** Tabela com Precision, Recall, F1-score e support por classe, além de médias (macro, weighted, etc.).
5. Por que F1 é “média harmônica” e não média aritmética? **R:** A média harmônica penaliza mais quando uma das duas (Precision ou Recall) é baixa; assim F1 só fica alto se ambas forem razoáveis.

---

## Materiais de apoio

- Scikit-learn – confusion_matrix: [sklearn.metrics.confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
- Scikit-learn – classification_report: [sklearn.metrics.classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
- ConfusionMatrixDisplay: [sklearn.metrics.ConfusionMatrixDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html)
