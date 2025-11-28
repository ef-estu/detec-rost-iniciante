# detec-rost-iniciante

Este projeto utiliza o modelo DNN (Deep Neural Network) do OpenCV para detectar rostos em uma imagem baixada da internet. O código realiza o download da imagem, carrega o modelo de detecção e marca os rostos encontrados com retângulos coloridos.

---

## 🧠 Funcionalidade
- Baixa uma imagem a partir de uma URL.
- Carrega automaticamente o modelo de detecção de rostos (SSD + ResNet).
- Processa a imagem e identifica rostos.
- Exibe o resultado com os rostos marcados.

---

## ▶️ Como executar (Google Colab)
1. Copie o código do projeto para o Google Colab.
2. Execute cada célula na ordem.
3. Veja o resultado final com os rostos detectados.

---

## 📦 Dependências
Instale com:

```bash
pip install opencv-python-headless matplotlib requests numpy
