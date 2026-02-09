from django.db import models

from .pergunta import Pergunta


class ContextRag(models.Model):
    """Contexto RAG usado na resposta de uma pergunta."""

    content = models.JSONField()
    tool_name = models.CharField(max_length=255)
    tool_args = models.JSONField(null=True, blank=True)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.tool_name
