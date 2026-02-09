"""
Testes para extração de phone/message e wrapper Evolution API.
"""

import pytest

from apps.whatsapp.views import _extract_phone_and_message


class TestExtractPhoneAndMessage:
    """Testes da função _extract_phone_and_message."""

    def test_extract_from_extended_text_message(self):
        data = {
            "data": {
                "key": {"remoteJid": "5511999999999@s.whatsapp.net"},
                "message": {"extendedTextMessage": {"text": "Olá"}},
            }
        }
        phone, message = _extract_phone_and_message(data)
        assert phone == "5511999999999"
        assert message == "Olá"

    def test_extract_from_conversation(self):
        data = {
            "data": {
                "key": {"remoteJid": "5521988888888@s.whatsapp.net"},
                "message": {"conversation": "Oi"},
            }
        }
        phone, message = _extract_phone_and_message(data)
        assert phone == "5521988888888"
        assert message == "Oi"

    def test_extract_data_at_root(self):
        data = {
            "key": {"remoteJid": "5533000000000@s.whatsapp.net"},
            "message": {"extendedTextMessage": {"text": "Teste"}},
        }
        phone, message = _extract_phone_and_message(data)
        assert phone == "5533000000000"
        assert message == "Teste"

    def test_extract_empty_returns_empty_strings(self):
        phone, message = _extract_phone_and_message({})
        assert phone == ""
        assert message == ""


@pytest.mark.django_db
class TestSendWhatsappReply:
    """Testes da função send_whatsapp_reply (com mocks)."""

    def test_send_whatsapp_reply_empty_phone_or_text_returns_true(self):
        from apps.whatsapp.wrapper_evolutionapi import send_whatsapp_reply

        assert send_whatsapp_reply("", "text") is True
        assert send_whatsapp_reply("5511", "") is True
