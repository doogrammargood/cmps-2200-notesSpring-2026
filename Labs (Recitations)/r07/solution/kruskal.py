"""
Rename this file as kruskal_solution.py
This file implements Kruskal's algorithm.
Goals:
    - To have an example of a greedy algorithm to compare to the optimal matching algorithm.
    - To demonstrate the naive implementation of the union/find data structure.
Gotchas:
    - The algorithm in this file asks for a minimal spanning tree, 
        while the algorithm in optimal_matching returns a maximal set of jobs.
    - To get the weight of an edge between vertices u and v, use G[u][v]['weight'].
Problem setup:
    Given: A graph G with positive edge weights
    Find: A subset of edges that form a spanning tree of G with minimum total weight.
Solution Framework:
    0. Initialize a list of edges current_subforrest, initially empty.
    1. Loop through the edges of G in increasing order of weights.
    2. If the current edge can be added to current_subforrest without creating a cycle with the previous edges,
        then add the edge to the current_subforrest.
        2.1 To check if a job can be added to the current_subforrest without creating a cycle:
            maintain a union/find data structure that records the connected component of each vertex.
        2.2 If an edge is added to the graph, 
            then update the union/find data structure to merge the components that contain the endpoints of the edge.
    3. Return current_subforrest
Data format:

"""
import networkx as nx
import random
import itertools

def create_edge_weighted_graph(num_nodes:int)->nx.Graph:
    """
    Args:
        num_nodes is the number of nodes that will be in the graph.
    Returns:
        A random edge-weighted nx.Graph with num_nodes nodes. Each edges appears with probability 0.5.
        The weights are assigned randomly between 1 and 100.
    """
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from(range(num_nodes))
    # Randomly add edges with weights
    edges = []
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            # Randomly decide whether to add an edge
            if random.random() < 0.5:  # 50% chance
                weight = random.randint(1, 100)  # Weight between 1 and 100
                G.add_edge(i, j, weight=weight, label=str(weight))
    return G
G= create_edge_weighted_graph(10)

class UnionFind(object):
    """
    A naive implementation of the union/find datastructure based on two dictionaries.

    The union-find data structure groups elements into components.
    In our implementation, the components will be represented by integers.
    """
    def __init__(self, elements:list) -> None:
        self.element_dict = {element : i for i, element in enumerate(elements)} #maps elements to components, initially, each different.
        self.component_dict = {i : [element] for i,element in enumerate(elements)} #maps each component to its list of elements
        return
    def find(self, element)-> int:
        """
        Args:
            element is an element of the union-find structure.
        Returns: 
            the component containing element.
        """
        return self.element_dict[element]
    def union(self, comp1:int,comp2:int)->None:
        """
        Args:
            comp1 and comp2 are integers, representing components.
        Returns:
            None
        """

        smaller = min(comp1, comp2)
        larger = max(comp1, comp2)
        for element in self.element_dict:
            if self.element_dict[element] == comp2:
                self.element_dict[element] = comp1
        self.component_dict[smaller]=self.component_dict[smaller] + self.component_dict[larger]
        self.component_dict[larger]=[]
            

def check_if_cycle_is_created(e:tuple, component_information: UnionFind) -> bool:
    """
    Args:
        e is an edge of a graph (a 2-tuple of vertices)
        component_information is a UnionFind object that records the current connected components of the graph.
    Returns:
        True if e joins two different components
        False otherwise
    """
    a,b = e
    return component_information.find(a)==component_information.find(b)
    
def kruskal_algorithm(G):
    """
    Args: 
        G, a networkx graph.
        We assume that G has positive edge weights
    Returns: 
        A sorted list of edges in a minimal spanning tree of G
    """
    U = UnionFind(G.nodes()) #initially, each node is in its own connected component.
    
    current_subforest = []
    considered = []
    sorted_edges = sorted(G.edges(), key=lambda edge: G[edge[0]][edge[1]]['weight'])
    #TODO: Complete the greedy strategy by using the functions provided above. ~7 lines
    pass
