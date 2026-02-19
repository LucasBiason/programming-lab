# Aula 3 - Detecção e Rastreamento de objetos

**Fase 1 - IA para Devs** | **Seção 5 - Computer Vision**

---

## Resumo executivo

Esta aula aborda **detecção** e **rastreamento de objetos** em imagens e vídeos. **Detecção** consiste em localizar e classificar objetos em um frame (bounding boxes e classes); **rastreamento** consiste em seguir o mesmo objeto ao longo do tempo (múltiplos frames). São apresentados conceitos como regiões de interesse (ROI), bounding boxes, e pipelines que combinam detecção (ex.: classificador ou rede que localiza objetos) com rastreamento (associação de identidade frame a frame). Ferramentas típicas incluem OpenCV (Haar cascades, funções de rastreamento), e modelos de deep learning (YOLO, detectores baseados em CNN). Métricas comuns: precisão da localização (IoU), e métricas de rastreamento (ex.: MOT). Este resumo consolida os conceitos centrais.

**Objetivos de aprendizagem:**

- Diferenciar detecção de objetos (onde e o quê em um frame) de rastreamento (seguir o mesmo objeto no tempo).
- Entender bounding box, ROI e pipeline detecção → rastreamento.
- Conhecer abordagens clássicas (OpenCV) e baseadas em deep learning (YOLO, etc.).
- Interpretar métricas de detecção (ex.: IoU) e noção de rastreamento multi-objeto.

---

## Conceitos-chave (flashcards)

**P:** O que é detecção de objetos?  
**R:** Tarefa de **localizar** (ex.: bounding box) e **classificar** objetos em uma imagem ou frame; resposta: “o quê” e “onde” (coordenadas da caixa e classe).

**P:** O que é rastreamento de objetos?  
**R:** **Seguir** o mesmo objeto ao longo de vários frames (vídeo); manter a **identidade** do objeto entre frames (associação detecção-atual com detecção-anterior).

**P:** O que é uma bounding box?  
**R:** Retângulo (ou forma) que **delimita** o objeto na imagem; geralmente definido por (x, y, largura, altura) ou (x_min, y_min, x_max, y_max).

**P:** O que é IoU (Intersection over Union)?  
**R:** Métrica de **sobreposição** entre a caixa predita e a caixa real: área da interseção / área da união; valor entre 0 e 1; maior IoU = melhor localização.

**P:** Cite uma abordagem rápida para detecção em tempo real. **R:** **YOLO** (You Only Look Once): rede que prediz bounding boxes e classes em uma única passada; permite detecção em tempo real.

---

## Mapa conceitual

```
Detecção e rastreamento
├── Detecção: localizar + classificar (bounding box, classe)
├── Rastreamento: manter identidade do objeto no tempo (vídeo)
├── Pipeline: detecção em cada frame → associação com objetos já rastreados
├── Abordagens: OpenCV (Haar, trackers), deep learning (YOLO, etc.)
└── Métricas: IoU (detecção), métricas de rastreamento (MOT)
```

---

## Receita prática

1. **Detecção:** usar modelo pré-treinado (ex.: YOLO, SSD) ou detector OpenCV; obter bounding boxes e classes.
2. **Rastreamento:** em vídeo, associar detecções do frame t com as do frame t-1 (por proximidade, IoU ou rede de re-identificação).
3. **Avaliar:** IoU para qualidade da caixa; métricas de rastreamento (precisão/recall de identidade) para multi-objeto.
4. **Otimização:** balancear precisão e velocidade (ex.: YOLO para tempo real).

---

## Perguntas para teste de reforço

1. Detecção responde a quais perguntas? **R:** “O quê” (classe) e “onde” (posição, ex.: bounding box) na imagem.
2. Por que rastreamento é mais que “detectar em cada frame”? **R:** É preciso **associar** a mesma entidade entre frames (manter ID); detecção sozinha não diz se duas caixas em frames diferentes são o mesmo objeto.
3. O que é ROI? **R:** Region of Interest: região da imagem (ex.: retângulo) em que se concentra o processamento (detecção/rastreamento).
4. IoU = 0,5 significa quê? **R:** Sobreposição moderada entre caixa predita e caixa real; em benchmarks costuma-se considerar detecção “correta” se IoU > 0,5.
5. YOLO é detecção ou rastreamento? **R:** Detecção (por frame); pode ser usado como etapa de detecção dentro de um pipeline de rastreamento (associando resultados entre frames).

---

## Materiais de apoio

- OpenCV – Object Detection and Tracking: documentação OpenCV.
