import cv2
import random

def detectar_rostos(img, scaleFactor=1.1, minNeighbors=5, tamanho_min=(40, 40), proporcao_min=0.75, proporcao_max=1.3):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=tamanho_min
    )

    faces = [f for f in faces if proporcao_min <= f[2]/f[3] <= proporcao_max]

    filtradas = []
    for f in faces:
        if not any(abs(f[0]-o[0])<20 and abs(f[1]-o[1])<20 for o in filtradas):
            filtradas.append(f)

    return filtradas


def desenhar_rostos(img, faces):
    img_copy = img.copy()
    random.seed(42)

    for i, (x, y, w, h) in enumerate(faces):
        cor = tuple([random.randint(0, 255) for _ in range(3)])
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), cor, 2)
        cv2.putText(img_copy, f"Rosto {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)

    return img_copy
