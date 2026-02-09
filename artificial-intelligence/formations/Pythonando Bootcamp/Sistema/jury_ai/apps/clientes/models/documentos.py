"""
Modelo de documento do cliente (Contrato, Petição, etc.).

O campo content armazena o texto extraído pelo OCR (Docling). No arcabe3
usa-se MartorField; aqui mantemos TextField por simplicidade (ver
CONSTRUCAO_DA_BASE.md - Decisões de paridade).
"""

from django.db import models

from .cliente import Cliente


class Documentos(models.Model):
    """Documento vinculado a um cliente (arquivo + conteúdo para RAG e análise)."""

    TIPO_CHOICES = [
        ("C", "Contrato"),
        ("P", "Petição"),
        ("CONT", "Contestação"),
        ("R", "Recursos"),
        ("O", "Outro"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, choices=TIPO_CHOICES, default="O")
    arquivo = models.FileField(upload_to="documentos/")
    data_upload = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"

    def __str__(self):
        return self.tipo
