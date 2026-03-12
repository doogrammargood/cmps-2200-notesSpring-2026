#This file contains tests for the code contained in lab4_cliques_solution.py and lab4_sudoku_solution.py
#Be sure to rename those files so that they are appropriately tested.
#Some tests may already pass with the starter code.

import unittest
import itertools
import functools
import random
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from lab4_sudoku_solution import *
from lab4_cliques_solution import *
random.seed(50)

class TestCodeRuns(unittest.TestCase):
    
    #---Tests for Sudoku.---#
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_brute_force_small(self):
        '''
        Tests that the brute force solution works on a puzzle with only 2 blanks.
        '''
        puzzle = easy_puzzle
        P = MySudoku(puzzle)
        solutions = P.solve_brute_force()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify()

    def test_solve_backtracking(self):
        '''
        Checks that the solve_backtracking() method finds the unique solution to puzzle1
        '''
        P = MySudoku(puzzle1)
        solutions = P.solve_backtracking()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify(full=True)
    
    def test_solve_iterative(self):
        '''
        Tests that the solution using the iterable finds the unique solution to puzzle 1.
        '''
        P = MySudoku(puzzle1)
        solutions = P.solve_iterative()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify(full=True)

    #--- Tests for cliques. ---#
    def test_list_cliques_brute_force(self):
        #Tests the brute force solution to calculate cliques.
        G = nx.cycle_graph(4)
        CI = CliqueIterable(G)
        cliques = CI.list_cliques_brute_force()
        assert len(set(cliques))==len(cliques) #Check that there are no duplicates.
        correct_cliques = [(0,),(1,),(2,),(3,),(0,1),(0,3),(1,2), (2,3)]
        assert len(correct_cliques)==len(cliques)
        assert set(correct_cliques)==set(cliques)

    def test_list_cliques_recursive_backtracking(self):
        G = nx.complete_bipartite_graph(3,3)
        CI = CliqueIterable(G)
        cliques = CI.list_of_cliques_recursive_backtracking()
        assert len(set(cliques))==len(cliques)
        assert set(cliques)== set(CI.list_cliques_brute_force())

    def test_list_cliques_iterator(self):
        G = nx.complete_bipartite_graph(3,3)
        CI = CliqueIterable(G)
        cliques = CI.list_of_cliques_recursive_backtracking()
        count = 0
        for c in CI:
            count += 1
            assert c in cliques
        assert count == len(cliques)


if __name__=="__main__":
    unittest.main()