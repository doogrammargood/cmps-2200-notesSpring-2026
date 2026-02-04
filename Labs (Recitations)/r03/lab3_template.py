'''
Lab 3.
Rename this file as lab3_solution.py

Introduction:
    We have seen Karatsuba's Algorithm, which is a divide-and-conquer algorithm for implementing multiplication.
    In this lab, we will implement an alternative to Karatsuba's Algorithm based on the Chinese Remainder Theorem.
    The idea is to represent integers by a list of their residues modulo p, where p runs over the first r primes.
    This allows us to represent all integers between 0 and the product of the first r primes.
    The representation allows us to perform addition and multiplication element-wise.
    We also implement exponentiation and subtraction.
    Finally, we implement converting from the ModularInt representation to the usual integer representation.
    The details of this conversion are written in Knuth's The Art of Computer Programming, page 290.
        We will see that good algorithms can depend on the data structures available. 
        In this case, multiplication can be performed quickly in the ModularInt representation.
Goals:
    -Theoretical goals:
        -To practice implementing common numerical algorithms:
            -The Extended Euclidean Algorithm.
            -Exponentiation by repeated squaring.
            -To see an example where the availability of good algorithms depends on the format of the data.
        -To see an example of the Chinese Remainder Theorem can be useful. It is important in the representation of ModularInt.
        -To see examples of how code can be used to check itself.
    -Skill goals:
        -To practice reading and implementing a textbook algorithm, converting from the ModularInt representation to the usual int representation.
    -Python goals:
        -To understand the organization of object-oriented Python code.
        -To see examples where class methods achieve polymorphic initialization.
        -To practice with dunder methods.
Gotchas:
    -Remember to rename this file as lab3_solution.py
    -Remember that you can remove mentions of gradescope in tests_for_lab3.py if it stops the code from running.
    -We don't actually need to know Karatsuba's Algorithm for this lab.
    -ModularInts are only defined modulo the product of the first r primes. Exponentiating too much can cause overflow.
    -You're supposed to use cls in classmethods instead of the name of the class. This won't actually cause an error.
    -Implement methods like __repr__ first so that you can see what you're doing with print statements.
Format of this file:
0. Implement number-theoretic functions to get the first few primes (Given)
1. Implement the extended euclidean algorithm.
2. Complete the ModularInt class, filling in magic methods.
3. The integer typecasting method of ModularInt will require you to follow the instructions given in Knuth's book.

Fill in every instance of #TODO (except this <- ) with code that accomplishes the task. 
See tests_for_lab3.py for tests.
'''

from sympy import isprime
import functools

def first_r_primes(r: int) -> list[int]:
    '''
    Input: an integer r.
    Output: a list of the first r prime numbers.
    '''
    i=2
    primes = []
    while len(primes) < r:
        if isprime(i):
            primes.append(i)
        i += 1
    return primes

def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    '''
    Input: integers a and b.
    Output: a triple: GCD, x, y such that ax + by = GCD. Here, GCD is the greatest common divisor of a and b.
    Side-Effects: None
    '''
    #TODO: detect base case and return something (2 lines)
    
    # Recursive call
    gcd, x1, y1 = extended_euclidean(b, a % b)

    #TODO: Update x and y using the results from the recursion. Return something. (~3 lines)
    pass

class ModularInt(object):
    '''
    We are going to store integers as lists, [u_0, u_1, ..., u_{r-1}]
    This list represents the number x that satisfies x = u_i % p_i, where p_i is the ith prime.
    Each instance of this class contains the attributes
    self.modular_rep . . . . . The list [u_0, u_1, ..., u_{r-1}]
    self.r . . . . . . . . . . The number of primes used, also the length of self.modular_rep
    self.primes_list . . . . . A list of the first r primes.
    '''
   
    @classmethod #Class methods are methods that are attached to classes instead of instances. See https://pynative.com/python-class-method/
    def create_ModularInt_from_value(cls, value: int, r: int = 10) -> "ModularInt":
        '''
        Input: value, an integer that we will represent by a ModularInt.
                r, the number of primes to use to represent the value.
                Assume that value is between 0 and the product of the first r primes.
        Output: a ModularInt
        '''
        #TODO: return something (1 line)
        pass
    
    @classmethod
    def ModularInt_zero(cls,r): 
        '''Returns the ModularInt representing zero'''
        return cls([0]*r, r)
    
    @classmethod
    def ModularInt_one(cls, r): 
        '''Returns the ModularInt representing one.'''
        return cls([1]*r, r)

    #DUNDER METHODS aka MAGIC METHODS are methods surrounded by double underscores. 
    #They have special significance in Python.
    def __init__(self, modular_rep: list[int], r: int) -> None:
        '''
        The dunder __init__ method creates an instance of a ModularInt.
        Input: modular_rep (the list of integers in the Chinese Remainder Theorem representation)
        '''
        #initializes from a list [u_0,u_1,...,u_{r-1}]
        assert r == len(modular_rep) #checks consistency of r with modular_rep
        self.r = r
        self.modular_rep = modular_rep
        self.primes_list = first_r_primes(r)
    
    def __repr__(self) -> str:
        '''
        The dunder __repr__ method allows you to use the print() function to inspect objects.
        Input: None
        Output: str
        Side-Effects: None
        '''
        #TODO: return something. (1 line.)
        pass
    
    def __eq__(self, other: "ModularInt") -> bool:
        '''
        The dunder __eq__ method allows you to check equality of objects using ==.
        Input: other is a ModularInt that you want to compare self to.
        Output: True or False, depending on whether self represents the same or different value that other.
        Side-Effects: None
        '''
        if self.r != other.r:
            return False
        else:
            return all([self_ui == other_ui for self_ui,other_ui in zip(self.modular_rep,other.modular_rep)])
    
    def __add__(self, other: "ModularInt") -> "ModularInt":
        '''
        The dunder __add__ method allows you to add objects using +
        Input: other is a ModularInt
        Output: A ModularInt that represents the sum of self and other.
        Side-Effects: None
        '''
        assert self.r == other.r #We assume the numbers have the same r.
        #TODO: create a list, new_modular_rep, that represents the sum of self and other. Return something (~2 lines)
        pass    
    def __neg__(self) -> "ModularInt":
        '''
        The dunder __neg__ method allows you to negate an object using -
        Input: None
        Output: a ModularInt
        Side-Effects: None
        '''
        return ModularInt([(-ui)%p for ui,p in zip(self.modular_rep,self.primes_list) ],self.r)
    
    def __sub__(self, other: "ModularInt") -> "ModularInt":
        '''
        The dunder __sub__ method allows you to subtract objects using -
        Input: other is a modular int.
        Output: a ModularInt representing the difference self - other
        Side-Effects: None
        '''
        return self + (-other)
    
    def __mul__(self, other: "ModularInt") -> "ModularInt":
        '''
        The dunder method __mul__ allows you to multiply using *
        Input: other
        Output: A ModularInt representing the product self * other
        Side-Effects: None
        Note: This is a quick alternative to Karatsuba's algorithm, assuming the ModularInt representation of integers.
        '''
        assert self.r == other.r
        #TODO: define the product of self and other. 
        #First create a list. Use the list to define a ModularInt. 
        #Return the modularint (~2 lines.)
        pass
    
    def __pow__(self, other: int) -> "ModularInt":
        '''
        The dunder __pow__ method allows you to exponentiate using **
        Input: other is a non-negative integer.
        Output: A modular int representing self ** other
        '''
        assert isinstance(other, int) #We are only implementing positive integer powers.
        assert other >= 0
        if other == 1:
            return ModularInt(self.modular_rep,self.r)
        elif other == 0:
            return ModularInt.ModularInt_one(self.r)
        #TODO: Complete the power function by repeated squaring. (~7 lines)
    
    def __int__(self) -> int:
        '''
        This function allows you to convert a ModularInt to 
                the integer between 0 and the product of the 
                first self.r primes that represents it.
        Input: None
        Output: an integer
        '''
        #TODO: Follow Knuth's recipe on page 290 of TAOCP. (~15 lines)
        pass