#!/usr/bin/env python3
"""
Acessa a página Notion 'Funcionalidades com IA' via Playwright (evita ERR_BLOCKED_BY_CLIENT).
Salva o conteúdo em docs/FUNCIONALIDADES_COM_IA.md e redacta possíveis secrets.
"""

from pathlib import Path
import re
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Instale: pip install playwright && playwright install chromium")
    sys.exit(1)

NOTION_URL = "https://grizzly-amaranthus-f6a.notion.site/Funcionalidades-com-IA-2fc6cf8ea89f80d18000dfac39b15b46"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_FILE = OUTPUT_DIR / "FUNCIONALIDADES_COM_IA.md"


def redact_secrets(text: str) -> str:
    """Redacta apenas padrões claros de API key (ex.: OpenAI sk-proj-...)."""
    text = re.sub(r"sk-proj-[A-Za-z0-9_-]{20,}", "sk-proj-***REDACTED***", text)
    return text


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; rv:131.0) Gecko/20100101 Firefox/131.0"
        )
        page = context.new_page()
        try:
            page.goto(NOTION_URL, wait_until="domcontentloaded", timeout=15000)
            page.wait_for_timeout(3000)
            # Notion renderiza conteúdo em article ou [data-content-editable-root]
            content = page.evaluate("""() => {
                const el = document.querySelector('article') || document.querySelector('[data-content-editable-root]') || document.querySelector('main') || document.body;
                return el ? el.innerText : document.body.innerText;
            }""")
        finally:
            browser.close()

    if not content or len(content.strip()) < 10:
        print("Aviso: pouco conteúdo extraído. Verifique a URL ou o seletor.")
    content = redact_secrets(content)

    header = f"""# Funcionalidades com IA

**Fonte (Notion):** [Funcionalidades com IA]({NOTION_URL})

Conteúdo extraído via Playwright em execução local (evita bloqueio de extensões).

---

"""
    OUTPUT_FILE.write_text(header + content.strip(), encoding="utf-8")
    print(f"Conteúdo salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
