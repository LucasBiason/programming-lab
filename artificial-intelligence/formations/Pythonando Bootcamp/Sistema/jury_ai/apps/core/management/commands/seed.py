"""
Comando para popular o banco com dados de teste (usuário e clientes).

Uso:
  python manage.py seed
  python manage.py seed --no-input   # não pergunta antes de criar

Usuário padrão: teste@jury.ai / senha1234
"""

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.clientes.models import Cliente
from apps.users.models import User

USUARIO_EMAIL = "teste@jury.ai"
USUARIO_PASSWORD = "senha1234"
USUARIO_USERNAME = "teste"
USUARIO_FIRST = "Teste"
USUARIO_LAST = "User"

CLIENTES = [
    {
        "nome": "Maria Silva",
        "email": "maria@email.com",
        "telefone": "11999990000",
        "cpf_cnpj": "123.456.789-00",
        "observacoes": "Cliente desde 2024.",
    },
    {
        "nome": "João Santos",
        "email": "joao.santos@empresa.com",
        "telefone": "11988881111",
        "cpf_cnpj": "987.654.321-00",
        "observacoes": "Contrato vigente até dez/2026.",
    },
    {
        "nome": "Empresa XYZ Ltda",
        "email": "contato@xyz.com.br",
        "telefone": "1133334444",
        "cpf_cnpj": "12.345.678/0001-90",
        "observacoes": "Pessoa jurídica - área cível.",
    },
]


class Command(BaseCommand):
    help = "Cria usuário e clientes de teste para desenvolvimento e Postman."

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-input",
            action="store_true",
            help="Não pedir confirmação antes de criar.",
        )

    def handle(self, *args, **options):
        with transaction.atomic():
            user, created = User.objects.get_or_create(
                email=USUARIO_EMAIL,
                defaults={
                    "username": USUARIO_USERNAME,
                    "first_name": USUARIO_FIRST,
                    "last_name": USUARIO_LAST,
                    "is_active": True,
                },
            )
            if created:
                user.set_password(USUARIO_PASSWORD)
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Usuário criado: {USUARIO_EMAIL} (senha: {USUARIO_PASSWORD})"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Usuário já existe: {USUARIO_EMAIL}")
                )

            for data in CLIENTES:
                _, c_created = Cliente.objects.get_or_create(
                    user=user,
                    nome=data["nome"],
                    defaults={
                        "email": data["email"],
                        "telefone": data["telefone"],
                        "cpf_cnpj": data["cpf_cnpj"],
                        "observacoes": data["observacoes"],
                    },
                )
                if c_created:
                    self.stdout.write(
                        self.style.SUCCESS(f"  Cliente criado: {data['nome']}")
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed concluído. Use no Postman: email={USUARIO_EMAIL}, password={USUARIO_PASSWORD}"
            )
        )
