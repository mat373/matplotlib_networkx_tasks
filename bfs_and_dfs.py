import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 0), (0, 6), (0, 2),
                  (2, 5), (2, 3), (3, 4)])

F = nx.DiGraph([(0, 1), (3, 2), (0, 2), (5, 4), (4, 0), (4, 3),
                (1, 5), (7, 2), (6, 3), (5, 7), (7, 0), (5, 6)])

# nx.draw(F, with_labels=True)

A = nx.Graph()
A.add_edges_from([(1, 3), (1, 8), (1, 4),
                  (3, 5), (3, 7), (8, 2), (8, 9), (4, 9),
                  (9, 6)])


# nx.draw(A, with_labels=True)


def bfs(graph: nx.Graph):
    for x in range(1, graph.number_of_nodes()):
        bfslista = list(nx.bfs_tree(graph, 1))
        if bfslista.len() == graph.number_of_nodes():
            return True
    return False


def dfs(graph: nx.DiGraph):
    for i in graph.nodes:
        dfslist = list(nx.dfs_postorder_nodes(graph, i))
        if dfslist.__len__() == graph.number_of_nodes():
            print("started from: {}, dfs sort is: {}".format(i, dfslist))


def my_bfs(graph: nx.Graph(), start_node: nx.Graph.nodes):
    bfs_list = []
    queue = []
    visited = []

    queue.insert(0, start_node)
    visited.append(start_node)
    bfs_list.append(start_node)

    while queue.__len__() > 0:
        top = queue.pop(0)
        adjList = list(graph.adj.get(top))

        for i in adjList:
            if not visited.__contains__(i):
                visited.append(i)
                bfs_list.append(i)
                queue.append(i)
    return bfs_list


print("bfs: ", list(nx.bfs_tree(A, 4)))
print("my bfs: ", list(my_bfs(A, 1)))
plt.show()

