"""
This file contains examples of tree decompositions.
"""

from tree_decomposition_solution import *
def example_tree_decomposition():
    """
    This function implements the example from page 158.
    """
    G = nx.Graph()
    G.add_nodes_from(['a','b','c','d','e','f','g','h','i'])
    G.add_edges_from([('a','b'),
                      ('a','c'),
                      ('b','c'), 
                      ('b','e'), 
                      ('b','d'),
                      ('c','d'),
                      ('c','e'),
                      ('d','e'), 
                      ('d','f'),
                      ('d','g'),
                      ('d','h'),
                      ('e','g'),
                      ('e','h'),
                      ('e','i'),
                      ('f','g'),
                      ('h','i')])
    T = nx.Graph()
    T.add_nodes_from(['X1','X2','X3','X4','X5'])
    T.add_edges_from([('X1','X2'),
                      ('X2','X3'),
                      ('X3','X4'),
                      ('X4','X5')])
    
    H={}
    H['X1'] = ['a','b','c']
    H['X2'] = ['b','e','d','c']
    H['X3'] = ['d','e','f','g']
    H['X4'] = ['d','e','h']
    H['X5'] = ['i','e','h']

    for v in G.nodes():
        H[v]=[]

    for t in H:
        if t in T.nodes:
            for v in H[t]:
                H[v].append(t)

    tree_decomposition = TreeDecomposition(G,T,H)
    return tree_decomposition