"""
URL configuration for Jury AI.

Rotas de páginas (HTML): index, login, cadastro, clientes, documentos, chat,
ver-referencias, analise-jurisprudencia, processar-analise, config-empresas.
APIs REST: api/auth/, api/clientes/, api/config-empresa/, api/documents/,
api/chat/, api/whatsapp/ (webhook Evolution API).
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.chat.views import (
    analise_jurisprudencia_view,
    processar_analise,
    ver_referencias,
)
from apps.core.views import (
    cadastro_view,
    chat_view,
    cliente_detail_view,
    clientes_list_view,
    config_empresas_view,
    documentos_view,
    index,
    login_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("clientes/", clientes_list_view, name="clientes-list"),
    path("clientes/<int:pk>/", cliente_detail_view, name="cliente-detail"),
    path("documentos/", documentos_view, name="documentos"),
    path("chat/", chat_view, name="chat"),
    path("config-empresas/", config_empresas_view, name="config-empresas"),
    path(
        "ver-referencias/<int:pergunta_id>/",
        ver_referencias,
        name="ver_referencias",
    ),
    path(
        "analise-jurisprudencia/<int:documento_id>/",
        analise_jurisprudencia_view,
        name="analise_jurisprudencia",
    ),
    path(
        "processar-analise/<int:documento_id>/",
        processar_analise,
        name="processar_analise",
    ),
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.users.urls")),
    path("api/clientes/", include("apps.clientes.urls")),
    path("api/config-empresa/", include("apps.clientes.urls_config")),
    path("api/documents/", include("apps.documents.urls")),
    path("api/chat/", include("apps.chat.urls")),
    path("api/whatsapp/", include("apps.whatsapp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
