from datetime import datetime

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render

from .models import Produto, Vendas, Vendedor


def home(request):
    return render(request, "home.html")


def retorna_total_vendido(request):
    total = Vendas.objects.aggregate(Sum("total"))["total__sum"] or 0
    if request.method == "GET":
        return JsonResponse({"total": total})


def relatorio_faturamento(request):
    vendas = Vendas.objects.all()
    meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for _ in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        total_mes = sum(v.total for v in vendas if v.data.month == mes and v.data.year == ano)
        labels.append(meses[mes - 1])
        data.append(total_mes)
    return JsonResponse({"data": data[::-1], "labels": labels[::-1]})


def relatorio_produtos(request):
    produtos = Produto.objects.all()
    label = []
    data = []
    for produto in produtos:
        vendas = Vendas.objects.filter(nome_produto=produto).aggregate(Sum("total"))
        total = vendas["total__sum"] or 0
        label.append(produto.nome)
        data.append(total)
    x = list(zip(label, data))
    x.sort(key=lambda t: t[1], reverse=True)
    x = list(zip(*x))
    return JsonResponse({"labels": list(x[0][:3]), "data": list(x[1][:3])})


def relatorio_funcionario(request):
    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum("total"))
        total = vendas["total__sum"] or 0
        label.append(vendedor.nome)
        data.append(total)
    x = list(zip(label, data))
    x.sort(key=lambda t: t[1], reverse=True)
    x = list(zip(*x))
    return JsonResponse({"labels": list(x[0][:3]), "data": list(x[1][:3])})
