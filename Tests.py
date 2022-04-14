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
    print("Cycle : ", hierarchy(G, ranks))

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
    print("Chain : ", hierarchy(G, ranks))

def test_fig_two_a():
    G = nx.DiGraph()
    edges =[
        (1, 2),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 3),
        (6, 5)
    ]

    G.add_edges_from(edges)
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print("Figure Two on the Right h(G) = ", hierarchy(G, ranks))

def test_fig_two_b():
    G = nx.DiGraph()
    edges =[
        (1, 2),
        (3, 2),
        (2, 6),
        (4, 3),
        (5, 3),
        (6, 5)
    ]
    G.add_edges_from(edges)
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print("Figure Two on the Left h(G) = ", hierarchy(G, ranks))

def test_collection_of_cycles():
    G = nx.DiGraph()
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 1),
        (7, 8),
        (8, 3),
        (3, 9),
        (9, 7),
        (9, 4),
        (4, 10),
        (10, 6),
        (6, 9)
    ]

    G.add_edges_from(edges)
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print("Collection of cycles h(G)=", hierarchy(G, ranks))

def test_tree():
    G = nx.DiGraph()
    edges = [
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 3),
        (6, 3),
        (7, 6),
        (8, 6),
        (9, 4),
        (10, 4),
        (11, 4),
        (12, 4)
    ]
    G.add_edges_from(edges)
    g, DAG, H = max_euler_subgraph(G)
    ranks, agonies = agony_label(g, DAG, H)
    print("Tree h(G)=", hierarchy(G, ranks))
