# Lab 7: Matroid Greedy Algorithms

In this lab, we will implement two greedy algorithms. They are closely related through the mathematical object known as the matroid.

## Problems and Motivations

### Minimal Spanning Tree

Given a graph with edge weights, find a minimal spanning tree.

Motivation: The nodes may represent research facilities. The edges may represent possible connections between facilities, and the edges may represent the cost of building that connection. In this context, the minimal spanning tree of the graph is the cheapest way to connect all research facilities.

### Optimal Matching

Given a bipartite $G=W\cup J$ and a weighting $val:J\to \mathbb{R}$, find the set of jobs $J^\prime \subset J$ such that $J^\prime$ can be matched with $W$, and the sum of values of $J^\prime$ is maximal.

Motivation: The set $W$ represents workers and $J$ represents jobs. Edges represent that a worker can perform a job. We assume each worker can only perform one job at a time. The function $val$ represents how much we value each job. The solution to the optimal matching problem is the most valuable set of jobs that we can accomplish with our workers.

Note: We saw in the lecture that there is an alternate formulation, in which our value function has $W$ as its domain. In that case, we viewed $val$ as a wage and sought a matching with minimum total wages to pay.

## Student Tasks

Complete kruskal.py to implement the greedy strategy. We have already implemented the consistency checks that determine whether an edge creates a cycle. Rename kruskal.py to kruskal_solution.py

Complete optimal_matching.py to implement the consistency checks that determine whether or not we have enough workers to take on a new job. The greedy strategy has already been implemented for you. Rename optimal_matching.py to optimal_matching_solution.py.