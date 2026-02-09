"""
Clientes - Usuários / Cliente - Usuários (Construção da base).
"""

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cliente, DadosEmpresa, Documentos
from .serializers import ClienteSerializer, DadosEmpresaSerializer, DocumentoSerializer


class ClienteListCreateView(generics.ListCreateAPIView):
    """Lista e cria clientes do usuário logado."""

    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detalhe, atualização e exclusão de um cliente."""

    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(user=self.request.user)


class DocumentoListCreateView(generics.ListCreateAPIView):
    """Lista e cria documentos de um cliente."""

    serializer_class = DocumentoSerializer

    def get_queryset(self):
        return Documentos.objects.filter(
            cliente__user=self.request.user,
            cliente_id=self.kwargs["cliente_pk"],
        )

    def perform_create(self, serializer):
        cliente = get_object_or_404(
            Cliente,
            pk=self.kwargs["cliente_pk"],
            user=self.request.user,
        )
        serializer.save(cliente=cliente)


class DadosEmpresaView(APIView):
    """GET: retorna dados da empresa. POST: cria ou atualiza."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj = DadosEmpresa.objects.first()
        if obj:
            return Response(DadosEmpresaSerializer(obj).data)
        return Response({"dados": ""})

    def post(self, request):
        obj = DadosEmpresa.objects.first()
        if obj:
            serializer = DadosEmpresaSerializer(obj, data=request.data, partial=True)
        else:
            serializer = DadosEmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
