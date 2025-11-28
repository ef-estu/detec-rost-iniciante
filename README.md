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

# 3. Como usar
vai no notebook e aperte em opem colab,
depois pesquise uma imagem de rosto e copie o endereço,
agora coloque o endereço na url,
e agora é só rodar

---

# 4. Resultado do projeto

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
Auc
0,82 (~82%)

---

# 5. Gráficos

<img width="1178" height="1102" alt="baixados (7)" src="https://github.com/user-attachments/assets/4ef25d71-49c7-4d5a-b784-5266d7e834e8" />

Um ponto na curva próximo ao canto superior esquerdo (alto TPR e baixo FPR) representa bom desempenho do modelo


<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/62885835-206b-4e69-a280-9245f9d5f0f4" />

Acurácia:  
Proporção de imagens corretamente classificadas. Útil como medida geral, mas pode ser enganosa se houver desequilíbrio entre classes.

Precisão (Precision): 
Indica a confiabilidade do modelo ao detectar um rosto. Baixa precisão significa muitos falsos positivos, ou seja, objetos confundidos com rostos.

Recall (Sensibilidade): 
Mede a capacidade do modelo de não deixar de identificar rostos. Criticamente importante, pois falsos negativos podem comprometer a função de segurança.

F1-Score: 
Balanceia precisão e recall, fornecendo uma métrica composta crucial quando existe um trade-off entre detectar todos os rostos e evitar falsos positivos.

Especificidade: 
Indica a habilidade do modelo de não classificar erroneamente objetos como rostos.
