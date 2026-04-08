from unittest import TestCase
from optimal_matching_solution import *
from kruskal_solution import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

#setup graph: random choice. Keep this consistent.
random.seed(50)
#---Example Gs: I got these from running the function generate_graph.

class TestsOfStarterCode(TestCase):


    G_5_10_2 = {'w0': ['j5', 'j3'], 'w1': ['j2', 'j0'], 'w2': ['j1', 'j4'], 'w3': ['j7', 'j9'], 'w4': ['j8', 'j6'], 'j0': ['w1'], 'j1': ['w2'], 'j2': ['w1'], 'j3': ['w0'], 'j4': ['w2'], 'j5': ['w0'], 'j6': ['w4'], 'j7': ['w3'], 'j8': ['w4'], 'j9': ['w3']}
    G_5_10_4 = {'w0': ['j7', 'j1', 'j4', 'j8'], 'w1': ['j7', 'j9', 'j0', 'j3'], 'w2': ['j1', 'j6', 'j3', 'j5'], 'w3': ['j0', 'j7', 'j9', 'j6'], 'w4': ['j3', 'j2', 'j1', 'j0'], 'j0': ['w1', 'w3', 'w4'], 'j1': ['w0', 'w2', 'w4'], 'j2': ['w4'], 'j3': ['w1', 'w2', 'w4'], 'j4': ['w0'], 'j5': ['w2'], 'j6': ['w2', 'w3'], 'j7': ['w0', 'w1', 'w3'], 'j8': ['w0'], 'j9': ['w1', 'w3']}
    G_5_15_5 = {'w0': ['j10', 'j12', 'j6', 'j13', 'j9'], 'w1': ['j7', 'j6', 'j14', 'j12', 'j0'], 'w2': ['j1', 'j3', 'j2', 'j7', 'j11'], 'w3': ['j8', 'j9', 'j5', 'j7', 'j3'], 'w4': ['j0', 'j4', 'j14', 'j8', 'j10'], 'j0': ['w1', 'w4'], 'j1': ['w2'], 'j2': ['w2'], 'j3': ['w2', 'w3'], 'j4': ['w4'], 'j5': ['w3'], 'j6': ['w0', 'w1'], 'j7': ['w1', 'w2', 'w3'], 'j8': ['w3', 'w4'], 'j9': ['w0', 'w3'], 'j10': ['w0', 'w4'], 'j11': ['w2'], 'j12': ['w0', 'w1'], 'j13': ['w0'], 'j14': ['w1', 'w4']}
    example_graphs = [(5, 10, G_5_10_2, 28), (5,10, G_5_10_4, 33), (5, 15, G_5_15_5, 57)]

    @number('1')
    @weight(10)
    @visibility('visible')
    def test_kruskal(self):
        G = create_edge_weighted_graph(50)
        print(G.edges())
        spanning_tree_edges = kruskal_algorithm(G) #Calls your code to find the edges of a minimal spanning tree
        spanning_tree_weight = int(sum(G[u][v]['weight'] for u,v in spanning_tree_edges))
        
        H=nx.Graph()
        H.add_nodes_from(G.nodes)
        H.add_edges_from(spanning_tree_edges) #H is a new graph whose nodes are those of G and edges are the spanning tree edges.
        assert spanning_tree_edges == sorted(spanning_tree_edges, key= lambda e: G[e[0]][e[1]]['weight'])
        assert nx.is_tree(H)
        assert spanning_tree_weight == 332
    @number('2')
    @weight(15)
    @visibility('visible')
    def test_optimal_workers(self):
        for W_size,J_size,G,opt_val in type(self).example_graphs:
            W = ['w'+str(i) for i in range(W_size)]
            J = ['j'+str(i) for i in range(J_size)]
            jobs, matches = get_maximal_matched_jobs(W,J,G)#This calls your code to get the maximum valued jobs.
            assert set(jobs)==set([m[1] for m in matches]) #Check that the jobs are the second coordinate of the edges in matches.
            for edge in matches:
                assert edge[1] in G[edge[0]] #Check that the matches were in the original graph.
            assert len([w for w,j in matches]+[j for w,j in matches])== 2*len(jobs) #check that the total number of vertices in the matches is twice the number of jobs. This ensures that its a matching.
            assert sum([int(j[1:]) for j in jobs]) >= opt_val #Check that the total value of the optimal solution is at least as good as the solution I found.
if __name__=="__main__":
    unittest.main()