"""
This code was modified this code from the course notes and describes the dynamic programming approach to the knapsack problem.
"""
def tabular_knapsack(objects:list[tuple[int,int]], W:int) -> list[list[int]]:
    """Expects objects to be a list of pairs of the form (value,weight). 
    Both value and weight are natural numbers.
    Expects W to be the capacity, a natural number.
    Returns a table, OPT, such that OPT[i][capacity] is the solution to
    the 0-1 knapsack problem when run on items[0:i+1] with capacity capacity."""
    n = len(objects)
    OPT = [[0]*(W+1)]#Temporarily fill in the row with 0's.
    
    # initialize the first row of the table
    for w in range(W+1):
        if objects[0][1] <= w:
            OPT[0][w] = objects[0][0]
        else:
            OPT[0][w] = 0
    
    # use the optimal substructure property to compute increasingly larger solutions
    for i in range(1,n):
        OPT.append([0]*(W+1)) #Temporarily fill in the row with 0's.
        v_i, w_i = objects[i]
        for w in range(W+1):
            if w_i <= w:
                OPT[i][w] = max(v_i + OPT[i-1][w-w_i], OPT[i-1][w])
            else:
                OPT[i][w] = OPT[i-1][w]
               
    #print(OPT)
    return OPT

def tabular_knapsack_value(objects:list[tuple[int,int]], W:int) -> int:
    """
    Inputs: a list of objects (each object is a pair: (value weight))
    """
    OPT = tabular_knapsack(objects,W)
    return OPT[len(objects)-1][W]
def tabular_knapsack_objects(objects:list[tuple[int,int]], W:int) -> list[tuple[int, int]]:
    """
    Input: objects is a list of pairs of the form (value, weight)
    Output: The objects that should be taken in an optimal solution.
    Note: calls tabular_knapsack
    """
    #TODO: Complete this function ~13 lines.
    pass