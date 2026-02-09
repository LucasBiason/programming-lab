from django.db import models

from apps.clientes.models import Documentos


class AnaliseJurisprudencia(models.Model):
    """Analise jurisprudencial de um documento."""

    documento = models.ForeignKey(
        Documentos, on_delete=models.CASCADE, related_name="analises"
    )
    indice_risco = models.IntegerField()
    classificacao = models.CharField(max_length=20)
    erros_coerencia = models.JSONField(default=list)
    riscos_juridicos = models.JSONField(default=list)
    problemas_formatacao = models.JSONField(default=list)
    red_flags = models.JSONField(default=list)
    tempo_processamento = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data_criacao"]

    def __str__(self):
        return (
            f"Analise - {self.documento.get_tipo_display()} "
            f"- {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        )
