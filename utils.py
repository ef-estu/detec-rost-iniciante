import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np

def baixar_imagem(url):
    response = requests.get(url)
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

def exibir_imagem(img, titulo="Imagem"):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.imshow(img_rgb)
    plt.title(titulo)
    plt.axis("off")
    plt.show()
