import cv2

def carregar_imagem(path):
    img = cv2.imread(path)
    return img

def preprocessar_imagem(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return gray
