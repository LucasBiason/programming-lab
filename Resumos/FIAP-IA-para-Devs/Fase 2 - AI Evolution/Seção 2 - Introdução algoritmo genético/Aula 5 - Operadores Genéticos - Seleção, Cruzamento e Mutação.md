# Aula 5 - Operadores Genéticos - Seleção, Cruzamento e Mutação

## Resumo executivo

Esta aula detalha os **operadores genéticos**: **Seleção** (escolher pais para a próxima geração; métodos: torneio, roleta, ranking), **Cruzamento** (recombinação de dois pais para gerar filhos; one-point, two-point, uniforme para binário; BLX, aritmético para real; OX, PMX para permutações), **Mutação** (alteração aleatória de genes para manter diversidade; flip de bit, Gaussian para real, swap para permutações). Taxas de cruzamento e mutação controlam exploração e convergência. Implementação em bibliotecas como DEAP.

**Objetivos de aprendizagem:** Aplicar seleção por torneio ou roleta; implementar cruzamento e mutação compatíveis com a codificação; ajustar taxas de cruzamento e mutação.

---

## Conceitos-chave (flashcards)

1. **O que é seleção por torneio?** **R:** Escolher k indivíduos aleatórios e selecionar o melhor (ou pior, para diversidade); k controla a pressão seletiva.
2. **Cruzamento one-point?** **R:** Cortar dois pais em um ponto e trocar as caudas; gera dois filhos a partir de dois pais.
3. **Por que mutação é necessária?** **R:** Reintroduz diversidade; evita convergência prematura; permite escapar de ótimos locais.

---

## Perguntas para teste de reforço

1. O que é seleção por torneio? **R:** Escolher k indivíduos aleatórios e selecionar o melhor; k controla a pressão seletiva.
2. Descreva cruzamento one-point. **R:** Cortar dois pais em um ponto e trocar as caudas; gera dois filhos.
3. Por que a mutação é essencial no AG? **R:** Reintroduz diversidade e ajuda a escapar de ótimos locais.
4. Cite um operador de cruzamento para permutações. **R:** OX (Order Crossover) ou PMX (Partially Mapped Crossover).

---

## Exemplos práticos

```python
# DEAP - operadores típicos
from deap import base, tools

toolbox = base.Toolbox()
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
```

---

## Materiais de apoio

- DEAP – Operators: [deap.readthedocs.io/en/master/api/tools.html](https://deap.readthedocs.io/en/master/api/tools.html)
