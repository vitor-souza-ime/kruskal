import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(len(vertices))
    mst = []
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    return mst

def plot_graph_and_mst(vertices, edges, mst):
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=600, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Sistema Elétrico - Grafo Original")

    plt.subplot(1, 2, 2)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='lightgray', node_size=600, font_weight='bold')
    mst_edges = [(u, v) for u, v, _ in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Árvore Geradora Mínima (MST)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    vertices = list(range(8))  # Barras 0 a 7

    # Linhas de transmissão entre barras (u, v, impedância/custo)
    edges = [
        (0, 1, 10),
        (0, 2, 8),
        (1, 2, 5),
        (1, 3, 7),
        (2, 3, 6),
        (2, 4, 9),
        (3, 5, 11),
        (4, 5, 4),
        (4, 6, 3),
        (5, 6, 2),
        (5, 7, 12),
        (6, 7, 1)
    ]

    mst = kruskal(vertices, edges)
    print("Arestas da árvore geradora mínima:")
    for u, v, weight in mst:
        print(f"Aresta ({u}, {v}) com peso {weight}")

    plot_graph_and_mst(vertices, edges, mst)
