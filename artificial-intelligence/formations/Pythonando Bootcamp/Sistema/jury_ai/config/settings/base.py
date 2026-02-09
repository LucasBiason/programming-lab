"""
Configurações comuns do Jury AI.
"""

from pathlib import Path

import environ
from django.contrib.messages import constants

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env.read_env(BASE_DIR.parent / ".env")

SECRET_KEY = env("SECRET_KEY", default="change-me-in-production")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "django_q",
    "apps.users",
    "apps.clientes",
    "apps.documents",
    "apps.chat",
    "apps.whatsapp",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=DEBUG)

LOGIN_URL = "/usuarios/login/"

# Funcionalidades com IA (Notion: Funcionalidades com IA)
OPENAI_API_KEY = env("OPENAI_API_KEY", default="")
OPENAI_MODEL_CHAT = env("OPENAI_MODEL_CHAT", default="gpt-4o-mini")
OPENAI_MODEL_VISION = env("OPENAI_MODEL_VISION", default="gpt-4o")

MESSAGE_TAGS = {
    constants.SUCCESS: "bg-green-50 text-green-700",
    constants.ERROR: "bg-red-50 text-red-700",
}

# Google Calendar (SecretariaAI / WhatsApp - Bloco 4)
# Caminho direto ao JSON (ex.: Downloads) ou deixe vazio para usar GOOGLE_CLIENT_ID/SECRET
GOOGLE_CREDENTIALS_PATH = env("GOOGLE_CREDENTIALS_PATH", default="")
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID", default="")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET", default="")
GOOGLE_CALENDAR_CREDENTIALS_DIR = BASE_DIR / "credentials"
GOOGLE_CALENDAR_TOKEN_PATH = env(
    "GOOGLE_CALENDAR_TOKEN_PATH", default=str(BASE_DIR / "token.json")
)

# Evolution API (WhatsApp - Bloco 4)
EVOLUTION_API_URL = env(
    "EVOLUTION_API_URL",
    default="https://evolution-api-production-ca5f.up.railway.app",
)
EVOLUTION_API_KEY = env("EVOLUTION_API_KEY", default="")
EVOLUTION_INSTANCE = env("EVOLUTION_INSTANCE", default="default")

Q_CLUSTER = {
    "name": "jury_ai",
    "workers": 1,
    "retry": 200,
    "timeout": 180,
    "queue_limit": 50,
    "orm": "default",
}
