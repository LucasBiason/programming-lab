"""
Gera o arquivo JSON de credenciais Google a partir de variáveis de ambiente.
O arquivo é salvo em diretório local (gitignored) para uso pelo GoogleCalendarTools.
Nunca commitar o arquivo gerado nem as chaves no .env.
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv

# .env fica na pasta pai (Bloco 2)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

DIR_CREDENTIALS = Path(__file__).resolve().parent / "credentials"
DIR_CREDENTIALS.mkdir(exist_ok=True)
FILENAME = "google_client_secret.json"


def get_credentials_path() -> Path:
    """
    Retorna o path do JSON de credenciais Google.
    Se GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET estiverem no .env,
    gera o arquivo a partir deles. Caso contrário, espera um arquivo
    em credentials/google_client_secret.json (baixado do Google Cloud).
    """
    client_id = os.getenv("GOOGLE_CLIENT_ID", "").strip()
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET", "").strip()
    path = DIR_CREDENTIALS / FILENAME

    if client_id and client_secret:
        payload = {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": ["http://localhost", "urn:ietf:wg:oauth:2.0:oob"],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "",
            }
        }
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    elif not path.exists():
        raise FileNotFoundError(
            "Configure GOOGLE_CLIENT_ID e GOOGLE_CLIENT_SECRET no .env ou coloque "
            f"o arquivo de credenciais em: {path}"
        )
    return path
