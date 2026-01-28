'''
Lab 2
Rename this file as lab2_solution.py for the autograder.

Introduction:
    In this lab, we compare the sorting methods mergesort and quicksort.
    We count the number of comparisons used in both methods. We plot the results.

    We will see that quicksort can perform poorly, but on average performs well.
    Mergesort performs well generally.

Goals:
    -To practice implementing quicksort and mergesort
    -To demonstrate the growth behaviors of the number of comparisons used.
    -Programming:
        -To see how to fit a curve.
        -To practice Python list manipulations.
        -To practice recursive functions (not recommended in Python.)
Gotchas:
    -Remember to rename this file (see top of file)
    -Most of this file was copy/pasted from lab1, but some variable names have been changed. e.g. operations_counter->counter.
    -There may be multiple correct implementations.
    -Your algorithms should work correctly, even in the edge case that the list is empty.
    -You should not need to change your recursion_limit. If you hit that limit, something in your code is wrong.
    -Remember to use the custom compare() function each time you make a comparison. Also, don't call compare twice on the same inputs by accident.
    
Format of this file:
0.  Implement a compare function, that increments a counter each time the function is called. (Given)
1.  Implement instance functions, that take an integer n and return a list of n integers. (Given)
2.  Implement the merge_step, mergesort, and quicksort.
3.  Plot the number of comparisons for mergesort and quicksort.
4.  (optional) add lines of best fit.

Fill in every instance of #TODO (except this <- ) with code that accomplishes the task. 
See tests_for_lab1.py for tests.
    '''
from collections import Counter
from typing import Callable
import matplotlib.pyplot as plt
import math
from typing import Literal
from collections import Counter
import numpy as np
from scipy.optimize import curve_fit


counter = Counter()

def compare(x: int, y: int) ->  Literal[-1, 0, 1]: #Literal means that the output is -1, 0 or 1.
    '''
    Input: integers x,y.
    Output: -1, 0, or 1 depending on whether x<y, x==y, or x>y, respectively.
    Side-Effect: increments the comparison_counter
    '''
    counter['compare']+=1
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1
    

#--Step 2 Implement instance functions---

def already_sorted_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: the best-case instance our algorithms to sort a list of length n. In particular, the list is already sorted.
    Side-Effects: None
    Note: This is a worst-case for quicksort.
    '''
    return list(range(n))

def sorted_in_reverse_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: the worst-case instance our algorithms to sort a list of length n. In particular, the list is sorted in reverse
    Side-Effects: None
    Note: This is a worst case for quicksort
    '''
    return list(range(n))[::-1]

def average_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: an average-case instance our algorithms to sort a list of length n. In particular, the list is the integers 0,1,..,n-1 permuted uniformly at random. 
    Side-Effects: None
    Note: quicksort and mergesort are both good, on average.
    '''
    return list(np.random.permutation(n))

def merge_step(arr1: list[int], arr2: list[int]) -> list[int]:
    '''
        Input: arr1 and arr2 are lists of integers, assumed to be sorted.
        Output: the sorted concatenation of arr1 and arr2, (equivalent to sorted(arr1+arr2))
        Side-Effects: Removes all elements from arr1 and arr2.
    '''
    outputlist = []
    while len(arr1) * len(arr2) > 0:
        comparison_value = compare(arr1, arr2)
        if comparison_value==-1: #arr1[0]<arr2[0]
            outputlist.append(arr1.pop(0))
        else:
            #TODO: put the smallest element of arr2 onto the end of outputlist. (1 line)
            pass #remove this word pass. It serves to prevent a syntax error from the empty 'else' block.
    #TODO: add the remaining elements to the end of the list.
    arr1.clear()
    arr2.clear()
    return outputlist

def mergesort(arr: list[int]) -> list[int]:
    '''
        Input: arr is a list of integers.
        Output: a sorted version of arr.
        Side-Effects: None. arr is unchanged.
    '''
    #TODO: Implement mergesort.
    pass
    
def quicksort(arr: list[int]) -> list[int]:
    '''
        Input: arr is a list of integers to be sorted.
        Output: another list of intgers, the sorted version of arr.
        Side-Effects: None. Does not modify the input.
    '''
    if len(arr) <= 1:
        return arr[:]
    
    pivot_index = 0 #assume the zeroth is the pivot
    left = []
    middle = [arr[pivot_index]]
    right = []
    #TODO: add the elements of arr to left, middle and right 
    #   depending on whether they are less than, equal to or greater than the pivot. (a few lines)
    #TODO: Make recursive calls and return something. (1 line.)

    
instance_functions = [already_sorted_case, sorted_in_reverse_case, average_case]
sorting_functions = [quicksort, mergesort]

def get_results(max_n: int) -> list[tuple[str, str, str, int, int]]:
    '''
    Input: The maximum length of a list to test the algorithms on.
    Output: A list of tuples. Each tuple in the list will consist of
        - a name of an instance function ("worst_case", "best_case", "average_case")
        - an operation that is counted. ("compare" or "swap")
        - the name of a sorting function (bubble_sort, selection_sort, insection_sort)
        - an instance size
        - the number of those operations used when the sorting function is used.
    '''

    results = []
    counter.clear()
    for instance in instance_functions:
        for s in sorting_functions:
            for n in range(max_n):
                arr = instance(n)
                counter.clear()
                arr = s(arr)
                assert arr == sorted(arr) #Check that the sorting was correct.
                results.append((instance.__name__, "compare", s.__name__, n,  counter["compare"]))
                counter.clear()
    return results
def generate_plots(max_n: int, results: list[tuple[str, str, str, int, int]], show_fit = True) -> None:
    '''
    Input: a list of tuples that are the output of get_results.
    Output: None
    Side-Effects: Creates and save six plots. One for each input type and comparison operator. 
                  Each plot should show all three functions in different colors.
                  Each plot should have titles and axes.
    '''
    for i in instance_functions:
        for s in sorting_functions:  
            outputs = [result[-1] for result in results if result[0]== i.__name__ and result[1]=='compare' and result[2]==s.__name__]
            plt.plot(list(range(max_n)), outputs,label = f"{s.__name__}" )
            if show_fit:
                #TODO: (optional) add a fit to the model. Use curve_fit from scipy.optimize
                pass
        plt.legend()
        plt.title(f"{i.__name__} count of comparisons")
        plt.xlabel("list length")
        plt.ylabel("number of operations")
        plt.savefig(f"{i.__name__}_plot_.png") #saves the figure.
        plt.show()
        plt.clf()

if __name__=='__main__': #This line ensures that the plots are only generated when this file is run directly. 
                         #They will not be generated when this file is imported in lab2_tests.py
    generate_plots(200, get_results(200))