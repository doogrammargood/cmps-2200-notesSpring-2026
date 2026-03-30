'''This file should contain all of the tools that you use to solve the cube.
Complete the #TODO's and rename this file as pocket_cube_solver_solution.py'''
from pocket_cube import *
from functools import lru_cache #used for caching
from heapq import heappush, heappop 
from collections import deque

def BFS(source,                                                  #source is the node where the search starts.
        condition = lambda cube: cube.is_solved(),  #condition is a function that expects a node and returns a bool that is True if we've found what we're looking for.
        get_neighbors=lambda cube: cube.get_neighbors(),         #get_neighbors is a function that expects a node and returns the neighbors of that node.
        continue_condition=lambda visited: True):                #continue_condition is a function that expects a the dictionary, visited. If function returns False, the search terminates.
    """
    Performs a breadth first search from a source node.

    Args:
        source: The starting node of the search. Could be any hashable type (no lists or sets). 
        condition (callable, optional): Function that takes a node and returns True 
            if the goal is reached. Defaults to a function that checks if 
            cube.state equals the solved state.
        get_neighbors (callable, optional): Function that takes a node and returns 
            its neighbors. Defaults to cube.get_neighbors().
        continue_condition (callable, optional): Function that takes the visited 
            dictionary and returns True if the search should continue. Defaults to always True.

    Returns:
        tuple: (last_node, visited)
            - last_node: The node found by the search  or None, if the search is discontinued.
            - visited (dict): Keys are nodes that have been visited, values are the last move (str) to reach that node 
              in the shortest path from the source.
    
    returns the last node found and a dictionary: 
    The keys are the nodes found in the search. 
    The value is the last move in the shortest paths to get to the key node.
    """
    frontier = deque() #deque is a doubly ended queue. You may need .append() .extend() and .popleft() methods.
    frontier.append((source,"_"))
    visited = {}
    #TODO: Complete this function ~11 lines

def dijkstra(
    source, 
    condition=lambda cube: cube.is_solved(),
    get_neighbors=lambda cube: cube.get_neighbors(),
    continue_condition=lambda visited: True
):
    """
    Performs Dijkstra's search from a source node.

    Args:
        source: The starting node of the search. Could be any hashable type (no lists or sets). 
        condition (callable, optional): Function that takes a node and returns True 
            if the goal is reached. Defaults to a function that checks if 
            cube.state equals the solved state.
        get_neighbors (callable, optional): Function that takes a node and returns 
            its neighbors. Defaults to cube.get_neighbors().
        continue_condition (callable, optional): Function that takes the visited 
            dictionary and returns True if the search should continue. Defaults to always True.

    Returns:
        tuple: (last_node, visited)
            - last_node: The last node found by the search (may be the goal or the last expanded node), or None, if the search space is exhausted.
            - visited (dict): Keys are nodes that have been visited, values are the last move (str) to reach that node 
              in the shortest path from the source.
    """
    frontier = []
    heappush(frontier, (0, source, "_")) #You will also need to use heappop, which pops from the heap.
    visited = {}  # store the final shortest paths for each node.

    #TODO: Complete this function, ~8 lines
    return None, visited

def A_star_search(
    source,
    heuristic,
    condition=lambda cube: cube.is_solved(),
    get_neighbors=lambda cube: cube.get_neighbors(),
    continue_condition=lambda visited: True,
):
    """
    Performs the A star search from a source node.

    Args:
        source: The starting node of the search. Could be any hashable type
        heuristic: a function that takes a node and returns a lower bound on the distance to a vertex that we are seeking.
        condition (callable, optional): Function that takes a node and returns True 
            if the goal is reached. Defaults to a function that checks if 
            cube.state equals the solved state.
        get_neighbors (callable, optional): Function that takes a node and returns 
            its neighbors. Defaults to cube.get_neighbors().
        continue_condition (callable, optional): Function that takes the visited 
            dictionary and returns True if the search should continue. Defaults to always True.

    Returns:
        tuple: (last_node, visited)
            - last_node: The last node found by the search (may be the goal or the last expanded node).
            - visited (dict): Keys are nodes visited, values are the last move to reach that node 
              in the shortest path from the source.
    """
    frontier = []
    heappush(frontier, (heuristic(source), source, "_"))
    visited = {}  # store the final shortest paths for each node.

    #TODO: Complete this method, similar to Dijkstra's algorithm. ~9 lines
    return None, visited

def get_path_from_search(source, target, visited):
    """
    Reconstructs the path from a source vertex to a target vertex using a visited dictionary.

    Args:
        source: The starting vertex (of type Pocket Cube). Typically, this is the scrambled cube.
        target: The destination vertex (of type Pocket Cube). Typically, this is the source cube.
        visited (dict): A dictionary where keys are vertices and values are 
            the move that leads to that vertex from its predecessor, expected to be the second output from a search function.

    Returns:
        list: A sequence of moves that takes you from the source to the target.

    Notes:
        - If you encounter a KeyError (e.g., "key error '_p'"), it may be because 
          the source and target are reversed. Try switching them.
    """
    move_sequence = []
    current = PocketCube(state = target.state)
    while current != source:
        mv = visited[current]
        if isinstance(mv, tuple):
            mv = list(mv)
        else: #in this case, mv is just a string.
            mv = [mv]
        mv = PocketCube.invert_move_sequence(mv)
        move_sequence.extend(mv)
        current.perform_move_sequence(mv)
    return PocketCube.invert_move_sequence(move_sequence)
def solve_small_scramble(cube:"PocketCube", method = "BFS") -> list[str]:
    '''
    Args:
        cube is a PocketCube to solve. 
        method is a string that allows you to choose between different functions
    Returns:
        A list of moves that return the cube to its original state.
    Side Effects:
        None. Does not modify cube.
    '''
    if method == "BFS":
        #TODO: complete this function ~1 line
        pass
    elif method == "dijkstra":
        _, visited = dijkstra(cube, condition=lambda cube: cube.is_solved())
    #TODO: recover the solve sequence ~1 line
    return solve_seq

def solve_cube_inefficiently(cube):
    '''A slow, complicated method to solve the cube.
        Returns:
            a list of moves to perform
        Notes:
            The method works by:
                1. Search near the solved cube and store the resulting dictionary.
                2. Search from the input cube for a cube that has two adjacent cubes with the same placement and orientation as a cube near the solved cube.
                3. Search for a solution that goes between the two cubes identified in step 2. If not, continue in step 2.
            The point of this method is to demonstrate that 
            it is possible to solve the PocketCube by using ad-hoc methods, 
            but it isn't as fast or clean as the A* method.
            It does not give optimal solutions.
    '''
    def similar_to_cube_in_solved_neighborhood(cube,solved_neighborhood):
        for nearly_solved_cube in solved_neighborhood:
            cubies = cube.get_adjacent_pair_of_correctly_placed_and_oriented_cubies(nearly_solved_cube)
            if cubies is None:
                continue
            else:
                cubie1, cubie2 = cubies
                nearby_solved, intermediate_neighborhood = dijkstra(cube,
                                                                    condition= lambda cube: cube==nearly_solved_cube, 
                                                                    get_neighbors=lambda cube: cube.get_neighbors_avoiding(cubie1) & cube.get_neighbors_avoiding(cubie2))
                if nearby_solved is None:
                    continue
                else: 
                    return nearby_solved, intermediate_neighborhood
        return False
    #Step 1:
    #print("step 1")
    solved_cube = PocketCube()
    _, solved_neighborhood = dijkstra(solved_cube, condition= lambda cube: False, continue_condition=lambda visited: len(visited)<=3*18**3)
    
    #Step 2:
    #print("step 2")
    nearby_scrambled, scrambled_neighborhood = dijkstra(cube, 
                                                        condition = lambda cube: similar_to_cube_in_solved_neighborhood(cube,solved_neighborhood))

    #(cubie1,cubie2),nearby_solved = [(nearby_scrambled.get_adjacent_pair_of_correctly_placed_and_oriented_cubies(nearly_solved) ,nearly_solved) for nearly_solved in solved_neighborhood if not nearby_scrambled.get_adjacent_pair_of_correctly_placed_and_oriented_cubies(nearly_solved) is None][0]
    nearby_solved, intermediate_neighborhood = similar_to_cube_in_solved_neighborhood(nearby_scrambled,solved_neighborhood)
    #Step 3
    #print("step 3")
    #_, intermediate_neighborhood = dijkstra(nearby_scrambled,condition= lambda cube: cube==nearby_solved, get_neighbors=lambda cube: cube.get_neighbors_avoiding(cubie1) & cube.get_neighbors_avoiding(cubie2))
    
    move_seq1 = get_path_from_search(cube,nearby_scrambled,scrambled_neighborhood)
    move_seq2 = get_path_from_search(nearby_scrambled,nearby_solved,intermediate_neighborhood)
    move_seq3 = get_path_from_search(solved_cube,nearby_solved, solved_neighborhood)
    move_seq3 = PocketCube.invert_move_sequence(move_seq3)
    return move_seq1+move_seq2+move_seq3

#This method is the preprocessing step for the A* algorithm.
@lru_cache(maxsize=None) #This decorator ensures that this function will only compute once. After that
def create_pruning_table():
    '''
    Args:
        None
    Returns:
        A pair of dictionaries: a cubie_table and a twist_table
        The keys are (respectively) twists of the cubies, and permutations of the cubies. They are the output of PocketCube.get_permutation_twist_rep()
        The values are the lengths of the shortest paths to an untwisted cube, and a cube where the cubies are in the correct locations, respectively.
    Notes:
        If the cost metric is fixed, the outputs of this function could be hardcoded. 
        This function takes about a minute to run on my machine.
    '''

    def get_twist_neighbors(twist_list):
        '''
        Args:
            twist_list is a tuple of -1, 0, 1 of length 8.
        Returns:
            A list of tuples (tl, mv), 
            where tl is the neighboring twist_list 
            that is the result of applying the move mv to twist_list.
        '''
        #TODO: Complete this method, ~2 lines.
        pass
    def get_permutation_neighbors(permutation):
        '''
        Args
            permutation is a tuple of numbers 0-7 that represents a permutation of the cubies.
        Returns:
            A list of tuples (p, mv), 
            where p is the neighboring permutation of the cubies
            that is the result of applying the move mv to permutation.
        '''
        #TODO: complete this method, ~2 lines.
        pass
    #TODO: use Dijkstra's algorithm to calculate a table of last moves in a shortest move sequence that solves 
    # the positions of the cubies (ignoring twists), and similarly for twists (ignoring positions of cubies), ~6 lines. 
    #TODO: Convert the previous output to the desired cubie_table and twist_table as described in the docstring.
    return cubie_table, twist_table
    
def solve_cube_A_star(P):
    '''
    Uses the A star search method to solve the cube.
    '''
    permutation_table, twist_table = create_pruning_table()
    def heuristic(cube:"PocketCube") -> float:
        '''
        The heuristic is the maximum of 
            1. the number of moves needed 
                to solve just the positions of the cubies
            2. the number of moves needed to solve just the twists

        '''
        #TODO: Complete this function, ~2 lines.
        pass
    visited = A_star_search(P, heuristic)[1]
    return get_path_from_search(P, PocketCube(), visited)

def solve_cube(cube, method="a_star"):
    '''provides a single function that lets you choose the method of solution using the method flag.
    Expects a scrambled cube, cube and a method to solve.
    Returns a move sequence that unscrambles the cube. Does not mutate cube.'''
    if method == "inefficient":
        return solve_cube_inefficiently(cube)
    elif method == "BFS":
        return solve_small_scramble(cube, "BFS")
    elif method == "dijkstra":
        return solve_small_scramble(cube, "dijkstra")
    elif method == "a_star":
        return solve_cube_A_star(cube)
    else:
        raise ValueError("Invalid method")