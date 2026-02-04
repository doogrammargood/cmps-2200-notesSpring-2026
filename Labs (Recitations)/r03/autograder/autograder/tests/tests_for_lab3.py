import unittest
import itertools
import functools
import random
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from lab3_solution import *
random.seed(50)

class TestCodeRuns(unittest.TestCase):
    def setUp(self):
        '''creates the lists of values and r_vals to check.'''
        self.r_vals = [10, 15, 20, 40, 50]
        self.values = [1,2,3,6,7,10,15,100,123] 
    @weight(10)
    @number('1')
    @visibility('visible')
    def test_addition(self):
        '''
        Tests that addition was implemented correctly.
        '''
        for r_val in self.r_vals:
            for a,b in itertools.combinations(self.values,2):
                assert a+b == int(ModularInt.create_ModularInt_from_value(a,r_val) + ModularInt.create_ModularInt_from_value(b,r_val)) 
    @weight(10)
    @number('2')
    @visibility('visible')
    def test_multiplication(self):
        '''
        tests that multiplication was implemented correctly.
        '''
        for r_val in self.r_vals:
            for a,b in itertools.combinations(self.values,2):
                assert a*b == int(ModularInt.create_ModularInt_from_value(a,r_val) * ModularInt.create_ModularInt_from_value(b,r_val)) 
    @weight(10)
    @number('3')
    @visibility('visible')
    def test_powers(self):
        '''
        Tests that exponentiation was implemented correctly.
        '''
        for r_val in self.r_vals:
            for a in self.values:
                for b in [0,1,2,3,5,7]:
                    assert (a**b% functools.reduce(lambda x,y: x*y,first_r_primes(r_val),1) 
                            == int(ModularInt.create_ModularInt_from_value(a,r_val) ** b))
    @weight(10)
    @number('4')
    @visibility('visible')
    def test_multiplication_self_test(self):
        '''
        Tests multiplication and addition against each other by testing the distributive property.
        '''
        for r in self.r_vals:
            for a,b in itertools.combinations(self.values,2):
                a1 = random.randint(0,functools.reduce(lambda a,b:a*b, first_r_primes(r)))
                a2 = a - a1
                b1 = random.randint(0,functools.reduce(lambda a,b:a*b, first_r_primes(r)))
                b2 = b - b1
                a_mod,b_mod = ModularInt.create_ModularInt_from_value(a,r), ModularInt.create_ModularInt_from_value(b,r)
                a1_mod,a2_mod = ModularInt.create_ModularInt_from_value(a1,r), ModularInt.create_ModularInt_from_value(a2,r)
                b1_mod,b2_mod =  ModularInt.create_ModularInt_from_value(b1,r), ModularInt.create_ModularInt_from_value(b2,r)
                assert (a1_mod + a2_mod) * (b1_mod+b2_mod) == a_mod * b_mod
if __name__=="__main__":
    unittest.main()