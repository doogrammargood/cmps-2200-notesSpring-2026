'''
This file contains some examples on usage of the PocketCube class.
'''
from pocket_cube_solver_solution import *
import profile
import time

def first_example():
    '''
    This first example demonstrates the PocketCube class.
    '''
    P=PocketCube() #creates a new PocketCube
    print(P) #P has ascii printing.
    print("The moves available:", PocketCube.move_list)
    print("See PocketCube documentation for the meaning of each move.")
    moves = P.scramble(length=3)
    print(f"We scrambled P with the moves {moves}, resulting in {P}")
    print("We can reverse those moves.")
    reversed_moves = PocketCube.invert_move_sequence(moves)
    print("The reversed moves are the opposite moves in the opposite order.")
    print(f"{reversed_moves=}")
    print(P.perform_move_sequence(reversed_moves))
    print("P should be solved:", P)
    print("Our solution had cost", PocketCube.move_sequence_cost(reversed_moves))

def invariants_example():
    '''
    This example demonstrates the fact that 
    the total of the twists of the cube is always 0 modulo 3.
    '''
    P=PocketCube()
    Q=P.perform_move_sequence(['F','R'], mutate=False) #be aware of this mutate flag. Usually, 

    print("P is still not scrambled.", P)
    print("Q is scrambled.", Q)

    Q.perform_move_sequence(['B2', 'L', 'B','D2','U','D','Lp','B2','L'], 
                            mutate=True)
    print("we scrambed Q more", Q)
    print("A representation of Q as cubies and twists:", Q.get_permutation_twist_rep())

    twist_list = Q.get_permutation_twist_rep()[1]
    print("twist list of Q is", twist_list)

    print("total twists modulo 3 is", sum(twist_list)%3)

def solve_small_scramble_example():
    '''
    This example checks that you can solve a small scramble. 
    You should be able to do this once you complete BFS
    '''
    P = PocketCube()
    scramble_seq = P.scramble(length=5)
    solved_cube = PocketCube()
    solve_seq = solve_cube(P,method="dijkstra")
    P.perform_move_sequence(solve_seq)
    print("Scramble sequence ", scramble_seq)
    print("cost to scramble", PocketCube.move_sequence_cost(scramble_seq))
    print("solve sequence", solve_seq)
    print("cost to solve", PocketCube.move_sequence_cost(solve_seq))
    assert P==solved_cube

def solve_cube_example():
    '''
    This example lets you test if you can solve a long scramble.
    '''
    scrambled_cube =PocketCube()
    scramble_seq = scrambled_cube.scramble(length=25) #you can comment this and uncomment the next 2 lines if you don't want a random example.
    #scramble_seq= ['R', 'U', 'L', 'Dp', 'Up', 'D', 'R', 'D', 'L2', 'Rp', 'U', 'F2', 'Dp', 'R']
    #scrambled_cube.perform_move_sequence(scramble_seq)
    
    print("scramble sequence: ", scramble_seq)
    solve_moves = solve_cube(scrambled_cube)
    scrambled_cube.perform_move_sequence(solve_moves)
    print("solve sequence: ", solve_moves)
    print("cost of solve sequence: ", PocketCube.move_sequence_cost(solve_moves))
    
    assert scrambled_cube.is_solved()



if __name__=='__main__':
    #solve_cube_example()
    # solve_small_scramble_example()
    #invariants_example()
    first_example()