"""
Chat - IA: agente geral, streaming, analise, referencias.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.ChatView.as_view(), name="chat-api"),
    path("stream/", views.ChatStreamView.as_view(), name="chat-stream"),
    path(
        "analise-jurisprudencia/",
        views.AnaliseJurisprudenciaView.as_view(),
        name="chat-analise-jurisprudencia",
    ),
]
