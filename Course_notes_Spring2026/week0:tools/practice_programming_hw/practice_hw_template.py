#This file contains a solution to a practice homework.
#This does not count towards credit for the class.

#Purpose of this practice assignment:
#   -To practice with key Python concepts: list comprehensions, and lambda expressions.
#   -To practice with the concept of testing code.
#   -To see an example of a quiz related to a programming assignment, to give a sense of how closely related they are.
#   -To check that you are able to use gradescope.
#   -To check if there is anything wrong with your process of writing code.
#   -To check if there is anything wrong with my process of writing assignments or quizzes.

#--Instructions:
#You should start by opening the homework template and completing the code.
#You should then run the tests.

from typing import Callable, Optional #Used to define function types, and types that could be None.

#Problem 1: Create a doubly nested list.
def subtraction_matrix( m: int, n: int) -> list[list[int]]:
    '''
    Input: two integers, m,n.
    Output: an mxn matrix (m rows and n columns). The i,jth entry should be i-j.
    Side effects: None
    Note: Indexing starts at 0.
    '''
    pass

# Problem 2: 
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    '''
    Input: A list of lists of integers. Each inner list should have the same length, n. The outer list has length m.
    Output: The transpose, which is also a list of lists of integers. The i,jth entry of the input is the j,ith entry of the output.
    Side effects: None. Do not modify the input matrix.
    '''
    pass
# Problem 3:
def matrix_to_function(matrix: list[list[int]])-> Callable[[int, int], Optional[int]]:
    '''
    Input: A matrix (a list of list of integers, where each inner list has the same length.)
    Output: A function of two integers.
        On input i,j the function returns the ijth entry of the matrix, unless that entry is not defined. In this case, the function returns None
    '''
    pass