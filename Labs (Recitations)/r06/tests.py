from unittest import TestCase
from edit_distance_solution import *
from longest_common_substring_solution import *
from knapsack_solution import *
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
class CreateTests(TestCase):
    #Tests for edit distance
    @weight(5)
    @number('1')
    def test_MED(self):
        test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('relevant', 'elephant')]
        for S, T in test_cases:
            assert fast_MED(S, T) == MED(S, T)

    @weight(5)
    @number('2')
    def test_align(self):
        def count_difference_from_aligned(S_align:str, T_align:str) -> int:
            '''Takes two aligned strings, S_align and T_align
            Returns the number of edits between the two strings.'''
            assert len(S_align)==len(T_align)
            assert len([index for index,char in enumerate(S_align) if T_align[index]=='-' and char=='-'])==0
            return len([(x,y) for x,y in zip(S_align,T_align) if x!=y or x=='-'])
    
        #Checks the test cases to make sure the alignments give the same number of edits as MED.
        test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('relevant', 'elephant')]
        for i in range(len(test_cases)):
            S, T = test_cases[i]
            align_S, align_T = fast_align_MED(S, T)
            assert align_S.replace('-', '') == S
            assert align_T.replace('-', '') == T
            assert count_difference_from_aligned(align_S,align_T)==MED(S,T)

    #tests for longest common subsequence/substring
    @weight(5)
    @number('3')
    def test_longest_common_subsequence(self):
        """
        Generally, the solution to longest_common_subsequence is not unique
        We wrote these tests by hand to ensure that there is a unique solution.
        """
        test_pairs_and_answers = [("01001abbacb0", "00abbacb1110",9,"00abbacb0"),
                                ("01001a2bbacb0", "00abbacb1110",9,"00abbacb0"),
                                ("answer1001000", "__answer",6,"answer"),
                                ("", "blank", 0, ""),
                                ("1", "w", 0, ""),
                                ("elephants", "relevants", 7, "eleants"),
                                ("","",0,"")]
        for S,T,length, common_subsequence in test_pairs_and_answers:
            assert length_longest_common_subsequence(S,T)==length
            assert longest_common_subsequence(S,T)==common_subsequence
        
    @weight(5)
    @number('4')
    def test_longest_common_substring(self):
        """
        Generally, the solution to longest_common_substring is not unique
        We wrote these tests by hand to ensure that there is a unique solution.
        """
        test_pairs_and_answers = [("01001abbacb0", "00abbacb1110",6,"abbacb"),
                                ("01001a2bbacb0", "00abbacb1110",5,"bbacb"),
                                ("answer1001000", "__answer",6,"answer"),
                                ("", "blank", 0, ""),
                                ("1", "w", 0, ""),
                                ("elephants", "relevants", 4, "ants"),
                                ("","",0,"")]
        for S,T,length,common_substring in test_pairs_and_answers:
            assert length_longest_common_substring(S,T) == length 
            assert longest_common_substring(S,T) == common_substring

    #test for knapsack
    @weight(10)
    @number('5')
    def test_tabular_knapsack_objects(self):
        test_scenarios = [(((10,5), (6,3), (7,2)),5),
                        (((20,5), (6,3), (7,2)),5),
                        (((1, 2), (3, 5), (4, 7), (6, 1), (2, 9), (8, 3), (5, 6)),15),
                        (((2, 0), (7, 4), (5, 3), (9, 1), (6, 8)), 11)
                        ]
        for objects, W in test_scenarios:
            value_check = tabular_knapsack_value(objects, W)
            taken_objects = tabular_knapsack_objects(objects,W)
            #print(taken_objects)
            value = sum([obj[0] for obj in taken_objects])
            #print(value, value_check)
            assert value ==value_check
if __name__=="__main__":
    unittest.main()