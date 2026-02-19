# Aula 1 - Introdução à GenAI (Inteligência Gerada por Algoritmos Genéticos)

## Resumo executivo

Esta aula introduz **GenAI** no sentido de **inteligência gerada por algoritmos genéticos**: técnicas de otimização inspiradas na **evolução natural** (seleção, reprodução, mutação) para buscar boas soluções em espaços de busca grandes ou complexos. Difere de "IA generativa" (geração de conteúdo com redes neurais): aqui **algoritmos genéticos (AG)** evoluem uma **população** de **indivíduos** (cromossomos) ao longo de **gerações**, usando **função de aptidão (fitness)** para guiar a seleção. Aplicações: otimização de parâmetros, design, scheduling, aprendizado de redes neurais (neuroevolução).

**Objetivos de aprendizagem:** Diferenciar GenAI por AG de IA generativa (LLMs, GANs); descrever ideia de população, fitness e evolução; citar aplicações de algoritmos genéticos.

---

## Conceitos-chave (flashcards)

1. **O que são algoritmos genéticos (AG)?** **R:** Metaheurísticas inspiradas na evolução: população de soluções candidatas evolui por seleção, cruzamento e mutação, guiadas por uma função de aptidão.
2. **O que é fitness?** **R:** Função que avalia a qualidade de um indivíduo (solução); quanto maior (ou menor, conforme a convenção), melhor; guia a seleção para reprodução.
3. **GenAI por AG vs IA generativa?** **R:** GenAI/AG = otimização evolutiva (busca de soluções). IA generativa = modelos que geram conteúdo (texto, imagem), ex.: LLMs, GANs.

---

## Mapa conceitual

```
GenAI (Algoritmos Genéticos)
├── Inspiração: evolução natural (seleção, reprodução, mutação)
├── População, indivíduos (cromossomos), gerações
├── Função de aptidão (fitness)
├── Operadores: seleção, cruzamento, mutação
└── Aplicações: otimização, design, scheduling, neuroevolução
```

---

## Receita prática

1. Definir representação (codificação) da solução (cromossomo). 2. Definir função de fitness. 3. Inicializar população aleatória. 4. Loop: avaliar fitness → selecionar → cruzar → mutar → nova geração; repetir até critério de parada.

---

## Perguntas para teste de reforço

1. O que é GenAI no contexto de algoritmos genéticos? **R:** Inteligência gerada por evolução de uma população de soluções usando seleção, cruzamento e mutação, guiadas por fitness.
2. Qual a diferença entre GenAI por AG e IA generativa (ex.: ChatGPT)? **R:** AG = otimização evolutiva para buscar soluções; IA generativa = modelos que geram conteúdo (texto, imagem).
3. O que é função de fitness? **R:** Mede a qualidade de um indivíduo (solução); guia a seleção dos que vão reproduzir.
4. Cite uma aplicação de algoritmos genéticos. **R:** Otimização de parâmetros, design, scheduling, neuroevolução.

---

## Materiais de apoio

- DEAP (Distributed Evolutionary Algorithms in Python): [deap.readthedocs.io](https://deap.readthedocs.io/)
- Holland, J. – Adaptation in Natural and Artificial Systems (1975)
