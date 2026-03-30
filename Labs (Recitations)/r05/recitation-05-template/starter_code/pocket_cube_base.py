'''
This file contains PocketCubeBase class, which contains the basic methods for the PocketCube.

To represent a state of the pocket cube, we will represent it by a list of length 24.
The numbers in the list represent the faces of the cubies according to the following diagram.

          +----+----+
          | 0  | 1  |
          +----+----+
          | 2  | 3  |
+----+----+----+----+----+----+----+----+
| 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 |
+----+----+----+----+----+----+----+----+
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
          +----+----+
          | 20 | 21 |
          +----+----+
          | 22 | 23 |
          +----+----+
'''
import numpy as np
from functools import total_ordering


def determine_move_permutations():
    '''
    Returns a dictionary whose keys are moves
    The values are pairs, the permutations enacted by those moves.
    This function will be called once and used when defining our PocketCube class.
    '''
    moves =[direction+suffix for direction in ["F","B", "R","L", "U","D"] for suffix in ["","p","2"]]
    def rotate_F(state): #Rotate the front face clockwise.
        new_state = state[:]
        new_state[6] = state[14]
        new_state[7] = state[6]
        new_state[15] = state[7]
        new_state[14] = state[15]
        #---
        new_state[2] = state[13]
        new_state[3] = state[5]
        new_state[8] = state[2]
        new_state[16] = state[3]
        new_state[21] = state[8]
        new_state[20] = state[16]
        new_state[13] = state[21]
        new_state[5] = state[20]
        return new_state
    def rotate_R(state):
        new_state = state[:]
        new_state[8] = state[16]
        new_state[9] = state[8]
        new_state[17] = state[9]
        new_state[16] = state[17]
        #----
        new_state[3] = state[15]
        new_state[1] = state[7]
        new_state[10] = state[3]
        new_state[18] = state[1]
        new_state[23] = state[10]
        new_state[21] = state[18]
        new_state[15] = state[23]
        new_state[7] = state[21]
        return new_state
    def rotate_U(state):
        new_state = list(range(24))
        new_state[0] = state[2]
        new_state[1] = state[0]
        new_state[3] = state[1]
        new_state[2] = state[3]
        #---
        new_state[5] = state[7]
        new_state[4] = state[6]
        new_state[11] = state[5]
        new_state[10] = state[4]
        new_state[9] = state[11]
        new_state[8] = state[10]
        new_state[7] = state[9]
        new_state[6] = state[8]
        return new_state
    def rotate_L(state):
        new_state=state[:]
        new_state[4]= state[12]
        new_state[5]= state[4]
        new_state[13]=state[5]
        new_state[12]=state[13]
        #---
        new_state[0]= state[19]
        new_state[2]= state[11]
        new_state[6]= state[0]
        new_state[14]=state[2]
        new_state[20]=state[6]
        new_state[22]=state[14]
        new_state[19]=state[20]
        new_state[11]=state[22]
        return new_state
    def rotate_D(state):
        new_state=state[:]
        new_state[20] = state[22]
        new_state[21] = state[20]
        new_state[23] = state[21]
        new_state[22] = state[23]
        #---
        new_state[14] = state[12]
        new_state[15] = state[13]
        new_state[16] = state[14]
        new_state[17] = state[15]
        new_state[18] = state[16]
        new_state[19] = state[17]
        new_state[12] = state[18]
        new_state[13] = state[19]
        return new_state
    def rotate_B(state):
        new_state = state[:]
        new_state[10] = state[18]
        new_state[11] = state[10]
        new_state[19] = state[11]
        new_state[18] = state[19]
        #----
        new_state[17] = state[22]
        new_state[9] = state[23]
        new_state[1] = state[17]
        new_state[0] = state[9]
        new_state[4] = state[1]
        new_state[12] = state[0]
        new_state[22]= state[4]
        new_state[23] = state[12]
        return new_state
    to_return = {}
    for mv in moves:
        mv_permutation = list(range(24))
        if len(mv)==1:
            num_rotations = 1
        elif mv[1]=="2":
            num_rotations = 2
        else:
            num_rotations = 3
        for i in range(num_rotations):
            if mv[0]=="R":
                mv_permutation = rotate_R(mv_permutation)
            elif mv[0]=="L":
                mv_permutation = rotate_L(mv_permutation)
            elif mv[0]=="U":
                mv_permutation = rotate_U(mv_permutation)
            elif mv[0]=="D":
                mv_permutation = rotate_D(mv_permutation)
            elif mv[0]=="B":
                mv_permutation = rotate_B(mv_permutation)
            elif mv[0]=="F":
                mv_permutation = rotate_F(mv_permutation)
        to_return[mv] = mv_permutation
    return to_return

@total_ordering #this decorator allows all six comparison operators < <= == != > >= based on the definitions of only __lt__ and __eq__.
class PocketCubeBase(object):
    '''
    This is the main object in this file. It simulates the pocket cube.
    '''

    #move_permutation_dict is a dictionary from moves to permutations. The permutation is the permutation of the 24 cubie faces.
    move_permutation_dict = determine_move_permutations()#This function only gets called once, when the class is defined.
    
    #The costs are encoded as the values of move_cost_dict. The keys are moves.
    #The costs are summarized by a string, the class variable, cost_type. 
    #To change the cost_move_dict, use the class method PocketCube.change_cost_type("QTM")
    cost_type = "ALT"
    move_cost_dict = {m: 2 if len(m)==1 or m[1]=="p" else 3 for m in move_permutation_dict}
    move_list = [mv for mv in move_permutation_dict]
    #--Dunder Methods--#
    def __init__(self, state=list(range(24))):
        '''by default, the cube is initialized in the solved state.'''
        self.state = state
    def __repr__(self):
        '''Prints the state of the pocket cube as an ASCII diagram.
        ChatGPT was helpful with this, but its output needed some tweaking'''
        def pad(num): 
            '''expects num to be a 1 or 2 digit number.
                Returns a string of length 2 that represents that number.'''
            return f"{num:2}"
        
        foldout = f"""
          +----+----+
          | {pad(self.state[0])} | {pad(self.state[1])} |
          +----+----+
          | {pad(self.state[2])} | {pad(self.state[3])} |
+----+----+----+----+----+----+----+----+
| {pad(self.state[4])} | {pad(self.state[5])} | {pad(self.state[6])} | {pad(self.state[7])} | {pad(self.state[8])} | {pad(self.state[9])} | {pad(self.state[10])} | {pad(self.state[11])} |
+----+----+----+----+----+----+----+----+
| {pad(self.state[12])} | {pad(self.state[13])} | {pad(self.state[14])} | {pad(self.state[15])} | {pad(self.state[16])} | {pad(self.state[17])} | {pad(self.state[18])} | {pad(self.state[19])} |
+----+----+----+----+----+----+----+----+
          | {pad(self.state[20])} | {pad(self.state[21])} |
          +----+----+
          | {pad(self.state[22])} | {pad(self.state[23])} |
          +----+----+
        """
        return foldout
    def __eq__(self,other):
        return self.state==other.state
    def __hash__(self):
        '''
        Note:
            We need to define this dunder method in order to use pocket cubes as keys in a dictionary.
            The implementation below appears to be the most efficient way to hash a list.
        '''
        return hash(tuple(self.state))
    def __lt__(self,other):
        '''
        We need to be able to compare pocket cubes to put them in a heap.
        The comparison is arbitrary. This appears to be the fastest way to do it.
        '''
        return tuple(self.state)<tuple(other.state)
    
    #The next two functions are important.
    def is_solved(self):
        '''
        Returns True or False, based on whether the cube is solved or not.
        '''
        return self.state == list(range(24))
    def perform_move(self, move,mutate=False):
        '''
        Expects move to be a string, like "Fp", "R2" or "L".
        If mutate, mutates self by performing move and returns none. 
        Otherwise, returns a new pocket cube whose state is that of self, after performing move.
        '''
        new_state = [self.state[index] for index in PocketCubeBase.move_permutation_dict[move]]
        if mutate:
            self.state = new_state
        else:
            return self.__class__(state = new_state)
    def perform_move_sequence(self, move_sequence,mutate=True):
        '''
        Expects move_sequence to be a list of moves, like ["F","B2","Rp"]
        Either returns None and mutates self (if mutate=True)
        Or returns a new cube and does not affect self.
        '''
        if mutate:
            for move in move_sequence:
                self.perform_move(move,mutate=True)
        else:
            cube = self.__class__(state = self.state)
            for move in move_sequence:
                cube.perform_move(move,mutate=True)
            return cube

    def scramble(self,length:int=30) -> list[str]:
        '''Scrambles the cube by randomly turning it length number of times.
        Returns the list of moves used to scramble it.'''
        scramble_sequence = np.random.choice(list(PocketCubeBase.move_permutation_dict.keys()), size=length)
        self.perform_move_sequence(scramble_sequence)
        return [str(mv) for mv in scramble_sequence]
    
    #Some neighborhood functions. These can allow you to explore possible move sequences.
    def get_neighbors(self):
        '''Returns the set of cubes that can be reached using a quarter turn or half turn.'''
        return {(self.perform_move(move,mutate=False), move) for move in PocketCubeBase.move_permutation_dict}
    def get_half_neighbors(self):
        '''Returns the set of cubes that can be reached using a quarter turn.'''
        return {(self.perform_move(move,mutate=False), move) for move in PocketCubeBase.move_permutation_dict if move[-1] !="2"}
    
    @classmethod
    def move_sequence_cost(cls,move_sequence):
        '''Expects move_sequence to be a list of moves.
        Returns the sum of costs of the move sequence.'''
        return sum([cls.move_cost_dict[mv] for mv in move_sequence])
    
    @classmethod
    def invert_move_sequence(cls,move_sequence):
        '''move_sequence is a list of moves. For example, ['R','L','Dp']
        returns the move sequence that undoes move_sequence'''
        invert_sequence = []
        for mv in move_sequence[::-1]:#loop through move_sequence in reverse.
            if len(mv)==1:
                invert_sequence.append(mv+"p") #Replace a clockwise turn with the counterclockwise turn.
            elif mv[1]=='2':
                invert_sequence.append(mv) #A full turn is its own inverse.
            else:
                invert_sequence.append(mv[0]) #A clockwise turn inverts a counterclockwise turn.
        return invert_sequence
    
    @classmethod
    def change_cost_type(cls,new_cost_type):
        '''
        Expects new_cost_type to be "HTM", "QTM", "ALT", or the new move_cost_dict
        Updates the class variables PocketCube.class_type and PocketCube.move_cost_dict
        Returns None
        '''
        if new_cost_type is dict:
            cls.cost_type = "ALT"
            if not new_cost_type.keys() == cls.move_cost_dict.keys():
                raise "cost dictionary invalid" #invalid keys
            elif any([ not isinstance(new_cost_type[key],(int, float) ) or new_cost_type[key]<0 for key in new_cost_type]):
                raise "wrong type of values to set costs"
        elif new_cost_type == "HTM":
            cls.cost_type = new_cost_type
            cls.move_cost_dict = {m: 1 if len(m)==1 or m[1]=="p" else 1 for m in cls.move_permutation_dict}
        elif new_cost_type == "QTM":
            cls.cost_type = "QTM"
            cls.move_cost_dict = {m: 1 if len(m)==1 or m[1]=="p" else 2 for m in cls.move_permutation_dict}
        elif new_cost_type == "ALT":
            cls.cost_type = "ALT"
            cls.move_cost_dict = {m: 2 if len(m)==1 or m[1]=="p" else 3 for m in cls.move_permutation_dict}
        else:
            raise "changed cost_type incorrectly."