# Aula 06 - Quick Wins

**Módulo:** Fundamentos IA Generativa | **Curso:** Full Cycle MBA

---

## Resumo executivo

- **Context 7:** Repositório de documentações oficiais de libs, linguagens e frameworks; oferece servidor MCP.
- **MCP (Model Context Protocol):** Padrão para expor ferramentas e dados a agentes de IA.
- **Uso com Claude Code:**
  1. `claude mcp add --transport http context7 https://mcp.context7.com/mcp`
  2. Entrar na pasta do projeto: `cd ~/Project` e `claude`
  3. Prompt: Analise o codebase (src, requirements.txt), identifique bibliotecas, use Context7 para buscar documentação de cada uma e crie arquivos em `/docs/libs` (ex.: LANGCHAIN.md, PINECONE.md). **Garanta que utilizará o Context7 MCP.**
- **Documentação defasada:** Clonar o repo oficial na versão usada e pedir à IA para vasculhar e gerar doc/snippets. Para sites com muitas subpáginas: **Firecrawl** (MCP) para navegação recursiva.

---

## Conceitos-chave (flashcards)

- **P: O que é Context 7?**  
  R: Serviço com documentações oficiais de libs e frameworks; acessível via MCP.

- **P: O que é MCP?**  
  R: Model Context Protocol — padrão para conectar ferramentas e fontes de dados a agentes de IA.

- **P: Quando usar Firecrawl?**  
  R: Para sites com muitas subpáginas; faz webscraping recursivo e condensa a documentação.

- **P: E se a doc oficial estiver desatualizada?**  
  R: Clonar o repositório da lib na versão que você usa e pedir à IA para extrair informação do código.

---

## Mapa conceitual

```
Context 7 e MCP
├── Context 7
│   └── Doc oficial de libs via MCP
├── MCP
│   └── Protocolo para ferramentas/dados
├── Workflow
│   └── Analisar codebase → Context7 → /docs/libs
└── Alternativas
    ├── Clonar repo oficial
    └── Firecrawl (webscraping)
```

---

## Perguntas de reforço

1. Context 7 substitui o README da lib? Não; Context 7 fornece a doc oficial; você pode condensá-la em /docs/libs.
2. MCP funciona só com Claude? Não; é um protocolo; outras ferramentas podem implementá-lo.
3. Firecrawl é gratuito? Depende do plano; verificar em firecrawl.dev.
