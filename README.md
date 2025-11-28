# detec-rost-iniciante

## Equipe
- Nome do aluno — RA: XXXXXXX  
Turma: X | Curso: Ciência da Computação | Noturno | Ano: 2025

---

## 1. Problema / Contexto

A detecção de rostos é fundamental em aplicações de segurança, monitoramento, educação e reconhecimento visual. Muitos iniciantes precisam de uma solução simples, rápida e com boa precisão, que funcione sem necessidade de treinar modelos do zero.

Neste projeto, “funcionar” significa identificar corretamente os rostos presentes em uma imagem, marcá-los com retângulos e exibir o resultado de maneira clara.

---

## 2. Tipo de IA Utilizado

**Técnica usada:**  
➡️ *DNN (Deep Neural Network) — SSD (Single Shot Detector) com backbone ResNet-10, via OpenCV.*

**Por que essa técnica é adequada?**

- Modelo pré-treinado, não exige dataset nem treinamento.
- Mais robusto e preciso que Haar Cascade.
- Funciona rapidamente no Google Colab e em máquinas modestas.
- Excelente para demonstrações acadêmicas e protótipos.
- Arquitetura real usada em sistemas modernos de visão computacional.

---

## 3. Como Executar (Google Colab)

1. Abra um notebook no Colab.
2. Copie e cole todo o código do arquivo principal.
3. Execute a célula de instalação:

```bash
!pip install opencv-python-headless matplotlib requests
````

4. O modelo será baixado automaticamente (`deploy.prototxt.txt` + `.caffemodel`).
5. O script irá:

   * baixar uma imagem da internet
   * detectar rostos com o DNN
   * desenhar retângulos nos rostos
   * exibir o resultado final

Nenhuma configuração extra é necessária.

```
## 5. Tecnologias Utilizadas

* Python 3
* OpenCV (cv2.dnn)
* SSD-ResNet10 (modelo pré-treinado)
* NumPy
* Matplotlib
* Requests

---

## 6. Exemplo de Resultado

O sistema exibe a imagem com retângulos coloridos destacando cada rosto detectado, acompanhado do número de rostos encontrados.


---

