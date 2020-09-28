import networkx as nx
import matplotlib.pyplot as plt

F = nx.DiGraph([(0, 1), (4, 2), (0, 2), (5, 4), (4, 0), (4, 3),
                (1, 5), (7, 2), (6, 3), (5, 7), (7, 0), (5, 6)])


def sort(g: nx.DiGraph):
    if g.number_of_nodes() >= 7:
        nx.draw(g, with_labels=True)
        plt.show()
    print(list(nx.topological_sort(g)))

def my_top_sort(G: nx.DiGraph):
    if nx.is_directed_acyclic_graph(G):
        sorted_list = []
        while G.nodes:
            for i in G.nodes:
                if G.in_degree(i) == 0:
                    sorted_list.append(i)
                    G.remove_node(1)
                    break
        return sorted_list
    else:
        return "acyclic or no directed"