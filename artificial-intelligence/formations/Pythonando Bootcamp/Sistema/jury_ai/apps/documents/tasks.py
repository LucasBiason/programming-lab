"""
Tasks de processamento de documentos (django-q2).

Executadas em background apos o upload de um documento:
1. ocr_and_markdown_file: extrai texto do documento via Docling
2. rag_documentos: indexa o texto no vetor DB (LanceDB) para RAG
3. rag_dados_empresa: indexa dados da empresa no vetor DB
"""

from django.shortcuts import get_object_or_404


def ocr_and_markdown_file(instance_id):
    """Extrai texto do documento via OCR/Docling e salva no campo content."""
    from docling.document_converter import DocumentConverter

    from apps.clientes.models import Documentos

    documentos = get_object_or_404(Documentos, id=instance_id)

    converter = DocumentConverter()
    result = converter.convert(documentos.arquivo.path)
    doc = result.document
    texto = doc.export_to_markdown()

    documentos.content = texto
    documentos.save()


def rag_documentos(instance_id):
    """Indexa o conteudo do documento no vetor DB para RAG."""
    from apps.chat.services.agent_agno import JuriAI
    from apps.clientes.models import Documentos

    documentos = get_object_or_404(Documentos, id=instance_id)
    JuriAI.knowledge.insert(
        name=documentos.arquivo.name,
        text_content=documentos.content,
        metadata={
            "cliente_id": documentos.cliente.id,
            "name": documentos.arquivo.name,
        },
    )


def rag_dados_empresa(instance_id):
    """Indexa os dados da empresa no vetor DB para RAG (SecretariaAI)."""
    from apps.clientes.models import DadosEmpresa

    dados = get_object_or_404(DadosEmpresa, id=instance_id)

    from agno.knowledge.embedder.openai import OpenAIEmbedder
    from agno.knowledge.knowledge import Knowledge
    from agno.vectordb.lancedb import LanceDb
    from django.conf import settings

    knowledge = Knowledge(
        vector_db=LanceDb(
            table_name="empresa",
            uri=str(settings.BASE_DIR / "lancedb"),
            embedder=OpenAIEmbedder(),
        ),
    )
    knowledge.insert(
        name="dados_empresa",
        text_content=dados.dados,
        metadata={"type": "dados_empresa"},
    )
