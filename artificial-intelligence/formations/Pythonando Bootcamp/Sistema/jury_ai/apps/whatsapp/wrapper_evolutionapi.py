"""
Wrapper para a Evolution API (WhatsApp - Bloco 4).

Usa EVOLUTION_API_URL, EVOLUTION_API_KEY e EVOLUTION_INSTANCE do Django settings.
Nunca commitar a API key; usar .env.
"""

import logging
from urllib.parse import urlencode, urljoin

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class BaseEvolutionAPI:
    """Classe base para comunicação com a Evolution API."""

    def __init__(self, base_url=None, api_key=None, instance=None):
        self._BASE_URL = (
            base_url or getattr(settings, "EVOLUTION_API_URL", "")
        ).rstrip("/")
        self._API_KEY = api_key or getattr(settings, "EVOLUTION_API_KEY", "")
        self._INSTANCE = instance or getattr(settings, "EVOLUTION_INSTANCE", "default")

    def _send_request(
        self, path, method="GET", body=None, headers=None, params_url=None
    ):
        if not self._BASE_URL or not self._API_KEY:
            logger.warning(
                "Evolution API: EVOLUTION_API_URL ou EVOLUTION_API_KEY nao configurados."
            )
            return None

        method = method.upper()
        url = self._mount_url(path, params_url or {})

        if not isinstance(headers, dict):
            headers = {}
        headers.setdefault("Content-Type", "application/json")
        headers["apikey"] = self._API_KEY

        request_func = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete,
        }.get(method, requests.get)

        try:
            return request_func(url, headers=headers, json=body, timeout=30)
        except requests.RequestException as e:
            logger.exception("Evolution API request failed: %s", e)
            return None

    def _mount_url(self, path, params_url):
        path = path.lstrip("/")
        url = urljoin(self._BASE_URL + "/", path)
        if isinstance(params_url, dict) and params_url:
            url = url + "?" + urlencode(params_url)
        return url


class SendMessage(BaseEvolutionAPI):
    """Envia mensagens de texto via Evolution API."""

    def send_text(self, number, text):
        """
        Envia mensagem de texto para um número WhatsApp.

        number: número com DDI, sem símbolos (ex.: 5511999999999)
        text: conteúdo da mensagem
        """
        path = f"message/sendText/{self._INSTANCE}"
        body = {"number": number, "text": text}
        return self._send_request(path, method="POST", body=body)


def send_whatsapp_reply(phone: str, text: str) -> bool:
    """
    Envia a resposta do agente de volta para o usuário no WhatsApp.

    Retorna True se enviou com sucesso (ou se API não está configurada e ignorou),
    False se tentou enviar e a API retornou erro.
    """
    if not text or not phone:
        return True
    if not getattr(settings, "EVOLUTION_API_KEY", ""):
        return True
    sender = SendMessage()
    resp = sender.send_text(phone, text)
    if resp is None:
        return False
    if resp.status_code in (200, 201):
        return True
    logger.warning("Evolution API sendText status %s: %s", resp.status_code, resp.text)
    return False
