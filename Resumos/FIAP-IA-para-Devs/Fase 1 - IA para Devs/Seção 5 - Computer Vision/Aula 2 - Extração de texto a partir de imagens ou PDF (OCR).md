# Aula 2 - Extração de texto a partir de imagens ou PDF (OCR)

**Fase 1 - IA para Devs** | **Seção 5 - Computer Vision**

---

## Resumo executivo

Esta aula trata de **OCR (Optical Character Recognition)**: tecnologia que converte **documentos digitalizados, imagens ou PDFs** em texto **editável e pesquisável**. Abrange **componentes** do sistema OCR: aquisição de imagem, processamento (grayscale, filtragem, thresholding/binarização, deskew), reconhecimento de texto. São apresentadas ferramentas como **Tesseract** (open-source, Google) e **PaddleOCR** (Baidu, deep learning), além de menção a serviços em nuvem (Google Cloud Vision, Azure, AWS Textract). O hands-on cobre instalação, carregamento de imagem, pré-processamento (grayscale, redimensionamento, filtros, Canny) e extração com Tesseract e PaddleOCR; uso de **expressões regulares** para extrair campos específicos (CPF/CNPJ, datas, valores) do texto extraído.

**Objetivos de aprendizagem:**

- Definir OCR e listar aplicações (digitalização, automação, acessibilidade, indexação).
- Descrever o pipeline: aquisição → processamento de imagem → reconhecimento de texto.
- Usar Tesseract (pytesseract) e PaddleOCR para extrair texto de imagens e PDFs.
- Aplicar pré-processamento (grayscale, filtros, binarização) para melhorar a precisão do OCR.
- Extrair informações estruturadas com regex a partir do texto bruto do OCR.

---

## Conceitos-chave (flashcards)

**P:** O que é OCR?  
**R:** **Reconhecimento Óptico de Caracteres**: técnica que extrai **texto** de imagens ou documentos digitalizados e o converte em dados textuais editáveis e pesquisáveis; combina visão computacional e processamento de linguagem.

**P:** Por que pré-processar a imagem antes do OCR?  
**R:** Melhorar **contraste**, reduzir **ruído** e destacar o texto (ex.: grayscale, binarização/thresholding) aumenta a precisão do reconhecimento; imagens borradas ou com fundo irregular prejudicam o OCR.

**P:** O que é Tesseract?  
**R:** Motor de OCR **open-source** (inicialmente HP, mantido pelo Google); suporta muitos idiomas; pode ser usado com **pytesseract** em Python; permite treinamento customizado.

**P:** O que é PaddleOCR?  
**R:** Biblioteca de OCR baseada em **deep learning** (PaddlePaddle/Baidu); detecta regiões de texto e reconhece caracteres; suporta múltiplos idiomas e layout complexo (tabelas, colunas); pode processar PDFs.

**P:** Para que usar regex após o OCR?  
**R:** O OCR retorna **texto bruto**; expressões regulares permitem extrair **campos específicos** (CPF, CNPJ, datas, valores) de forma estruturada para integração em sistemas.

---

## Exemplos práticos

```python
# Tesseract (Python)
import pytesseract
import cv2

img = cv2.imread("documento.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
texto = pytesseract.image_to_string(img_cinza, lang='por')
print(texto)
```

```python
# Pré-processamento para melhorar OCR (ex.: threshold)
_, binaria = cv2.threshold(img_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
texto = pytesseract.image_to_string(binaria, lang='por')
```

```python
# Extrair CPF com regex
import re
cpf_pattern = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
cpfs = re.findall(cpf_pattern, texto)
```

---

## Mapa conceitual

```
OCR
├── Componentes: aquisição → processamento → reconhecimento
├── Processamento: grayscale, filtros, thresholding, deskew
├── Ferramentas: Tesseract, PaddleOCR, Google/Azure/AWS
├── Hands-on: OpenCV + Tesseract/PaddleOCR; pré-processamento
└── Pós-processamento: regex para CPF, datas, valores
```

---

## Receita prática

1. **Instalar:** Tesseract (sistema) + pytesseract; ou PaddleOCR (pip).
2. **Carregar imagem:** OpenCV ou PIL; converter para grayscale se necessário.
3. **Pré-processar:** suavizar, binarizar (threshold) ou ajustar contraste para destacar texto.
4. **Extrair:** pytesseract.image_to_string(imagem, lang='por') ou PaddleOCR.
5. **Estruturar:** definir padrões regex (CPF, datas, etc.) e aplicar ao texto extraído.

---

## Perguntas para teste de reforço

1. OCR é visão computacional ou NLP? **R:** Ambos: visão para “ler” a imagem e extrair símbolos; NLP pode ser usado em pós-processamento (correção, interpretação).
2. O que é binarização (thresholding) no contexto de OCR? **R:** Converter imagem em tons de cinza em **preto e branco** (0 ou 255) por um limiar; ajuda a separar texto do fundo.
3. Tesseract exige que a imagem esteja em determinada resolução? **R:** Resolução muito baixa prejudica; em geral imagens nítidas e com texto legível (ex.: 300 DPI em escaneados) funcionam melhor.
4. Para que serve o parâmetro lang no Tesseract? **R:** Especificar o **idioma** do texto (ex.: 'por' para português); melhora a precisão do reconhecimento.
5. PaddleOCR é baseado em que tipo de modelo? **R:** Redes neurais (deep learning); detecta regiões de texto e reconhece caracteres com modelos pré-treinados.

---

## Materiais de apoio

- Tesseract: [github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- PaddleOCR: documentação oficial PaddlePaddle.
