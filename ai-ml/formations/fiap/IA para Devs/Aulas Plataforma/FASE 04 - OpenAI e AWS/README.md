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

**processador-contratos.py**
- API Flask para processar contratos e extrair dados
- Processa arquivos .docx e .txt automaticamente
- Usa GPT para extrair informações estruturadas em JSON
- Endpoint `/processar` para upload de arquivos
- Endpoint `/health` para verificação de status

**Como usar:**
```bash
pip install flask openai python-docx chardet python-dotenv
python processador-contratos.py
```

**Uso da API:**
```bash
curl -X POST http://localhost:5000/processar \
  -F "arquivo=@contrato.docx"
```

### Video Analysis

**webcam-faces.py**
- Detecção de faces em tempo real via webcam
- Usa OpenCV com classificador Haar Cascade
- Mostra contador de faces detectadas
- Interface simples e direta

**Como usar:**
```bash
pip install opencv-python
python webcam-faces.py
```

**analisar-emocoes-video.py**
- Analisa emoções em vídeos frame por frame
- Usa DeepFace para detecção de emoções
- Gera vídeo de saída com emoções marcadas
- Processa arquivo `video.mp4` e gera `video_emocoes.mp4`

**Como usar:**
```bash
pip install opencv-python deepface tqdm
python analisar-emocoes-video.py
```

**detectar-poses-video.py**
- Detecta poses corporais em vídeos
- Usa MediaPipe para identificar pontos-chave
- Desenha esqueleto sobre o corpo
- Gera vídeo processado com poses marcadas

**Como usar:**
```bash
pip install opencv-python mediapipe tqdm
python detectar-poses-video.py
```

**reconhecer-faces.py**
- Sistema de reconhecimento facial em tempo real
- Compara faces da webcam com banco de imagens
- Carrega imagens da pasta `imagens/`
- Identifica pessoas conhecidas

**Como usar:**
```bash
pip install opencv-python face-recognition numpy
mkdir imagens
# Adicione fotos das pessoas na pasta imagens/
python reconhecer-faces.py
```

**classificador-texto.py**
- Classificador de texto usando aprendizado supervisionado
- Usa Naive Bayes com TF-IDF
- Classifica textos em categorias (tecnologia, comida, doméstico)
- Exemplo didático de classificação de texto

**Como usar:**
```bash
pip install scikit-learn
python classificador-texto.py
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

