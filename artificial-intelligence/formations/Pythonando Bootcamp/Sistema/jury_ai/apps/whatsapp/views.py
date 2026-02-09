"""
Secretaria no WhatsApp -- webhook para Evolution API (Bloco 4).

Recebe mensagens da Evolution API, processa com SecretariaAI (RAG + Google Calendar)
e envia a resposta de volta pelo WhatsApp via Evolution API.
"""

import json
import logging

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .wrapper_evolutionapi import send_whatsapp_reply

logger = logging.getLogger(__name__)


def _extract_phone_and_message(data):
    """
    Extrai telefone e texto do payload da Evolution API.

    Estrutura esperada: data.data.key.remoteJid e data.data.message (conversation
    ou extendedTextMessage.text).
    """
    data_inner = data.get("data") or data
    key = data_inner.get("key", {})
    remote_jid = key.get("remoteJid", "")
    phone = remote_jid.split("@")[0] if remote_jid else ""

    msg_data = data_inner.get("message", {})
    message = msg_data.get("conversation") or ""
    if not message:
        extended = msg_data.get("extendedTextMessage", {})
        message = extended.get("text", "")

    return phone.strip(), (message or "").strip()


@method_decorator(csrf_exempt, name="dispatch")
class EvolutionWebhookView(View):
    """
    Webhook para Evolution API (WhatsApp).
    GET: verificação de URL (Evolution API valida o endpoint).
    POST: recebe mensagem, processa com SecretariaAI e envia resposta no WhatsApp.
    """

    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "ok", "webhook": "jury_ai"})

    def post(self, request, *args, **kwargs):
        try:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                logger.warning("Webhook: body JSON invalido.")
                return JsonResponse({"received": True}, status=200)

            phone, message = _extract_phone_and_message(data)

            if not phone or not message:
                logger.info("Webhook: sem phone ou message, ignorando.")
                return JsonResponse({"received": True}, status=200)

            logger.info("WhatsApp de %s: %s", phone, message[:100])

            response_text = None
            try:
                from .agent import SecretariaAI

                agent = SecretariaAI.build_agent(session_id=phone)
                response = agent.run(message)
                response_text = response.content
                logger.info("Resposta SecretariaAI: %s", (response_text or "")[:100])
            except Exception:
                logger.exception("Erro ao processar mensagem com SecretariaAI")
                response_text = (
                    "Desculpe, tive um problema ao processar sua mensagem. "
                    "Tente novamente em instantes."
                )

            if response_text:
                send_whatsapp_reply(phone, response_text)

            return JsonResponse(
                {"received": True, "response": response_text}, status=200
            )

        except Exception:
            logger.exception("Erro no webhook WhatsApp")
            return JsonResponse({"received": True}, status=200)


def health(_request):
    """Health check para a Evolution API validar o endpoint."""
    return JsonResponse({"status": "ok", "service": "jury_ai_whatsapp"})
