from django.urls import path

from . import views

urlpatterns = [
    path("", views.ClienteListCreateView.as_view(), name="cliente-list-create"),
    path("<int:pk>/", views.ClienteDetailView.as_view(), name="cliente-detail"),
    path(
        "<int:cliente_pk>/documentos/",
        views.DocumentoListCreateView.as_view(),
        name="cliente-documentos",
    ),
]
