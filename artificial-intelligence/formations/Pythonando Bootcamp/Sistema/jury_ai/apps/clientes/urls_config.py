from django.urls import path

from .views import DadosEmpresaView

urlpatterns = [
    path("", DadosEmpresaView.as_view(), name="dados-empresa"),
]
