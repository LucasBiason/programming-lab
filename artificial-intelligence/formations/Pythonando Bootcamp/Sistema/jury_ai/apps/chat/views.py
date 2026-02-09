"""
Chat -- IA: agente geral, streaming, ver referencias (Funcionalidades com IA).
"""

from collections.abc import Iterator

from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clientes.models import Cliente

from .models import AnaliseJurisprudencia, ContextRag, Pergunta
from .services.agent import analise_jurisprudencia_invoke


class ChatView(APIView):
    """
    POST: cria uma Pergunta no banco e retorna o id.
    Body: { "pergunta": "...", "cliente_id": N }
    O streaming da resposta e feito via ChatStreamView.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        message = (request.data.get("pergunta") or "").strip()
        if not message:
            return Response(
                {"detail": "Campo 'pergunta' e obrigatorio."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        cliente_id = request.data.get("cliente_id")
        if not cliente_id:
            return Response(
                {"detail": "Campo 'cliente_id' e obrigatorio."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            cliente = Cliente.objects.get(pk=cliente_id, user=request.user)
        except Cliente.DoesNotExist:
            return Response(
                {"detail": "Cliente nao encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )

        pergunta_obj = Pergunta.objects.create(pergunta=message, cliente=cliente)
        return Response({"id": pergunta_obj.id})


class ChatStreamView(APIView):
    """
    POST: streaming de resposta do agente (agno).
    Body: { "id_pergunta": N }
    """

    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> StreamingHttpResponse:
        id_pergunta = request.data.get("id_pergunta")
        pergunta = get_object_or_404(Pergunta, id=id_pergunta)

        def gerar_resposta():
            try:
                from agno.agent import RunEvent, RunOutputEvent

                from .services.agent_agno import JuriAI

                agent = JuriAI.build_agent(
                    knowledge_filters={"cliente_id": pergunta.cliente.id}
                )

                stream: Iterator[RunOutputEvent] = agent.run(
                    pergunta.pergunta, stream=True, stream_events=True
                )
                for chunk in stream:
                    if chunk.event == RunEvent.run_content:
                        yield str(chunk.content)
                    elif chunk.event == RunEvent.tool_call_completed:
                        context = ContextRag(
                            content=chunk.tool.result,
                            tool_name=chunk.tool.tool_name,
                            tool_args=chunk.tool.tool_args,
                            pergunta=pergunta,
                        )
                        context.save()
            except Exception as e:
                yield f"\n[Erro: {e!s}]"

        response = StreamingHttpResponse(
            gerar_resposta(),
            content_type="text/plain; charset=utf-8",
        )
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"
        return response


class AnaliseJurisprudenciaView(APIView):
    """
    POST: analisa texto juridico (jurisprudencia).
    Body: { "texto": "...", "pergunta": "..." } (pergunta opcional)
    """

    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        texto = (request.data.get("texto") or "").strip()
        if not texto:
            return Response(
                {"detail": "Campo 'texto' e obrigatorio."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        pergunta = (request.data.get("pergunta") or "").strip() or None
        try:
            analise = analise_jurisprudencia_invoke(texto, pergunta=pergunta)
        except ValueError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except Exception as e:
            return Response(
                {"detail": f"Erro na analise: {e!s}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response({"analise": analise})


@csrf_exempt
def ver_referencias(request, pergunta_id):
    """Exibe os contextos RAG usados para responder uma pergunta."""
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    contextos = ContextRag.objects.filter(pergunta=pergunta)
    return render(
        request,
        "core/ver_referencias.html",
        {"pergunta": pergunta, "contextos": contextos},
    )


@csrf_exempt
def analise_jurisprudencia_view(request, documento_id):
    """Exibe a analise jurisprudencial de um documento."""
    from apps.clientes.models import Documentos

    documento = get_object_or_404(Documentos, id=documento_id)
    analise = AnaliseJurisprudencia.objects.filter(documento=documento).first()
    return render(
        request,
        "core/analise_jurisprudencia.html",
        {"documento": documento, "analise": analise},
    )


@csrf_exempt
def processar_analise(request, documento_id):
    """Processa a analise jurisprudencial de um documento via IA."""
    import time

    from django.contrib import messages
    from django.contrib.messages import constants
    from django.shortcuts import redirect

    from apps.clientes.models import Documentos

    if request.method != "POST":
        messages.add_message(request, constants.ERROR, "Metodo nao permitido.")
        return redirect("analise_jurisprudencia", documento_id=documento_id)

    try:
        documento = get_object_or_404(Documentos, id=documento_id)
        if not (documento.content or "").strip():
            messages.add_message(
                request,
                constants.ERROR,
                "Documento sem texto. Execute o OCR no documento ou preencha o conteudo antes de analisar.",
            )
            return redirect("analise_jurisprudencia", documento_id=documento_id)

        start_time = time.time()

        from .services.agent_langchain import JurisprudenciaAI

        agent = JurisprudenciaAI()
        response = agent.run(documento.content)

        processing_time = int(time.time() - start_time)

        indice = response.indice_risco
        if indice <= 30:
            classificacao = "Baixo"
        elif indice <= 60:
            classificacao = "Médio"
        elif indice <= 80:
            classificacao = "Alto"
        else:
            classificacao = "Crítico"

        AnaliseJurisprudencia.objects.update_or_create(
            documento=documento,
            defaults={
                "indice_risco": indice,
                "classificacao": classificacao,
                "erros_coerencia": response.erros_coerencia,
                "riscos_juridicos": response.riscos_juridicos,
                "problemas_formatacao": response.problemas_formatacao,
                "red_flags": response.red_flags,
                "tempo_processamento": processing_time,
            },
        )

        messages.add_message(
            request, constants.SUCCESS, "Analise realizada com sucesso!"
        )
    except Exception as e:
        messages.add_message(
            request, constants.ERROR, f"Erro ao processar analise: {e!s}"
        )

    return redirect("analise_jurisprudencia", documento_id=documento_id)
