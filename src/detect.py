import cv2
from .data_prep import preprocessar_imagem

def detectar_rostos(img):
    gray = preprocessar_imagem(img)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    return faces
