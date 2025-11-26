import cv2
import os

def detectar_rostos_em_imagem(image_path):
    """
    Detecta rostos em uma imagem estática
    Alternativa para quando webcam não funciona
    """
    
    # Verificar se imagem existe
    if not os.path.exists(image_path):
        print(f"❌ Erro: Arquivo '{image_path}' não encontrado!")
        print(f"\nPara usar este script:")
        print(f"  1. Tire uma foto sua (ou baixe uma imagem com pessoas)")
        print(f"  2. Salve como: foto_teste.jpg")
        print(f"  3. Execute: python3 face_detection_image.py")
        return
    
    # Carregar imagem
    print(f"📸 Carregando imagem: {image_path}")
    frame = cv2.imread(image_path)
    
    if frame is None:
        print(f"❌ Erro ao carregar imagem!")
        return
    
    print(f"✅ Imagem carregada: {frame.shape[1]}x{frame.shape[0]} pixels")
    
    # Carregar Haar Cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    if face_cascade.empty():
        print("❌ Erro ao carregar Haar Cascade!")
        return
    
    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostos
    print("\n🔍 Detectando rostos...")
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    print(f"✅ {len(faces)} rosto(s) detectado(s)!")
    
    # Desenhar retângulos
    for i, (x, y, w, h) in enumerate(faces, 1):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(
            frame,
            f"Face {i}",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )
        print(f"  Face {i}: x={x}, y={y}, largura={w}, altura={h}")
    
    # Salvar imagem com detecções
    output_path = image_path.replace('.jpg', '_detected.jpg').replace('.png', '_detected.png')
    cv2.imwrite(output_path, frame)
    print(f"\n💾 Imagem salva: {output_path}")
    
    # Exibir imagem
    print(f"\n🖼️  Exibindo imagem... (Pressione qualquer tecla para fechar)")
    cv2.imshow('Face Detection - Imagem Estática', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(f"\n✅ Detecção concluída!")

if __name__ == "__main__":
    # Tentar usar foto_teste.jpg
    image_file = 'foto_teste.jpg'
    
    # Se não existir, listar imagens disponíveis
    if not os.path.exists(image_file):
        print(f"⚠️  '{image_file}' não encontrado.")
        print(f"\nBuscando imagens na pasta atual...")
        
        images = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        if images:
            print(f"\n📷 Imagens encontradas:")
            for i, img in enumerate(images, 1):
                print(f"  {i}. {img}")
            
            print(f"\nUsando primeira imagem: {images[0]}")
            image_file = images[0]
        else:
            print(f"\n❌ Nenhuma imagem .jpg ou .png encontrada!")
            print(f"\n📝 Instruções:")
            print(f"  1. Tire uma foto ou baixe uma imagem")
            print(f"  2. Salve nesta pasta como: foto_teste.jpg")
            print(f"  3. Execute novamente este script")
            return
    
    detectar_rostos_em_imagem(image_file)




