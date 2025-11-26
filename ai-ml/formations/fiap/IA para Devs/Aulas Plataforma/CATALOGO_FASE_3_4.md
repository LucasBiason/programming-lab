# Catálogo - Fase 3 e Fase 4 - FIAP IA para Devs

Este documento cataloga todo o conteúdo migrado das Fases 3 e 4 que não estava organizado no laboratório.

## Fase 3 - LangChain e Fine-Tuning

### Conteúdo Migrado

#### LangChain - Agentes
- **agent-investimentos.py**: Agente para consulta de ações brasileiras
  - Function calling com OpenAI
  - Integração com yfinance
  - Geração de gráficos
  - Interface Streamlit

#### RAG - Retrieval Augmented Generation
- **assistente-receitas.py**: Assistente de receitas com RAG
  - LangChain + ChromaDB
  - Busca vetorial de receitas
  - Geração de respostas com contexto

#### Fine-Tuning
- **fine-tuning-rag-documentos-fiap-main/**: Projeto completo
  - Aula 01: Preparação de dados para fine-tuning
    - Web scraping de notícias
    - Formatação de dados
    - Geração de dataset JSONL
  - Aula 02: Fine-tuning de LLM
    - Fine-tuning com Unsloth
    - Modelo para sumarização
    - Treinamento otimizado
  - Aula 03: RAG para documentos
    - Aplicação RAG completa
    - Integração com LangChain
    - Busca em documentos

### Arquivos Originais (Mantidos)
- Notebooks originais preservados em `fine-tuning/`
- Códigos adaptados em `langchain/` e `rag/`

---

## Fase 4 - OpenAI e AWS

### Conteúdo Migrado

#### OpenAI API
- **extrair-dados-contrato.py**: API Flask para extração de dados
  - Processamento de .docx e .txt
  - Extração estruturada com GPT
  - Retorno em JSON

- **IADT-openai-api-main/**: Projetos originais
  - Aula 03: APIs OpenAI (notebook)
  - Aula 04: API DALL-E (notebook)
  - Aula 05: Integração e Automação (código Python)

#### Video/Audio/Text Analysis
- **deteccao-facial.py**: Detecção de faces em tempo real
  - OpenCV + Haar Cascade
  - Webcam em tempo real

- **transcricao-audio.py**: Transcrição de áudio
  - Google Speech Recognition
  - Suporte pt-BR

- **sumarizacao-texto.py**: Sumarização de documentos
  - Transformers pipeline
  - Processamento de .docx

- **IADT-Video_Audio_Text_Analysis-main/**: Projetos originais
  - Aula 1: Reconhecimento facial webcam
  - Aula 2: Reconhecimento facial em vídeos
  - Aula 3: Detecção de poses
  - Aula 4: Transcrição de áudio
  - Aula 5: Classificadores
  - Aula 6: Sumarização

### Documentação AWS
- Resumos de aulas sobre Textract e Comprehend
- Guias de uso dos serviços AWS
- Exemplos práticos

---

## Adaptações Realizadas

### Simplificações
1. **Códigos Python**:
   - Comentários traduzidos para português
   - Nomes de variáveis mais claros
   - Estrutura simplificada
   - Remoção de código desnecessário

2. **Documentação**:
   - READMEs criados para cada fase
   - Instruções de uso simplificadas
   - Requirements.txt organizados

3. **Organização**:
   - Estrutura por tema/fase
   - Separação clara de projetos
   - Códigos adaptados separados dos originais

### Mantido
- Funcionalidade original
- Estrutura de projetos complexos
- Notebooks originais (para referência)
- Dados e arquivos de exemplo

---

## Estrutura Final

```
FASE 03 - LangChain e Fine-Tuning/
├── langchain/
│   ├── agent-investimentos.py
│   └── requirements.txt
├── rag/
│   ├── assistente-receitas.py
│   └── requirements.txt
└── fine-tuning/
    └── fine-tuning-rag-documentos-fiap-main/ (original)

FASE 04 - OpenAI e AWS/
├── openai-api/
│   ├── extrair-dados-contrato.py
│   ├── requirements.txt
│   └── IADT-openai-api-main/ (original)
└── video-analysis/
    ├── deteccao-facial.py
    ├── transcricao-audio.py
    ├── sumarizacao-texto.py
    ├── requirements.txt
    └── IADT-Video_Audio_Text_Analysis-main/ (original)
```

---

## Status

- ✅ Códigos adaptados e simplificados
- ✅ READMEs criados
- ✅ Requirements organizados
- ✅ Estrutura organizada por fase
- ✅ Projetos originais preservados
- ✅ Funcionalidade mantida

**Última atualização**: 2025-11-26

