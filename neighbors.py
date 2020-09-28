import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 3), (1, 8), (1, 4),
                  (3, 5), (3, 7), (8, 2), (8, 9), (4, 9),
                  (9, 6)])

neighbors_list = [[1, 2, 6], [0, 3, 5], [2, 3], [3], [2], [0]]
visited = [False] * neighbors_list.__len__()
print(visited)


def DFS(neighbors_list, visited, top):
    visited[top] = True
    print(top)
    neighbors = neighbors_list[top]
    for x in neighbors:
        if not visited[x]:
            DFS(neighbors_list, visited, x)


DFS(neighbors_list, visited, 5)
