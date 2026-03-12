
'''
This file exists to compare the recursive backtracking algorithm with the depth-first search recursion

Note that in the Sudoku solve_backtracking() method, 
we don't need to keep track of visited, because the vertices are totally ordered, 
and we visit them in order.

Also, the underlying graph is a tree, so there is no risk of hitting a vertex that has been visited.

The recursive structure of depth first search is simple: 
        You call the recursive algorithm on each child. 

The Graph for sudoku. This is most naturally a Digraph.
Vertices: partial assignments of Sudoku that are filled left to right.
Edges: There is an edge from one partial assignment (A) to another (B) 
if B comes from filling in the first empty square of A with a number.
Hence, each vertex has 9 children, except for the leaves, which are the total assignments.


Code source: https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/

'''
def dfsRec(adj, visited, s, res): #This corresponds to the backtrack function.
    visited[s] = True
    res.append(s)

    # Recursively visit all adjacent vertices 
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)

def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

##--The rest of this sets up an example.
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    
    
if __name__ == "__main__":
    V = 5
    adj = []
    
    # creating adjacency list
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    # Perform DFS starting from vertex 0
    res = dfs(adj)

    for node in res:
        print(node, end=" ")