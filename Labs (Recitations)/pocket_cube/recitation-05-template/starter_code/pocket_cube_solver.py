#This file should contain all of the tools that you use to solve the cube.
#You can add whatever methods you want.
#Be sure that there is a solve method implemented here.
from pocket_cube import *
def BFS(source,                                                  #source is the node where the search starts.
        condition = lambda cube: cube.state == list(range(24)),  #condition is a function that expects a node and returns a bool that is True if we've found what we're looking for.
        get_neighbors=lambda cube: cube.get_neighbors(),         #get_neighbors is a function that expects a node and returns the neigbors of that node.
        continue_condition=lambda visited: True):                #continue_condition is a function that expects a the dictionary, visited. If function returns False, the search terminates.
    #returns the last node found and a dictionary: The keys are the nodes found in the search, 
    pass
def dijkstra(source,                                                  #source is the node where the search starts.
             condition = lambda cube: cube.state == list(range(24)),  #condition is a function that expects a node and returns a bool that is True if we've found what we're looking for.
             get_neighbors=lambda cube: cube.get_neighbors(),         #get_neighbors is a function that expects a node and returns the neigbors of that node.
             continue_condition=lambda visited: True):                #continue_condition is a function that expects a the dictionary, visited. If function returns False, the search terminates.
    #returns the last node found and a dictionary: The keys are the nodes found in the search, 
    #                                              The values are the last move to that key in a shortest path from source.
    pass
def solve_cube_method1():
    pass
def get_path_from_search(source,target,visited):
    #expects two vertices, source and target, and a dictionary, visited.
    #We assume that the keys of visited are vertices and the value is move that takes you to that key.
    #Returns a sequence of moves from source to target.
    pass
def solve_small_scramble(cube, method = "BFS"):
    if method == "BFS":
        _, visited = BFS(cube,condition=lambda cube: cube.state == list(range(24)))
    elif method == "dijkstra":
        _, visited = dijkstra(cube,condition=lambda cube: cube.state == list(range(24)))
    solve_seq = get_path_from_search(cube,pocket_cube(),visited)
    return solve_seq
def solve_cube(cube, method="dijkstra"):
    #provides a single function that lets you choose the method of solution using the method flag.
    #Expects a scrambled cube, cube and a method to solve.
    #Returns a move sequence that unscrambles the cube. Does not mutate cube.
    if method == "method1":
        return solve_cube_method1(cube)
    elif method == "BFS":
        return solve_small_scramble(cube, "BFS")
    elif method == "dijkstra":
        return solve_small_scramble(cube, "dijkstra")
    else:
        raise "Invalid method"