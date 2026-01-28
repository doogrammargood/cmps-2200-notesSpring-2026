from unittest import TestCase
from lab2_solution import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
import random
random.seed(50) #Random choices are the same each time these tests are run.
class CreateTests(TestCase):
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_sorting_correctness(self):
        for n in range(100):
            arr = average_case(n)
            arr_copy = arr[:]
            arr_quicksorted = quicksort(arr)
            arr_mergesorted = mergesort(arr)
            assert arr_quicksorted == arr_mergesorted
            assert arr_mergesorted == sorted(arr)
            assert arr == arr_copy
    
    @weight(10)
    @number('2')
    @visibility('visible')
    def test_quicksort_on_constant_list(self):
        for n in range(100):
            arr = [1]*n
            counter.clear()
            quicksort(arr)
            assert counter["compare"]<= max(n-1,0)
            counter.clear()
    
    @weight(10)
    @number('3')
    @visibility('visible')
    def test_mergesort_reversed_equal_comparisons(self):
        for exp in range(7):
            n=2**exp
            arr = average_case(n)
            counter.clear()
            mergesort(arr)
            num_comparisons = counter['compare']
            counter.clear()
            mergesort(arr[::-1])
            num_comparisons_reversed = counter['compare']
            assert num_comparisons == num_comparisons_reversed
if __name__=="__main__":
    unittest.main()