import cv2


def find_camera_index(preferred_index: int = 32, max_index: int = 40) -> int | None:
    candidates = [preferred_index] + [idx for idx in range(max_index) if idx != preferred_index]

    for idx in candidates:
        cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)
        if not cap.isOpened():
            cap.release()
            continue

        ret, _ = cap.read()
        cap.release()

        if ret:
            return idx

    return None


def main() -> None:
    camera_index = find_camera_index()
    if camera_index is None:
        print("Não foi possível encontrar uma webcam funcional.")
        return

    cap = cv2.VideoCapture(camera_index, cv2.CAP_V4L2)

    if not cap.isOpened():
        print(f"Erro ao acessar a webcam no índice {camera_index}.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print("Pressione 'q' para encerrar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar frame. Encerrando...")
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Face Detection - Logitech C922", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

