"""
Documentos — IA: upload, OCR, RAG (Funcionalidades com IA).
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.ocr import ocr_extract_text


class OCRExtractView(APIView):
    """
    POST: envia um arquivo (PDF ou imagem) e recebe o texto extraído (OCR).
    Funcionalidade: OCR (Notion — Funcionalidades com IA).
    """

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request: Request) -> Response:
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"detail": "Envie um arquivo no campo 'file' (PDF ou imagem)."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        content = file.read()
        filename = file.name or "file"
        content_type = getattr(file, "content_type", None)
        try:
            text = ocr_extract_text(content, filename, content_type)
        except Exception as e:
            return Response(
                {"detail": f"Erro ao extrair texto: {e!s}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response({"text": text, "filename": filename})


@api_view(["GET"])
@permission_classes([AllowAny])
def placeholder_list(_request: Request) -> Response:
    """Lista de documentos — em construção (RAG, petições)."""
    return Response({"detail": "Documentos-IA: em construção (RAG, petições)."})
