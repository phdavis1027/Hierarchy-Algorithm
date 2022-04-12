import networkx as nx
from Algo import(
    max_euler_subgraph
)

def main():
    G = nx.DiGraph()
    nodes = [i for i in range(6)]
    edges = [(5, 1)]
    for i,v in enumerate(nodes[:(len(nodes) - 1)]):
        edges.append((v, nodes[i + 1]))
    G.add_edges_from(edges) # we now have a cycle graph as depicted 
                            # on page 559 of the paper that introduces
                            # this algo
    max_euler_subgraph(G) 


if __name__ == '__main__':
    main()