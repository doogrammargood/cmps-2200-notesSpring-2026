"""
This file contains starter code for the longest common substring and longest common subsequence.

The difference is that a substring must be contiguous, whereas a subsequence can skip. 
For example, abcdefg has the substring cde, which is also a subsequence.
But the subsequence adg is not a substring, because those letters are not contiguous in the example string.

A "common substring" (common subsequence) of two strings S and T is a string that is a substring (subsequence) of both S and T.

The point of considering these two similar examples side-by-side 
is to explore where the nuance in the concepts becomes a nuance 
in the code. The goal is to better understand the dynamic programming paradigm.
"""

def _longest_common_substring(S:str, T:str) -> list[list[int]]:
    """Expects S and T to be strings.
    Returns a len(S)xlen(T) table.
    Table[i,j] will contain the length of the longest common substring of S[:i+1] and T[:j+1] that ends in S[i] and T[j]."""
    Table = [['_' for _ in range(len(T))] for _ in range(len(S))] 
    #TODO: Fill in table ~8 lines
    return Table

def length_longest_common_substring(S:str, T:str) -> int:
    """Returns the length of the longest common substring of S and T"""
    Table = _longest_common_substring(S,T)
    #TODO: Complete this function ~2 lines.

def arg_max(Table:list[list[int]]) -> tuple[int, int, int]:
    """expects Table to be 2-dimensional array of natural numbers.
    returns i,j,Table[i][j] such that Table[i][j] is maximal."""
    max_i=0
    max_j=0
    current_max = 0
    for i in range(len(Table)):
        for j in range(len(Table[0])):
            if Table[i][j]> current_max:
                current_max = Table[i][j]
                max_i, max_j = i,j
    #print(max_i,max_j)
    if max_i<len(Table) and max_j<len(Table[0]):
        max_entry = Table[max_i][max_j]
    else: 
        max_entry=0
    return max_i, max_j, max_entry

def longest_common_substring(S:str, T:str) -> str:
    """Returns the longest common substring of S and T
        Note: calls _longest_common_substring() and refers to the output table.
    """
    Table = _longest_common_substring(S,T)
    #TODO: Get the longest common substring from table and return it ~2 lines.

def _longest_common_subsequence(S:str,T:str) -> list[list[int]]:
    """Expects S, T to be strings.
    Returns Table such that Table[i][j] contains the length of the longest common subsequence of S[:i+1], T[:j+1]
    Note that subesquences are not required to be contiguous."""
    Table = [['_' for _ in range(len(T))] for _ in range(len(S))] 
    #TODO: Fill in Table. ~10 lines.
    return Table
def length_longest_common_subsequence(S:str, T:str) -> int:
    """
    Inputs: strings S and T
    Output: the length of the longest common subsequence of S and T.
    """
    Table=_longest_common_subsequence(S,T)
    #TODO: Return the length of the longest common subsequence ~2 lines.
def longest_common_subsequence(S:str, T:str) -> str:
    """
    Inputs: strings S and T
    Outputs the longest common subsequence between S and T.
    Note: Calls _longest_common_subsequence to create a table,
          uses the table to reconstruct the path.
    """
    #TODO: Return the longest common subsequence ~16 lines.
    pass