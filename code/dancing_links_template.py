'''
Rename this file as dancing_links_solution.py

This file illustrates Donald Knuth's dancing links algorithm.
See Donald Knuth's explanation here: https://www.youtube.com/watch?v=_cR9zDlvP88

The algorithm solves the exact cover problem.

The exact cover problem: Given a set X of size n and a subsets of X S1,S2,...,Sm,
                         Find all subsets of S1, S2,..., Sm 
                         such that each element of X is in exactly one of the chosen subsets.
                        In other words, we want to obtain all of the partitions of X into parts Si for i in 1,...,m.

Terminology: the elements of X are called 'items.'
             the subsets S1,S2,...,Sm are called 'options.'

We approach the problem mathematically be constructing a "constraint matrix," which is an m x n binary matrix.
The rows are indexed by the options, and the columns are indexed by the items.
The constraint matrix has a 1 in entry i,j if the ith option contains the jth item. (if Xj is in Si).
                        
Knuth's implementation uses an intricate system of pointers, hence the name "Dancing Links."

The implementation here is designed based on Knuth's insight that efficiency comes from moving references to data rather than data itself.
In particular, we should avoid copying the constraint matrix.

Our implementation consists of a doubly nested list of bits, together with two lists of bits, row_mask and column_mask.
The row_mask has length m (the number of options) and the column mask has length n (the number of items).

When row_mask[i]==1, this indicates that ith option is still available.
When row_mask[i]==0, this indicates that the ith option is not available. Maybe it has been chosen, or maybe one of the chosen options conflicts with it.
When column_mask[j]==1, this indicates that the jth item has not yet been covered.
When column_mask[j]==0, this indicates that the jth item has been covered.

The drawback of this implementation is that when rows are removed (by updating row_mask[i]=0) 
we must remember which rows have been removed in order to backtrack correctly. This will information will be stored as a local variable of self.solve().
In contrast, Knuth's Dancing Links datastructure keeps track of this information automatically.

Note: A better Python implementation exists here: https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html

Complete each #TODO: with the appropriate code.
'''
import math

class DancingLinks(object):
    def __init__(self, constraint_matrix: list[list[int]]) -> None:
        '''
        Input: constraint_matrix is a doubly nested list of 0's and 1's.
        Output: None
        Side Effects: initializes a DancingLinks object.
        '''
        self.constraint_matrix = constraint_matrix
        self.num_options = len(constraint_matrix)
        self.num_items = len(constraint_matrix[0])
        self.row_mask = [1] * self.num_options #self.column_mask and self.row_mask record which items and which options are still available. 1 means available.
        self.column_mask = [1] * self.num_items #Note: We will take advantage of the fact that 1 converted to the boolean "True" with idioms such as "if column_mask[i]:"
        
        #The following attribute is a list of the number of available options for each column.
        self.option_counts_of_items = [len([self.constraint_matrix[r][c] 
                                            for r in range(self.num_options)])
                                            for c in range(self.num_items)]

        self.found_solutions = [] #The solutions that have already been found.
        self.partial_solution = [] #the solution that we are building up in steps.
    
    def hide_row(self,r: int) -> None:
        '''
        Input: r is the index of the row to hide.
        Output: None
        Side Effect: Sets self.row_mask[r]=0
            Updates self.option_counts_of_items now that r is hidden.
        '''
        #TODO: Complete this function ~4 lines
    
    def cover_column(self,c: int) -> None:
        '''
        Input: c is the index of a column to cover.
        Output: The rows that are hidden as a result of covering column c (see below)
        Side Effects: Sets self.colmun_mask[c]=0 to cover it. 
                        Hides the rows that are not yet hidden and have a 1 in column c.
        '''
        #TODO: Complete this function ~7 lines.

    def unhide_row(self,r):
        '''
        Input: r is the index of a row to unhide.
        Output: None
        Side Effects: sets self.row_mask[r]=1.
                    Updates self.option_counts_of_items now that the row is available. 
        Note: This reverses self.hide_row(r)
        '''
        self.row_mask[r]=1
        for c in range(self.num_items):
            if self.constraint_matrix[r][c]==1:
                self.option_counts_of_items[c] +=1
    
    def uncover_column(self, c: int, rows_affected: list[int]) -> None:
        '''
        Input: c is the index of a column. rows_affected is a list of rows. 
                                            rows_affected are expected to be the indicies of the rows 
                                            that were hidden when c was covered.
        Output: None
        Side Effects
        Note: This method reverses self.cover_column(c,rows_affected).
        '''
        self.column_mask[c]=1
        for r in rows_affected:
            self.unhide_row(r)
    
    def smallest_uncovered_column(self) -> int:
        '''
        Input: None
        Output: Returns the index of the column that has not been covered with the fewest remaining options.
        Side Effects: None
        Note: If we chose the uncovered column with the smallest index, then the algorithm would still be correct.
              But choosing the uncovered column with the smallest number of 1's will be reduce the branching factor of the search.
        '''
        record = math.inf
        smallest = -1
        for c in range(self.num_items):
            if self.column_mask[c] and self.option_counts_of_items[c]<record:
                record=self.option_counts_of_items[c]
                smallest = c
        return smallest

    def extract_submatrix(self):
        '''
        Input: None
        Output: The sub-matrix of self.constraint_matrix consisting of the rows and columns that are still present.
        Side Effects: None
        Note: We use this method as part of initializing sudoku via dancing links.
        '''
        return [[entry for c, entry in enumerate(row) if self.column_mask[c]] 
                    for r, row in enumerate(self.constraint_matrix) if self.row_mask[r]]

    def __repr__(self):#This dunder method allows printing.
        '''
        Input: None
        Output: a string representation of the DancingLinks object.
                We print '-' for elements in a covered row or hidden column.
        Side Effects: None
        '''
        list_of_row_strings = []
        for r in range(self.num_options):
            row_list = [] #We'll put the row into this list before joining it together.
            for c in range(self.num_items):
                if self.row_mask[r] ==0 or self.column_mask[c]==0:
                    row_list.append('-')
                else:
                    row_list.append(str(self.constraint_matrix[r][c]))
            list_of_row_strings.append("".join(row_list))
        return "\n".join(list_of_row_strings)
    
    def solve(self) -> list[tuple[int]]:
        '''
        Input: None
        Assumes that self.row_mask and self.column_mask are initially all 1's (all items and options available)
        Output: A list of tuples. Each tuple contains the indicies of rows that form a solution.
        Side Effects: None
        '''
        if self.column_mask == [0] * self.num_items:
            #solution found
            self.found_solutions.append(tuple(sorted(self.partial_solution)))
            return
        col = self.smallest_uncovered_column() #col is the index of the next column to cover.

        if len([r for r in range(self.num_options) if self.constraint_matrix[r][col] and self.row_mask[r]])==0:
            #no solution found
            return
        
        option_candidates = self.cover_column(col)
        for option in option_candidates:
            pass
            #TODO: Complete the recursive part of the function. ~9 lines.
        for option in option_candidates:
            self.unhide_row(option)
        self.uncover_column(col,option_candidates)