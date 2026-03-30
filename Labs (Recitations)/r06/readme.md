# Lab 6: Dynamic Programming Exercises

This lab consists of three dynamic programming exercises. It asks you to implement three algorithms from the notes.

## Goals

1. To understand the dynamic programming paradigm.
2. To practice retrieving the optimal solution from a table of optimal costs.
3. To practice creating recursive formulae from optimal substructures.

## Gotchas

- Remember that Python lists are mutable. If you create a list like ```[['_']*5]*10```, you may get errors, because each row references the same list. If one row changes, then all rows will change.
- Be sure to complete the dynamic programming tables in order so that each cell is filled in based on the values of previously-filled cells.
- You may need to add additional rows or columns to the dynamic programming tables to cover edge cases.
- Be aware of the subtle distinction that we are drawing between a substring and a subsequence (see Problem 3 description).
-

## Problems and motivations

Here is a description of the three problems in this lab.

Each problem comes with two parts: first, we calculate the value of the optimal solutions and store them in a table. Then, we use these values to reconstruct the optimal solution. This is a generalization of reconstructing optimal paths from their lengths in Dijkstra's algorithm.

### Problem 1: Knapsack

Given n items, each with various values and weights, and a knapsack of capacity $W$, what is the largest total value of items that you can fit into your knapsack?

Application: We often want to find the maximal number of items that will fit. For example, the capacity $W$ could be measured in Watts, and we may want to hook up computing units with a maximum total amount of compute, without overdrawing power.

### Problem 2: Edit distance

Given two strings, what is the minimal number of edits needed to make both the same? The edits are insertion, substitution and deletion.

Application: When you mistype, a program can offer typo suggestions based on valid words with a short edit distance. Could be useful for AI detection.

### Problem 3: Longest common substring/subsequence

Given two strings, what is the length of the longest common substring? What about subsequence? Here, we draw the distinction that a substring must consists of contiguous letters, whereas a subsequence is allowed to skip letters.

Application: These strings may be genomes and we may want do calculate similarities between the genomes.

### Student task

Complete knapsack.py, edit_distance.py and longest_common_substring.py.

Rename them as knapsack_solution.py, edit_distance_solution.py and longest_common_substring_solution.py, respectively.