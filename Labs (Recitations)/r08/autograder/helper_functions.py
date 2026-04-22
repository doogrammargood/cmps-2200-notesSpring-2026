"""
This file contains two functions that will be used to calculate the independence number via the tree decomposition.
Both functions were studied earlier in this course.
"""

import itertools
import networkx as nx
def list_independent_sets_brute_force(G):
    '''
    Implements the brute force solution, which tests all subsets of vertices.
    Returns a list of independent sets. Each independent set is a tuple.
    Note: modified from Lab 4.
    '''
    solutions = []
    if len(G.nodes)==0:
        return solutions
    else:
        for r in range(len(G.nodes)+1):
            potential_independent_vertices_of_size_r = itertools.combinations(G.nodes,r)
            for potential_independent_vertices in potential_independent_vertices_of_size_r:
                is_independent = True
                for pair in itertools.combinations(potential_independent_vertices,2):
                    x,y = pair
                    if G.has_edge(x,y):
                        is_independent = False
                if is_independent:
                    solutions.append(potential_independent_vertices)
    return solutions

def depth_first_search(G:nx.Graph, start_node):
    '''
    Args: 
        G, a graph
        start_node: a node to start the search from
    Returns: 
        An ordering of the vertices as they are encountered in depth-first order.
    Note: copied from earlier in the course
    '''
    current_node = start_node
    next_node = None
    current_chain = []
    visited_nodes = [start_node] #These are the nodes that we have visited.
    while True:
        while len([node for node in G.neighbors(current_node) if not node in visited_nodes]) > 0:
            next_node = [node for node in G.neighbors(current_node) if not node in visited_nodes][0]
            visited_nodes.append(next_node)
            current_chain.append(current_node)
            current_node = next_node
        if len(current_chain)>0:
            current_node = current_chain.pop()
        else:
            break
    return visited_nodes