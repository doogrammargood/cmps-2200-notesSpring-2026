import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
import my_solution


class TestCodeRuns(unittest.TestCase):
    def setUp(self):
        return None 
    
    @weight(10)
    @visibility('after_due_date')
    @number("1")
    def test_addition(self):
        """Checks addition,multiplication and powers"""
        r_vals = [10, 15, 20, 40, 50]
        values = [1,2,3,6,7,10,15,100,123]  
        my_solution.test_addition(r_vals,values)
        my_solution.test_multiplication(r_vals,values)
        my_solution.test_multiplication_self_test(r_vals,values)
        my_solution.test_powers(r_vals,values)
        return None
       

