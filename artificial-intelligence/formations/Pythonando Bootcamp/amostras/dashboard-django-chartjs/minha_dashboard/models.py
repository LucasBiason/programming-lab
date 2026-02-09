import datetime

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Vendas(models.Model):
    nome_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.nome_produto.nome
