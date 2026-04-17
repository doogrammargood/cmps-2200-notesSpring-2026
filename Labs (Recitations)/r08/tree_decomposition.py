from chordal_graphs_solution import *
from graph_examples import *
import matplotlib.pyplot as plt


class TreeDecomposition(object):
    """
    This class represents the tree decomposition of a graph.
    See Chapter 7 of Parameterized Algorithms by Cygan et al. 
    https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf

    Page numbers in this document refer to the page numbers of Cygan's book.

    Note: We do not force the tree decomposition axioms- we only check them.
    """
    def __init__(self, G:nx.Graph, T:nx.Graph, H:dict) -> None:
        """
        Args:
            G is the original graph, assumed to be simple.
            T is the tree of the tree decomposition.
            H is a dictionary whose keys are vertices of G and T.
                The values are lists of vertices of the other graph.
        Returns:
            None
        Note: When is a node of T, elements of H[t] are called "bags."
        """

        self.G=G
        self.T=T
        self.H=H

    def _next_gnode_name(self) -> str:
        """
        Returns a name for a self.G node that is unused.
        """
        count = 1
        while 'G'+str(count) in self.G.nodes:
            count += 1
        return 'G'+str(count)
    def _next_tnode_name(self) -> str:
        """
        Returns a name for a self.T node that is unused.
        """
        count = 1
        while 'X' + str(count) in self.T.nodes:
            count += 1
        return 'X'+str(count)
    
    def check_tree_decomposition(self) -> bool:
        """
        Verifies that the tree decomposition satisfies the axioms T1,T2,T3. 
        See the tree decomposition concept from the Readme, or page 160 of Cygan, or the Wikipedia article on tree decompositions.
        """
        #First, check that the vertices of G and T are disjoint.
        if len([n for n in self.G.nodes() if n in self.T.nodes()]) >0:
            assert False
        #Check that whenever a vertex is in a bag, the corresponding bag has that vertex.
        for v in self.G.nodes():
            for t in self.H[v]:
                assert v in self.H[t]
        #Check that whenever a bag contains a vertex, that vertex is in the corresponding bag.
        for t in self.T.nodes():
            for v in self.H[t]:
                assert t in self.H[v]

        #check that T is a tree
        if not nx.is_tree(self.T):
            return False
        #Axiom 1: every vertex of G is in a bag.
        for v in self.G.nodes():
            if len(self.H[v])==0:
                return False
        #Axiom 2: every edge of G is in a bag.
        for u,v in self.G.edges():
            if len([t for t in self.H[v] if u in self.H[t]])==0:
                return False
        #Axiom 3: For each vertex v of G, the set of bags containing v forms a subtree of T.
        for v in self.G.nodes():
            #TODO: Complete this function ~3 lines
            pass
        return True
    
    def treewidth(self) -> int:
        """
        Args:
            None
        Returns:
            The treewidth, which is one less than the size of the largest bag.
        """
        return max([len(self.H[t]) for t in self.T.nodes])-1
    def add_bag(self, new_bag:tuple, neighbor) -> None:
        """
        Args:
            new_bag is a tuple of vertices to be a new bag.
            neighbor is a node of T or None
        Returns:
            None
        Side-Effect:
            Adds a new node to self.T.
            Updates self.H so that the new node is associated with new_bag
        """
        new_tnode = self._next_tnode_name()
        self.T.add_node(new_tnode)
        if neighbor is not None:
            self.T.add_edge(new_tnode, neighbor)
        self.H[new_tnode] = list(new_bag)
        for vertex in new_bag:
            self.H[vertex].append(new_tnode)
    def add_vertex_to_bag(self, vertex, t_node) -> None:
        """
        Args:
            vertex is a vertex of self.G,
            t_node is a vertex of self.T.
        Returns:
            None
        Side-Effects:
            Updates self.H so that the bag of t_node contains vertex.
        """
        self.H[t_node].append(vertex)
        if vertex in self.H:
            self.H[vertex].append(t_node)
        else:
            self.H[vertex]=[t_node]

    def tree_decomposition_of_subgraph(self, S:nx.Graph) -> "TreeDecomposition":
        """
        Args: 
            S is a subgraph of self.G with the same node set.
        Returns:
            The TreeDecomposition obtained by restricting self.G to S.
        """
        Hp = {v : self.H[v] for v in S.nodes} | {t : [v for v in self.H[t] if v in S.nodes] for t in self.T.nodes}
        return TreeDecomposition(S,self.T,Hp)
    @classmethod
    def tree_decomposition_of_chordal_graph(self, G:nx.Graph) -> "TreeDecomposition":
        """
        Args: 
            G is a chordal graph. 
        Returns:
            a TreeDecomposition of G.
        Implementation:
            Loop through the chordal order.
            For each vertex v, 
                1. if its previous neighbors are exactly an existing bag, then add v to that bag.
                2. Otherwise, there exists a bag that contains all of v's previous (in the chordal order) neighbors.
                    In this case, we create a new node of T whose bag is v and its previous neigbors.
                        and create an edge between the new node 
                                       and an existing node of T 
                                       whose bag contains v's previous neighbors.
            Note: In case 2, there may be a choice of how to attach the next node to the T. 
                  Any choice works.
        """
        chordal_order = get_chordal_order(G)
        TD = TreeDecomposition(G, nx.Graph(), {n:[] for n in G.nodes})
        for index, cur_node in enumerate(chordal_order):
            previous_neighbors = [n for n in G.neighbors(cur_node) 
                                  if n in chordal_order[:index]]
            if index == 0:
                TD.add_bag((cur_node,),None)
            else:
                #TODO: Complete this function ~6 lines
                pass
        return TD

if __name__=="__main__":
    print("main")