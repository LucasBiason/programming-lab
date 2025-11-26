import cv2
import os

def testar_todas_cameras():
    """Testa TODOS os dispositivos /dev/video* no Linux"""
    
    print("=" * 70)
    print("DIAGNÓSTICO DE WEBCAM - LINUX")
    print("=" * 70)
    
    print(f"\nOpenCV: {cv2.__version__}")
    print(f"Sistema: Linux\n")
    
    # Listar dispositivos disponíveis
    video_devices = []
    for i in range(50):
        device_path = f"/dev/video{i}"
        if os.path.exists(device_path):
            video_devices.append(i)
    
    print(f"Dispositivos /dev/video* encontrados: {len(video_devices)}")
    print(f"Índices: {video_devices}\n")
    
    print("=" * 70)
    print("TESTANDO CADA DISPOSITIVO")
    print("=" * 70)
    
    cameras_funcionais = []
    
    for i in video_devices:
        print(f"\n📹 Testando /dev/video{i}...")
        
        try:
            cap = cv2.VideoCapture(i)
            
            if cap.isOpened():
                # Tentar capturar frame
                ret, frame = cap.read()
                
                if ret and frame is not None and frame.size > 0:
                    height, width = frame.shape[:2]
                    fps = cap.get(cv2.CAP_PROP_FPS)
                    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
                    
                    # Testar se consegue detectar rosto
                    try:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        face_cascade = cv2.CascadeClassifier(
                            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
                        )
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                        
                        cameras_funcionais.append({
                            'indice': i,
                            'resolucao': f"{width}x{height}",
                            'fps': fps,
                            'fourcc': fourcc,
                            'rostos_detectados': len(faces)
                        })
                        
                        print(f"   ✅ FUNCIONAL!")
                        print(f"   Resolução: {width}x{height}")
                        print(f"   FPS: {fps}")
                        print(f"   Rostos detectados no frame: {len(faces)}")
                    except Exception as e:
                        print(f"   ⚠️ Captura OK, mas erro ao processar: {e}")
                else:
                    print(f"   ❌ Abre mas não captura frame válido")
                
                cap.release()
            else:
                print(f"   ❌ Não consegue abrir")
        
        except Exception as e:
            print(f"   ❌ Erro: {e}")
    
    # Resumo
    print(f"\n{'=' * 70}")
    print("RESUMO E SOLUÇÃO")
    print("=" * 70)
    
    if cameras_funcionais:
        print(f"\n✅ {len(cameras_funcionais)} WEBCAM(S) FUNCIONAL(IS) ENCONTRADA(S)!\n")
        
        for cam in cameras_funcionais:
            print(f"Câmera /dev/video{cam['indice']}:")
            print(f"  Resolução: {cam['resolucao']}")
            print(f"  FPS: {cam['fps']}")
            print(f"  Rostos detectados: {cam['rostos_detectados']}")
            print()
        
        # Melhor câmera (maior resolução)
        melhor = max(cameras_funcionais, key=lambda x: int(x['resolucao'].split('x')[0]))
        
        print(f"🎯 RECOMENDADO: Use /dev/video{melhor['indice']}\n")
        print(f"📝 CÓDIGO PARA USAR:")
        print(f"\n```python")
        print(f"# No Linux, use índice {melhor['indice']}")
        print(f"cap = cv2.VideoCapture({melhor['indice']})")
        print(f"```")
        
        # Salvar resultado em arquivo
        with open('webcam_encontrada.txt', 'w') as f:
            f.write(f"WEBCAM FUNCIONAL: /dev/video{melhor['indice']}\n")
            f.write(f"Índice a usar: {melhor['indice']}\n")
            f.write(f"Resolução: {melhor['resolucao']}\n")
        
        print(f"\n✅ Resultado salvo em: webcam_encontrada.txt")
    else:
        print(f"\n❌ NENHUMA webcam funcional encontrada!")
        print(f"\n📋 POSSÍVEIS CAUSAS:")
        print(f"  1. Webcam desabilitada no hardware")
        print(f"  2. Permissões: usuário não está no grupo 'video'")
        print(f"  3. Driver não carregado")
        print(f"  4. Webcam com problema físico")
        print(f"\n🔧 SOLUÇÕES:")
        print(f"  # Verificar grupo:")
        print(f"  groups")
        print(f"  ")
        print(f"  # Adicionar ao grupo video:")
        print(f"  sudo usermod -a -G video $USER")
        print(f"  ")
        print(f"  # Listar câmeras:")
        print(f"  ls -l /dev/video*")

if __name__ == "__main__":
    testar_todas_cameras()




