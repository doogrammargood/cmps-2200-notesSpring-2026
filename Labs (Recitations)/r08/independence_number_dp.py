"""
This file implements a dynamic program that calculates the independence number from the tree decomposition of a graph.
"""
from tree_decomposition_solution import *
from helper_functions import *

def independent_set_bag_table(TD: "TreeDecomposition") -> dict:
    """
    Args: 
        TD is a tree decomposition of a graph.
    Returns:
        A dictionary whose keys are the nodes of T 
            and whose values are a list of the independent sets TD.G restricted to that bag.
            Each independent set is a sorted tuple of nodes.
    """
    to_return = {}
    for t in TD.T.nodes:
        subgraph = TD.G.subgraph(TD.H[t])
        to_return[t] = list_independent_sets_brute_force(subgraph)
    return to_return

def independence_number_table(TD: "TreeDecomposition") -> int:
    """
    Args:
        TD is a tree decomposition of a graph.
    Returns:
        A table whose keys are nodes of TD.T
                and whose values are dictionaries.
                The inner dictionaries have sorted tuples of vertices as keys and
                integer values. See the inline comment below.
    Note: See page 163 of Cygan et. Al, though we use a different strategy
    Hint: The recursion for table[t][S] comes starting with |S| and also adding:
            for each child tp of t,
            the largest value of table[tp][indep_set]
            where indep_set is an independent set of the bag of tp that agrees with S 
            on the intersection set(TD.H[tp]) & set(TD.H[t]).
            Remember to avoid double-counting on the intersections.
    """

    #Note that the topological order determines the descendants of a node. 
    #Specifically, the descendants of a node t 
    #are the nodes other than t in the connected component 
    #of TD.T restricted to the nodes up to t in the topological order.
    topological_order = depth_first_search(TD.T, list(TD.T.nodes)[0])[::-1]

    independent_sets_of_bags = independent_set_bag_table(TD)
    assert len(topological_order)==len(TD.T.nodes)
    table = {} #The table will be a dictionary of dictionaries
               #table[t][S] will store 
               #    the size of the maximum independent set 
               #    among vertices in the unions of the bags associated with t and its descendants.
               #    such that the intersection with the bag associated with t is exactly S.

    def independent_sets_transfer(t:str,S:tuple,tp:str)-> list[tuple[str]]:
        """
        Args:
            t is a node of TD.T
            S is an independent set of TD.H[t]
            tp is a node of TD.T that is adjacent to t.
        Returns:
            The list of independent sets of TD.H[tp] that
                agree with S on the intersection of TD.H[t] and TD.H[tp].
        """
        common = set(TD.H[t]) & set(TD.H[tp])
        return [X for X in independent_sets_of_bags[tp]
                if (set(X) & common) == (set(S) & common)]

    
    for index, t in enumerate(topological_order):
        previous_neighbors = [n for n in TD.T.neighbors(t) if n in topological_order[:index]]
        table[t]={}
        for S in independent_sets_of_bags[t]:
            value_to_store = len(S) #we will add to this
            for tp in previous_neighbors:
                #TODO:Complete this function ~5 lines
                pass
            table[t][S] = value_to_store
    return table

def number_from_table(table: dict)-> int:
    """
    Args:
        table is the table computed in independence_number_table.
    Returns:
        the independence number from the table.
    Note:
        Relies on the fact that keys of Python dictionaries maintain their insertion order.
    """
    root = list(table)[-1] #last key added should be the root node of the tree decomposition.
    return max([table[root][S] for S in table[root]])

def independent_set_from_table(table: dict,TD:"TreeDecomposition"):
    """
    Args:
        table is a dictionary, (the output of independence_number_table)
        TD is a tree decomposition.
    Returns:
        A maximum independent set of TD.G, according to the table.
    """
    current_independent_set = []
    previously_considered_vertices = []
    independence_number = number_from_table(table)
    for t in list(table)[::-1]:
       #TODO: Complete this function ~15 lines
        pass
            
    assert len(current_independent_set)==independence_number
    return current_independent_set

if __name__== "__main__":
    print("main")