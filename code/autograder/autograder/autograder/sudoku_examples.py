#Sources:https://norvig.com/easy50.txt

#This file contains examples of Sudoku puzzles. It also contains a function to check whether a cell violates sudoku rules. It was copied from Lab4.
def check_cell(board, r:int, c:int) -> bool:
        '''
        Input: r and c are indices of a cell. board is a doubly nested list of 1-9.
        Output: True/False, depending on whether this cell violates any Sudoku rule.
        '''
        val = board[r][c]
        if val == 0:
            return True

        # row
        for j in range(9):
            if j != c and board[r][j] == val:
                return False

        # column
        for i in range(9):
            if i != r and board[i][c] == val:
                return False

        # 3x3 box
        br = (r // 3) * 3
        bc = (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if (i != r or j != c) and board[i][j] == val:
                    return False
        return True

#They all get converted into the standard doubly-nested list of integers for use in lab4_sudoku_template.py

def to_list_format(puzzle: str) -> list[list[int]]:
    '''
    Returns the list format of a puzzle
    '''
    return [[int(entry) for entry in row] for row in puzzle.split() ]

puzzle1 = to_list_format('''000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000''')

puzzle2  = to_list_format('''
007256400
400000005
010030060
000508000
008060200
000107000
030070090
200000004
006312700
''')

puzzle3 = to_list_format('''
300200000
000107000
706030500
070009080
900020004
010800050
009040301
000702000
000008006
''')

easy_puzzle = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 0, 0]  # only 2 blank
]

medium_puzzle = [
    [5, 3, 0, 6, 7, 8, 9, 1, 2],
    [6, 0, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 0, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 0, 2, 3],
    [4, 2, 6, 8, 5, 0, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 0],
    [2, 8, 7, 0, 1, 9, 6, 3, 5],
    [3, 0, 5, 2, 8, 0, 1, 7, 9]
]

zero_puzzle = medium_puzzle =[[0 for c in range(9)] for row in range(9)]
vague_puzzle = [
    [9, 0, 0, 0, 6, 0, 8, 1, 2],
    [0, 0, 0, 7, 0, 3, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 4],
    
    [0, 0, 0, 0, 4, 0, 0, 0, 7],
    [0, 7, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    
    [4, 0, 6, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 4, 0],
    [0, 2, 0, 0, 8, 0, 0, 6, 0]
]

hard_puzzle = to_list_format(
'''
000596000
700300000
320800000
000001030
401000002
000060008
003000590
050008600
090000000
'''
)