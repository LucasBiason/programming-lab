#!/usr/bin/env python3
"""
Extrai conteúdo didático das aulas da Fase 2 - AI Evolution (PLN, Algoritmos Genéticos, ML na Nuvem, LLMs).
Requisitos: pip install playwright && playwright install chromium
Uso: cd scripts && python3 extract_fase2.py
Faça login na FIAP quando o navegador abrir; pressione Enter para iniciar a extração.
"""

from pathlib import Path
from datetime import date

# (id na URL, pasta da seção, número da aula, título para o arquivo)
# c=13226 para Fase 2
# Nomes das seções: Processamento de Linguagem Natural (6), Introdução algoritmo genético (5), Desenvolvimento de ML na cloud (3), Desvendando o Poder das LLMs (5)
AULAS_FASE2 = [
    # Seção 1 - Processamento de Linguagem Natural
    (
        487484,
        "Seção 1 - Processamento de Linguagem Natural",
        "01",
        "Definição, aplicações",
    ),
    (
        487485,
        "Seção 1 - Processamento de Linguagem Natural",
        "02",
        "Bag of words, Word cloud",
    ),
    (
        487486,
        "Seção 1 - Processamento de Linguagem Natural",
        "03",
        "Tokenização com NLTK e remoção de stop words",
    ),
    (
        487487,
        "Seção 1 - Processamento de Linguagem Natural",
        "04",
        "Stemming, TF IDF e Ngrams",
    ),
    (
        487488,
        "Seção 1 - Processamento de Linguagem Natural",
        "05",
        "Word Embedings com Word2Vec",
    ),
    (
        487489,
        "Seção 1 - Processamento de Linguagem Natural",
        "06",
        "Pré Processamento com Spacy",
    ),
    # Seção 2 - Introdução algoritmo genético
    (
        487501,
        "Seção 2 - Introdução algoritmo genético",
        "01",
        "Introdução à GenAI (Inteligência Gerada por Algoritmos Genéticos)",
    ),
    (
        487502,
        "Seção 2 - Introdução algoritmo genético",
        "02",
        "História e evolução dos Algoritmos Genéticos",
    ),
    (
        487503,
        "Seção 2 - Introdução algoritmo genético",
        "03",
        "Princípios e conceitos fundamentais dos Algoritmos Genéticos",
    ),
    (
        487504,
        "Seção 2 - Introdução algoritmo genético",
        "04",
        "Representação de Indivíduos e Codificação de Genes",
    ),
    (
        487505,
        "Seção 2 - Introdução algoritmo genético",
        "05",
        "Operadores Genéticos - Seleção, Cruzamento e Mutação",
    ),
    # Seção 3 - Desenvolvimento de ML na cloud
    (
        487515,
        "Seção 3 - Desenvolvimento de ML na cloud",
        "01",
        "Introdução ao Desenvolvimento de ML na Nuvem",
    ),
    (
        487516,
        "Seção 3 - Desenvolvimento de ML na cloud",
        "02",
        "Visão geral das Plataformas de Nuvem para ML - AWS, Azure, Google Cloud",
    ),
    (
        487517,
        "Seção 3 - Desenvolvimento de ML na cloud",
        "03",
        "Utilizando recursos escaláveis e de alto desempenho",
    ),
    # Seção 4 - Desvendando o Poder das LLMs
    (
        487522,
        "Seção 4 - Desvendando o Poder das LLMs",
        "01",
        "Introdução às LLM (Large Language Models)",
    ),
    (
        487523,
        "Seção 4 - Desvendando o Poder das LLMs",
        "02",
        "O impacto das LLM na área da tradução e localização",
    ),
    (
        487524,
        "Seção 4 - Desvendando o Poder das LLMs",
        "03",
        "Aplicações Práticas de LLMs em Tradução Automática e Localização",
    ),
    (
        487525,
        "Seção 4 - Desvendando o Poder das LLMs",
        "04",
        "Chatbots e Assistentes Virtuais Impulsionados por LLMs",
    ),
    (
        487526,
        "Seção 4 - Desvendando o Poder das LLMs",
        "05",
        "Construindo Aplicações com LLMs em Projetos Práticos",
    ),
]

BASE_URL = "https://on.fiap.com.br/mod/conteudoshtml/view.php?id={id}&c=13226&sesskey=1sHAKFiiHg"


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Instale: pip install playwright && playwright install chromium")
        raise SystemExit(1)

    script_dir = Path(__file__).resolve().parent
    # Resumos/FIAP-IA-para-Devs/Fase 2 - AI Evolution (grava CONTEUDO DIDATICO aqui também)
    fase2_dir = script_dir.parent / "Fase 2 - AI Evolution"
    apostilas_base = (
        script_dir.parent.parent.parent
        / "Apostilas e Materiais de Cursos"
        / "[FIAP] IA para Devs"
        / "Fase 2"
    )
    apostilas_base.mkdir(parents=True, exist_ok=True)
    state_file = script_dir / ".fiap_session_fase2.json"
    hoje = date.today().strftime("%Y-%m-%d")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state=state_file if state_file.exists() else None
        )
        page = context.new_page()
        page.set_default_timeout(60_000)

        page.goto("https://on.fiap.com.br/", wait_until="domcontentloaded")
        input(
            "Faça login na FIAP (se necessário) e pressione Enter para extrair as aulas da Fase 2... "
        )

        for url_id, section_folder, num, titulo in AULAS_FASE2:
            url = BASE_URL.format(id=url_id)
            dest_dir = apostilas_base / section_folder
            dest_dir.mkdir(parents=True, exist_ok=True)
            out_file = dest_dir / f"CONTEUDO DIDATICO - AULA {num} - {titulo}.md"
            # Também grava na pasta de resumos da Fase 2
            resumos_dir = fase2_dir / section_folder
            resumos_dir.mkdir(parents=True, exist_ok=True)
            out_file_resumos = (
                resumos_dir / f"CONTEUDO DIDATICO - AULA {num} - {titulo}.md"
            )

            print(f"Aula {num} - {titulo[:50]}...", end=" ", flush=True)
            try:
                page.goto(url, wait_until="domcontentloaded")
                page.wait_for_load_state("networkidle", timeout=30_000)
                body_text = page.evaluate(
                    """() => {
                    const iframes = Array.from(document.querySelectorAll('iframe'));
                    let best = '';
                    for (const iframe of iframes) {
                        if (iframe.title === 'reCAPTCHA') continue;
                        try {
                            const doc = iframe.contentDocument;
                            if (doc && doc.body) {
                                const text = doc.body.innerText || '';
                                if (text.length > best.length) best = text;
                            }
                        } catch (e) {}
                    }
                    return best || '(Nenhum iframe de conteúdo acessível. Faça login na FIAP.)';
                }"""
                )
                if not body_text or body_text.strip() == "":
                    body_text = "(Conteúdo vazio ou iframe não carregado. Verifique se está logado na FIAP.)"
                header = f"""# CONTEÚDO DIDÁTICO - AULA {num} - {titulo}

**Fonte:** Página FIAP – Conteúdo digital (extraído em {hoje})
**URL:** https://on.fiap.com.br/mod/conteudoshtml/view.php?id={url_id}&c=13226

---

"""
                content = header + body_text
                out_file.write_text(content, encoding="utf-8")
                out_file_resumos.write_text(content, encoding="utf-8")
                print("OK", out_file.name)
            except Exception as e:
                print("ERRO", e)
                continue

        context.storage_state(path=state_file)
        print("Sessão salva em", state_file.name)
        browser.close()

    print("Concluído. Arquivos em:", apostilas_base)


if __name__ == "__main__":
    main()
