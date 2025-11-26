"""
Detecção de faces em tempo real usando webcam
Usa OpenCV com classificador Haar Cascade
"""

import cv2


def capturar_video():
    """Captura vídeo da webcam e detecta faces"""
    # Iniciar captura da webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Não foi possível acessar a webcam")
        return

    # Carregar classificador para detecção de faces
    classificador_face = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    try:
        while True:
            # Capturar frame
            ret, frame = cap.read()

            if not ret:
                break

            # Converter para escala de cinza
            cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detectar faces
            faces = classificador_face.detectMultiScale(
                cinza,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Desenhar retângulos nas faces detectadas
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Mostrar frame
            cv2.imshow('Detecção de Faces', frame)

            # Parar ao pressionar 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capturar_video()

