import networkx as nx



def pyt2():
    G = nx.Graph()
    G.add_edges_from(['AB', 'AE', 'BC', 'BE', 'CD', 'CE', 'DE'])
    nx.draw(G, with_labels=True)

    max = 0
    wierzcholek = G.nodes.get(0)

    for i in G.nodes:
        print(i, "-> ", G.degree(i))
        if G.degree(i) > max:
            max = G.degree(i)
            wierzcholek = i

    print("wierzcholek z najwyzsza liczba  to: {},  stopien tego wieszchołka to: {} ".format(wierzcholek, max))

pyt2()

