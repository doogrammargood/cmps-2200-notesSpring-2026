'''
Rename this file sudoku_via_dancing_links_solution.py

In this file, we create an interface to convert Sudoku into 
an Exact Cover instance that can be solved using the DancingLinks.solve() method.

The items of the Exact Cover instance for Sudoku are the constraints:
    - Each cell must contain exactly 1 number. (81 constraints). We label these constraints prc, 
                                where r and c are the indicies of the row and column respectively.
                                For example, p08 represents the constraint that the bottom left position must be filled.
    - In each row, each digit 1-9 must occur exactly once. (81 constraints) We label these constraints hrd
                                where r is the index of the row and d is the digit. The h stands for "horizontal."
                                For example, h31 represents the constraint that 1 must appear in the row with index 3 exactly once.
    - In each column, each digit 1-9 must occur exactly once. (81 constraints) We label these constraints vcd
                                where c is the index of the row and d is the digit.
                                For example, v46 indicates that the digit 6 must appear in the column with index 4 exactly once.
    - In each 3x3 box, each digit 1-9 must occur exactly once. (81 constraints) We label these constraints bxd
                                where x is is the index of the 3x3 box, labeled left to right top to bottom starting at 0
                                and d is a digit 1-9. For example b48 represents the constaint that the digit 8 must appear in the middle box.

The options of Exact Cover are placements of digits.
These placements can be expressed as (r,c,d), r and c are in 0-8 and d is in 1-9.
This represents placing the digit d in the rth row and cth column.
The placement (r,c,d) satisfies the following constraints: prc, hrd, vcd, b( (r//3)*3 + c//3 )d
'''

from dancing_links_solution import *
from sudoku_examples import *
import copy

def option_contains_item(option: str, item: str): #option is of the form "rcd"
    '''
    Inputs: strings representing an option and an item.
    Output: 1 if the option covers the item. 0 otherwise.
    '''
    if item[0]=='p': #prc
        if item[1]==option[0] and item[2]==option[1]:
            return 1
        else: 
            return 0
    if item[0]=='h': #hrd
        if item[1] == option[0] and item[2]==option[2]:
            return 1
        else:
            return 0
    if item[0]=='v': #vcd
        if item[1] == option[1] and item[2]==option[2]:
            return 1
        else:
            return 0
    if item[0]=='b': #bx d
        pass
        #TODO: Complete this case. ~4 lines. See docstring at the top of the file for the format of x in terms r and c.
    assert False #This should not occur. One of the above possibilites should have happened.


class SudokuViaDancingLinks(object):
    
    def __init__(self, sudoku_board: list[list[int]]) -> list[list[int]]:
        '''
        Input: A doubly nested list of integers 0-9 representing a Sudoku board.
                The integer 0 represents a blank cell.
        Output: A binary matrix that can be used as the constraint_matrix for the DancingLinks class.
        Side Effects: None
        Implemented by calling sudoku_general_creation (see below)
            and then covering the columns that correspond to constraints 
            that have already been met by the existant clues.
        '''
        general_matrix = SudokuViaDancingLinks.sudoku_general_creation()
        starter_dancing_links = DancingLinks(general_matrix)
        self.sudoku_board = sudoku_board
        placements = [f"{r}{c}{sudoku_board[r][c]}" for r in range(9) for c in range(9) if self.sudoku_board[r][c] != 0]
        satisfied_constraints = []
        #TODO: Complete the list of satisfied_constraints. Those that are already satisfied from the placements.
        for item in satisfied_constraints:
            starter_dancing_links.cover_column(self.items.index(item))
        
        output_matrix = starter_dancing_links.extract_submatrix()
        
        #We need to maintain a mapping between the rows of the smaller matrix and the original.
        self.row_map = [] #The ith entry of this list will be the index of the ith row of the reduced matrix in the original.

        for r, bit in enumerate(starter_dancing_links.row_mask):
            if bit == 1:
                self.row_map.append(r)
        self.dancing_links = DancingLinks(output_matrix)
    
    def __repr__(self):
        return self.dancing_links.__repr__()

    def sudoku_solutions(self):
        '''
        Assumes that we have already created and solved sudoku by using the dancing links.
        Returns a list of the sudoku solutions based on the dancing links solutions.
        '''
        pass
        #TODO: Complete this function ~11 lines.
    @classmethod
    def sudoku_general_creation(cls) -> list[list[int]]:
        '''
        Input: None
        Output: A binary matrix that represents the constraint_matrix for an empty sudoku board.
        Side Effects: Defines cls.items and cls.options. Later, we can access self.items and self.options,
                    because Python will use the class attribute when it cannot find the instance attribute.
            '''
        #TODO: Complete this function ~8 lines.