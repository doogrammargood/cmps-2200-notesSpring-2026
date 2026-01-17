from unittest import TestCase
from practice_hw import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility

class CreateTests(TestCase):
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_subtraction_matrix(self):
        test_cases = [(0,0),(3,2),(5,4),(4,4)]
        for m,n in test_cases:
            matrix = subtraction_matrix(m,n)

            for i in range(m):
                for j in range(n):
                    assert matrix[i][j] == i-j

    @weight(10)
    @number('2')
    @visibility('visible')
    def test_transpose(self):
        test_cases = [(3,2),(5,4),(4,4)]
        for m,n in test_cases:
            matrix = subtraction_matrix(m,n)
            assert not (transpose(matrix)==matrix)
            assert transpose(transpose(matrix))==matrix


    @weight(10)
    @number(3)
    @visibility('visibile')
    def test_matrix_to_function(self):
        test_cases = [(3,2),(5,4),(4,4)]
        for m,n in test_cases:
            matrix = subtraction_matrix(m,n)
            f = matrix_to_function(matrix)
            for i in range(m):
                for j in range(n):
                    assert f(i,j) == matrix[i][j]
if __name__=="__main__":
    unittest.main()
