"""
Agente geral e Análise jurisprudência — Funcionalidades com IA (Notion).
"""

from django.conf import settings


def _get_llm():
    """LLM OpenAI para chat e análise (requer OPENAI_API_KEY)."""
    from langchain_openai import ChatOpenAI

    api_key = getattr(settings, "OPENAI_API_KEY", None) or ""
    if not api_key.strip():
        raise ValueError("OPENAI_API_KEY não configurada. Defina em .env.")
    model = getattr(settings, "OPENAI_MODEL_CHAT", "gpt-4o-mini")
    return ChatOpenAI(model=model, api_key=api_key)


def agente_geral_invoke(message: str, history: list[dict] | None = None) -> str:
    """
    Agente geral: responde à mensagem do usuário (chat).
    history: lista de {"role": "user"|"assistant", "content": "..."} para contexto.
    """
    from langchain_core.messages import AIMessage, HumanMessage

    llm = _get_llm()
    messages = []
    if history:
        for h in history[-20:]:  # últimas 20 trocas
            if h.get("role") == "user":
                messages.append(HumanMessage(content=h.get("content", "")))
            elif h.get("role") == "assistant":
                messages.append(AIMessage(content=h.get("content", "")))
    messages.append(HumanMessage(content=message))
    return llm.invoke(messages).content


def analise_jurisprudencia_invoke(texto: str, pergunta: str | None = None) -> str:
    """
    Análise jurisprudência: analisa texto jurídico (acórdão, decisão, lei).
    Se pergunta for None, faz uma análise resumida e destaca pontos relevantes.
    """
    from langchain_core.messages import HumanMessage, SystemMessage

    llm = _get_llm()
    system = """Você é um assistente jurídico especializado em análise de jurisprudência.
Analise o texto fornecido de forma objetiva: identifique tese, fundamentação, dispositivo e,
se pedido, responda à pergunta do usuário com base no texto."""
    user_content = f"Texto para análise:\n\n{texto}"
    if pergunta:
        user_content += f"\n\nPergunta do usuário: {pergunta}"
    else:
        user_content += (
            "\n\nFaça uma análise resumida e destaque os pontos mais relevantes."
        )
    messages = [
        SystemMessage(content=system),
        HumanMessage(content=user_content),
    ]
    return llm.invoke(messages).content
