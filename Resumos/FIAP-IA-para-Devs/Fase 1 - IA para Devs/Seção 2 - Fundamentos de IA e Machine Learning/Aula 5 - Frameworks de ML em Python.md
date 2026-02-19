# Aula 5 - Frameworks de ML em Python

**Fase 1 - IA para Devs** | **Seção 2 - Fundamentos de IA e Machine Learning**

---

## Resumo executivo

Esta aula introduz os **principais frameworks de Machine Learning em Python**: **Scikit-learn** (pipelines, GridSearchCV), **Keras** (interface de alto nível para deep learning), **TensorFlow** (modo eager, escalabilidade) e **PyTorch** (grafo dinâmico, pesquisa). Aborda **pipelines** para encadear pré-processamento e modelagem, **otimização de hiperparâmetros** com Grid Search, conceitos do Keras (camadas personalizadas, callbacks), inovações do TensorFlow 2.x e vantagens do PyTorch (flexibilidade, expressividade). Ao final, você saberá quando usar cada framework e como montar um pipeline de ML com Scikit-learn.

**Objetivos de aprendizagem:**
- Montar um pipeline Scikit-learn (scaler → PCA → classificador) e treinar/avaliar.
- Usar GridSearchCV para buscar melhores hiperparâmetros com validação cruzada.
- Reconhecer o papel do Keras como API de alto nível (TensorFlow).
- Diferenciar TensorFlow (eager, deploy) e PyTorch (grafo dinâmico, pesquisa).
- Aplicar callbacks no Keras quando necessário (salvar pesos, learning rate).

---

## Conceitos-chave (flashcards)

**P:** O que é um pipeline no Scikit-learn?  
**R:** Sequência de etapas (ex.: StandardScaler → PCA → RandomForestClassifier) encadeadas em um único estimador; garante que pré-processamento e modelo sejam aplicados de forma consistente (ex.: fit no treino, transform no teste).

**P:** Para que serve o GridSearchCV?  
**R:** Buscar a melhor combinação de hiperparâmetros em uma grade (param_grid); usa validação cruzada (cv) para avaliar cada combinação; retorna best_params_ e o melhor estimador.

**P:** O que o Keras oferece em relação ao TensorFlow puro?  
**R:** Interface de alto nível: construção de modelos com poucas linhas (Sequential, Dense, compile, fit); abstrai detalhes de baixo nível; suporta múltiplos backends (hoje TensorFlow é o principal).

**P:** O que é o modo eager no TensorFlow 2.x?  
**R:** Execução imediata das operações (não só no Session.run); facilita depuração e escrita de código imperativo; integração natural com Python.

**P:** Por que o PyTorch é popular em pesquisa?  
**R:** Grafo computacional construído dinamicamente (em tempo de execução); código mais intuitivo e fácil de depurar; integração forte com Python (loops, condicionais); flexibilidade para arquiteturas customizadas.

---

## Scikit-learn: pipelines e GridSearch

- **Pipeline:** `Pipeline([('scaler', StandardScaler()), ('pca', PCA(n_components=3)), ('classifier', RandomForestClassifier())])`. Ordem: pré-processamento primeiro, estimador final por último.
- **Treino:** `pipeline.fit(X_train, y_train)`; previsão: `pipeline.predict(X_test)`.
- **GridSearchCV:** definir `param_grid` com nomes no formato `'nome_etapa__parametro': [valores]`; `GridSearchCV(pipeline, param_grid, cv=5)`; `.fit(X_train, y_train)`; acessar `best_params_`, `best_estimator_`.

Exemplo de param_grid para o classificador do pipeline: `'classifier__n_estimators': [50, 100, 150]`, `'classifier__max_depth': [10, 20, 30]`.

---

## Keras

- **Interface de alto nível:** Sequential ou API funcional; camadas Dense, Conv2D, etc.; compile (loss, optimizer, metrics) e fit.
- **Versatilidade:** múltiplos backends (hoje predominantemente TensorFlow); camadas customizadas e callbacks.
- **Callbacks:** ações durante o treino (ModelCheckpoint, EarlyStopping, ReduceLROnPlateau); permitem salvar pesos e ajustar learning rate dinamicamente.

---

## TensorFlow

- **TensorFlow 2.x:** execução eager por padrão; Keras integrado; deploy em produção (TF Serving, TFLite).
- **Uso típico:** projetos que vão para produção, integração com ecossistema Google, modelos grandes e distribuídos.

---

## PyTorch

- **Flexibilidade:** grafo dinâmico; uso natural de control flow (if, for) no modelo; debugging mais simples.
- **Expressividade:** integração com Python; muito usado em pesquisa e prototipagem; comunidade acadêmica forte.
- **Uso típico:** pesquisa, experimentação, arquiteturas novas; também usado em produção (com ferramentas como TorchScript).

---

## Mapa conceitual

```
Frameworks de ML em Python
├── Scikit-learn
│   ├── Pipeline (scaler → redução → modelo)
│   └── GridSearchCV (hiperparâmetros, cv)
├── Keras
│   ├── Interface de alto nível
│   ├── Camadas, callbacks
│   └── Backend (TensorFlow)
├── TensorFlow
│   ├── Eager execution (TF2)
│   └── Escalabilidade, deploy
└── PyTorch
    ├── Grafo dinâmico
    └── Pesquisa, flexibilidade
```

---

## Receita prática

1. **ML clássico (classificação/regressão tabular):** Scikit-learn; montar pipeline com pré-processamento e modelo; usar GridSearchCV para hiperparâmetros.
2. **Deep learning rápido/prototipagem:** Keras (TensorFlow) com Sequential ou API funcional; callbacks para early stopping e checkpoint.
3. **Produção e escala (Google/cloud):** TensorFlow 2 + Keras; considerar TF Serving para deploy.
4. **Pesquisa e modelos customizados:** PyTorch; definir nn.Module, loop de treino explícito, backward e optimizer.step().

---

## Perguntas para teste de reforço

1. Por que usar um Pipeline no Scikit-learn? **R:** Encadear pré-processamento e modelo de forma reproduzível; evitar data leakage (o scaler/PCA é ajustado só no treino) e manter o código organizado.
2. O que GridSearchCV retorna após o fit? **R:** Melhor combinação de hiperparâmetros (best_params_), melhor estimador (best_estimator_) e resultados de validação cruzada.
3. O que são callbacks no Keras? **R:** Funções ou objetos chamados durante o treino (ex.: ao final de cada época) para salvar modelo, ajustar learning rate ou parar cedo.
4. Qual framework é associado a grafo dinâmico? **R:** PyTorch.
5. O que mudou no TensorFlow 2 em relação à execução? **R:** Modo eager como padrão: operações são executadas imediatamente, facilitando debug e uso imperativo.

---

## Materiais de apoio

- Scikit-learn – Pipelines: [scikit-learn.org/stable/modules/compose](https://scikit-learn.org/stable/modules/compose.html)  
- Keras: [keras.io](https://keras.io)  
- TensorFlow: [tensorflow.org](https://www.tensorflow.org)  
- PyTorch: [pytorch.org](https://pytorch.org)
