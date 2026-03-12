'''
This file contains starter code for implementations of sudoku solvers.

Rename this file as lab4_sudoku_solution.py

The goal of the solvers is to return all correct solutions to a given sudoku puzzle.

Sudoku:
    Sudoku is a puzzle on a 9x9 grid, broken into 9 3x3 subgrids. We call the grid a "board."
    Some of the squares of the puzzle are initially filled. 
    We call these initially-filled squares "clues."
    We call the squares that are not initially filled "blank." 
    We call the non-clue squares blank, even if we pencil in values.

    The goal of the puzzle is to fill in the blank squares 
    such that each row and column has each digit 1-9 exactly once,
    and such that each 3x3 subgrid contains each digit exactly once.

    Some puzzles may have multiple solutions.

Representing Sudoku:
This file implements a MySudoku class. 
We store the board as an attribute, board. 
It is represented by a doubly nested list of digits 0-9, where 0 indicates blank.
We store the clues as an attribute, clues. Each clue is a pair (r,c), 
where r is the index of the row in MySudoku.board of the clue and c is the index of the column in MySudoku.board of the clue.
We store a list of blank cells. Each blank cell is given by its coordinates, (r,c). 
The blank cells are stored in order from left to right, top to bottom. 
This is useful to map the ith blank cell to its coordinates on the board.

Gotchas for this file:
    -Remember that lists are mutable. The MySudoku class maintains a single board that is modified repeatedly.
    -Since the board is a doubly nested list and lists are mutable, you will need to call copy.deepcopy() when you save a solution so that the solution does not change when the board does.
    -You may need to call MySudoku.reset() to clear all the cells that were not given.
    -self.blank_cells refers to the cells that are initially blank (0). They may not be blank during the course of the algorithm.
    -The solving algorithms return a doubly nested list of integers, not a MySudoku object.
    -The keyword "nonlocal" allows you to modify a variable outside of the current scope. This can cause confusion if the variable is accidentally modified.

Format of this file:
0. Define MySudoku class. (Given)
1. Add verification functions, check_cell and verify to check whether the board obeys sudoku rules. (Given)
2. Define helper functions, reset and embed guess (Given)
3. Implement a brute force solver. (#TODO 1 line)
4. Implement a recursive backtracking solver. (Given)
5. Make the MySudoku class iterable by defining an __iter__() method that returns an iterator. In our case, the iterator is a generator. (#TODO: 1 line)
    
Fill in every instance of #TODO (except this <- and the two above) with code that accomplishes the task. 
See tests_for_lab4.py for tests. 
    
    '''

import itertools
from sudoku_examples import *
import copy
import profile
class MySudoku(object):
    def __init__(self: "MySudoku", board: list[list[int]]) -> None:
        '''
        Input: A board. This is a doubly nested list of digits 0-9. The digit 0 means that the square is blank.
        Output: None
        Side Effects: creates a sudoku board. It stores the indices of the non-zero digits as a list of pairs called clues.
        '''
        self.board = board
        self.clues = [(i,j) for i in range(9) for j in range(9) if self.board[i][j]>0] #A list of the coordinates of the clues, digits that were given in the puzzle.
        self.blank_cells = [(i, j) for i in range(9) for j in range(9) if (i,j) not in self.clues] #A list of coordinates of the blank cells, which are the non-clues.

    def __repr__(self) -> str:
        return "\n".join(["".join([str(r) for r in row]) for row in self.board]) + "\nclue positions: " + str(self.clues)
    
    def check_cell(self, r:int, c:int) -> bool:
        '''
        Input: r and c are indices of a cell.
        Output: True/False, depending on whether this cell violates any Sudoku rule.
        '''
        val = self.board[r][c]
        if val == 0:
            return True

        # row
        for j in range(9):
            if j != c and self.board[r][j] == val:
                return False

        # column
        for i in range(9):
            if i != r and self.board[i][c] == val:
                return False

        # 3x3 box
        br = (r // 3) * 3
        bc = (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if (i != r or j != c) and self.board[i][j] == val:
                    return False
        return True


    def verify(self, full = False) -> bool:
        '''
        Input: full is a Boolean. If True, then each cell must be filled (nonzero).
        Applies self.check_cell to each cell. 
        Returns True if the cell satisfies the sudoku rules.
        '''
        if full:
            if len([entry for row in self.board for entry in row  if entry ==0 ])!=0:
                return False
        for r in range(9):
            for c in range(9):
                if not self.check_cell(r, c):
                    return False
        return True

    def reset(self) -> None:
        '''
        Input: None
        Side Effects: Sets any non-clues to 0.
        Output: None
        '''
        for i in range(9):
            for j in range(9):
                if (i,j) not in self.clues:
                    self.board[i][j] = 0

    def embed_guess(self, assignment:list[int]) -> None:
        '''
        Input: assignment is a list of integers. They are the numbers that the solver has filled in.
        Output: None
        Side Effects: Modifies self.board so that the entries that the solver fills in are modified to fit assignment.
        '''
        assert len(self.blank_cells)==len(assignment)
        for (i, j), val in zip(self.blank_cells, assignment):
                self.board[i][j] = val
    
    def solve_brute_force(self) -> list[list[list[int]]]:
        '''
        Returns the list of solutions. Each solution is a doubly nested list of 1-9, not a MySudoku object.
        Temporarily modifies the board.
        '''
        solutions = []
        for blank_cell_assignment in itertools.product(range(1,10), repeat = 81- len(set(self.clues))):
            self.embed_guess(blank_cell_assignment)

            if self.verify():
                pass
                #TODO: (~1 line) Add self.board to the list of solutions.
                #Make sure that the solution does not change when self.board does. See Gotchas.
        self.reset()
        return solutions

    def solve_backtracking(self) -> list[list[list[int]]]:
        """
        Solve the Sudoku using recursive backtracking.
        Returns a list of solutions. Each solution is a doubly nested list of digits 1-9, not a MySudoku object.
        Temporarily modifies the board, then resets it.
        """
        solutions = []
        def backtrack(idx=0):
            '''idx is the number of the blank cell.
            Returns None.
            Side-effect: updates solutions to contain all of the solutions.
            '''
            nonlocal solutions
            if idx == len(self.blank_cells):
                # All blanks filled, solution found
                solutions.append(copy.deepcopy(self.board))
                return

            r, c = self.blank_cells[idx]
            for val in range(1, 10):
                self.board[r][c] = val
                if self.check_cell(r, c):
                    backtrack(idx + 1)
                self.board[r][c] = 0  # undo for next attempt
            return
        backtrack()
        self.reset()
        return solutions

    def __iter__(self):
        '''This dunder method allows looping through MySudoku objects.
            The terminology behind these concepts are elaborate. 
            Beware the difference between iterables vs iterators, generator functions vs generator objects.

        Objects with .__iter__() defined are iterables.
            .__iter__() returns an iterator. An iterator is an object with .__iter__() and .__next__() defined.
            Notice that we do not return and instead yield.
            The word 'yield' marks .__iter__() as a generator function. 
            When a generator function is called, it returns a generator object. 
            This generator object is our iterator.
        '''
        yield from copy.deepcopy(self).solve_generator_function(0)

    def solve_generator_function(self, i):
        '''
        Input: i is the index that we are filling in.
        Output: The associated generator object yields a MySudoku object, not a doubly nested list of 1-9
        Note: This is a generator function. 
        When called, it returns a generator object that serves as the iterator for MySudoku.
        '''
        if i == len(self.blank_cells):
            yield self
            return
        r,c = self.blank_cells[i]
        for v in range(1,10):
            self.board[r][c] = v
            if self.check_cell(r,c):
                yield from self.solve_generator_function(i+1) #yield from extracts a value from the generator self.solve(i+1). 
                                            #In contrast, "yield" would the yield of the generator object, self.solve(i+1)
        #TODO: reset the guess that was made for the cell indexed by i. (~1 line)
    
    def solve_iterative(self):
        '''
        Input: None
        Output: A list of the solutions to the sudoku puzzle.
        Side Effects: None
        '''
        return [copy.deepcopy(s.board) for s in self]
#---#
if __name__=="__main__":
    #This snippet of code gives an example of how we can iterate through the valid solutions of a puzzle, once the code is complete.
    P = MySudoku(zero_puzzle)
    for solution in itertools.islice(P,0,500,100):
        print(solution)