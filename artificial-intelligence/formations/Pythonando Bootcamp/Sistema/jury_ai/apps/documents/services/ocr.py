"""
OCR / transcrição de documentos — Docling (Notion: Funcionalidades com IA).
O tutorial do Bootcamp indica uso de Docling para extração de texto de PDF e imagens.
"""

import tempfile
from pathlib import Path

try:
    from docling.document_converter import DocumentConverter
except ImportError:
    DocumentConverter = None


def _extract_with_docling(file_path: str) -> str:
    """Extrai texto com Docling (PDF, imagens, DOCX, etc.)."""
    if DocumentConverter is None:
        raise ImportError(
            "Docling não está instalado. Instale com: pip install docling"
        )
    converter = DocumentConverter()
    result = converter.convert(file_path)
    return result.document.export_to_markdown().strip()


def ocr_extract_text(
    content: bytes, filename: str, content_type: str | None = None
) -> str:
    """
    Extrai texto de arquivo usando Docling (conforme tutorial do Bootcamp / Notion).

    Suporta PDF, imagens (PNG, JPEG, TIFF, etc.), DOCX e outros formatos
    suportados pelo Docling. O conteúdo é escrito em um arquivo temporário
    e processado pelo DocumentConverter.

    Retorna string vazia se o formato não for suportado ou Docling não estiver instalado.
    """
    if DocumentConverter is None:
        return ""

    suf = Path(filename).suffix.lower()
    # Extensões que o Docling costuma suportar
    supported = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".tiff",
        ".tif",
        ".docx",
        ".pptx",
        ".xlsx",
        ".html",
        ".htm",
    }
    if suf not in supported:
        return ""

    try:
        with tempfile.NamedTemporaryFile(suffix=suf, delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            return _extract_with_docling(tmp_path)
        finally:
            Path(tmp_path).unlink(missing_ok=True)
    except Exception:
        return ""
