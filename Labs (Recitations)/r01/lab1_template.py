'''
In this lab, we will compare different basic sorting methods.
Rename this file as lab1_solution.py for the autograder.

Goals:
    -To practice implementing the algorithms.
    -To see examples of worst-case, best-case and average-case behaviors.
    -To demonstrate concrete counts of operations that are used in the algorithms.
    -To compare the theoretical counts with the counts that we measure directly.
    -To practice with Python:
       -Treating functions as objects that are iterated over.
       -Structuring code to separate calculations and logic (get_results) from display (generate_plots).
       -Programmatically compare algorithms under varying parameters.
       -Practice testing behavior rather than implementation.
Gotchas:
    -All sorting methods use in-place sorting. They modify the input list and return None.
    -You must use the compare and swap operations that have been defined so that the operations are properly counted.
    -There may be multiple correct ways to implement the basic algorithms.
    -Your algorithms should work correctly, even in the edge case that the list is empty.
    -The operations_counter is a global variable. You must clear it using operations_counter.clear() to get accurate counts.
    -Some curves may not be visible in the plots, due to exact overlap with another curve.
    -Remember to rename this file as lab1_solution.py.

Format of this file:
    0. Implement compare and swap functions, 
        together with a counter that records how many times they are used.
    1. Implementing the three basic sorting algorithms
        -bubblesort (given)
        -selectionsort
        -insertionsort
    2. Implement three functions to generate sorting instances for lists of various sizes.
        -best_case (when the list is already sorted) (given)
        -worst_case (when the list is sorted in reverse)
        -average_case (when the list is a random permutation) (given)
    3. We calculate the number of operations used under every combination of 
        -choice of sorting algorithm
        -choice of instance function
        -instance size
    4. We draw and save 6 plots, one for each pair of instance function and operation. 
        -Each plot contains 3 curves, representing the three basic sorting algorithms. Some curves may not be visible due to overlaps.
        -The x-axis of the plots is the instance size. The y-axis is the number of operations used.
    Running this file produces and saves 6 plots.

Fill in every instance of #TODO (except this <- ) with code that accomplishes the task. 
See lab1_tests.py for the tests.
'''
from typing import Literal
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


#--Step 0. Implement compare, swap and counter---#
operations_counter = Counter()

def compare(x: int, y: int) ->  Literal[-1, 0, 1]: #Literal means that the output is -1, 0 or 1.
    '''
    Input: integers x,y.
    Output: -1, 0, or 1 depending on whether x<y, x==y, or x>y, respectively.
    Side-Effect: increments the comparison_counter
    '''
    operations_counter['compare']+=1
    if x<y:
        return -1
    elif x==y:
        return 0
    else:
        return 1

def swap(arr: list[int], i: int, j: int) -> None:
    '''
    Input: a list of integers arr, and valid indicies i,j for arr.
    Output: None
    Side-Effect: Swaps the positions of i and j. Increments the swap_counter if i !=j
    '''
    if i!=j:
        operations_counter['swap']+=1
        arr[i], arr[j] = arr[j], arr[i]


#--Step 1. Implement Sorting Algorithms---#
def bubble_sort(arr: list[int]) -> None:
    '''
    Input: arr, a list of integers to be sorted.
    Output: None
    Side-Effects: sorts arr, increments operations_counter with the number of comparisons and swaps.
    Note: Implements bubble sort.
    '''
    n=len(arr)
    for pass_number in range(n-1):
        for index in range(n-1-pass_number):
            if compare(arr[index], arr[index+1]) == 1:
                swap(arr, index, index+1)

def selection_sort(arr: list[int]) -> None:
    '''
    Input: arr, a list of integers to be sorted.
    Output: None
    Side-Effects: sorts arr, increments operations_counter with the number of comparisons and swaps.
    Note: Implements selection sort. Should use len(arr) or fewer swaps.
    '''
    #TODO: implement selection_sort using compare and swap. (several lines)
    pass
def insertion_sort(arr: list[int]) -> None:
    '''
    Input: arr, a list of integers to be sorted.
    Output: None
    Side-Effects: sorts arr, increments operations_counter with the number of comparisons and swaps.
    Note: Implements insertion sort. Should use len(arr) or fewer swaps and comparisons when the list is intially sorted.
    '''
    #TODO: implement insertion_sort using compare and swap. (several lines)
    pass
#--Step 2 Implement instance functions---

def best_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: the best-case instance our algorithms to sort a list of length n. In particular, the list is already sorted.
    Side-Effects: None
    Note: It is lucky that all three algorithms have the same best-case instance.
    '''
    return list(range(n))

def worst_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: the worst-case instance our algorithms to sort a list of length n. In particular, the list is sorted in reverse
    Side-Effects: None
    Note: It is lucky that all three algorithms have the same worst-case instance.
    '''
    #TODO: return a list of length n that is sorted in reverse. (1 line)
    pass

def average_case(n: int) -> list[int]:
    '''
    Input: an integer n.
    Output: an average-case instance our algorithms to sort a list of length n. In particular, the list is the integers 0,1,..,n-1 permuted uniformly at random. 
    Side-Effects: None
    Note: returns a random output, that may be different each time the function is called.
    '''
    return list(np.random.permutation(n))

#--Step 3-- Calculate the number of operations used, for every possible setting of instance_function, sorting function, operation and list length.

instance_functions = [worst_case, best_case, average_case]
sorting_functions = [bubble_sort, selection_sort, insertion_sort]

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
    operations_counter.clear() #resets the results counter.
    for instance in instance_functions:
        for s in sorting_functions:
            for n in range(max_n):
                arr = instance(n)
                #TODO: sort arr with the appropriate method. (1 line)
                assert arr == sorted(arr)#Check that the sorting was correct.
                results.append((instance.__name__, "compare", s.__name__, n,  operations_counter["compare"]))
                #TODO: append the information about the number of swaps to the results list. (1 line, similar to above.)
                #TODO: reset the results counter. (1 line)
    return results
def generate_plots(max_n: int, results: list[tuple[str, str, int, str, int]]) -> None:
    '''
    Input: a list of tuples that are the output of get_results.
    Output: None
    Side-Effects: Creates and save six plots. One for each input type and comparison operator. 
                  Each plot should show all three functions in different colors.
                  Each plot should have titles and axes.
    '''
    for i in instance_functions:
        for operation in ["compare", "swap"]:
            for s in sorting_functions:  
                outputs = [result[-1] for result in results if result[0]== i.__name__ and result[1]==operation and result[2]==s.__name__]
                plt.plot(list(range(max_n)), outputs,label = f"{s.__name__}" )
            plt.legend()
            plt.title(f"{i.__name__} count of {operation}")
            plt.xlabel("list length")
            plt.ylabel("number of operations")
            plt.savefig(f"{i.__name__}_plot_{operation}.png") #saves the figure.
            plt.show()
            plt.clf()

if __name__=='__main__': #This line ensures that the plots are only generated when this file is run directly. 
                         #They will not be generated when this file is imported in lab1_tests.py
    generate_plots(100, get_results(100))
