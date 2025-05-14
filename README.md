
# Aplicação do Algoritmo de Kruskal para Otimização de Sistemas Elétricos de Potência

Este projeto apresenta a implementação do algoritmo de **Kruskal** para encontrar a **árvore geradora mínima (MST)** em um sistema elétrico de potência modelado como um grafo. O objetivo é minimizar o custo total de conexão entre barras (subestações ou cidades), representado pelas linhas de transmissão com pesos associados.

## 📌 Objetivos

* Modelar um sistema elétrico como um grafo ponderado não direcionado.
* Aplicar o algoritmo de Kruskal para obter a árvore geradora mínima.
* Visualizar graficamente o sistema elétrico original e a solução ótima.
* Demonstrar o uso de estruturas de dados eficientes como Union-Find com compressão de caminho e união por rank.

## 📂 Estrutura

* `UnionFind`: Classe auxiliar que implementa a estrutura de conjuntos disjuntos.
* `kruskal`: Função que executa o algoritmo de Kruskal.
* `plot_graph_and_mst`: Função para visualização do grafo original e da MST.
* `main`: Define os vértices e arestas do sistema elétrico e executa a simulação.

## ⚙️ Dependências

Certifique-se de ter o Python 3 instalado. Instale as bibliotecas necessárias com:

```bash
pip install networkx matplotlib
```

## ▶️ Como Executar

Salve o código como `kruskal_power_system.py` e execute:

```bash
python main.py
```

A saída exibirá no terminal as arestas da árvore geradora mínima, e serão mostrados dois gráficos:

* O grafo original do sistema elétrico.
* A árvore geradora mínima em destaque.

## 📊 Exemplo de Saída

```text
Arestas da árvore geradora mínima:
Aresta (6, 7) com peso 1
Aresta (5, 6) com peso 2
Aresta (4, 6) com peso 3
Aresta (4, 5) com peso 4
Aresta (1, 2) com peso 5
Aresta (2, 3) com peso 6
Aresta (0, 2) com peso 8
```

## 🧠 Conceitos Envolvidos

* **Grafos ponderados não direcionados**
* **Árvore geradora mínima**
* **Algoritmo guloso (Kruskal)**
* **Estrutura Union-Find com path compression**

## 📘 Referências

* CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. *Algoritmos: Teoria e Prática*. 4ª ed. Rio de Janeiro: Elsevier, 2022.
* OLIVEIRA, L. D. *Estruturas de Dados em Python*. São Paulo: Novatec, 2021.

---

