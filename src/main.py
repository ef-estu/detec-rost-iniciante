from .data_prep import carregar_imagem
from .detect import detectar_rostos
from .evaluate import print_metricas

def pipeline(path):
    img = carregar_imagem(path)
    faces = detectar_rostos(img)
    print_metricas(faces)

if __name__ == "__main__":
    pipeline("data/raw/exemplo.jpg")
