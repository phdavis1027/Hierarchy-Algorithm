import networkx as nx
from Algo import(
    max_euler_subgraph,
    agony_label
)

def main():
    G = nx.DiGraph()
    nodes = [i for i in range(6)]
    edges = [(5, 0)]
    for i,v in enumerate(nodes[:(len(nodes) - 1)]):
        edges.append((v, nodes[i + 1]))
    G.add_edges_from(edges) # we now have a cycle graph as depicted 
                            # on page 559 of the paper that introduces
                            # this algo
    g, DAG, H = max_euler_subgraph(G)
    print(agony_label(g, DAG, H))


if __name__ == '__main__':
    main()