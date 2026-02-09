"""
Testes para apps.chat.views (ChatView, validações).
"""

import pytest
from rest_framework import status

from apps.chat.models import Pergunta
from apps.clientes.models import Cliente


@pytest.mark.django_db
class TestChatView:
    """Testes do endpoint de criação de pergunta (chat)."""

    def test_post_without_pergunta_returns_400(self, authenticated_client, user):
        cliente = Cliente.objects.create(
            user=user, nome="Cliente Teste", email="c@test.com"
        )
        response = authenticated_client.post(
            "/api/chat/",
            {"cliente_id": cliente.id},
            format="json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "pergunta" in (response.json().get("detail") or "").lower()

    def test_post_without_cliente_id_returns_400(self, authenticated_client):
        response = authenticated_client.post(
            "/api/chat/",
            {"pergunta": "Qual o prazo?"},
            format="json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "cliente_id" in (response.json().get("detail") or "").lower()

    def test_post_cliente_not_found_returns_404(self, authenticated_client):
        response = authenticated_client.post(
            "/api/chat/",
            {"pergunta": "Qual o prazo?", "cliente_id": 99999},
            format="json",
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_post_valid_creates_pergunta_and_returns_id(
        self, authenticated_client, user
    ):
        cliente = Cliente.objects.create(
            user=user, nome="Cliente Teste", email="c@test.com"
        )
        response = authenticated_client.post(
            "/api/chat/",
            {"pergunta": "Qual o prazo?", "cliente_id": cliente.id},
            format="json",
        )
        assert response.status_code == status.HTTP_200_OK
        assert "id" in response.json()
        assert Pergunta.objects.filter(
            pergunta="Qual o prazo?", cliente=cliente
        ).exists()
