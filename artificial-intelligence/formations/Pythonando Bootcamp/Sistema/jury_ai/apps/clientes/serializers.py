from rest_framework import serializers

from .models import Cliente, DadosEmpresa, Documentos


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "id",
            "nome",
            "email",
            "telefone",
            "cpf_cnpj",
            "observacoes",
            "tipo",
            "status",
            "criado_em",
            "atualizado_em",
        ]
        read_only_fields = ["id", "criado_em", "atualizado_em"]


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = ["id", "tipo", "arquivo", "data_upload", "content"]
        read_only_fields = ["id", "content"]


class DadosEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosEmpresa
        fields = ["id", "dados", "data_criacao", "data_atualizacao"]
        read_only_fields = ["id", "data_criacao", "data_atualizacao"]
