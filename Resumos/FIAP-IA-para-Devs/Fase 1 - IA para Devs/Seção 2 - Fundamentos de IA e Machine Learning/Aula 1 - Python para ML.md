# Aula 1 - Python para ML

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula apresenta **por que o Python é uma das melhores opções para IA e Machine Learning**: facilidade de aprendizado (sintaxe clara, legibilidade, documentação, comunidade, IDEs), **bibliotecas** essenciais (NumPy, SciPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow/Keras, PyTorch) e **suporte da comunidade** e de grandes empresas. Ao final, você terá uma visão do ecossistema Python para ML e exemplos de uso de cada biblioteca.

**Objetivos de aprendizagem:**
- Reconhecer os pilares da popularidade do Python em IA/ML (sintaxe, legibilidade, documentação, ferramentas, comunidade).
- Identificar o papel de NumPy e SciPy em cálculos numéricos e científicos.
- Usar Pandas para manipulação e análise de dados (DataFrame, leitura de CSV).
- Gerar visualizações com Matplotlib e Seaborn.
- Conhecer Scikit-learn para algoritmos de ML (ex.: regressão linear).
- Diferenciar TensorFlow/Keras e PyTorch para deep learning.

---

## Conceitos-chave (flashcards)

**P:** Por que a sintaxe do Python favorece o aprendizado?  
**R:** É simples, intuitiva e legível; usa indentação para blocos; exige menos código para tarefas equivalentes; se assemelha ao inglês.

**P:** Para que serve o NumPy em ML?  
**R:** Arrays multidimensionais e operações matemáticas eficientes; base para muitas bibliotecas de ML; processamento de imagens como matrizes de pixels.

**P:** Qual a relação entre SciPy e NumPy?  
**R:** SciPy é construída sobre o NumPy; adiciona módulos para otimização, álgebra linear, integração, processamento de sinais e problemas científicos avançados.

**P:** O que o Pandas oferece para análise de dados?  
**R:** Estruturas DataFrame e Series; leitura/escrita de arquivos (CSV, etc.); limpeza, manipulação e análise de dados; funções de tempo; preparação de datasets para ML.

**P:** Quando usar Matplotlib e quando Seaborn?  
**R:** Matplotlib: gráficos 2D customizáveis (linha, dispersão, barras, histogramas). Seaborn: gráficos estatísticos de alto nível (distribuições, heatmaps) com menos código e estética aprimorada.

**P:** O que o Scikit-learn oferece?  
**R:** Algoritmos de ML (regressão, classificação, clustering, redução de dimensionalidade), ferramentas de pré-processamento, validação e mineração de dados; integração com NumPy e Pandas.

**P:** Qual a diferença entre TensorFlow e PyTorch em termos de estilo?  
**R:** TensorFlow (Google): ecossistema amplo, execução eager no TF2, deploy em produção. PyTorch (Meta): grafo dinâmico, mais intuitivo para pesquisa e prototipagem; muito usado em academia.

**P:** O que é Keras no ecossistema TensorFlow?  
**R:** API de alto nível para construir redes neurais com poucas linhas; integrada ao TensorFlow; facilita criação e treino de modelos de deep learning.

---

## Facilidade no aprendizado

- **Sintaxe:** simples, intuitiva, legível; menos código para tarefas similares; indentação define blocos (sem chaves).
- **Documentação:** tutoriais oficiais, exemplos e referência completa de módulos e funções.
- **Comunidade:** Stack Overflow, GitHub, Reddit; muitos problemas já discutidos e resolvidos.
- **Ferramentas:** PyCharm, Jupyter Notebook, VS Code com suporte a Python (syntax highlight, debug, execução interativa).
- **Recursos:** cursos, livros, vídeos (ex.: Alura) cobrindo desde fundamentos até ML.
- **Suporte corporativo:** Google, Facebook, Amazon, Microsoft usam Python em projetos de IA/ML; validação e investimento em bibliotecas.

---

## Bibliotecas principais

| Biblioteca     | Função principal                          | Exemplo de uso em ML                          |
|----------------|--------------------------------------------|-----------------------------------------------|
| **NumPy**      | Arrays, operações numéricas                 | Matrizes de dados, médias, processamento de imagem |
| **SciPy**      | Cálculos científicos avançados              | Otimização, equações diferenciais, modelagem   |
| **Pandas**     | DataFrames, análise e limpeza de dados      | CSV, séries temporais, preparação de dataset |
| **Matplotlib** | Gráficos 2D                                 | Linhas, dispersão, histogramas                |
| **Seaborn**    | Gráficos estatísticos                       | Distribuições, heatmaps, estética             |
| **Scikit-learn** | Algoritmos de ML, pipelines, métricas    | Regressão, classificação, clustering          |
| **TensorFlow/Keras** | Deep learning (Google)               | Redes neurais, treino, deploy                 |
| **PyTorch**    | Deep learning (Meta)                        | Pesquisa, prototipagem, grafo dinâmico        |

---

## Exemplos de código (resumo)

- **NumPy:** `np.array`, `np.mean` para médias em matrizes.
- **Pandas:** `pd.read_csv('data.csv')`, operações em colunas.
- **Matplotlib:** `plt.plot(x, y)` e `plt.show()`.
- **Seaborn:** `sns.histplot(data)` para distribuição.
- **Scikit-learn:** `LinearRegression().fit(X, y)`, `model.coef_`.
- **TensorFlow/Keras:** `tf.keras.Input`, `Dense`, `Model`, `compile`, `fit`.
- **PyTorch:** `nn.Module`, `nn.Linear`, `optim.Adam`, loop de treino com `backward()` e `optimizer.step()`.

---

## Mapa conceitual

```
Python para ML
├── Facilidade de aprendizado
│   ├── Sintaxe e legibilidade
│   ├── Documentação e comunidade
│   └── IDEs e recursos
├── Cálculo e dados
│   ├── NumPy (arrays, matemática)
│   ├── SciPy (científico)
│   └── Pandas (DataFrame, análise)
├── Visualização
│   ├── Matplotlib (gráficos 2D)
│   └── Seaborn (estatístico)
├── Machine Learning
│   └── Scikit-learn (algoritmos, pipelines)
└── Deep Learning
    ├── TensorFlow / Keras
    └── PyTorch
```

---

## Receita prática

1. **Ambiente:** instalar Python 3 e criar ambiente virtual; instalar Jupyter ou usar IDE.
2. **Dados:** usar Pandas para carregar CSV/Excel e explorar (head, describe, tipos).
3. **Visualização:** Matplotlib/Seaborn para distribuições e tendências.
4. **ML clássico:** Scikit-learn para treino/avaliação (train_test_split, métricas).
5. **Deep learning:** Keras (TensorFlow) ou PyTorch conforme projeto (prototipagem vs produção).

---

## Perguntas para teste de reforço

1. Cite duas razões pelas quais o Python é popular em IA/ML. **R:** Sintaxe simples e legível; vasta coleção de bibliotecas (NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch).
2. Para que o Pandas é usado no pipeline de ML? **R:** Manipulação, limpeza e análise de dados; leitura de arquivos; preparação de datasets antes do treino.
3. O que o Scikit-learn oferece além de algoritmos? **R:** Pré-processamento, divisão treino/teste, métricas, pipelines.
4. Keras é independente do TensorFlow? **R:** Hoje não; Keras é a API de alto nível integrada ao TensorFlow.
5. Qual biblioteca é mais associada a pesquisa e grafo dinâmico? **R:** PyTorch.

---

## Materiais de apoio

- Documentação oficial Python: [python.org/docs](https://docs.python.org)  
- NumPy: [numpy.org](https://numpy.org)  
- Pandas: [pandas.pydata.org](https://pandas.pydata.org)  
- Scikit-learn: [scikit-learn.org](https://scikit-learn.org)  
- TensorFlow: [tensorflow.org](https://www.tensorflow.org)  
- PyTorch: [pytorch.org](https://pytorch.org)
