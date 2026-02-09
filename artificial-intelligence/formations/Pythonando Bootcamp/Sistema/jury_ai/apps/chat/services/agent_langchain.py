"""
Agente de analise jurisprudencial usando LangChain (Notion: Funcionalidades com IA).

Usa structured output para gerar analise detalhada de documentos juridicos.
"""

from abc import abstractmethod

from django.conf import settings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class JurisprudenciaOutput(BaseModel):
    """Resultado estruturado da analise jurisprudencial."""

    indice_risco: int = Field(
        ...,
        description="Indice de risco geral do processo ser perdido ou indeferido",
    )
    erros_coerencia: list[str] = Field(
        ...,
        description="Erros de coerencia entre fatos narrados e pedidos",
    )
    riscos_juridicos: list[str] = Field(
        ...,
        description="Riscos juridicos identificados",
    )
    problemas_formatacao: list[str] = Field(
        ...,
        description="Problemas de formatacao identificados",
    )
    red_flags: list[str] = Field(
        ...,
        description="Red flags criticas identificadas",
    )


def _get_llm():
    """LLM configurado com chave e modelo do Django settings."""
    api_key = getattr(settings, "OPENAI_API_KEY", None) or ""
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY nao configurada. Defina em .env (Funcionalidades com IA)."
        )
    model = getattr(settings, "OPENAI_MODEL_CHAT", "gpt-4o-mini")
    return ChatOpenAI(model=model, api_key=api_key)


class BaseAgent:
    """Agente base com LLM."""

    language: str = "pt-br"

    @property
    def llm(self):
        return _get_llm()

    @abstractmethod
    def _prompt(self): ...

    @abstractmethod
    def run(self): ...


class JurisprudenciaAI(BaseAgent):
    """Agente especializado em analise jurisprudencial de documentos."""

    PROMPT = """
        Voce e um especialista em analise juridica de documentos processuais
        com vasta experiencia em peticoes, contratos, recursos e demais pecas
        juridicas. Sua funcao e realizar uma analise completa e detalhada do
        documento fornecido, identificando pontos criticos que possam
        comprometer o sucesso processual.

        INSTRUCOES GERAIS:
        - Analise o documento de forma minuciosa e sistematica
        - Seja objetivo, preciso e fundamentado em sua analise
        - Priorize questoes que possam resultar em indeferimento, nulidade
          ou perda processual
        - Forneca sugestoes praticas e acionaveis para correcao dos problemas

        FORMATO DE SAIDA:
        Voce deve gerar uma analise estruturada com as seguintes secoes:

        1. INDICE DE RISCO GERAL (0-100):
        - Avalie o risco geral do processo ser perdido ou indeferido
        - Escala: 0-30 (Baixo), 31-60 (Medio), 61-80 (Alto), 81-100 (Critico)

        2. ERROS DE COERENCIA & LACUNAS ARGUMENTATIVAS:
        - Identifique inconsistencias entre fatos narrados e pedidos
        - Detecte contradicoes internas no documento
        - Aponte lacunas na fundamentacao juridica

        3. RISCOS JURIDICOS IDENTIFICADOS:
        - Identifique pedidos genericos ou imprecisos
        - Aponte falta de fundamentacao legal adequada
        - Detecte ausencia ou fragilidade de prova pre-constituida

        4. PROBLEMAS DE FORMATACAO E ESTRUTURA:
        - Verifique se a numeracao de paginas esta correta
        - Identifique falta de subtitulos ou secoes obrigatorias
        - Detecte problemas de formatacao

        5. RED FLAGS CRITICAS:
        - Identifique problemas que podem levar a indeferimento imediato
        - Detecte divergencias entre valor da causa e somatorio dos pedidos
        - Aponte falta de pedidos expressos obrigatorios

        CRITERIOS DE AVALIACAO:
        - Red Flags Criticas tem peso maior (cada uma adiciona 15-25 pontos)
        - Riscos Juridicos tem peso medio (cada um adiciona 8-15 pontos)
        - Erros de Coerencia tem peso medio (cada um adiciona 5-10 pontos)
        - Problemas de Formatacao tem peso menor (cada um adiciona 2-5 pontos)
    """

    def _prompt(self):
        return ChatPromptTemplate.from_messages(
            [
                ("system", self.PROMPT),
                (
                    "human",
                    "Analise o seguinte documento juridico e gere a analise "
                    "completa conforme as instrucoes:\n\n{documento}",
                ),
            ]
        )

    def run(self, documento: str) -> JurisprudenciaOutput:
        """Executa a analise jurisprudencial e retorna resultado estruturado."""
        texto = (documento or "").strip()
        if not texto:
            raise ValueError(
                "Documento sem texto para analise. Preencha o campo content ou execute OCR."
            )
        chain = self._prompt() | self.llm.with_structured_output(JurisprudenciaOutput)
        return chain.invoke({"documento": texto})
