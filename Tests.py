import networkx as nx
from Algo import (
    max_euler_subgraph,
    agony_label,
    hierarchy
)

def test_cycle():
    G = nx.DiGraph()
    nodes = [i for i in range(6)]
    edges = [(5, 0)]
    for i,v in enumerate(nodes[:(len(nodes) - 1)]):
        edges.append((v, nodes[i + 1]))
    G.add_edges_from(edges) # we now have a cycle graph as depicted 
                            # on page 559 of the paper that introduces
                            # this algo
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print(hierarchy(G, ranks))

def test_chain():
    G = nx.DiGraph()
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4)
    ]

    G.add_edges_from(edges)  # this is the chain graph from that same page of the paper
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print(hierarchy(G, ranks))