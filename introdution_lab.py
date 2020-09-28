import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()                             #Tworzy graf
G.add_nodes_from([2, 3, 1])                 #nodes - tworzy punkty
G.add_nodes_from("ABC")
G.add_edges_from([(1, 'A'), ('A', 2),       #edges tworzy połączenia
                  (2, 'B'), ('B', 3),
                  (3, 'C')])
nx.draw(G, with_labels=True)                # rysuje graf
plt.show()
