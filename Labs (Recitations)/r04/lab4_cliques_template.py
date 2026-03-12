'''
This file contains starter code for the implementation of an algorithm to list all cliques.

Recall that a clique of a graph is a nonempty set of vertices where every pair of distinct vertices is adjacent.

The algorithm is typically called the Bron-Kerbosch algorithm: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

See readme.md for a description of NetworkX and some helpful functions.

Gotchas: 
- We are listing the nonempty cliques that are not necessarily maximal. Each vertex should appear as a clique. 
- Each clique is represented as a tuple of integers in increasing order.
- We assume that all of the nodes in all of the graphs are unique non-negative integers.


Format of this file:
0.We define a class called CliqueIterable that wraps a NetworkX graph.
1.We implement a brute force algorithm that checks every set of vertices to see if they form a clique.
2.We implement a recursive backtracking algorithm to create a list of all cliques.
3.We define a .__iter__() method and a generator function to make CliqueIterable an iterable.


'''

import networkx as nx
import itertools
import copy
class CliqueIterable(object):
    def __init__(self,graph):
        '''
        Input: graph is a NetworkX graph.
        '''
        self.graph = graph
        self.current_vertices = [] #The current vertices that we are exploring.
    
    def list_cliques_brute_force(self):
        '''
        Implements the brute force solution, which tests all subsets of vertices.
        Returns a list of cliques. Each clique is a nonempty tuple of increasing integers.
        '''
        solutions = []
        if len(self.graph.nodes)==0:
            return solutions
        else:
            for r in range(1,len(self.graph.nodes)+1):
                potential_clique_vertices_of_size_r = itertools.combinations(self.graph.nodes,r)
                for potential_clique_vertices in potential_clique_vertices_of_size_r :
                    is_clique = True
                    for pair in itertools.combinations(potential_clique_vertices,2):
                        x,y = pair
                        if y not in self.graph.neighbors(x):
                            is_clique = False
                    if is_clique:
                        solutions.append(potential_clique_vertices)
        return solutions

    def list_of_cliques_recursive_backtracking(self):
        '''
        Returns a list of cliques by using recursive backtracking.
        Each clique is a sorted tuple of vertices.
        '''
        cliques = []
        current_graph = copy.copy(self.graph)
        def backtrack(idx, current_graph):
            nonlocal cliques
            #TODO: (~14 lines) Complete the backtrack function.
            #Hint1: Check the solve_backtracking() method of MySudoku. Mimic that solution here.
            #Hint2: In Sudoku, our choices are which number to write in the next cell.
            #       Here, our choices are whether to include or exclude the vertex idx from the clique.

        backtrack(0,current_graph)
        return cliques

    def __iter__(self): #This is the key function that makes CliqueIterable into an iterable.
        yield from self.backtrack_generator(0, copy.copy(self.graph))

    def backtrack_generator(self, idx, current_graph):
        '''
        Input: idx is an integer that represents a node of the original graph, self.graph.
                current_graph is an induced subgraph of the current graph that keeps track of which vertices we may add to the clique.
        Output: The associated generator object yields cliques one-by-one.
        Note: When called, this generator function returns a generator object, not a clique.
        '''
        pass
        #TODO:(~14 lines) Complete this generator function. 
        # Hint: It should look similar to list_of_cliques_recursive_backtracking, except that it yields instead of returns.