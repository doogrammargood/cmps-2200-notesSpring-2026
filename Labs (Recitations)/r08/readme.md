# Lab 8: Calculating the Independence Number via Tree Decomposition

## Introduction

We have seen that calculating the independence number is important for two reasons.

1. Many practical questions can be phrased in terms of calculating the independence number. For example, the scheduling problem for interval tasks is an instance of Independent Set.
2. The independence number problem is "NP-complete" meaning that an efficient general solution could be used to solve many problems of interest.

In this lab, we will investigate a technique to calculate the independence number for certain types of graphs. The technique shows that graphs can be understood through their *tree decompositions*. To calculate the independence number, we will calculate the tree decomposition and use its structure to construct an efficient dynamic program for the graph.

## Goals

This is the last lab in the class, and the most ambitious. The goals are listed in increasing order of conceptual demand.

- Practice the techniques that we have learned previously in a natural setting.
- Learn to recognize chordal graphs.
- Demonstrate the relationship between chordal graphs and tree decompositions.
- Relate tree decompositions to algorithmic techniques.

## Key Concepts

Most key concepts will be explained in notes in Week 10:tree_decompositions. Important concepts are collected here.

- A *Chordal Graph* is a graph that has no induced cycles of length greater than $3$.
- The *Tree decomposition* of a graph $G$ is a tree $T$ together with a function from $T$ to subsets of $V(G)$. The subset associated with a vertex $t\in V(T)$ is called a *bag*. The tree decomposition is assumed to satisfy three axioms.
    1. Every vertex is contained in some bag.
    2. Every pair of adjacent vertices appear together in some bag.
    3. The set of nodes $t\in V(T)$ whose bags contain a given vertex $v\in V(G)$ forms a connected subtree of $T$.
- The *treewidth* of a tree decomposition is one less than the size of the largest bag. Our algorithm is efficient when the treewidth is small.
- An *independent set* of a graph is a subset of vertices such that no pair of vertices in the subset is adjacent. The *independence number* of a graph is the size of a largest independent set.

## Steps to Calculate Independence Number via Tree Decomposition

This Lab involves many steps. Our goal is to calculate the independence number of a graph ```G```.

Here are some high-level steps to achieve our goal. Each step is explained in more detail in the docstrings for the relevant functions.

1. Define a "greedy search" function (sometimes called "maximum cardinality search") that repeatedly visits the next vertex with the most visited neighbors.
2. Use this greedy search algorithm to calculate a chordal completion of ```G```, ```G_chordal```, by adding appropriate edges until the graph is chordal.
3. Write an algorithm to get the tree decomposition (```TD```) of a chordal graph.
4. Use that tree decomposition as a decomposition of $G$ (```TD2```).
5. Calculate a topological ordering of the tree nodes of the decomposition, starting from an arbitrary root. This ordering ensures that we can fill in the dynamic programming table without referring to table entries that have not been calculated.
6. Calculate the independent sets in each bag (bags are (for example) ```TD2.H[t]```).
7. Define a dynamic program. The table's keys are pairs of tree nodes ```t``` and independent sets ```S``` of the bag associated with that treenode. Specifically, ```table[t][S]``` records the size of the maximum independent set of the union of the bags in the subtree rooted at ```t``` such that the intersection of the independent set with ```TD2.H[t]``` is exactly ```S```.
8. Use the table to compute the size of the largest independent set.
9. Use the standard techniques of backlinks to recover the independent set with the optimal size.
10. Check against NetworkX's builtin approximation for independent set for several examples.

## Files included in this lab

Here is a rundown of the files included in the lab and the role that each file plays. The files are listed in order of increasing dependencies on previous files.

| File name | Description | Purpose | Student Task | Rename?|
|-----------|-------------|---------|--------------|-------|
| chordal_graphs.py| This file contains functions for recognizing chordal graphs and calculating chordal completions of graphs. | Steps $1$ and $2$ our algorithm involve calculating the chordal completion.| Students will need to complete some functions in this file.|Rename this file as chordal_graphs_solution.py.|
|tree_decomposition.py| This file contains a class ```TreeDecomposition``` that represents the tree decomposition. | Steps $3$ and $4$ are achieved by this file. | The student will need to complete some functions in this file.| Rename this file as tree_decomposition_solution.py.|
|helper_functions.py| This file contains two functions that we have studied before, DFS and a brute force function to calculate independent sets.| We need DFS to calculate a topological order  in step $5$ so that the dynamic programming table is completed in a correct order. We use the brute force independent set function on each bag of the tree decomposition in step $6$.| No action needed| Do not rename this file.|
|independence_number_dp.py| This file contains the functions that calculate the independence number from the tree decomposition using dynamic programming.| This achieves the main goal of the lab in steps $7$, $8$ and $9$.| Students will need to complete some functions in this file. | Rename this file as independence_number_dp_solution.py|
|graph_examples.py| This file contains some functions to construct graphs that have small treewidth, so our algorithm is effective on them.| We need examples in order to test our algorithm.|No action needed | Do not rename this file.|
|example_tree_decomposition.py| This file contains a hard-coded example of a tree decomposition. | This hard-coded example exists for testing purposes.| No action needed |Do not rename this file.|
|tests.py| This file contains the tests for the lab.| It provides a basic check that the code is correct, which is step $10$.| Make sure the tests pass| Do not rename this file.|

## Gotchas

The lab is complicated, and there are many things that can go wrong.

- The tree decomposition object does not enforce correctness. Correctness can be checked with a provided function.
- When using the chordal order to make a graph chordal, be sure that the edges that you add don't affect the chordal order.
- The DFS function in helper functions has had several subtle bugs that should be fixed by now.
- There are many choices for what to store in the table. The choice recommended here is different from the textbook (Cygan et al's Parameterized Algorithms) and different from the warm-up problem about narrow grids, Homework 9 Problem 3.
- When calculating the table, you will need to refer to previous entries in the table.
- We repeatedly refer to a "topological order" of the tree of a tree decomposition. Technically, topological orders only refer to directed graphs. We choose an arbitrary vertex of the tree (using ```list(TD.T.nodes)[0]```) and treat it as a root. This allows us to treat the undirected graph as a directed graph by using the convention that each edge is oriented away from the root. The "topological order" is really a postorder traversal. The *children* of a tree node are defined relative to this direction.

## Resources

The concepts in this lab do not seem to appear in any single text. The ideas are drawn from several sources.
- [Knuth's 2012 christmas lecture](https://www.youtube.com/watch?v=txaGsawljjA)
    Good description of chordal graphs, but no mention of tree decompositions.
- [Cygan et Al's Parameterized Algorithms, Chapter 7](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf)
    Good description of tree decompositions, but no mention of chordal graphs.
- [Wikipedia page for tree decompositions](https://en.wikipedia.org/wiki/Tree_decomposition)
    Good first reference for tree decompositions, but no details about how to use them for dynamic programming.
- [A guided tour through treewidth](https://ics-archive.science.uu.nl/research/techreps/repo/CS-1992/1992-12.pdf)
    A good survey of the method that we are using, but it lacks many details.