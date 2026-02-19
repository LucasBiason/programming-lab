# Aula 05 - Quick Wins

**Módulo:** Fundamentos IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Janelas de contexto:** Todo modelo tem limite de tokens por interação. Ao ultrapassar, o modelo "esquece" o início (sliding window).
- **Recomendação:** Um chat por tarefa ou subtarefa — evita estourar a janela e mantém foco.
- **Trade-off:** Mais contexto = mais precisão, mas menos espaço para a conversa; documentos longos consomem tokens.
- **Modelos com janelas grandes:** Gemini 2.5 Pro, GPT-4.1 — até 1M tokens — ajudam em projetos complexos.

---

## Conceitos-chave (flashcards)

- **P: O que é janela de contexto?**  
  R: Número máximo de tokens que o modelo considera em uma única interação; além disso, o início é "esquecido".

- **P: O que é sliding window?**  
  R: Quando a janela é ultrapassada, os tokens mais antigos saem e os mais recentes entram.

- **P: Por que "um chat por tarefa"?**  
  R: Mantém contexto focado, evita poluir a janela e facilita retomar depois.

- **P: Mais documentos = sempre melhor?**  
  R: Não; documentos consomem tokens; é preciso equilibrar contexto vs espaço para a conversa.

---

## Mapa conceitual

```
Janelas de contexto
├── Limite de tokens por interação
├── Sliding window (esquece início)
├── Estratégia
│   └── Um chat por tarefa
├── Trade-off
│   └── Contexto vs espaço para conversa
└── Modelos grandes
    └── 1M tokens (Gemini, GPT)
```

---

## Perguntas de reforço

1. O que acontece se passar do limite? O modelo perde o início da conversa; respostas podem ficar incoerentes.
2. Quando usar modelos de janela grande? Projetos com muitos arquivos, documentação extensa ou conversas longas.
3. Posso colar todo o código no chat? Só se couber na janela; prefira referenciar arquivos ou trechos relevantes.
