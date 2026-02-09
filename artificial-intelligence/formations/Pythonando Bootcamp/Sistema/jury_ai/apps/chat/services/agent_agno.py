"""
Agente JuriAI usando agno framework (Notion: Funcionalidades com IA).

Agente geral com RAG (documentos do cliente) e tool DataJud (CNJ).
"""

import json

import requests
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.tools import tool
from agno.vectordb.lancedb import LanceDb
from django.conf import settings

from .literals import TribunalLiteral

DATAJUD_BASE_URL = "https://api-publica.datajud.cnj.jus.br"
DATAJUD_API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="


@tool
def search_datajud_api(tribunal: TribunalLiteral, process_number: str) -> str:
    """Busca informacoes de um processo judicial na API publica do DataJud (CNJ).

    Args:
        tribunal: Codigo do tribunal onde o processo esta tramitando.
        process_number: Numero do processo judicial no formato CNJ.

    Returns:
        Resposta da API em formato JSON como string.
    """
    url = f"{DATAJUD_BASE_URL}/api_publica_{tribunal}/_search"
    payload = {"query": {"match": {"numeroProcesso": process_number}}}
    headers = {
        "Authorization": f"APIKey {DATAJUD_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return json.dumps({"error": str(e)})


class JuriAI:
    """Agente juridico virtual com RAG e consulta ao DataJud."""

    VECTOR_DB_TABLE = "documentos"
    VECTOR_DB_URI = str(settings.BASE_DIR / "lancedb")
    MEMORY_DB_FILE = str(settings.BASE_DIR / "db.sqlite3")
    MEMORY_TABLE = "my_memory_table"
    AGENT_NAME = "Assistente Juridico Virtual"
    AGENT_DESCRIPTION = (
        "Assistente virtual especializado em questoes juridicas com acesso "
        "a base de conhecimento e consulta de processos judiciais."
    )

    INSTRUCTIONS = """
    SUAS CAPACIDADES:
    1. Acesso a Base de Conhecimento (RAG): Voce possui acesso a uma base de dados
       e deve usa-la para responder as perguntas do usuario de forma precisa e fundamentada.
    2. Consulta de Processos: Voce pode buscar informacoes sobre processos judiciais
       atraves da API do DataJud (CNJ).

    DIRETRIZES:
    - Sempre priorize informacoes da base de conhecimento quando disponiveis.
    - Ao consultar processos, forneca informacoes claras e organizadas.
    - Se nao tiver certeza sobre alguma informacao, indique isso ao usuario.
    - Mantenha um tom profissional e objetivo em todas as respostas.
    """

    knowledge = Knowledge(
        vector_db=LanceDb(
            table_name=VECTOR_DB_TABLE,
            uri=VECTOR_DB_URI,
            embedder=OpenAIEmbedder(),
        ),
    )

    @classmethod
    def build_agent(cls, knowledge_filters: dict | None = None) -> Agent:
        """Constroi o agente com filtros de conhecimento opcionais."""
        if knowledge_filters is None:
            knowledge_filters = {}

        db = SqliteDb(db_file=cls.MEMORY_DB_FILE, memory_table=cls.MEMORY_TABLE)

        return Agent(
            name=cls.AGENT_NAME,
            description=cls.AGENT_DESCRIPTION,
            tools=[search_datajud_api],
            instructions=cls.INSTRUCTIONS,
            db=db,
            update_memory_on_run=True,
            knowledge=cls.knowledge,
            knowledge_filters=knowledge_filters,
            search_knowledge=True,
        )
