from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "user", "criado_em"]
    list_filter = ["user"]
    search_fields = ["nome", "email", "cpf_cnpj"]
    raw_id_fields = ["user"]
