"""
Sistema de reconhecimento facial em tempo real
Compara faces da webcam com banco de imagens conhecidas
"""

import cv2
import face_recognition
import os
import numpy as np


def carregar_banco_faces(pasta_imagens):
    """Carrega imagens conhecidas e gera encodings"""
    encodings_conhecidos = []
    nomes_conhecidos = []
    
    if not os.path.exists(pasta_imagens):
        print(f"Pasta '{pasta_imagens}' não encontrada")
        return encodings_conhecidos, nomes_conhecidos
    
    # Processar cada imagem na pasta
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            caminho_completo = os.path.join(pasta_imagens, arquivo)
            
            # Carregar e processar imagem
            imagem = face_recognition.load_image_file(caminho_completo)
            encodings = face_recognition.face_encodings(imagem)
            
            if encodings:
                # Usar primeiro encoding encontrado
                encodings_conhecidos.append(encodings[0])
                # Nome do arquivo sem extensão
                nome = os.path.splitext(arquivo)[0]
                nomes_conhecidos.append(nome)
                print(f"Carregado: {nome}")
    
    return encodings_conhecidos, nomes_conhecidos


def identificar_face(encoding_face, encodings_conhecidos, nomes_conhecidos):
    """Identifica uma face comparando com banco conhecido"""
    if not encodings_conhecidos:
        return "Desconhecido"
    
    # Comparar com faces conhecidas
    comparacoes = face_recognition.compare_faces(
        encodings_conhecidos,
        encoding_face,
        tolerance=0.6
    )
    
    # Calcular distâncias
    distancias = face_recognition.face_distance(
        encodings_conhecidos,
        encoding_face
    )
    
    # Encontrar melhor match
    indice_melhor = np.argmin(distancias)
    
    if comparacoes[indice_melhor]:
        return nomes_conhecidos[indice_melhor]
    
    return "Desconhecido"


def desenhar_identificacao(frame, localizacao, nome):
    """Desenha retângulo e nome da pessoa identificada"""
    top, right, bottom, left = localizacao
    
    # Retângulo ao redor da face
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    
    # Fundo para o texto
    cv2.rectangle(
        frame,
        (left, bottom - 35),
        (right, bottom),
        (0, 255, 0),
        cv2.FILLED
    )
    
    # Texto com nome
    cv2.putText(
        frame,
        nome,
        (left + 6, bottom - 6),
        cv2.FONT_HERSHEY_DUPLEX,
        0.7,
        (255, 255, 255),
        1
    )


def executar_reconhecimento(pasta_imagens='imagens'):
    """Função principal de reconhecimento"""
    # Carregar banco de faces
    print("Carregando banco de faces conhecidas...")
    encodings, nomes = carregar_banco_faces(pasta_imagens)
    
    if not encodings:
        print("Nenhuma face conhecida encontrada!")
        print(f"Crie a pasta '{pasta_imagens}' e adicione fotos das pessoas")
        return
    
    print(f"{len(encodings)} face(s) conhecida(s) carregada(s)")
    
    # Inicializar webcam
    captura = cv2.VideoCapture(0)
    
    if not captura.isOpened():
        print("Erro ao abrir webcam")
        return
    
    print("Reconhecimento iniciado. Pressione 'q' para sair.")
    
    try:
        while True:
            ret, frame = captura.read()
            
            if not ret:
                break
            
            # Redimensionar para processamento mais rápido
            frame_pequeno = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            frame_rgb = np.ascontiguousarray(frame_pequeno[:, :, ::-1])
            
            # Detectar faces
            localizacoes = face_recognition.face_locations(frame_rgb)
            encodings_frame = face_recognition.face_encodings(frame_rgb, localizacoes)
            
            # Identificar cada face
            for localizacao, encoding in zip(localizacoes, encodings_frame):
                nome = identificar_face(encoding, encodings, nomes)
                
                # Ajustar coordenadas para tamanho original
                top, right, bottom, left = localizacao
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                
                desenhar_identificacao(frame, (top, right, bottom, left), nome)
            
            cv2.imshow('Reconhecimento Facial', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nInterrompido")
    finally:
        captura.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    executar_reconhecimento()

