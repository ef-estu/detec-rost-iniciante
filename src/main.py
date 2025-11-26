from utils import baixar_imagem, exibir_imagem
from face_detector import detectar_rostos, desenhar_rostos
import cv2

def main():

    url = "https://media.istockphoto.com/id/1256838328/pt/foto/headshot-portraits-of-diverse-smiling-people.jpg?s=612x612&w=0&k=20&c=ylSSWsavHxJCzZdTU-bRSZoCAKqsdgNFT2PwWh2zC2s="

    img = baixar_imagem(url)

    altura_max = 800
    escala = altura_max / img.shape[0]
    img_redimensionada = cv2.resize(img, (int(img.shape[1] * escala), altura_max)) if escala < 1.0 else img.copy()

    faces = detectar_rostos(
        img_redimensionada,
        scaleFactor=1.1,
        minNeighbors=8,
        tamanho_min=(40, 40),
        proporcao_min=0.75,
        proporcao_max=1.3
    )

    img_final = desenhar_rostos(img_redimensionada, faces)
    exibir_imagem(img_final, titulo=f"Rostos detectados: {len(faces)}")

if __name__ == "__main__":
    main()
