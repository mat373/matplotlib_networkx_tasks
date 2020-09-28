import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edge(1, 2)
G.add_edges_from([(1, 2), (1, 3)])

G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(list(G.edges))
for n in G:
    print(list(G.adj[n]))
print('-------------------------------------')
for n in G:
    print(list(G.degree([n])))

