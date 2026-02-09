"""
Gera o arquivo JSON de credenciais Google a partir de variaveis de ambiente.

O arquivo e salvo em diretorio local (gitignored) para uso pelo GoogleCalendarTools.
Nunca commitar o arquivo gerado nem as chaves no .env.
"""

import json
from pathlib import Path

from django.conf import settings


def get_credentials_path() -> Path | None:
    """
    Retorna o path do JSON de credenciais Google Calendar.

    Prioridade:
    1. GOOGLE_CREDENTIALS_PATH (arquivo absoluto, ex.: em Downloads)
    2. Arquivo existente em GOOGLE_CALENDAR_CREDENTIALS_DIR
    3. Gera a partir de GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET
    4. Retorna None se nenhum estiver configurado
    """
    explicit = getattr(settings, "GOOGLE_CREDENTIALS_PATH", "") or ""
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.exists():
            return p

    creds_dir = getattr(settings, "GOOGLE_CALENDAR_CREDENTIALS_DIR", None)
    if creds_dir is None:
        creds_dir = settings.BASE_DIR / "credentials"
    creds_dir = Path(creds_dir)
    creds_dir.mkdir(exist_ok=True)
    path = creds_dir / "google_client_secret.json"

    if path.exists():
        return path

    client_id = getattr(settings, "GOOGLE_CLIENT_ID", "")
    client_secret = getattr(settings, "GOOGLE_CLIENT_SECRET", "")

    if client_id and client_secret:
        payload = {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": [
                    "http://localhost",
                    "urn:ietf:wg:oauth:2.0:oob",
                ],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            }
        }
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return path

    return None
