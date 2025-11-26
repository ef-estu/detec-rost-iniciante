import cv2
import os
from data_prep import load_image, preprocess_image
from evaluate import plot_detection

def detect_faces(image_path):

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    img = load_image(image_path)
    gray = preprocess_image(img)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    return img

if __name__ == "__main__":
    image_path = "data/raw/sua_imagem.jpg"  # coloque uma imagem lá
    detected = detect_faces(image_path)
    plot_detection(cv2.imread(image_path), detected)
