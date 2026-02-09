Pocket Cube Lab:

In this lab, we will explore BFS and Dijkstra's algorithm using the Pocket Cube. See comments in PocketCube.py for a description.

In class, we covered BFS and Dijkstra's algorithm. However, the small examples in the notes seemed a little artificial becasue the graphs were held entirely in memory. The power of these algorithms is that they can be applied to large graphs.

The graph associated with the pocket cube has a vertex for every state of the cube and an edge when the states can be related by elementary moves, like twisting a face. The set of states forms a structure called a group. Generally speaking, a group is a set of transformations on an object. The elementary moves are called generators of the group whenever each configuration can be reached by applying the elementary moves. This occurs iff the graph is connected. Graphs whose vertices are a group and whose edges are generators are called Cayley graphs. They have nice symmetrical properties. Any configuration of the pocket cube could be considered as the solved state and the puzzle would still be the same.

These graphs are defined implicitly by the neighborhood function. This is a common situation. So the hope is the techniques needed to solve the pocket cube are generally applicable to a variety of solutions.

The lab will consist of two parts:

1. Implement breadth-first search (BFS) and dijkstra's algorithm to solve small scrambles (length <5). You will notice that the implementations of these algorithms from the notes are inadequate. You should use a profiler to improve the performance of your implementations and use higher-order functions to make the algorithms flexible enough to allow a variety of approaches to a solution.

2. Solve the pocket cube. Ideally, with the shortest solution according to the costs of each move, which can be customized in the code. The ideas is that we can empircally time how long it takes someone to perform each move, then use these empirical times to design an optimal solution for them. You will notice that the number of configurations is too large to solve directly using BFS or dijkstra's algorithm. So you should use BFS or dijkstra's algorithm as steps within a larger algorithm to solve the cube. This larger algorithm could involve many ideas, such as:
   -using the number of correctly placed/oriented cubies as an estimate of how solved the cube is.
   -taking advantage of invariants to expedite the search, like the amount of twist.
   -using commutators (sequences like ['F', 'D', 'Fp' 'Dp'])
   -use ideas from the standard solutions on Jaap's.

We may give significant hints on Nov. 11.

We may hold a competition to see which team can find the shorest solution (on average). The algorithms must terminate within 1 minute per solution and should always give a correct solution. The winning team will get +20 points toward the final. This may change depending on how detailed the hints are on Nov. 11.

This repo contains the following files:
pocket_cube.py . . . . Contains the pocket_cube class that simulates the pocket cube.
examples.py . . . . . .Contains some examples from which I wrote tests.
readme.md . . . . . . .This file
utils . . . . . . . . .Contains a decorator that stops your code after a certain amount of time.
tests.py . . . . . . . Contains tests.

You should create a file called pocket_cube_solver.py and write your solving methods there.
You may modify any of the prewritten code.
