"""
Testes para páginas principais (core views).
"""

from django.test import Client
from django.urls import reverse


def test_index_returns_200():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200


def test_login_page_returns_200():
    client = Client()
    response = client.get(reverse("login"))
    assert response.status_code == 200


def test_cadastro_page_returns_200():
    client = Client()
    response = client.get("/cadastro/")
    assert response.status_code == 200


def test_health_whatsapp_returns_200():
    client = Client()
    response = client.get(reverse("whatsapp-health"))
    assert response.status_code == 200
