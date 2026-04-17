"""
This file implements functions relevant to chordal graphs.
"""

import networkx as nx
import itertools

def get_next_vertex_greedily(G:nx.Graph,visited_vertices: list,frontier: list[list]):
    """
    Args:
        G is a Graph.
        visited_vertices is a list of vertices that have been visited.
        The frontier is a list of pairs [v, i], where v is an unvisited vertex and i is the number of visited neighbors.
    Returns:
        The next vertex added to the visited list.
    Side-Effects:
        Modifies visited_vertices by adding the next vertex.
        Modifies frontier.
    """
    if len(frontier)==0:
        return
    frontier.sort(key= lambda x: x[1])
    next_vertex, _ = frontier.pop()
    visited_vertices.append(next_vertex)
    neighbors = [ n for n in G.neighbors(next_vertex) if n not in visited_vertices]
    for f in frontier:
        vertex, num_neighbors = f
        if G.has_edge(vertex,next_vertex):
            f[1]+=1
            neighbors.remove(vertex)
    frontier.extend([[n,1] for n in neighbors])

    return next_vertex

def get_chordal_order(G:nx.Graph) -> list:
    """
    Args:
        G is a graph, assumed to be chordal
    Returns:
        A list of the nodes of G.
        They are ordered so that each vertex's neigbors that preceed it form a clique of G.
    """
    vertex = next(iter(G.nodes))
    visited_vertices = []
    frontier = [[vertex,1]]
    while vertex is not None:
        vertex = get_next_vertex_greedily(G,visited_vertices, frontier)
    return visited_vertices
def get_chordal_completion(G:nx.Graph) -> nx.Graph:
    """
    Args:
        G is a graph.
    Returns: 
        the chordal completion of G,
        i.e. a copy of G with extra edges to make it chordal.
    Hint1: 
        Which edges need to be added to G if check_chordal_order(G) is to return True?
    Hint2:
        Loop through the vertices in the reverse of get_chordal_order.
        Add edges to make sure that each time a vertex is processed, 
            its previous (in the original order) neighbors form a clique.
    Note:
        It is possible to implement this function so that it correctly returns a chordal completion,
        but adds too many edges and will cause the dynamic program to be unnacceptably inefficient.
    """
    H = G.copy()
    #TODO: Complete this function ~5 lines
    return H

def is_subclique(G:nx.Graph, nodelist:list) -> bool:
    """
    Input: G, a network x graph
           nodelist, a list of nodes
    Returns:
        True or False, depending on whether nodelist is a clique
    Source:
    https://stackoverflow.com/questions/59009712/fastest-way-of-checking-if-a-subgraph-is-a-clique-in-networkx
    """
    H = G.subgraph(nodelist)
    n = len(nodelist)
    return H.size() == n*(n-1)/2

def check_chordal_order(G:nx.Graph, chordal_order:list)-> bool:
    """
    Inputs:
        G: a nx.Graph
        chordal_order: a list of vertices of G in the order
                        so that, for each vertex v, 
                        the neighbors of v that appear before v form a clique.
    Returns:
        True if the graph is chordal. False otherwise.
    """
    #TODO: implement this function ~5 lines
    return True
def check_chordal(G:nx.Graph) -> bool:
    """
    Args:
        G is a NetworkX graph
    Returns:
        True or False, depending on whether the graph is chordal.
    """
    return check_chordal_order(G,get_chordal_order(G))
