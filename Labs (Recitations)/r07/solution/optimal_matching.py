"""
Rename this file as optimal_matching_solution.py

This file contains the starter code for the greedy algorithm for the employment problem.

Goals:
- To see an example of a greedy algorithm.
- To introduce some concepts related to scheduling and assignment problems.
- To introduce the concept of alternating/augmenting path arguments in Graph Theory
- To see an example where code written at a high-level of abstraction can be easily applied in new settings (BFS from Lab 5).

Gotchas:
- The perspective differs a bit from the notes. Here, we seek to maximize the value of the jobs, rather than minimize the wages of the works.
    This is intentional to encourage you to work through the logic of alternating/augmenting paths.
- You will need to read the logic of the proof of the augmentation property of transversal matroids in Week 9 day 2, 
    then translate the logic into checking whether a job can be added.
- This file does not contain networkX graphs. The Kruskal's algorithm file does.
- There are several references to nonlocal variables. 
    Recall that Python can read nonlocal variables without explicitly using the nonlocal keyword.   

Problem Setup:
    Given: 1.) a list W of workers and a list J of jobs 
    and a bipartite graph on W+J whose edges represent 
    that a worker is qualified for the job,
           2.) and a value function val:J->R that represents how much we value accomplishing each job.
    Find: a list of jobs that maximizes this value, such that each job can be matched with a worker.
    
Solution Framework:
    We solve this problem with a greedy algorithm that is very similar to Kruskal's Algorithm.
    0. Initialize a list of worker/job pairs that will be used: current_workers_jobs, initially empty
    1. Loop through the jobs in decreasing order of their values.
    2. If a job can be added to current_workers_jobs while maintaining the property that there is a matching to W,
       then add the job to current_workers_jobs.
        2.1. To check if a job can be added, we check whether there is 
             an "alternating path" A path that starts at the job and whose edges alternate between unused edges of the G.
             See Course Notes for details.
        2.2 If there is an alternating path, use it to update current_workers_jobs.
    3. Return current jobs.

Data Format:
Throughout, we use the format:
G is a bipartite graph, expressed as an adjacency list. 
       Each vertex is a string. See tests for examples.
W,J are the partition of G, and so are lists of strings.
current_workers_jobs is a list of pairs of workers/jobs that form a matching in G.
"""



import random
from collections import deque
from typing import Callable

def generate_graph(W_size:int,J_size:int,num_worker_neighbors:int):
    """
    Args:
        W_size is the number of workers.
        J_size is the number of jobs.
        num_worker_neighbors is the number of jobs that each neighbor can perform.
    Returns:
        A triple W, J, G, where
        W is a list of strings, that represents the workers.
        J is a list of strings, that represents the jobs.
        G is a dictionary whose keys are strings and values are lists of strings.
            G represents a graph as an adjacency list.
    Note:
        This function can be used to create examples of graphs to test your algorithm.
    """
    while True: #I'm picking the edges randomly until every job can be done by some worker.
        W = ['w'+str(i) for i in range(W_size)]
        J = ['j'+str(i) for i in range(J_size)]
        G = {w: random.sample(J, num_worker_neighbors) for w in W} #Set the edges of G randomly based on the workers.
        for j in J:
            G[j]= [w for w in W if j in G[w]] #Adds the adjacencies for the jobs to make sure G is an undirected graph.
        if len([j for j in J if len(G[j])>0])==J_size: #check that every job in J has some worker that can perform it.
            break
    return W,J,G


def match(edges:list[tuple[str]],v:str) -> str:
    """
    Args:
        v to be a vertex.
    Edges are a list of edges in a matching.
    Returns: 
        the other vertex in the edge containing v,
        unless v is not matched. In that case, it returns None.
    """
    edges_incident_v = [e for e in edges if v==e[0] or v==e[1]]
    if len(edges_incident_v)==0:
        return None
    e = edges_incident_v[0]
    if v== e[0]:
        return e[1]
    elif v== e[1]:
        return e[0]
    
def BFS(source:str,
    condition:Callable,
    get_neighbors:Callable
    ) -> tuple[str, dict]:
    """
    Inputs: source is the node where the search starts.
            condition is a function that expects a node and returns a bool that is True if we've found what we're looking for.
            get_neighbors is a function that expects a node and returns the neigbors of that node.

    Returns returns the last node found and a dictionary: 
    The keys are the nodes found in the search, values are the previous node in the search.

    Note: Modify your implementation of BFS from the Lab 5 (PocketCube Lab).
    """
    #TODO: Complete this function, ~16 lines.
    pass
def augment(a:str, 
            current_workers_jobs: list[tuple[str]], 
            W:list[str], 
            J:list[str], 
            G:dict) -> list[tuple[str]]:
    """
    Args: 
        a is a job
        current_workers_jobs is a list of edges (w,j) that is a matching.
        W and J are lists of strings, representing workers and jobs respectively.
        G is an adjacency list representation of a bipartite graph on W and J.
    Returns:
        a matching containing current_workers_jobs. 
        The matching also contains the job a, if possible.
    Note:
        This function implements the alternating path argument. See Week 9 Day 2.
    """
    
    use_match_edge = False #This flag will determine which type of edge (in matching or not) that we are using in an alternating path.
    current = a
    
    def end_vertex_condition(vertex:str) -> bool:
        """
        Args:
            vertex is a worker or a job.
        Returns:
            True if vertex is in W and doesn't have a match in current_workers_jobs.
        """
        #TODO: Complete this function. ~4 lines.
        pass
    def get_neighbors(vertex:str) -> list[str]:
        """
        Args:
            vertex is a string, representing a worker or job.
        Returns:
            A list of 'neighbors' of vertex.
        Side-Effect:
            Toggles the truthvalue of use_match_edge
        Note: The 'neigbors' are either edges of G                    (if use_match_edge is False)
                                    or edges of current_workers_jobs. (if use_match_edge is True)
        """
        nonlocal use_match_edge
        #TODO: Complete this function ~8 lines
        pass
        
    e, visited = BFS(a,end_vertex_condition, get_neighbors)

    if e is None: #We don't find an end to the augmenting path starting at a.
        return current_workers_jobs #the matching is unchanged.
    else:
        #TODO: Complete this function ~8 lines.
        pass
    
def get_maximal_matched_jobs(W:list[str],
                             J:list[str],
                             G:dict,
                             value = lambda j: int(j[1:])) -> tuple[list[str],list[tuple[str]]]:
    """
    Args: 
        W is a list of workers.
        J is a list of jobs.
        G is a bipartite graph with parts W,J
        value is a function from J to non-negative real numbers 
                    that represents how much we value each job.
    By default, the value is the number of the job.

    Returns: a pair.The first coordinate is the list of jobs that achieves the maximal value. 
                    The second coordinate is the list of edges that achieves the pairing.
                    edges must be ordered pairs, (w,j). The job must be the second coordinate.
    """
    sorted_J = sorted(J,key=value)
    current_workers_jobs = []
    for j in sorted_J[::-1]: #loop through the jobs in reverse of their order.
        current_workers_jobs = augment(j,current_workers_jobs,W,J,G) #add j to the jobs of current_workers_jobs, if possible.
    return [j for w,j in current_workers_jobs], current_workers_jobs