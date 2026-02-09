from django.db import models


class DadosEmpresa(models.Model):
    """Dados da empresa para configuração."""

    dados = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "dados da empresa"
        verbose_name_plural = "dados das empresas"

    def __str__(self):
        return f"Dados da empresa - {self.data_criacao.strftime('%d/%m/%Y')}"
