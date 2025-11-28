# detec-rost-iniciante
# 1. Problema / Contexto

A detecção automática de rostos é um recurso essencial em diversos sistemas, como monitoramento, autenticação visual e ferramentas educacionais. Para muitos estudantes e desenvolvedores, existe a necessidade de um método simples e funcional que identifique rostos em imagens sem exigir treino pesado ou grandes bases de dados.  
Neste projeto, “funcionar” significa: **detectar corretamente rostos em uma imagem**, marcar as regiões encontradas e exibir o resultado de forma clara. Isso permite validação rápida de um pipeline real de visão computacional.

---

# 2. Tipo de IA Escolhido e Justificativa

**Técnica utilizada:**  
➡️ *Detecção de objetos via DNN (Deep Neural Network) – SSD (Single Shot Detector) com backbone ResNet-10, usando OpenCV.*

**Por que é adequado:**  
- O modelo SSD pré-treinado possui boa precisão e é mais robusto que Haar Cascade.  
- Não exige treinamento: basta carregar os pesos prontos.  
- Funciona bem no Google Colab e computadores comuns.  
- É ideal para protótipos rápidos e demonstrações acadêmicas.  
- Permite evolução futura para algoritmos mais avançados.

---
# 3. Dados

Verdadeiros Positivos (VP) = 348 
Falsos Positivos (FP) = 1
Falsos Negativos (FN) = 153
Verdadeiros Negativos (VN) = 19

Acurácia
0,704 (~70,4%)
Sensibilidade / Recall
0,695 (~69,5%)
Especificidade
0,95 (95%)
Precisão
0,997 (~99,7%)
F1-Score
0,818 (~81,8%)



