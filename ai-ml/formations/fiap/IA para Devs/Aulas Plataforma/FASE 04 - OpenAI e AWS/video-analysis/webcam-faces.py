"""
Detecção de faces em tempo real usando webcam
Usa OpenCV com classificador Haar Cascade
"""

import cv2


def inicializar_webcam():
    """Inicializa e retorna objeto de captura de vídeo"""
    captura = cv2.VideoCapture(0)
    
    if not captura.isOpened():
        print("Não foi possível abrir a webcam")
        return None
    
    return captura


def carregar_detector_faces():
    """Carrega o classificador para detecção de faces"""
    caminho_classificador = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    classificador = cv2.CascadeClassifier(caminho_classificador)
    return classificador


def processar_frame(frame, detector):
    """Processa um frame detectando faces e desenhando retângulos"""
    # Converter para escala de cinza
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar faces
    faces = detector.detectMultiScale(
        cinza,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Desenhar retângulos nas faces encontradas
    for (x, y, largura, altura) in faces:
        cv2.rectangle(frame, (x, y), (x + largura, y + altura), (0, 255, 0), 2)
        cv2.putText(
            frame,
            'Face',
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )
    
    return frame, len(faces)


def executar_deteccao():
    """Função principal que executa a detecção em tempo real"""
    captura = inicializar_webcam()
    if captura is None:
        return
    
    detector = carregar_detector_faces()
    
    print("Detecção iniciada. Pressione 'q' para sair.")
    
    try:
        while True:
            # Capturar frame
            sucesso, frame = captura.read()
            
            if not sucesso:
                print("Erro ao capturar frame")
                break
            
            # Processar frame
            frame_processado, num_faces = processar_frame(frame, detector)
            
            # Mostrar contador de faces
            cv2.putText(
                frame_processado,
                f'Faces: {num_faces}',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )
            
            # Exibir frame
            cv2.imshow('Detecção de Faces - Webcam', frame_processado)
            
            # Sair ao pressionar 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário")
    finally:
        # Liberar recursos
        captura.release()
        cv2.destroyAllWindows()
        print("Recursos liberados")


if __name__ == "__main__":
    executar_deteccao()

