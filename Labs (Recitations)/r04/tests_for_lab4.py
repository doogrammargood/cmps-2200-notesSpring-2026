import unittest
import itertools
import functools
import random
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from lab4_solution import *
random.seed(50)

class TestCodeRuns(unittest.TestCase):
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_brute_force_small(self):
        '''
        Tests that addition was implemented correctly.
        '''
        puzzle = easy_puzzle
        P = MySudoku(puzzle)
        solutions = P.solve_brute_force()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify()

    def test_solve_backtracking(self):
        P = MySudoku(puzzle1)
        solutions = P.solve_backtracking()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify(full=True)
    
    def test_solve_iterative(self):
        P = MySudoku(puzzle1)
        solutions = P.solve_iterative()
        assert len(solutions)==1
        assert MySudoku(solutions[0]).verify(full=True)
if __name__=="__main__":
    unittest.main()