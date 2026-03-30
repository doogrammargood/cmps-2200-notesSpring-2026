# Lab 5: PocketCube Lab

## Introduction

In this lab, we will use Breadth First Search (BFS), Dijkstra's algorithm, and the A star algorithm to solve the PocketCube. These algorithms allow us to search the graph whose vertices are configurations of the PocketCube and whose edges are the allowed moves. See comments in PocketCube.py for a description of the puzzle.

This example demonstrates that the power of graph search algorithms lies in their ability to explore massive graphs that are too big to be held in memory. These graphs are defined implicitly by the neighborhood function. This is a common situation. The hope is the techniques needed to solve the PocketCube are generally applicable to a variety of problems.

## Lab Contents

### Files

This repo contains the following files:

|file name | Contents | Student Task|
|----------|----------|-------------|
|pocket_cube.py| Defines the PocketCube class, which inherits from ```PocketCubeBase```, ```PocketCubeDecomposition```, and ```PocketCubeAdvanced``` | Refer to for documentation.|
|pocket_cube_base.py| Defines basic functions of the PocketCube class | Use functions available here. No changes needed.|
|pocket_cube_decomposition.py| Defines functions for the PocketCube as a representation by permutations of cubies and twists of the cubies.| Use the functions ```PocketCube.get_permutation_twist_rep``` and ```PocketCube.get_facelist_from_permutation_twists```|
|pocket_cube_advanced.py|Defines some advanced functions of the PocketCube.| Ignore this file.|
|utils/timeout.py| Creates a timer decorator to stop code after a given duration.| Ignore this file.|
|examples.py| Gives some examples of usage of the PocketCube class.| Read and run examples to understand the PocketCube class.|
|tests.py| This file contains the tests for the code.| Make sure the tests pass when you run them. |
|pocket_cube_solver.py| This file will contain the functions to solve the cube.| All of your work is in this file. Rename it as ```pocket_cube_solver_solution.py```|
|readme.md| This file explains the contents of the lab.| Read this file.|

### Tasks

The lab will consist of three tasks, all of which are to be completed in ```pocket_cube_solver.py```

1. Implement breadth-first search (BFS) and Dijkstra's algorithm to solve small scrambles (length <5). You will notice that the implementations of these algorithms from the notes are inadequate. You should use a profiler to improve the performance of your implementations and use higher-order functions to make the algorithms flexible enough to allow a variety of approaches to a solution.

2. Use the methods ```PocketCube.get_permutation_and_twist_rep``` and ```PocketCube.get_facelist_from_permutation_twists``` to compute lower bounds on the number of moves needed to solve the cube. This is an application of Dijkstra's Algorithm.

3. Solve the PocketCube with the A star algorithm, using the lower bounds from the previous step as the heuristic.

## Further Information

### Mathematical Background of PocketCube Graph

The graph associated with the PocketCube has a vertex for every state of the cube and an edge when the states can be related by elementary moves, like twisting a face. The set of states forms a structure called a *group*. Generally speaking, a group is a set of transformations on an object. The elementary moves are called *generators* of the group whenever each configuration can be reached by applying the elementary moves. This occurs iff the graph is connected. Graphs whose vertices are a group and whose edges are generators are called *Cayley graphs*. They have nice symmetrical properties. Any configuration of the PocketCube could be considered as the solved state and the puzzle would still be the same.

The PocketCube is a special type of group. Its configurations can be decomposed uniquely into cubie positions and twists. Conversely, every permutation of the cubies and twists for them is a configuration of the PocketCube, as long as the sum of the twists is a multiple of $3$. We can consider the cubie positions alone as its own group $S_8$, ignoring their twists. The twists also form their own group $\mathbb{Z}_3^7$ if we ignore the cubie positions. The cube group is a semidirect product of the groups $S_8 \rtimes \mathbb{Z}_3^7$.

### Useful Resources

Jaap's Puzzle Page
https://www.jaapsch.net/puzzles/cube2.htm

Jaap's notes on computer solving
https://www.jaapsch.net/puzzles/compcube.htm

David Singmaster's original notes on the Rubik's Cube
https://maths-people.anu.edu.au/~burkej/cube/singmaster.pdf