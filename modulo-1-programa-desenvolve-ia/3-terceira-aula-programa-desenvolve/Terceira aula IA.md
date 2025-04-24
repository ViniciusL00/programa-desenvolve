# 🤖 Revisão da Terceira Aula: Inteligência Artificial (IA)

## 💡 Como a Inteligência Artificial Aprende?

A IA pode aprender a partir de:

- **Vídeos**
- **Áudios**
- **Imagens**
- **Pesquisas (dados textuais ou numéricos)**

Esses dados são **transformados em números**, que são processados por redes neurais. Após o processamento, os **números resultantes** são convertidos novamente em:

- Textos
- Imagens
- Áudios
- Vídeos

> 💬 **Exemplo**: Quando você pede para uma IA descrever uma imagem, ela transforma essa imagem em dados numéricos, processa com a rede neural, e devolve uma descrição textual com base nesses dados.

---

## 🧠 Tipos de Aprendizado de Máquina

### 1. Aprendizado Supervisionado

- A IA **recebe dados com respostas certas** (rótulos).
- Ela aprende a **prever ou classificar** com base nesses exemplos.

> 📌 **Exemplo**: Treinar uma IA para reconhecer se uma imagem é de um gato ou um cachorro, usando imagens que já estão rotuladas.

---

### 2. Aprendizado Não Supervisionado

- A IA **não recebe rótulos** nos dados.
- Ela tenta encontrar **padrões ou agrupamentos** sozinha.

> 📌 **Exemplo**: Agrupar clientes com comportamento de compra semelhante sem saber quem são.

---

### 3. Aprendizado por Reforço

- A IA **observa o ambiente**, **toma ações** e **recebe recompensas ou penalidades** com base nos resultados.
- Ela **ajusta sua política de ação** com base nessas experiências, melhorando a performance com o tempo.

#### Ciclo do Aprendizado por Reforço:

1. Observar o ambiente  
2. Selecionar uma ação com base em uma política  
3. Executar a ação  
4. Obter recompensa ou penalidade  
5. Atualizar a política (aprendizado)  
6. Repetir até aprender

> 🎮 **Exemplo**: Um agente IA jogando xadrez aprende com cada partida que joga, ganhando ou perdendo pontos.

---

### 4. Classificação vs Clustering

| Conceito       | Definição                                                                 | Exemplo                                 |
|----------------|---------------------------------------------------------------------------|-----------------------------------------|
| **Classificação** | Atribui categorias a novos dados com base em dados rotulados.             | Identificar se um e-mail é spam ou não. |
| **Clustering**     | Agrupa dados semelhantes sem usar rótulos prévios.                        | Agrupar músicas por estilo sem saber o gênero. |