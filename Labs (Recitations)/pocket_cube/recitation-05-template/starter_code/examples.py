#This file contains some examples and print statements that may help you.
from pocket_cube_solver import *
import cProfile
def solve_small_scramble_example():
    P=PocketCube()
    scramble_seq = P.scramble(length=5)
    solved_cube= PocketCube()
    solve_seq = solve_cube(P,method="dijkstra")
    P.perform_move_sequence(solve_seq)
    print("Scramble sequence ", scramble_seq)
    print("cost to scramble", PocketCube.move_sequence_cost(scramble_seq))
    print("solve sequence", solve_seq)
    print("cost to solve", PocketCube.move_sequence_cost(solve_seq))
    assert P==solved_cube

def solve_cube_example():
    #This example lets you test if you can solve a long scramble.
    scrambled_cube =PocketCube()
    scramble_seq = scrambled_cube.scramble(length=25) #you can comment this and uncomment the next 2 lines if you don't want a random example.
    #scramble_seq= ['R', 'U', 'L', 'Dp', 'Up', 'D', 'R', 'D', 'L2', 'Rp', 'U', 'F2', 'Dp', 'R']
    #scrambled_cube.perform_move_sequence(scramble_seq)
    print("scramble sequence: ", scramble_seq)
    solve_moves = solve_cube(scrambled_cube)
    scrambled_cube.perform_move_sequence(solve_moves)
    print("solve sequence: ", solve_moves)
    print("cost of solve sequence: ", PocketCube.move_sequence_cost(solve_moves))
    assert scrambled_cube.state == list(range(24))

def timed_example():
    #This example shows how you can use the profiler to get info about what's slowing your algorithm down.
    scrambled_cube =PocketCube()
    scramble_seq = ['Bp','U', 'R2', 'Dp', 'Dp', 'L']
    scrambled_cube.perform_move_sequence(scramble_seq)
    print("scramble sequence: ", scramble_seq)
    profiler = cProfile.Profile()
    profiler.enable()
    #found_node, visited = dijkstra(scrambled_cube,None, condition = lambda node: node.num_nonfixed()==(0,0))
    found_node,visited = BFS(scrambled_cube,condition = lambda node: node.num_nonfixed()==(0,0))
    profiler.disable()
    profiler.print_stats()

def invariants_example():
    p=PocketCube()

    Q=p.perform_move_sequence(['F','R'],mutate=False)
    Q.perform_move_sequence(['B2', 'L', 'B','D2','U','D','Lp','B2','L'], mutate=True)
    total_twist = 0
    scramble_seq = Q.scramble(length=3)

    for cubie in itertools.product([0,1],repeat = 3):
        total_twist += Q.get_twist_of_cubie(cubie)
    total_twist= total_twist%3


if __name__=='__main__':
    # #timed_example()
    # pocket_cube.change_cost_type("HTM")
    # print(pocket_cube.move_cost_dict)
    # print(pocket_cube.cost_type)
    # solve_cube_example()
    solve_small_scramble_example()
    #invariants_example()