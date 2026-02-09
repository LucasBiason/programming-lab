"""
Documentos - IA: OCR, upload, RAG (Funcionalidades com IA).
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.placeholder_list),
    path("ocr/", views.OCRExtractView.as_view(), name="documents-ocr"),
]
