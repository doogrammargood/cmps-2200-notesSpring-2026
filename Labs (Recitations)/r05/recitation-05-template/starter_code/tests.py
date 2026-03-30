from unittest import TestCase
from pocket_cube_solver_solution import *
import unittest
from utils.timeout import timeout
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
import profile
import time
class TestsOfStarterCode(TestCase):
    '''
    These tests ensure that the starter code works as intended.
    '''
    def test_rotations(self):
        '''
        Check that each rotation has order 4.
        This is a basic assurance that the move permutations were written correctly.
        '''
        P = PocketCube()
        Q = PocketCube()
        for mv in PocketCube.move_permutation_dict:
            for i in range(4):
                P.perform_move(mv,mutate=True)
            assert P==Q 
    def test_scramble_unscramble(self):
        '''
        Check that scrambling, then performing the reverse moves unscrambles the cube.
        This is a basic assurance that move sequences are being inverted correctly.
        '''
        P=PocketCube()
        scramble_sequence = P.scramble()
        assert not P.is_solved() #This may occasionally fail if we scramble back to identity. But this is rare.
        unscramble_sequence = PocketCube.invert_move_sequence(scramble_sequence)
        P.perform_move_sequence(unscramble_sequence)
        assert P.is_solved()

    def test_twist_invariant(self):
        '''
        Checks that the total twist is always 0.
        '''
        P=PocketCube()
        P.scramble()
        for mv in PocketCube.move_cost_dict:
            Q = P.perform_move(mv)
            total_twist = 0
            for cubie in itertools.product([0,1],repeat = 3):
                total_twist += Q.get_twist_of_cubie(cubie)
            assert total_twist%3==0
    
    def test_list_from_permutation_twists(self):
        '''
        Checks that we can correctly reconstruct the cube from the permutations and twists.
        '''
        P=PocketCube()
        P.scramble()
        #P.perform_move_sequence(['Fp', 'Bp', 'Lp', 'U2', 'F2', 'R2', 'Lp', 'D2', 'Up', 'F2', 'D2', 'F2', 'F', 'B2', 'R2'])
        permutation, twists = P.get_permutation_twist_rep()
        facelist_from_permutation_twists = PocketCube.get_facelist_from_permutation_twists(permutation,twists)
        C = PocketCube(facelist_from_permutation_twists)
        assert P == C
        #assert False

class TestsOfStudentCode(TestCase):
    small_scrambles = [['F'],['U2'],['F','B'],['Bp','U','R2','Dp','L'], ['R','L','U','R','D'],['Dp','Up','R','B2','Lp']]
    large_scrambles = [['D', 'U', 'D', 'Rp', 'Rp', 'F', 'U', 'B', 'F', 'Dp', 'Up', 'R', 'Rp', 'L2', 'B', 'L2', 'F', 'U', 'R', 'Bp', 'U', 'B', 'Bp', 'Fp', 'L', 'U', 'R', 'Fp', 'L2', 'D'], 
                       ['Fp', 'F2', 'R2', 'L2', 'Lp', 'Up', 'Lp', 'Up', 'Fp', 'U', 'D2', 'B', 'U', 'L', 'R', 'Fp', 'R', 'R', 'L', 'R', 'D2', 'F', 'U', 'L2', 'B', 'Dp', 'B2', 'D', 'U', 'D'], 
                       ['B', 'Up', 'Fp', 'D2', 'U2', 'D2', 'R', 'Dp', 'Dp', 'U', 'D', 'U', 'Rp', 'L2', 'Lp', 'Lp', 'F', 'D', 'U2', 'R2', 'Dp', 'B2', 'Bp', 'Bp', 'F', 'Dp', 'U2', 'U2', 'U2', 'Lp'], 
                       ['Lp', 'F', 'L', 'D2', 'B', 'L2', 'Lp', 'L', 'R2', 'F', 'U', 'R', 'Bp', 'D2', 'R2', 'F', 'B', 'L2', 'L2', 'B2', 'D', 'Rp', 'B', 'Lp', 'B2', 'R', 'Lp', 'F2', 'L', 'F2'], 
                       ['Up', 'U2', 'U', 'Rp', 'Rp', 'U2', 'Lp', 'F2', 'Lp', 'U', 'R2', 'Dp', 'R', 'Dp', 'R2', 'Rp', 'Up', 'U2', 'U', 'B', 'L', 'Lp', 'L', 'B', 'L', 'B', 'B2', 'R2', 'Lp', 'L2'], 
                       ['U', 'R2', 'D', 'U2', 'Lp', 'F', 'F', 'Fp', 'Rp', 'L2', 'R', 'F', 'B', 'D2', 'D', 'R2', 'Dp', 'R', 'Up', 'F2', 'R', 'U', 'L2', 'Dp', 'L2', 'R', 'Up', 'Dp', 'D2', 'B2'], 
                       ['R', 'F2', 'F', 'Fp', 'Bp', 'D2', 'D2', 'D2', 'L', 'Dp', 'Lp', 'F', 'D', 'L', 'Rp', 'F', 'U2', 'U2', 'Fp', 'B', 'F2', 'B', 'F', 'L', 'Bp', 'Dp', 'U', 'Lp', 'Dp', 'D2']]

    @timeout(100)
    @weight(20)
    @number('1')
    @visibility('visible')
    def test_small_solution(self):
        for scramble_seq in type(self).small_scrambles:
            P=PocketCube()
            P.perform_move_sequence(scramble_seq)
            assert not P.is_solved()
            solve_sequence = solve_small_scramble(P)
            P.perform_move_sequence(solve_sequence)
            assert P.is_solved()
    
    @timeout(120*2) #this timer imposes a 120*1.5 second limit on this test.
    @weight(30)
    @number('2')
    @visibility('visible')
    def test_general_solution(self):
        '''
        This test checks that you can solve the cube generally.
        Don't submit to gradescope until this test passes locally, within the time limit. 
        Let me know if the test passes locally but not on gradescope.
        '''
        for scramble_seq in type(self).large_scrambles:
            P = PocketCube()
            P.perform_move_sequence(scramble_seq) #scramble the cube.
            assert not P.is_solved() #check that the cube is scrambled.
            solve_sequence = solve_cube(P) #use your method to find a solution
            P.perform_move_sequence(solve_sequence) #perform your solution.
            assert P.is_solved() #check that the cube is solved.

if __name__=="__main__":
    unittest.main()