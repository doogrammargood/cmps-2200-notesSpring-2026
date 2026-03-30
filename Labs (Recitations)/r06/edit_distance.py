"""
This file contains starter code for the edit distance calculation algorithm.
"""

#We store the allowed edits in this dictionary.
#keys are edit types. 
#Values are (i,j,cost) where the edit causes us to recurse to subproblem
#S[i:], T[j:] and takes cost of cost.
edit_dict = {"Insert": (0,1,1),
             "Delete": (1,0,1),
             "Substitute": (1,1,1)}

def edit_function(edit:str, S:str, T:str) -> tuple[tuple[int,int],int]:
    """Expects edit to be one of "Insert", "Delete", "Substitute". We can add more edits here.
    Returns a new pair strings and a cost."""
    global edit_dict
    S_index, T_index, cost = edit_dict[edit]
    return (S[S_index:], T[T_index:]), cost

def MED(S:str, T:str, edits:list[str] = ["Insert", "Delete", "Substitute"]) -> int:
    """Expect S and T to be strings.
    Returns the minimal edit distance.
    Note: This function returns the minimal edit distance by recursion, without memoization or dynamic programming.
    """
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    else:
        if S[0] == T[0]:
            return MED(S[1:], T[1:])
        else:
            return min([edit_function(edit,S,T)[1] + MED(*edit_function(edit,S,T)[0]) for edit in edits])


def _fast_MED(S:str, T:str, edits:list[str] = ["Insert", "Delete", "Substitute"]) -> list[list[int]]:
    """Expect S and T to be strings.
    Returns a Table where Table[i][j] is the edit distance between S[i:] and T[j:]."""
    global edit_dict
    Table = [['_'] * (len(T) + 1) for _ in range(len(S) + 1)] #Will be a 2-d table to return.
    #TODO: Fill in Table using recursive formula. ~9 lines.
    return Table

def fast_MED(S:str, T:str ,edits :list[str] = ["Insert", "Delete", "Substitute"]) -> int:
    """
    Inputs: strings S and T.
    Output: The edit distance between S and T.
    This function should behave identically to MED, except that it uses _fast_MED to calculate faster by using dynamic programming.
    """
    return _fast_MED(S, T, edits= edits)[0][0]

def fast_align_MED(S:str, T:str, edits:list[str] = ["Delete", "Insert", "Substitute"]):
    """
        Inputs: S and T are strings. edits is a list of allowed edits.
        Returns: A pair of strings. The first string is S interspersed with -'s.
                                    The second string is T interspersed with -'s,
                                    so that the two strings line up.
        Note: calls _fast_MED(S,T,edits=edits) then uses output table to construct the alignment.
    """
    global edit_dict
    Table = _fast_MED(S,T,edits = edits)
    #TODO: Complete this function ~40 lines
    pass