#!/usr/bin/env python3
"""
Captura screenshots do Figma (design Arcane-3) via Playwright.
Salva imagens em docs/figma_captures/ para referência no frontend.

Uso:
  python3 scripts/capture_figma_playwright.py              # headless
  python3 scripts/capture_figma_playwright.py --headed     # browser visível (login no Figma se precisar)
"""

import argparse
from pathlib import Path
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Instale: pip install playwright && playwright install chromium")
    sys.exit(1)

FIGMA_URL = "https://www.figma.com/design/4IF8seRuIodeRCwlzJg8GO/Arcane-3?node-id=0-1&t=7kuMx74wK2kAAvj2-0"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "figma_captures"
VIEWPORT = {"width": 1920, "height": 1080}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Captura screenshots do Figma com Playwright"
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Abre o navegador visível (útil para login no Figma)",
    )
    parser.add_argument(
        "--url", default=FIGMA_URL, help="URL do Figma (default: Arcane-3)"
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        context = browser.new_context(
            viewport=VIEWPORT,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()
        try:
            page.goto(args.url, wait_until="domcontentloaded", timeout=25000)
            page.wait_for_timeout(3000)
            # Fecha banner de cookies se aparecer
            for label in ("Allow all cookies", "Permitir todos os cookies"):
                btn = page.get_by_role("button", name=label)
                if btn.is_visible():
                    btn.click()
                    page.wait_for_timeout(1000)
                    break
            # Figma carrega o canvas de forma assíncrona
            page.wait_for_timeout(10000)

            # Screenshot da viewport (o que cabe na tela)
            viewport_path = OUTPUT_DIR / "arcane3_viewport.png"
            page.screenshot(path=str(viewport_path))
            print(f"Salvo: {viewport_path}")

            # Screenshot da página inteira (pode ser longo no Figma)
            full_path = OUTPUT_DIR / "arcane3_full.png"
            page.screenshot(path=str(full_path), full_page=True)
            print(f"Salvo: {full_path}")
        finally:
            browser.close()

    print(f"Imagens em: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
