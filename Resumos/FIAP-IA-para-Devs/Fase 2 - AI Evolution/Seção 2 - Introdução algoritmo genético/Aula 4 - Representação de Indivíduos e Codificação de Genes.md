# Aula 4 - Representação de Indivíduos e Codificação de Genes

## Resumo executivo

Esta aula trata da **representação de indivíduos** e **codificação de genes** em algoritmos genéticos: como uma solução do problema é mapeada para um **cromossomo** (vetor de genes). Codificações comuns: **binária** (0/1), **inteira** (permutações, índices), **real** (valores contínuos). A escolha da representação afeta **operadores** de cruzamento e mutação e a **decodificação** (fenótipo) para avaliação da fitness. **Permutações** são usadas em TSP e scheduling; **vetores reais** em otimização contínua; **binária** em problemas discretos ou históricos.

**Objetivos de aprendizagem:** Escolher codificação adequada ao problema (binária, inteira, real, permutação); implementar codificação/decodificação; garantir que cruzamento e mutação produzam indivíduos válidos.

---

## Conceitos-chave (flashcards)

1. **O que é codificação binária?** **R:** Cromossomo como vetor de 0s e 1s; útil para subconjuntos, parâmetros discretos; cruzamento e mutação bit a bit.
2. **Quando usar representação por permutação?** **R:** Problemas de ordem (TSP, scheduling); cada gene é único (ex.: cidade ou job); operadores devem preservar permutação (OX, PMX).
3. **Fenótipo vs genótipo?** **R:** Genótipo = cromossomo (representação interna). Fenótipo = solução decodificada usada para calcular a fitness.

---

## Perguntas para teste de reforço

1. Quando usar codificação binária? **R:** Subconjuntos, parâmetros discretos; operadores bit a bit.
2. Em que tipo de problema se usa representação por permutação? **R:** Ordem (TSP, scheduling); cada gene único.
3. O que é fenótipo no contexto de AG? **R:** Solução decodificada usada para calcular a fitness.
4. O que é codificação real? **R:** Cromossomo com valores contínuos; usada em otimização contínua.

---

## Exemplos práticos

```python
# Codificação binária: 5 genes
individuo = [1, 0, 1, 1, 0]

# Codificação real: pesos de um modelo
individuo_real = [0.5, -0.2, 1.1, 0.0]

# Permutação: ordem de cidades (TSP)
permutacao = [2, 0, 3, 1]
```

---

## Materiais de apoio

- DEAP – Creating types: [deap.readthedocs.io/en/master/tutorials/basic/part1.html](https://deap.readthedocs.io/en/master/tutorials/basic/part1.html)
