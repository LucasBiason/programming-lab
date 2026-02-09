"""
Testes para apps.documents.views (OCR e placeholder).
"""

import io
from unittest.mock import patch

import pytest
from rest_framework import status


@pytest.mark.django_db
class TestOCRExtractView:
    """Testes do endpoint de OCR."""

    def test_post_without_file_returns_400(self, authenticated_client):
        response = authenticated_client.post("/api/documents/ocr/")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "file" in (response.json().get("detail") or "").lower()

    @patch("apps.documents.views.ocr_extract_text")
    def test_post_with_file_returns_text(self, mock_ocr, authenticated_client):
        mock_ocr.return_value = "Texto extraído"
        f = io.BytesIO(b"fake pdf content")
        f.name = "doc.pdf"
        response = authenticated_client.post(
            "/api/documents/ocr/",
            data={"file": f},
            format="multipart",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get("text") == "Texto extraído"
        assert response.json().get("filename") == "doc.pdf"


@pytest.mark.django_db
def test_placeholder_list_returns_200(api_client):
    response = api_client.get("/api/documents/")
    assert response.status_code == status.HTTP_200_OK
    assert "em construção" in (response.json().get("detail") or "").lower()
