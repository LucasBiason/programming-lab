# Aula 02 - Quick Wins

**Módulo:** Fundamentos IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Documentos de contexto:** Ativos de longo prazo, como testes automatizados; reduzem complexidade com o tempo.
- **Rules / Memories:**
  - **Rules:** Regras que a IA deve seguir (formatação, padrões, testes).
  - **Memories:** Lembretes de comportamento (ex.: "Sempre documentar funções públicas com comentário acima").
- **Onde configurar:** Cursor: `.cursor/rules`. Claude Code: `CLAUDE.md` (ou equivalente).
- **Context Engineering vs Prompt Engineering:** Prompt = instruções estáticas. Context = isso + contextos dinâmicos, múltiplas fontes e formatação adequada para o modelo.

---

## Conceitos-chave (flashcards)

- **P: O que são Rules no contexto de IA para dev?**  
  R: Arquivos que definem regras que a IA deve seguir (convenções, testes, estilo).

- **P: O que são Memories?**  
  R: Lembretes de comportamento persistente; a IA aplica em toda interação (ex.: documentar funções públicas).

- **P: Onde ficam as rules no Cursor?**  
  R: Pasta `.cursor/rules`; cada arquivo pode cobrir um aspecto (estilo, testes, stack).

- **P: Context Engineering vs Prompt Engineering?**  
  R: Prompt = texto estático. Context = instruções + documentos dinâmicos + ferramentas + formatação ideal para a LLM.

---

## Mapa conceitual

```
Documentos de contexto
├── Rules (regras)
│   └── O que a IA deve seguir
├── Memories (lembretes)
│   └── Comportamento persistente
├── Localização
│   ├── Cursor: .cursor/rules
│   └── Claude: CLAUDE.md
└── Context Engineering
    └── Além do prompt: contexto dinâmico, múltiplas fontes
```

---

## Perguntas de reforço

1. Rules substituem o README? Não; README descreve o projeto; Rules orientam como a IA deve agir.
2. A IA usa Memories automaticamente? Sim, quando configuradas no ambiente (ex.: Cursor memories).
3. Por que "Context Engineering" é importante? A maioria das falhas em sistemas com LLM vem de contexto, instruções ou ferramentas inadequadas, não do modelo em si.
