# Aula 3 - Utilizando recursos escaláveis e de alto desempenho

## Resumo executivo

Esta aula trata do **uso de recursos escaláveis e de alto desempenho** para ML na nuvem: **compute** sob demanda (instâncias CPU/GPU/TPU), **escalonamento horizontal** (múltiplos workers para treino distribuído), **escalonamento de inferência** (auto-scaling de endpoints), **armazenamento** escalável (objetos, data lakes) e **pipelines** orquestrados. Conceitos de **treino distribuído** (data parallel, model parallel), **batch vs tempo real**, **spot/preemptible** para redução de custo, e **monitoramento** de uso e custos. Boas práticas: escolher tamanho de instância, usar spot quando possível, definir políticas de scaling.

**Objetivos de aprendizagem:** Configurar clusters de treino (ex.: SageMaker, Vertex); distinguir inferência em batch e em tempo real; aplicar auto-scaling e políticas de custo (spot).

---

## Conceitos-chave (flashcards)

1. **O que é treino distribuído?** **R:** Dividir dados ou modelo entre múltiplos workers (data parallel ou model parallel) para acelerar o treino em grandes conjuntos ou modelos.
2. **Inferência batch vs tempo real?** **R:** Batch = processar grandes volumes em jobs agendados (menor custo por exemplo). Tempo real = baixa latência, endpoints escalonados (maior custo, maior disponibilidade).
3. **O que são instâncias spot/preemptible?** **R:** Recursos com preço reduzido que podem ser interrompidos pela cloud; úteis para treino tolerante a falhas e economia.

---

## Perguntas para teste de reforço

1. O que é treino distribuído? **R:** Dividir dados ou modelo entre múltiplos workers para acelerar o treino.
2. Diferença entre inferência em batch e em tempo real? **R:** Batch = jobs agendados, menor custo; tempo real = endpoints, baixa latência.
3. Para que servem instâncias spot? **R:** Redução de custo em cargas tolerantes a interrupção (ex.: treino).
4. O que é auto-scaling em inferência? **R:** Ajustar número de réplicas conforme a demanda para equilibrar custo e disponibilidade.

---

## Materiais de apoio

- AWS – Distributed Training: [docs.aws.amazon.com/sagemaker](https://docs.aws.amazon.com/sagemaker/)
- Google Cloud – Training options: [cloud.google.com/vertex-ai/docs/training](https://cloud.google.com/vertex-ai/docs/training)
