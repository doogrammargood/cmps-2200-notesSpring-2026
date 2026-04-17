from unittest import TestCase
from chordal_graphs_solution import *
from independence_number_dp_solution import *
import random
import unittest
from example_tree_decomposition import *
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

#setup graph: random choice. Keep this consistent.
random.seed(50)
class TestsOfStarterCode(TestCase):

    @number('1')
    @weight(10)
    @visibility('visible')
    def test_chordal_graphs(self):
        """
        Checks that the chordal completion works.
        """
        G=nx.petersen_graph()
        assert not check_chordal(G)
        G_chordal = get_chordal_completion(G)
        assert check_chordal(G_chordal)
    
    @number('2')
    @weight(10)
    @visibility('visible')
    def test_tree_decomposition(self):
        """
        Checks that the tree decomposition 
        from examples.py is recognized as a correct tree decomposition.
        """
        TD = example_tree_decomposition()
        assert TD.check_tree_decomposition()
    
    @number('3')
    @weight(10)
    @visibility('visible')
    def test_tree_decomposition_chordal(self):
        """
        Checks that you can get the tree decomposition of a chordal graph.
        """
        G=nx.cycle_graph(100)
        G_chordal=get_chordal_completion(G)
        TD = TreeDecomposition.tree_decomposition_of_chordal_graph(G_chordal)
        assert TD.check_tree_decomposition()
        TD2 = TD.tree_decomposition_of_subgraph(G)
        assert TD2.check_tree_decomposition()
        assert TD2.treewidth()==2 #If this fails, your chordal completion may be adding too many edges.
    
    @number('4')
    @weight(20)
    @visibility('visible')
    def test_independent_set(self):
        """
        Checks that our algorithm for the largest independent set is correct
        by showing that its output is really an independent set
        and that the size of this independent set is at least as large as NetworkX's builtin approximation.
        """
        test_graphs = [nx.cycle_graph(15), 
                       nx.petersen_graph(),
                       windowed_path_graph(n=200,m=400,window=7),
                       generate_cactus(300,100),
                       ]
        
        for G in test_graphs:
            G_chordal=get_chordal_completion(G)
            TD = TreeDecomposition.tree_decomposition_of_chordal_graph(G_chordal)
            TD2 = TD.tree_decomposition_of_subgraph(G)
            assert TD2.check_tree_decomposition()
            table=independence_number_table(TD2)
            indep_set = independent_set_from_table(table,TD2)
            assert len(G.subgraph(indep_set).edges()) == 0
            approx_set = nx.approximation.maximum_independent_set(G) #builtin approximation.
            assert len(G.subgraph(approx_set).edges())==0
            lower_bound = len(approx_set)
            assert TD2.G==G
            assert len(table)==len(TD2.T.nodes)
            assert len(indep_set)>=lower_bound
if __name__ == "__main__":
    unittest.main()