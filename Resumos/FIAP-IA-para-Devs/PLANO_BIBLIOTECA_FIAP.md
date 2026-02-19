# Plano: Biblioteca de Resumos FIAP IA para Devs

**Objetivo:** Manter uma biblioteca única com 100% do conteúdo do curso, unificando **texto didático (página FIAP)**, **apostila PDF** e **card Notion** em um único arquivo por aula, com estrutura **idêntica ao Notion**.

---

## Ferramenta de extração FIAP (obrigatório)

- **Usar sempre Playwright** (MCP cursor-ide-browser ou script com Playwright).
- **Não usar Firecrawl** para páginas da FIAP: as URLs redirecionam para login quando acessadas sem sessão.
- **Abrir o navegador que já tem a sessão/login salva** (mesmo perfil onde você já logou na FIAP), para que as páginas de conteúdo e PDF carreguem sem precisar digitar senha a cada vez.

---

## Estrutura de pastas (igual ao Notion)

```
Resumos/FIAP-IA-para-Devs/
├── Fase 1 - IA para Devs/
│   ├── Seção 1 - Fundamentos de Inteligência Artificial/
│   │   ├── CONTEUDO DIDATICO - AULA 01 - Introdução e Historia.md   (intermediário)
│   │   ├── Aula 1 - Introdução e história.md                        (resumo final)
│   │   ├── Aula 2 - [título].md
│   │   └── ...
│   ├── Seção 2 - ...
│   └── ...
├── Fase 2 - IA para Devs/
│   └── ...
└── ...
```

- **Um arquivo .md por aula** com o resumo completo (teorias, explicações, diagramas, exercícios, código, perguntas).
- **CONTEUDO DIDATICO** = extração bruta da página FIAP (texto da aula); pode ser removido após merge ou mantido como rastreabilidade.
- **Apostilas e Materiais de Cursos:** manter **apenas PDFs** das apostilas; remover arquivos de “Resumos de Aulas” e demais resumos conforme o processamento avança.

---

## Padrão do arquivo de resumo (.md)

Ao gerar ou editar resumos, **não incluir**:

- **Fontes:** não colocar linha ou seção "Fontes" (ex.: Card Notion, Conteúdo didático, Apostila PDF).
- **Menções ao Notion:** não falar sobre Notion, "resumo no Notion", "base do card" ou equivalente no texto.
- **"O que vem por aí (contexto da aula):** não incluir esse trecho/bloco em nenhum resumo.
- **Materiais de apoio:** na seção "Materiais de apoio" (ou equivalente), incluir **apenas links externos** quando houver (ex.: referências bibliográficas, sites). Não listar Conteúdo didático FIAP, apostila PDF FIAP nem card Notion.
- **Rodapé:** não incluir "Atualizado:", "Status:" ou similar no final do arquivo.

---

## Fluxo por aula

1. **Extrair texto didático**
   - **Playwright:** abrir o navegador que já tem a sessão/login FIAP salva (não usar Firecrawl).
   - Navegar para a URL da aula (ex.: `conteudoshtml/view.php?id=...&c=...&sesskey=...`).
   - Extrair todo o texto do **iframe:** `page.evaluate(() => document.querySelector('iframe').contentDocument.body.innerText)`.
   - **Persistir:** o resultado do evaluate vem como string (com `\n`). Gravar em `CONTEUDO DIDATICO - AULA NN - [Título].md` em **Apostilas e Materiais de Cursos/[FIAP] IA para Devs/Fase X/Seção Y - [nome]/**.
   - **Script auxiliar:** `scripts/save_conteudo_from_result.py` lê um arquivo com `### Result` + string entre aspas e gera o .md (uso quando o output do tool for salvo em arquivo).

2. **Extrair apostila PDF**
   - **Playwright (mesmo navegador com sessão):** abrir a URL do PDF (ex.: `conteudospdf/view.php?c=...&id=...`).
   - Baixar o PDF ou extrair texto/imagens do viewer (conforme disponível).
   - Incluir no resumo unificado (ou anexar referência se for só link).

3. **Extrair card Notion**
   - Obter título, Descrição e corpo (blocks) do card da aula.
   - Fonte: `notion-hierarchy.md` + MCP Notion (get_page e blocos filhos, se disponível).

4. **Unificar e gerar resumo completo**
   - Unificar: texto didático + apostila (texto/imagens) + conteúdo do card Notion.
   - Gerar um único `.md` com: teorias, explicações, diagramas (Mermaid), exercícios, código, flashcards, perguntas de reforço (formato study-summary-rich).
   - Salvar em: `Fase X - IA para Devs/Seção Y - [nome]/Aula Z - [título].md`.

5. **Replicar no Notion**
   - Converter o resumo .md em blocks (heading_1/2/3, paragraph, listas, code, callout, divider).
   - Atualizar o corpo do card da aula no Notion.
   - _Nota:_ Pode ser necessário usar script do `notion-automation-suite` (md→blocks + `append_blocks(block_id, children)`).

6. **Limpeza em Apostilas e Materiais**
   - Remover arquivos de resumo antigos em `Apostilas e Materiais de Cursos/[FIAP] IA para Devs/` (ex.: “Resumos de Aulas”).
   - Manter apenas as apostilas em PDF em cada pasta (Apostilas/Seção X/).

---

## Ordem de execução

- Por **fase** → **seção** → **aula**.
- Exemplo Fase 1: Seção 1 (Fundamentos de IA) → Aulas 1, 2, 3, 4; depois demais seções.
- Repetir para todas as fases do curso até completar a biblioteca.

---

## Referências

- **Hierarquia Notion:** `Infraestrutura/cursor-multiagent-system/config/studies/catalogo/fiap/notion-hierarchy.md`
- **Mapeamento resumos:** `config/studies/catalogo/fiap/resumos-map.md`
- **Skill resumos:** `study-summary-rich` (estrutura de resumo rico)
- **URLs FIAP:** obtidas na página “Conteúdo digital” com sessão logada (ou mapeamento id/c por aula).
