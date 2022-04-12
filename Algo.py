import networkx as nx

def max_euler_subgraph(G):
    g = G.copy()
    for f, t in g.edges(): # assign every edge a weight of -1
        g[f][t]['weight'] = -1 
    done = False
    while not done:
        done = True
        cycles = nx.simple_cycles(g)
        for c in cycles:
            if is_neg_cycle(c):
                done = False
                invert_edge_weights(c, g)
                reverse_edge_directions(c, g)
                break
    
    neg_edges = []
    pos_edges = []
    for t, f in g.edges():
        if g.get_edge_data(t,f)['weight'] == -1:
            neg_edges.append((t,f))
        else:
            pos_edges.append((t,f))
    

    DAG = nx.DiGraph()
    DAG.add_edges_from(neg_edges)

    H = nx.DiGraph()
    H.add_edges_from(pos_edges)
    for t, f in H.edges():
        H[t][f]['weight'] = 1 # gotta re-weight the edges since they were lost 
                              # in translation
    edges = list(H.edges())
    reverse_edge_directions(edges, H)


    return g, DAG, H

def agony_label(g, DAG, H):
    output = {}
    ranks = {node : 0 for node in g.nodes()}
    nx.set_node_attributes(g, ranks, 'rank') # set every node's rank to zero
    weights = nx.get_edge_attributes(g, 'weight')
    done = False
    while not done:
        for u, v in g.edges():
            if label_compare(u, v, g, weights):
                print(g.nodes[v]['rank'], " < ", g.nodes[u]['rank'], " - ", weights[u, v])
                done = False
                g.nodes[v]['rank'] = g.nodes[u]['rank'] - weights[u, v]
                break
            else: done = True
    print({n : g.nodes[n]['rank'] for n in g.nodes})
    '''
    for u, v in DAG.edges():
        output[u,v] = 0
    for u, v in H.edges():
        output[u,v] = g.nodes[u]['rank'] - g.nodes[v]['rank'] + 1
    '''
    
    return output

def label_compare(u, v, g, weights):
    return g.nodes[v]['rank'] < g.nodes[u]['rank'] - weights[u, v]
    

def is_neg_cycle(c, g):
    sum = 0
    for source, target in c:
        sum += g.get_edge_data(source, target)['weight']
    return sum < 0

def invert_edge_weights(c, g):
    for source, target in c:
        g[source][target]['weight'] = -g[source][target]['weight']

def reverse_edge_directions(c, g):
    for source, target in c:
        weight = g.get_edge_data(source, target)['weight']
        g.remove_edge(source, target)
        g.add_edge(target, source)
        g[target][source]['weight'] = weight