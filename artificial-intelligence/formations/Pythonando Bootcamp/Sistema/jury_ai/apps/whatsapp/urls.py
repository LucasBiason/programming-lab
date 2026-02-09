"""
Secretaria no WhatsApp — Evolution API (Funcionalidades com IA).
"""

from django.urls import path

from . import views

urlpatterns = [
    path("webhook/", views.EvolutionWebhookView.as_view(), name="whatsapp-webhook"),
    path("health/", views.health, name="whatsapp-health"),
]
