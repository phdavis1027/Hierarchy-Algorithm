import networkx as nx

def max_euler_subgraph(G):
    g = G.copy()
    for edge in g.edges(): # assign every edge a weight of -1
        g[edge[0]][edge[1]]['weight'] = -1 
    try: 
        while True:
            c = nx.find_cycle(g) # get some cycle
            if is_neg_cycle(c, g):
                invert_edge_weights(c, g)
                reverse_edge_directions(c, g)
            return
    except nx.NetworkXNoCycle:
        pass

def is_neg_cycle(c, g):
    sum = 0
    for e in c:
        source, target = e
        sum += g.get_edge_data(source, target)['weight']
    return sum < 0

def invert_edge_weights(c, g):
    for e in c:
        source, target = e
        g[source][target]['weight'] = -g[source][target]['weight']

def reverse_edge_directions(c, g):
    pass