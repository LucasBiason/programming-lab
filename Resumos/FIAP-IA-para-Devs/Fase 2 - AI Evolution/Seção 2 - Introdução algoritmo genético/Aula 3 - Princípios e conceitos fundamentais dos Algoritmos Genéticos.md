# Aula 3 - Princípios e conceitos fundamentais dos Algoritmos Genéticos

## Resumo executivo

Esta aula detalha os **princípios e conceitos fundamentais** dos algoritmos genéticos: **população** (conjunto de indivíduos), **indivíduo/cromossomo** (uma solução candidata codificada), **geração** (ciclo de seleção–cruzamento–mutação), **espaço de busca** (domínio das soluções), **exploração vs exploração** (diversidade vs refinamento). **Convergência** e **diversidade** devem ser balanceadas; **elitismo** (manter os melhores na próxima geração) e **pressão seletiva** (intensidade da seleção) afetam o comportamento. Critérios de parada: número máximo de gerações, fitness alvo ou estagnação.

**Objetivos de aprendizagem:** Definir população, cromossomo, geração; explicar trade-off exploração/exploração; descrever elitismo e critérios de parada.

---

## Conceitos-chave (flashcards)

1. **O que é população em AG?** **R:** Conjunto de indivíduos (cromossomos), cada um representando uma solução candidata; evolui ao longo das gerações.
2. **Exploração vs exploração?** **R:** Exploração = buscar novas regiões do espaço (diversidade, mutação). Exploração = refinar soluções boas (seleção, cruzamento). Equilíbrio é essencial.
3. **O que é elitismo?** **R:** Garantir que os melhores indivíduos da geração atual passem intactos para a próxima; evita perder a melhor solução encontrada.

---

## Perguntas para teste de reforço

1. O que é população em um AG? **R:** Conjunto de indivíduos (cromossomos), cada um uma solução candidata.
2. Explique o trade-off exploração vs exploração. **R:** Exploração = diversidade (mutação); exploração = refinamento (seleção). É preciso equilíbrio.
3. O que é elitismo e por que usar? **R:** Manter os melhores na próxima geração; evita perder a melhor solução.
4. Cite dois critérios de parada típicos em AG. **R:** Número máximo de gerações, fitness alvo, estagnação.

---

## Materiais de apoio

- DEAP – Tutorial: [deap.readthedocs.io/en/master/tutorials/basic](https://deap.readthedocs.io/en/master/tutorials/basic/)
