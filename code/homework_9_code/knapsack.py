"""
This code was copied and modified from Lab 6.
The code is correct assuming that all values and weights are positive.
"""

def safe_access(OPT,i,w,W):
    """
    Use this funtion to handle IndexErrors.
    """
    #TODO: Modify this function so that it safely accesses OPT.
    return OPT[i][w]

def tabular_knapsack(objects:list[tuple[int,int]], W:int) -> list[list[int]]:
    """Expects objects to be a list of pairs of the form (value,weight). 
    Both value and weight are natural numbers.
    Expects W to be the capacity, a natural number.
    Returns a table, OPT, such that OPT[i][capacity] is the solution to
    the 0-1 knapsack problem when on items[0:i+1] with capacity capacity."""
    n = len(objects)
    # we'll rely on indices to also represent weights, so we'll index from 1...W 
    # in the weight dimension of the table
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
                OPT[i][w] = max(v_i + safe_access(OPT,i-1,w-w_i,W), safe_access(OPT, i-1, w,W))
            else:
                OPT[i][w] = safe_access(OPT,i-1,w,W)
               
    #print(OPT)
    return OPT

def tabular_knapsack_value(objects:list[tuple[int,int]], W:int) -> int:
    """
    Inputs: a list of objects (each object is a pair: (value weight))
    """
    OPT = tabular_knapsack(objects,W)
    return OPT[len(objects)-1][W]

if __name__=="__main__":
    #TODO:check what happens when some numbers are negative and see how to fix it.
    objects = [(2,5),(3,4),(1,6),(3,4),(2,2),(1,2),(7,3),(10,4)]
    value = tabular_knapsack_value(objects,10)
    assert value == 19
