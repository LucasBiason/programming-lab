"""
Signals para o app clientes.

Ao criar um Documentos, enfileira OCR + RAG via django-q2 Chain.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Documentos


@receiver(post_save, sender=Documentos)
def post_save_documentos(sender, instance, created, **kwargs):
    """Enfileira OCR e RAG quando um documento e criado."""
    if created:
        from django_q.tasks import Chain

        chain = Chain()
        chain.append("apps.documents.tasks.ocr_and_markdown_file", instance.id)
        chain.append("apps.documents.tasks.rag_documentos", instance.id)
        chain.run()
