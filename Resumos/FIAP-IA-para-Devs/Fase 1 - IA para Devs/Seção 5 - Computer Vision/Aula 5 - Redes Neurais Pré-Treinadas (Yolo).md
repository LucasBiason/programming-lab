# Aula 5 - Redes Neurais Pré-Treinadas (Yolo)

**Fase 1 - IA para Devs** | **Seção 5 - Computer Vision**

---

## Resumo executivo

Esta aula aborda o uso de **redes neurais pré-treinadas**, com foco em **YOLO (You Only Look Once)** para **detecção de objetos em tempo real**. YOLO trata a detecção como um problema de **regressão**: uma única rede prediz bounding boxes e classes em **uma passada** sobre a imagem, dividida em grade (ex.: 7x7), com múltiplas caixas e scores por célula. Versões (YOLOv3, v4, v5, v8) evoluíram em precisão e velocidade. **Pré-treinamento** (ex.: em COCO, ImageNet) permite usar modelos já capazes de detectar muitas classes; **fine-tuning** ou uso direto com suas classes é comum. Frameworks como Darknet, PyTorch (YOLOv5/v8) e OpenCV (DNN) permitem carregar modelos pré-treinados e inferência em imagens e vídeo. Este resumo consolida os conceitos centrais.

**Objetivos de aprendizagem:**

- Entender a ideia do YOLO: detecção em **uma única passada** (regressão de caixas e classes).
- Diferenciar YOLO de detectores em duas etapas (ex.: R-CNN): mais rápido, adequado a tempo real.
- Saber carregar e usar um modelo YOLO **pré-treinado** (weights + config ou formato do framework).
- Aplicar detecção em imagem e vídeo; interpretar saída (bounding boxes, classes, confiança).

---

## Conceitos-chave (flashcards)

**P:** O que significa “You Only Look Once” no YOLO?  
**R:** A rede processa a imagem **uma única vez** (uma forward pass) e já produz todas as detecções (caixas + classes); em contraste com métodos que primeiro geram propostas e depois classificam (duas etapas).

**P:** Como o YOLO divide a imagem?  
**R:** Em uma **grade** (ex.: 7x7 ou 13x13); cada célula é responsável por prever um número fixo de bounding boxes e probabilidades de classe; a saída é interpretada para obter as caixas finais (com supressão de não-máximos, NMS).

**P:** O que é um modelo pré-treinado?  
**R:** Rede **já treinada** em um grande dataset (ex.: COCO, ImageNet); os pesos aprendidos podem ser reutilizados para **inferência** direta ou **fine-tuning** em outra tarefa/dataset, economizando dados e tempo.

**P:** Para que serve NMS (Non-Maximum Suppression) na detecção?  
**R:** Eliminar **caixas redundantes** que cobrem o mesmo objeto; mantém a caixa com maior score e remove outras com sobreposição (IoU) acima de um limiar; reduz duplicatas.

**P:** YOLO é adequado para tempo real? **R:** Sim; por ser uma única passada e arquiteturas otimizadas (YOLOv5, v8), atinge muitos FPS em GPU, sendo usado em vídeo ao vivo, drones, veículos autônomos.

---

## Mapa conceitual

```
YOLO e redes pré-treinadas
├── YOLO: detecção em uma passada, grade, regressão de caixas + classes
├── Pré-treinamento: COCO, ImageNet; reutilização de pesos
├── Uso: carregar weights/config, inferência em imagem/vídeo
├── Pós-processamento: NMS (reduzir caixas sobrepostas)
└── Versões: YOLOv3, v4, v5, v8 (precisão e velocidade)
```

---

## Receita prática

1. **Escolher versão e framework:** ex.: YOLOv5 ou YOLOv8 (PyTorch); baixar weights pré-treinados (ex.: yolov5s.pt).
2. **Carregar modelo:** conforme API do framework (ex.: torch.hub ou script oficial).
3. **Inferência:** passar imagem (tensor ou array); obter lista de detecções (x, y, w, h ou x1,y1,x2,y2, class_id, confidence).
4. **Desenhar:** usar OpenCV para desenhar bounding boxes e labels na imagem.
5. **Vídeo:** loop de frames; rodar detecção em cada frame; opcionalmente aplicar NMS se a saída já não vier filtrada.

---

## Perguntas para teste de reforço

1. YOLO prediz o quê exatamente? **R:** Para cada célula da grade (e eventualmente escalas): coordenadas da bounding box (ou offsets), score de objeto e probabilidades por classe; a decodificação produz as caixas finais.
2. O que é o dataset COCO? **R:** Dataset grande de imagens com anotações para **detecção** e **segmentação**; muitas classes (pessoa, carro, etc.); usado para treinar e avaliar YOLO e outros detectores.
3. Fine-tuning de YOLO: quando fazer? **R:** Quando precisamos detectar **classes** que não estão (ou estão pouco) no dataset de pré-treinamento; treinar (ou ajustar) a rede no nosso dataset mantendo parte dos pesos congelados.
4. O que é confidence (confiança) na saída do YOLO? **R:** Score que indica quão “certo” o modelo está de que há um objeto naquela caixa (e da classe atribuída); filtramos detecções por um limiar (ex.: 0,5) para reduzir falsos positivos.
5. Por que YOLO é mais rápido que R-CNN clássico? **R:** R-CNN gera muitas propostas de região e classifica cada uma (muitas forward passes); YOLO faz **uma** passada e regride tudo de uma vez; menos etapas e menos custo.

---

## Materiais de apoio

- YOLO (original): [pjreddie.com/darknet/yolo](https://pjreddie.com/darknet/yolo/)
- YOLOv5 (PyTorch): [github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
