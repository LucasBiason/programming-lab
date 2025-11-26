# Fase 4 - OpenAI e AWS

Conteúdo da Fase 4 do curso FIAP IA para Devs sobre APIs OpenAI e serviços AWS.

## Estrutura

```
FASE 04 - OpenAI e AWS/
├── openai-api/         # Integração com OpenAI API
├── aws-services/       # Serviços AWS (Textract, Comprehend)
└── video-analysis/     # Análise de vídeo, áudio e texto
```

## Projetos

### OpenAI API

**extrair-dados-contrato.py**
- API Flask para extrair dados de contratos
- Processa arquivos .docx e .txt
- Usa GPT para extrair informações estruturadas
- Retorna JSON com dados do contrato

**Como usar:**
```bash
pip install flask openai python-docx chardet python-dotenv
python extrair-dados-contrato.py
```

**Notebooks:**
- `Aula 03 - APIs OpenAI.ipynb` - Primeiros passos com API
- `Aula 04 - API-DALLE.ipynb` - Geração de imagens
- `Aula 05 - Integração e Automação.py` - Automação completa

### Video Analysis

**deteccao-facial.py**
- Detecção de faces em tempo real via webcam
- Usa OpenCV com Haar Cascade
- Interface simples e direta

**Como usar:**
```bash
pip install opencv-python
python deteccao-facial.py
```

**transcricao-audio.py**
- Transcreve áudio para texto
- Usa Google Speech Recognition
- Suporta português brasileiro

**Como usar:**
```bash
pip install SpeechRecognition
python transcricao-audio.py
```

**sumarizacao-texto.py**
- Sumariza documentos .docx
- Usa transformers pipeline
- Gera resumos automáticos

**Como usar:**
```bash
pip install python-docx transformers torch
python sumarizacao-texto.py
```

## Tecnologias

- OpenAI API (GPT, DALL-E)
- Flask
- OpenCV
- Speech Recognition
- Transformers
- AWS Textract (documentação)
- AWS Comprehend (documentação)

## Notas

- Códigos simplificados e funcionais
- Comentários em português
- Estrutura organizada
- Pronto para uso e aprendizado

