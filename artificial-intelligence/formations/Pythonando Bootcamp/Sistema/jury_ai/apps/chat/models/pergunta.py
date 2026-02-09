from django.db import models

from apps.clientes.models import Cliente


class Pergunta(models.Model):
    """Pergunta feita pelo usuario no chat."""

    pergunta = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.pergunta
