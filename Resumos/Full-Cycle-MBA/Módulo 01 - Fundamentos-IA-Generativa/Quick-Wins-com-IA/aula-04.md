# Aula 04 - Quick Wins

**Módulo:** Fundamentos IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Tipos de documentos essenciais:**

| Tipo           | Uso                                                                |
| -------------- | ------------------------------------------------------------------ |
| Contexto Geral | Descreve do que o projeto se trata (produto, técnica)              |
| Stack / Libs   | Libs e frameworks; acesso à doc (Context7); clonar repo; Firecrawl |
| Guidelines     | Regras para IA (formatação, documentação, testes)                  |
| README         | Execução do projeto, índice da documentação                        |
| ADRs           | Por que determinada arquitetura/ferramenta foi escolhida           |
| Plano de ação  | Visão de alto nível do que será desenvolvido                       |
| Tarefa         | Itens passo a passo + TODO list                                    |
| State.local.md | Estado atual do projeto, onde parou o desenvolvimento              |

- **Nota mental:** Cada novo chat é como um novo dev entrando na empresa — precisa do que for necessário para entregar a tarefa com eficiência.

---

## Conceitos-chave (flashcards)

- **P: Para que serve o State.local.md?**  
  R: Indicar onde o desenvolvimento parou; evita que a IA "perca o fio da meada" em sessões longas.

- **P: O que são ADRs?**  
  R: Architecture Decision Records — registram decisões técnicas e suas justificativas.

- **P: Qual documento descreve o produto?**  
  R: Contexto Geral (ou PRD, Product Requirements Document).

- **P: Por que Guidelines separadas do README?**  
  R: README descreve o projeto; Guidelines orientam como a IA e o time devem trabalhar.

---

## Mapa conceitual

```
Documentos essenciais
├── Contexto Geral / Stack / Guidelines
├── README / ADRs
├── Plano de ação / Tarefa
├── State.local.md
└── Princípio
    └── Novo chat = novo dev (precisa de contexto)
```

---

## Perguntas de reforço

1. State.local.md deve ir no git? Não; é estado local; use .gitignore.
2. ADR ajuda a IA? Sim; explica o "porquê" das decisões, evitando sugestões que contrariem a arquitetura.
3. Quantos documentos criar antes de usar IA? O mínimo: README + stack + State.local.md; o ideal inclui Guidelines e ADRs quando existirem.
