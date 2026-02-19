# Aula 03 - Quick Wins

**Módulo:** Fundamentos IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Context Engineering:** Construção de sistemas e workflows que fornecem as informações e ferramentas corretas no formato ideal para a LLM.
- **Problema central:** A maioria das falhas em sistemas baseados em LLM não ocorre porque o modelo é ruim, mas porque contexto, instruções ou ferramentas não foram fornecidos adequadamente.
- **Referência:** [The Rise of Context Engineering (LangChain)](https://blog.langchain.com/the-rise-of-context-engineering/).

---

## Conceitos-chave (flashcards)

- **P: O que é Context Engineering?**  
  R: Projetar sistemas que entregam o contexto certo (documentos, instruções, ferramentas) no formato ideal para a LLM.

- **P: Por que o modelo "erra" com frequência?**  
  R: Em muitos casos, não é capacidade do modelo, e sim falta de contexto, instruções mal escritas ou ferramentas mal expostas.

- **P: O que inclui Context Engineering além do prompt?**  
  R: Organização de contextos dinâmicos, integração de múltiplas fontes e formatação adequada para o modelo.

---

## Mapa conceitual

```
Context Engineering
├── Objetivo
│   └── Contexto certo, formato certo
├── Causa de falhas
│   └── Contexto/instruções/ferramentas inadequados
├── Escopo
│   ├── Prompt (instruções)
│   ├── Documentos dinâmicos
│   └── Ferramentas e formatação
└── Ref
    └── blog.langchain.com
```

---

## Perguntas de reforço

1. Prompt Engineering é suficiente? Para tarefas complexas, não; Context Engineering cobre prompt + fluxo + documentos.
2. O que "formato ideal" significa? Estruturar o input (JSON, markdown, bullets) para maximizar a qualidade da saída.
3. Quem define o contexto? O desenvolvedor/arquiteto; a IA consome o que é fornecido.
