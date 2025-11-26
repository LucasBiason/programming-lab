import cv2
import platform
import sys

def diagnostico_completo():
    """Diagnóstico completo de webcam"""
    
    print("=" * 60)
    print("DIAGNÓSTICO DE WEBCAM")
    print("=" * 60)
    
    # 1. Informações do sistema
    print(f"\nSistema: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    print(f"OpenCV: {cv2.__version__}")
    
    # 2. Backends disponíveis
    print(f"\nBackends disponíveis:")
    backends = [
        ("DirectShow (Windows)", cv2.CAP_DSHOW),
        ("Microsoft Media Foundation", cv2.CAP_MSMF),
        ("Video for Windows", cv2.CAP_VFW),
        ("Any (auto)", cv2.CAP_ANY)
    ]
    
    for nome, backend in backends:
        try:
            cap_test = cv2.VideoCapture(0, backend)
            if cap_test.isOpened():
                print(f"  ✅ {nome}")
                cap_test.release()
            else:
                print(f"  ❌ {nome}")
        except:
            print(f"  ❌ {nome} (erro)")
    
    # 3. Testar índices
    print(f"\n{'=' * 60}")
    print("TESTANDO ÍNDICES DE CÂMERA")
    print("=" * 60)
    
    cameras_encontradas = []
    
    for i in range(5):
        # Tentar com DirectShow
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        
        if cap.isOpened():
            ret, frame = cap.read()
            
            if ret:
                height, width = frame.shape[:2]
                fps = cap.get(cv2.CAP_PROP_FPS)
                cameras_encontradas.append(i)
                
                print(f"\n✅ CÂMERA {i}: FUNCIONAL")
                print(f"   Backend: DirectShow")
                print(f"   Resolução: {width}x{height}")
                print(f"   FPS: {fps}")
                
                # Testar detecção de rosto
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_cascade = cv2.CascadeClassifier(
                    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
                )
                faces = face_cascade.detectMultiScale(gray)
                print(f"   Rostos detectados: {len(faces)}")
            else:
                print(f"\n⚠️ Câmera {i}: Abre mas não captura")
            
            cap.release()
    
    # 4. Resumo
    print(f"\n{'=' * 60}")
    print("RESUMO")
    print("=" * 60)
    
    if cameras_encontradas:
        print(f"\n✅ {len(cameras_encontradas)} câmera(s) funcional(is)!")
        print(f"\n🎯 USE ESTE CÓDIGO:")
        print(f"\n```python")
        print(f"cap = cv2.VideoCapture({cameras_encontradas[0]}, cv2.CAP_DSHOW)")
        print(f"```")
        
        print(f"\nCâmeras disponíveis: {cameras_encontradas}")
    else:
        print(f"\n❌ NENHUMA câmera funcional detectada!")
        print(f"\n📋 CHECKLIST:")
        print(f"  [ ] Webcam habilitada (devmgmt.msc)")
        print(f"  [ ] Permissões de privacidade")
        print(f"  [ ] Drivers atualizados")
        print(f"  [ ] Antivírus não bloqueia")
        print(f"  [ ] App Câmera do Windows funciona")
        print(f"  [ ] BIOS: Integrated Camera = Enabled")

if __name__ == "__main__":
    diagnostico_completo()




