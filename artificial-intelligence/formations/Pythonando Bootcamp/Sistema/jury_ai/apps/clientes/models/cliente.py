from django.conf import settings
from django.db import models


class Cliente(models.Model):
    """Cliente do escritório (Clientes - Usuários, Cliente - Usuários)."""

    TIPO_CHOICES = [
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="clientes",
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=32, blank=True)
    cpf_cnpj = models.CharField("CPF/CNPJ", max_length=18, blank=True)
    observacoes = models.TextField(blank=True)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default="PF")
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
