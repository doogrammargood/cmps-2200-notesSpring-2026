# Lab 4: Backtracking: Sudoku and Cliques

## Introduction

We have studied depth first search and recursive backtracking.
In this lab, we implement these ideas for sudoku.
We will implement the brute force solution,
                a recursive backtracking solution
            and a Python generator solution.

The Sudoku solution will be mostly given. By undertanding the technique to solve Sudoku, we can solve many problems. We will implement the ideas again to list all of the cliques of a graph.

The connection between the two problems is that they are both constraint satisfaction problems. 
In Sudoku, the constraints are the usual rules of sudoku.
For listing cliques, the constraints are that we want solutions where every pair of vertices are adjacent, so the edges serve as the constraints. There are many other constraint satisfaction problems, and recursive backtracking (aka depth first search) can be applied to all of them.

## Goals

### Theoretical Goals

- To understand backtracking algorithms
- To understand the connection between depth first search and backtracking
- To practice recognizing different applications of backtracking: in sudoku, and for listing cliques of a graph.
- To see examples where a brute force algorithm fails.

### Python Goals

- To understand iterators and generators
- To practice manipulating lists and indexing in Python.
- To practice manipulating graphs using the networkx package

### Skill Goals

- To practice reading code, understanding a solution (sudoku), and applying that solution in a different setting (listing cliques)

## Files

This project contains several files, which are summarized here:

| File Name | Contents | Purpose | TODO|
|-----------|----------|---------|-----|
|lab4.zip   |A compressed file that contains the entire project| This file exists to package the entire project as a single file.| Unzip this file to retrieve all the other files.|
|readme.md  | This current file, which describes the goal of the lab and the contents of the other files.| This file serves as the starting point for explaining the lab | Read this file.|
|dfs.py     |dfs.py contains the standard recursive depth first search (dfs), and comments about how dfs relates to backtracking in sudoku and listing cliques.|This file exists to facilitate comparing the dfs implementation to the backtracking implementations.| No action required.|
|sudoku_examples.py| This file contains several examples of sudoku puzzles.| The file exists so that we can test our sudoku solver on examples.|No action required.|
|lab4_sudoku_template.py| This file contains starter code to implement the backtracking algorithm for sudoku.| The purpose of this file is to provide an example of a backtracking algorithm.| One or two lines must be completed, and the file must be renamed as lab4_sudoku_solutions.py|
|lab4_cliques_template.py| This file contains starter code to implement the backtracking algorithm to list all cliques of a graph.| The purpose of this file is to provide an opportunity to check your understanding of backtracking by implementing it.| Follow the example set in lab4_sudoku_template.py to guide your implementation of a backtracking algorithm and an ```.__iter__()``` method. Rename the file as lab4_clique_solutions.py|
|test_for_lab4.py| This file contains tests that check your code| The purpose is to provide a basic check that the code is correct. The tests are not intended to be comprehensive | Make sure that all tests pass.|

## Iterables, Iterators, Generators

In this section, we describe iterables, iterators and generators. The terminology is extremely confusing.

Many tutorials can be found online. e.g. https://www.datacamp.com/tutorial/python-iterators-generators-tutorial
See the docstring of ```.__iter__()``` in lab4_sudoku_template.py for a specific example.

### Motivation

Python's lists are very powerful. Lists are examples of iterables, meaning that you can loop through them. If l is a list, then ```for x in l:``` is correct Python.

The drawback to lists is that they must be held entirely in memory. If the list is very large, then this can crash performance. For this reason, it is more efficient to use an object called a generator, whose values are only generated when they are needed. This concept is called lazy evaluation.

To give a concrete example, suppose that I am running a server to answer questions about graphs. A user inputs a graph, and requests several of the cliques of the graph. The difficulty is that the graph may have exponentially many cliques, so even expressing the full answer requires exponential time. Instead, we generate the cliques as the user requests them.

Generators are particularly important for datascience, where we have a massive stream of data that should not be held entirely in memory.

### Python Iteration Glossary

|term | description| creation | gotchas |
|-----|------------|-----|---------|
|iterable| An iterable is an object that you can loop through.| The function ```.__iter__()``` must be defined.| Iterables are not necessarily iterators. See below.|
|iterator| An iterator is an object that is returned by an ```.__iter__()``` method| An iterator must have ```.__iter__()``` (which returns ```self```) and ```.__next__()``` defined.|Every iterator is also an iterable, but not the reverse.|
|generator function | A generator function is a function that returns a generator object| A generator function looks like a function, except that it uses the word ```yield``` instead of ```return```. | Calling a generator function returns a generator object. See below. The word "generator" alone usually refers to a generator object.|
|generator object | A generator object is an object with ```.__next__()``` defined. It is a type of iterator| Generator objects can be returned by generator functions, or by using the parenthesis-comprehension syntax, e.g. ```(x for x in l)```.| Generator objects get used up as you iterate through them. Generator objects are iterators, but not necessarily the reverse.|
|```.__iter__()```| This dunder method marks an object as an iterable.| Define it in the class, like any other dunder method.| ```.__iter__()``` can either return an iterator (often  ```self``` if self has ```.__next__()``` defined and so ```self``` is an iterator) or yield a value, in which case ```.__iter__()``` is a generator function, which, when called, returns a generator object which is a type of iterator.|
|```.__next__()```| This dunder method dictates how to extract the next element during iteration.| Define ```.__next__()``` like any other dunder method. | ```.__next__()``` should be a function, not a generator function. Use ```return``` not ```yield```. Also, typically you want to call ```next(my_object)```, not ```my_object.__next__()```.|

## Networkx

Networkx is a standard Python module for manipulating graphs.
Documentation can be found here: https://networkx.org/en/

The following functions will be helpful. You should not need any networkx functions outside of this list. For this list, assume that G is a networkx graph.

|function | meaning | use in this lab| example | gotcha |
|---------|---------|----------------|---------|--------|
|```nx.cycle_graph(4)```| Creates a cycle graph of size 4. | Used to create a quick example graph.| ```G = nx.cycle_graph(4)```| No gotchas known|
|```G.nodes```| An iterable of the vertices of G.| to iterate through all of the nodes of G| ```if 0 in G.nodes:``` (to check if 0 is a node)| The nodes are typically the numbers 0,1,...,len(G)-1. This is always the case in this lab, but not always the case generally. ```G.nodes``` is actually not a list.|
|```G.neighbors(0)```| Returns an iterable of the neighbors of 0 in G. | This gives a way to check whether two vertices are adjacent, or get all of the neighbors of a vertex.|  If G is the 4-cycle, ```list(G.neighbors(0))=[1,3]```| ```G.neighbors(0)``` is not a list. Also, make sure ```0``` is actually a node of ```G``` |
|```G.subgraph([0,1,2])``` | Gets the induced subgraph containing the nodes 0,1,2. | The backtracking algorithm keeps track of a current clique, and augments it using a new vertex. This new vertex must be adjacent to all previous vertices in the clique. It must come from a particular subgraph of the original graph. Use in conjunction with ```G.neighbors(0)```| ```G.subgraph([0,1])``` is a networkx graph that contains two vertices (0 and 1) and an edge between them.|The nodes do not get renamed starting with 0 when you take a subgraph. This is good, because it means that the names are consistent.|
