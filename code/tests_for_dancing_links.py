from sudoku_via_dancing_links_solution import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
class TestCodeRuns(unittest.TestCase):
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_basic_example(self):
        D=DancingLinks(
                   [[0,0,1,1,0],
                    [0,1,0,1,0],
                    [1,1,0,1,1],
                    [1,0,0,0,1],
                    [0,1,1,0,0],
                    [0,1,1,0,1],
                    [1,0,0,1,0],
                    [0,1,1,1,0],
                    [1,0,1,0,1],
                ])
        D.solve()
        assert set([sol for sol in D.found_solutions])=={(3, 7), (5, 6), (1, 8)}
    @weight(10)
    @number('2')
    @visibility('visible')
    def test_empty_sudoku_setup(self):
        exact_cover_from_blank_sudoku = SudokuViaDancingLinks.sudoku_general_creation()
        for row in exact_cover_from_blank_sudoku:
            assert sum(row)==4
    @weight(10)
    @number('4')
    @visibility('visible')
    def test_sudoku_generate(self):
        D = SudokuViaDancingLinks(puzzle1)
        #First, we count the number of rows that should be in the constraint matrix.
        counter = 0
        for r,row in enumerate(puzzle1):
            for c, entry in enumerate(row):
                if puzzle1[r][c]==0:
                    for digit in range(1,10):
                        puzzle1[r][c]=digit
                        if check_cell(puzzle1,r,c): #defined in sudoku_examples. 
                            counter +=1
                    puzzle1[r][c]=0
        #Now we check whether there are the correct number of rows.
        assert len(D.dancing_links.constraint_matrix) == counter
    @weight(10)
    @number('4')
    @visibility('visible')
    def test_sudoku_solve(self):
        D = SudokuViaDancingLinks(puzzle1)
        D.dancing_links.solve()
        solutions = D.sudoku_solutions()
        assert len(solutions)==1
        assert solutions[0]==to_list_format('''462831957
                                            795426183
                                            381795426
                                            173984265
                                            659312748
                                            248567319
                                            926178534
                                            834259671
                                            517643892''') #Solution copied from Lab4.

if __name__=="__main__":
    unittest.main()