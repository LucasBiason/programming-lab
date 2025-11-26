import cv2

print("Testando câmera...")

# Tentar com DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Câmera 0 falhou. Tentando índice 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if cap.isOpened():
    print("✅ Câmera aberta!")
    ret, frame = cap.read()
    
    if ret:
        print(f"✅ Frame capturado! Resolução: {frame.shape[1]}x{frame.shape[0]}")
        cv2.imshow('Teste Webcam - Pressione qualquer tecla', frame)
        cv2.waitKey(3000)
    else:
        print("❌ Não conseguiu capturar frame")
    
    cap.release()
    cv2.destroyAllWindows()
else:
    print("❌ Nenhuma câmera encontrada!")
    print("\nVerifique:")
    print("  1. Gerenciador de Dispositivos (devmgmt.msc)")
    print("  2. Configurações → Privacidade → Câmera")
    print("  3. App Câmera do Windows funciona?")




