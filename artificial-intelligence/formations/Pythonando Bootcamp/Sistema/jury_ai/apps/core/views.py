"""
Página inicial e páginas do frontend (roteiro Construção da base).
"""

from django.shortcuts import render


def index(request):
    """Página inicial."""
    return render(request, "core/index.html")


def login_view(request):
    """Login - Usuários."""
    return render(request, "core/login.html")


def cadastro_view(request):
    """Cadastro - Usuários."""
    return render(request, "core/cadastro.html")


def clientes_list_view(request):
    """Clientes - Usuários (lista)."""
    return render(request, "core/clientes_list.html")


def cliente_detail_view(request, pk):
    """Cliente - Usuários (detalhe/edição)."""
    return render(request, "core/cliente_detail.html", {"cliente_id": pk})


def documentos_view(request):
    """Documentos - IA (placeholder)."""
    return render(request, "core/documentos.html")


def chat_view(request):
    """Chat - IA (placeholder)."""
    return render(request, "core/chat.html")


def config_empresas_view(request):
    """Config empresas - Usuários (placeholder)."""
    return render(request, "core/config_empresas.html")
