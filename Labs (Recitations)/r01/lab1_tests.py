'''
This file contains the tests for lab1. By running this file, you can check your code.

We implement 3 tests:
    - test_sorting_correctness. For each sorting function, we check whether the function sorts the averge case correctly.
    - test_selection_sort_swaps. We test that Selectionsort uses at most n swap operations to sort a list of length n.
    - test_near_sorted_insertion. We check that insertion sort uses few operations when applied to a list that is sorted, except that the first and last elements are switched.
        We will justify the last test as a Homework exercise.

Gotchas:
    - This file will not run unless you have the gradescope_utils module installed. 
        Fix: Either install it (recommended) or manually remove all mention of gradescope, specifically the import commpand and all of the decorators)
    - We use a random seed, so this file should run deterministically. Re-running should produce identical results.
'''

from unittest import TestCase
from lab1_solution import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
import random
random.seed(50)
class CreateTests(TestCase):
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_sorting_correctness(self):
        '''
        This checks the correctness of the sorting algorithms by running them on a random permutation.
        '''
        sorting_functions = [bubble_sort, selection_sort, insertion_sort]
        for list_size in range(100):
            for f in sorting_functions:
                arr = list(range(list_size))
                random.shuffle(arr)
                assert f(arr) is None #The algorithms are in-place sorts, and so should return None.
                assert arr == sorted(arr) #Checks that arr is sorted.

    @weight(10)
    @number('2')
    @visibility('visible')
    def test_selection_sort_swaps(self):
        '''
        This will test that selection sort uses at most n swaps to sort a list of length n.
        '''
        operations_counter.clear()
        for list_size in range(100):
            instance = average_case(list_size)
            selection_sort(instance)
            assert operations_counter["swap"]<=list_size
            operations_counter.clear()


    @weight(10)
    @number('3')
    @visibility('visible')
    def test_near_sorted_insertion(self):
        '''
        This will test that insertion sort has good behavior 
            when applied to a list that is in order except that the first and last elements are swapped.
            This verifies a problem on homework 1.
        '''
        for list_size in range(2,100):
            arr = list(range(list_size))
            arr[0], arr[-1] = arr[-1], arr[0]
            operations_counter.clear()
            insertion_sort(arr)
            assert operations_counter["compare"] <= 3*list_size
            assert operations_counter["swap"] <= 2*list_size
            operations_counter.clear()
if __name__=="__main__":
    unittest.main()