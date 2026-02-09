"""
Testes para apps.whatsapp.views (webhook Evolution API).
"""

import json
from unittest.mock import patch

import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestEvolutionWebhookView:
    """Testes do webhook WhatsApp (Evolution API)."""

    def test_webhook_get_returns_ok(self):
        # Arrange
        client = Client()
        url = reverse("whatsapp-webhook")

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data.get("status") == "ok"
        assert data.get("webhook") == "jury_ai"

    def test_webhook_post_invalid_json_returns_200(self):
        client = Client()
        url = reverse("whatsapp-webhook")
        response = client.post(
            url,
            data="not json",
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json().get("received") is True

    def test_webhook_post_empty_data_returns_200(self):
        client = Client()
        url = reverse("whatsapp-webhook")
        response = client.post(
            url,
            data=json.dumps({}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json().get("received") is True

    def test_webhook_post_missing_phone_or_message_returns_200(self):
        client = Client()
        url = reverse("whatsapp-webhook")
        payload = {"data": {"key": {"remoteJid": ""}, "message": {}}}
        response = client.post(
            url,
            data=json.dumps(payload),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json().get("received") is True

    @patch("apps.whatsapp.views.SecretariaAI")
    @patch("apps.whatsapp.views.send_whatsapp_reply")
    def test_webhook_post_valid_payload_returns_200_and_response(
        self, mock_send, mock_secretaria_class, evolution_webhook_payload
    ):
        # Arrange
        mock_agent = mock_secretaria_class.build_agent.return_value
        mock_agent.run.return_value.content = "Resposta do agente"
        mock_send.return_value = True
        client = Client()
        url = reverse("whatsapp-webhook")

        # Act
        response = client.post(
            url,
            data=json.dumps(evolution_webhook_payload),
            content_type="application/json",
        )

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["received"] is True
        assert data["response"] == "Resposta do agente"
        mock_secretaria_class.build_agent.assert_called_once_with(
            session_id="5511999999999"
        )
        mock_agent.run.assert_called_once_with("Olá, quero agendar uma reunião.")
        mock_send.assert_called_once_with("5511999999999", "Resposta do agente")

    @patch("apps.whatsapp.views.SecretariaAI")
    @patch("apps.whatsapp.views.send_whatsapp_reply")
    def test_webhook_post_agent_exception_returns_200_and_fallback_message(
        self, mock_send, mock_secretaria_class, evolution_webhook_payload
    ):
        mock_secretaria_class.build_agent.return_value.run.side_effect = Exception(
            "erro"
        )
        client = Client()
        url = reverse("whatsapp-webhook")
        response = client.post(
            url,
            data=json.dumps(evolution_webhook_payload),
            content_type="application/json",
        )
        assert response.status_code == 200
        data = response.json()
        assert "Desculpe" in (data.get("response") or "")


def test_health_returns_ok():
    client = Client()
    url = reverse("whatsapp-health")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json().get("status") == "ok"
    assert response.json().get("service") == "jury_ai_whatsapp"
