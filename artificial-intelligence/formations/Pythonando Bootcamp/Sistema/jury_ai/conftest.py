"""
Fixtures compartilhadas para testes do Jury AI.
"""

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    """Cliente REST para testes de API."""
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def user(db):
    """Usuário de teste."""
    return User.objects.create_user(
        username="testuser",
        email="teste@jury.ai",
        password="senha1234",
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Cliente API autenticado com JWT."""
    from rest_framework_simplejwt.tokens import RefreshToken

    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client


@pytest.fixture
def evolution_webhook_payload():
    """Payload mínimo de mensagem da Evolution API (messages.upsert)."""
    return {
        "event": "messages.upsert",
        "instance": "default",
        "data": {
            "key": {
                "remoteJid": "5511999999999@s.whatsapp.net",
                "fromMe": False,
                "id": "test-msg-id",
            },
            "pushName": "TestUser",
            "message": {
                "extendedTextMessage": {"text": "Olá, quero agendar uma reunião."},
            },
        },
    }
