"""
Detecção de poses corporais em vídeos usando MediaPipe
Identifica pontos-chave do corpo e desenha esqueleto
"""

import cv2
import mediapipe as mp
import os
from tqdm import tqdm


def configurar_mediapipe():
    """Configura e retorna objetos do MediaPipe"""
    mp_pose = mp.solutions.pose
    detector_pose = mp_pose.Pose()
    desenhador = mp.solutions.drawing_utils
    return detector_pose, desenhador, mp_pose


def obter_info_video(captura):
    """Extrai informações do vídeo"""
    return {
        'largura': int(captura.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'altura': int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': int(captura.get(cv2.CAP_PROP_FPS)),
        'total': int(captura.get(cv2.CAP_PROP_FRAME_COUNT))
    }


def processar_video_poses(caminho_entrada, caminho_saida):
    """Processa vídeo detectando poses"""
    detector, desenhador, mp_pose = configurar_mediapipe()
    
    captura = cv2.VideoCapture(caminho_entrada)
    
    if not captura.isOpened():
        print(f"Erro ao abrir vídeo: {caminho_entrada}")
        return
    
    info = obter_info_video(captura)
    
    # Criar vídeo de saída
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    video_saida = cv2.VideoWriter(
        caminho_saida,
        codec,
        info['fps'],
        (info['largura'], info['altura'])
    )
    
    print(f"Processando {info['total']} frames...")
    
    for _ in tqdm(range(info['total']), desc="Detectando poses"):
        ret, frame = captura.read()
        
        if not ret:
            break
        
        # Converter BGR para RGB (MediaPipe usa RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detectar pose
        resultado = detector.process(frame_rgb)
        
        # Desenhar landmarks se detectado
        if resultado.pose_landmarks:
            desenhador.draw_landmarks(
                frame,
                resultado.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
        
        video_saida.write(frame)
        
        # Mostrar preview (opcional)
        cv2.imshow('Preview - Detecção de Poses', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Finalizar
    captura.release()
    video_saida.release()
    cv2.destroyAllWindows()
    print(f"Vídeo processado: {caminho_saida}")


def main():
    """Função principal"""
    diretorio = os.path.dirname(os.path.abspath(__file__))
    entrada = os.path.join(diretorio, 'video.mp4')
    saida = os.path.join(diretorio, 'video_poses.mp4')
    
    if not os.path.exists(entrada):
        print(f"Arquivo não encontrado: {entrada}")
        print("Coloque um arquivo 'video.mp4' na pasta do script")
        return
    
    processar_video_poses(entrada, saida)


if __name__ == "__main__":
    main()

