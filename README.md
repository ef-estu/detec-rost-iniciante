# detec-rost-iniciante

Este projeto implementa uma IA básica de detecção de rostos utilizando o algoritmo Haar Cascade do OpenCV. O código baixa uma imagem da internet, realiza pré-processamento (conversão para tons de cinza e equalização de contraste) e detecta rostos presentes na imagem, destacando cada um com retângulos coloridos.

## 🔧 Tecnologias utilizadas
- Python
- OpenCV
- NumPy
- Matplotlib

## ▶️ Como executar
1. Abra o arquivo no Google Colab ou Python local.
2. Instale as dependências:
   pip install opencv-python numpy matplotlib requests
3. Execute o código para carregar a imagem e detectar rostos automaticamente.

## 📌 Funcionalidade
- Baixa uma imagem a partir de uma URL
- Processa a imagem para melhorar a detecção
- Localiza rostos usando Haar Cascade
- Exibe a imagem com as detecções marcadas

## 📷 Exemplo
O código identifica rostos humanos frontais em imagens com boa iluminação e resolução razoável.
