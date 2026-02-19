#!/usr/bin/env python3
"""
Extrai conteúdo didático das aulas da Fase 1 – Seção 4 (Aulas 2–7) e Seção 5 (Aulas 1–6)
abrindo a página FIAP no navegador e copiando o texto do iframe.

Requisitos: pip install playwright && playwright install chromium

Uso:
  1. cd scripts && python3 extract_fase1_s4_s5.py
  2. Quando o navegador abrir, faça login na FIAP (se ainda não estiver logado).
  3. No terminal, pressione Enter para o script começar a extrair.
  4. Ao final, a sessão é salva em .fiap_session.json; na próxima execução
     o script carrega essa sessão e não pede login de novo.

Login automático (opcional): defina FIAP_USER e FIAP_PASS no ambiente. Se a página
exibir reCAPTCHA, resolva no navegador e pressione Enter no terminal quando pedido.
  FIAP_USER=seu_usuario FIAP_PASS=sua_senha python3 extract_fase1_s4_s5.py
"""

from pathlib import Path
from datetime import date

# (id na URL, pasta da seção em Apostilas, número da aula, título para o arquivo)
AULAS = [
    # Seção 4 - Machine Learning Avançado
    (473858, "Seção 4 - Machine Learning Avançado", "02", "KNN, SVM"),
    (473859, "Seção 4 - Machine Learning Avançado", "03", "Kmeans"),
    (
        473860,
        "Seção 4 - Machine Learning Avançado",
        "04",
        "Modelos Baseados em Árvores",
    ),
    (
        473861,
        "Seção 4 - Machine Learning Avançado",
        "05",
        "Validação Cruzada e Pipeline no Sklearn",
    ),
    (
        473862,
        "Seção 4 - Machine Learning Avançado",
        "06",
        "Classification report e métricas de classificação",
    ),
    (473863, "Seção 4 - Machine Learning Avançado", "07", "AUC score e ROC Curve"),
    # Seção 5 - Computer Vision
    (473873, "Seção 5 - Computer Vision", "01", "Introdução a Visão Computacional"),
    (
        473874,
        "Seção 5 - Computer Vision",
        "02",
        "Extração de texto a partir de imagens ou PDF (OCR)",
    ),
    (473875, "Seção 5 - Computer Vision", "03", "Detecção e Rastreamento de objetos"),
    (473876, "Seção 5 - Computer Vision", "04", "Redes Neurais Convolucionais (CNN)"),
    (473877, "Seção 5 - Computer Vision", "05", "Redes Neurais Pré-Treinadas (Yolo)"),
    (473878, "Seção 5 - Computer Vision", "06", "Redes Neurais Adversativas (GAN)"),
]

BASE_URL = "https://on.fiap.com.br/mod/conteudoshtml/view.php?id={id}&c=12967&sesskey=1sHAKFiiHg"


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Instale: pip install playwright && playwright install chromium")
        raise SystemExit(1)

    # Pasta Apostilas: a partir do script, sobe para Estudos e entra em Apostilas
    script_dir = Path(__file__).resolve().parent
    # Estudos/programming-lab/Resumos/FIAP-IA-para-Devs/scripts -> 4 níveis até Estudos
    estudos = script_dir.parent.parent.parent.parent
    apostilas_base = (
        estudos / "Apostilas e Materiais de Cursos" / "[FIAP] IA para Devs" / "Fase 1"
    )
    apostilas_base.mkdir(parents=True, exist_ok=True)
    state_file = script_dir / ".fiap_session.json"

    hoje = date.today().strftime("%Y-%m-%d")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            storage_state=state_file if state_file.exists() else None
        )
        page = context.new_page()
        page.set_default_timeout(60_000)

        # Abre a página inicial da FIAP; tenta login automático se FIAP_USER e FIAP_PASS estiverem definidos
        page.goto("https://on.fiap.com.br/", wait_until="domcontentloaded")
        fiap_user = os.environ.get("FIAP_USER")
        fiap_pass = os.environ.get("FIAP_PASS")
        if fiap_user and fiap_pass:
            page.goto(
                "https://on.fiap.com.br/login/index.php", wait_until="domcontentloaded"
            )
            page.wait_for_load_state("networkidle", timeout=15_000)
            try:
                page.locator("#usuario").fill(fiap_user)
                page.locator("#senha").fill(fiap_pass)
                page.locator("#logar").click()
                page.wait_for_load_state("networkidle", timeout=20_000)
                # Se aparecer reCAPTCHA, usuário resolve no navegador
                if (
                    "recaptcha" in page.content().lower()
                    or page.locator("iframe[title='reCAPTCHA']").count() > 0
                ):
                    input(
                        "Resolva o reCAPTCHA no navegador (se apareceu) e pressione Enter para extrair... "
                    )
                else:
                    page.wait_for_url(
                        lambda u: "on.fiap.com.br" in u and "login" not in u,
                        timeout=15_000,
                    )
            except Exception as e:
                print("Login automático falhou:", e)
                input(
                    "Faça login manualmente no navegador e pressione Enter para extrair as 12 aulas... "
                )
        else:
            input(
                "Faça login na FIAP no navegador (se necessário) e pressione Enter para extrair as 12 aulas... "
            )

        for url_id, section_folder, num, titulo in AULAS:
            url = BASE_URL.format(id=url_id)
            dest_dir = apostilas_base / section_folder
            dest_dir.mkdir(parents=True, exist_ok=True)
            out_file = dest_dir / f"CONTEUDO DIDATICO - AULA {num} - {titulo}.md"

            print(f"Aula {num} - {titulo} ...", end=" ", flush=True)
            try:
                page.goto(url, wait_until="domcontentloaded")
                page.wait_for_load_state("networkidle", timeout=30_000)
                # Pega o iframe de conteúdo (ignora reCAPTCHA): o que tiver body maior
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
**URL:** https://on.fiap.com.br/mod/conteudoshtml/view.php?id={url_id}&c=12967

---

"""
                out_file.write_text(header + body_text, encoding="utf-8")
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
