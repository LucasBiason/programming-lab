"""
Análise de emoções em vídeos usando DeepFace
Processa vídeo frame por frame e detecta emoções nas faces
"""

import cv2
from deepface import DeepFace
import os
from tqdm import tqdm


def obter_propriedades_video(captura):
    """Obtém propriedades do vídeo"""
    return {
        'largura': int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'altura': int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': int(captura.get(cv2.CAP_PROP_FPS)),
        'total_frames': int(captura.get(cv2.CAP_PROP_FRAME_COUNT))
    }


def criar_video_saida(caminho, largura, altura, fps):
    """Cria objeto para escrever vídeo de saída"""
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    return cv2.VideoWriter(caminho, codec, fps, (largura, altura))


def processar_video_emocoes(caminho_entrada, caminho_saida):
    """Processa vídeo detectando e marcando emoções"""
    captura = cv2.VideoCapture(caminho_entrada)
    
    if not captura.isOpened():
        print(f"Erro: não foi possível abrir o vídeo {caminho_entrada}")
        return
    
    props = obter_propriedades_video(captura)
    video_saida = criar_video_saida(
        caminho_saida,
        props['largura'],
        props['altura'],
        props['fps']
    )
    
    print(f"Processando {props['total_frames']} frames...")
    
    for _ in tqdm(range(props['total_frames']), desc="Analisando emoções"):
        ret, frame = captura.read()
        
        if not ret:
            break
        
        # Analisar emoções no frame
        try:
            resultados = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )
            
            # Processar cada face detectada
            if isinstance(resultados, list):
                for face in resultados:
                    desenhar_emocao(frame, face)
            else:
                desenhar_emocao(frame, resultados)
                
        except Exception as e:
            # Continuar mesmo se houver erro em um frame
            pass
        
        video_saida.write(frame)
    
    # Finalizar
    captura.release()
    video_saida.release()
    cv2.destroyAllWindows()
    print(f"Vídeo processado salvo em: {caminho_saida}")


def desenhar_emocao(frame, resultado_face):
    """Desenha retângulo e emoção detectada no frame"""
    regiao = resultado_face.get('region', {})
    x = regiao.get('x', 0)
    y = regiao.get('y', 0)
    w = regiao.get('w', 0)
    h = regiao.get('h', 0)
    
    emoção = resultado_face.get('dominant_emotion', 'unknown')
    
    # Desenhar retângulo
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Escrever emoção
    cv2.putText(
        frame,
        emoção.upper(),
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )


def main():
    """Função principal"""
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    video_entrada = os.path.join(diretorio_atual, 'video.mp4')
    video_saida = os.path.join(diretorio_atual, 'video_emocoes.mp4')
    
    if not os.path.exists(video_entrada):
        print(f"Erro: arquivo {video_entrada} não encontrado")
        print("Coloque um arquivo 'video.mp4' na mesma pasta do script")
        return
    
    processar_video_emocoes(video_entrada, video_saida)


if __name__ == "__main__":
    main()

