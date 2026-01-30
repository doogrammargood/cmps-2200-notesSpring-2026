from collections import Counter
from typing import Callable
import matplotlib.pyplot as plt
import math
from typing import Literal
from collections import Counter
import numpy as np

counter = Counter()
def recursion_operation_count(n: int, 
                              a: int, 
                              b: int, 
                              f: Callable[[int],int], 
                              start: bool = True) -> None:
    '''
    Input: n, an integer that represents the size of a problem.
            a and b are integers, such that our recursion satisfies R(n)=a*R(n//b)+f(n)
            start, a boolean that indicates whether this was the first call (made by the user)
    Output: None
    Side-Effects: Updates counter["balanced_operations"] with the number of steps used.
    '''
    if start:
        counter.clear()
    if n<=1:
        return
    counter["operations_count"]+=f(n) # do n operations
    for _ in range(a):
        recursion_operation_count(n/b, a, b, f, start = False)

def create_operation_count_plot(max_n: int,a: int,b: int,f: Callable[[int],int],ideal: Callable[[int],int] | None = None) -> None:
    '''
    Input: max_n an integer. The x-axis will go from 0 to n-1.
            a and b are integers that appear in the recurrence to be studied.
            f is a function that appears in the recurrence to be studied.
            ideal is a function that should be close to the number of operations, according to the Master Theorem.
    Output: None
    Side-Effects: Creates a plot with 2 curves. 
                    One curve measures the number of operations in the recursion R(n)=a*R(n//b)+f(n).
                    Another curve is our ideal estimate for the number of operations using the Master Theorem.
    '''
    outputs = []
    ideal_output = []
    for n in range(1,max_n):
        recursion_operation_count(n, a, b, f)
        outputs.append(counter["operations_count"])
        if ideal is not None:
            ideal_output.append(ideal(n))
    plt.plot(list(range(1,max_n)), outputs,label = f"{a=},{b=},{f.__name__}" )
    if ideal is not None:
        plt.plot(list(range(1,max_n)), ideal_output,label = "ideal")
    plt.legend()
    plt.title(f"Count of operations for recursion {a=},{b=},{f.__name__}")
    plt.xlabel("list length")
    plt.ylabel("number of operations")
    plt.show()
    plt.clf()

def create_ratio_plot(max_n: int,a: int,b: int,f: Callable[[int],int],ideal: Callable[[int],int]) -> None:
    '''
    Input: max_n an integer. The x-axis will go from 0 to n-1.
            a and b are integers that appear in the recurrence to be studied.
            f is a function that appears in the recurrence R to be studied.
            ideal is a function that should be close to the number of operations, according to the Master Theorem.
    Output: None
    Side-Effects: Creates a plot with 1 curve, whose value is R(n)/ideal(n)
    '''
    outputs = []
    for n in range(2,max_n):
        recursion_operation_count(n, a, b, f)
        outputs.append(counter["operations_count"]/ideal(n))
    plt.plot(list(range(2,max_n)), outputs,label = f"{a=},{b=},{f.__name__}" )
    plt.legend()
    plt.title(f"ratio of measured vs approximate operations counts")
    plt.xlabel("list length")
    plt.ylabel("Ratio")
    plt.show()
    plt.clf()

def identity(n: int) -> int:
    return n
def square(n: int) -> int:
    return n**2
def create_plots():
    create_operation_count_plot(1000,3,2,identity,lambda n: n**math.log2(3)) #leaf dominated
    create_operation_count_plot(1000,2,2,identity,lambda n: n*math.log2(n)) #balanced
    create_operation_count_plot(1000,2,2,square, lambda n: n**2) #root dominated
def create_ratio_plots():
    create_ratio_plot(1000,3,2,identity,lambda n: n**math.log2(3)) #leaf dominated
    create_ratio_plot(1000,2,2,identity,lambda n: n*math.log2(n)) #balanced
    create_ratio_plot(1000,2,2,square, lambda n: n**2) #root dominated
#create_plots()
create_operation_count_plot(3000,2,2,identity,None) #leaf dominated
