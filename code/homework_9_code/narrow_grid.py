"""
This file contains code to check your solution to the narrow grid problem.
See 7.1 of Cygan et al's Parameterized Algorithms.
"""
import networkx as nx
import random
import matplotlib.pyplot as plt
import itertools
import math
random.seed(108)
def create_grid(k:int, N:int, vertex_param:float = 0.9, edge_param:float = 0.9):
    """
    args:
        k is an integer that is the height of the graph.
        N is the width of the graph. Assume N>>k.
        We start from a kxN grid graph and remove vertices and edges.
        vertex_param is the probability of keeping a vertex.
        edge_param is the probability of keeping an edge.
    Returns:
        a subgraph of the grid graph, chosen randomly.
    """
    grid_graph = nx.grid_graph((k,N))
    vertices_to_keep = [ node for node in grid_graph.nodes if random.random() <= vertex_param]
    induced_subgraph = grid_graph.subgraph(vertices_to_keep).copy()
    for edge in induced_subgraph.edges():
        if random.random() >= edge_param:
            induced_subgraph.remove_edge(edge[0],edge[1])
    return induced_subgraph

#Now we define some helper functions.

def is_independent(j:int,S:tuple[int],G:nx.Graph):
    """
    Args:
        j is the index of a collumn of G
        S is a sorted tuple of row-coordinates.
        G is a subgraph of the grid graph.
    Returns True if the vertices of the form (j,s) for s in S are independent in G.
    Note: if any vertex of the form (j,s) is not in the graph, then it returns False.
    """
    if any([(j,s) not in G.nodes for s in S]):
        return False
    else:
        return len(G.subgraph([(j,s) for s in S]).edges())==0
def get_prev_neighbors(j:int, S:tuple[int],G:nx.Graph):
    """
    Args:
        j is the index of a column of G.
        S is a sorted tuple of row-coordinates in that column.
        G is a subgraph of the grid graph.
    Returns a sorte tuple of the neighbors of the verices (j,s) in the column j.
    """
    return tuple(sorted([n[1] for s in S for n in G.neighbors((j,s)) if n[0]==j-1 ]))

#create the table.
def independent_set_for_narrow_grid(G:nx.Graph, k:int, N:int) -> dict:
    """
    Input: G is a subgraph of a narrow grid graph.
        k and N are the dimensions of the grid graph.
        In particular, we assume that vertices are named by pairs of integers (x,y)
    Returns: a table c[j][Y], where j is a column number and Y is a subset of the rows, represented as a sorted tuple.
    We store the table as a dictionary of dictionaries.
    The entry c[j][Y] contains the size of the maximal independent set of the first j columns after Y is removed, 
    """
    
    c = {}
    Ys = [list(itertools.combinations(range(k), r)) for r in range(k + 1)]  
    Ys = [tuple(set(sorted(list(sublist)))) for g in Ys for sublist in g] # a list of all values for the subset Y.
    
    for j in range(N):
        for Y in Ys:
            #TODO: fill in the table. ~6 lines
            pass
    return c

def recover_independent_set_from_table(c:dict,k:int,N:int)->list[tuple[int]]:
    """
    Input: c is a table (dictionary of dictionaries of ints), 
           k and N are integers that are the dimensions of the grid graph.
    Returns a list of vertices in a largest independent set. Each vertex is a pair of integers.
    """
    j = N-1
    Y = []
    independent_set = []

    #TODO: Backtrack to get the independent set. ~9 lines.
    return independent_set

if __name__=="__main__":

    k=5
    N=20

    G = create_grid(5,20)
    c = independent_set_for_narrow_grid(G,k,N) #Defines a dictionary

    independent_set = recover_independent_set_from_table(c,k,N)
    assert len(G.subgraph(independent_set).edges)==0
    #networkx provides a function that finds a large independent set. 
    #But independent set may not be maximum, so it is only a lower bound on the independence number.
    lower_bound = len(nx.approximation.maximum_independent_set(G))
    print(lower_bound, len(independent_set))
    assert lower_bound <= len(independent_set)
    assert len(independent_set) == c[N-1][()]

    pos = {(x, y): (x, -y) for x, y in G.nodes()}
    nx.draw(G, pos=pos, with_labels=True)
    plt.show()