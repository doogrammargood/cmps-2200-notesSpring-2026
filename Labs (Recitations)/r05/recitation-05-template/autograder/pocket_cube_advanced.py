'''
This file contains advanced methods for the pocket cube.
They are not necessary for the lab, and so have been relegated to this file.
'''
import itertools
from pocket_cube_decomposition import *

class PocketCubeAdvanced(PocketCubeDecomposition):
    
    #avoiding_moves is a dictionary from cubies to the list of moves that don't change that cubie.
    avoiding_moves= {(0,0,0):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("F","D","R")],
                     (0,0,1):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("F","D","L")],
                     (0,1,0):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("F","U","R")],
                     (0,1,1):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("F","U","L")],
                     (1,0,0):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("B","D","R")],
                     (1,0,1):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("B","D","L")],
                     (1,1,0):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("B","U","R")],
                     (1,1,1):[mv for mv in PocketCubeBase.move_permutation_dict if mv[0] in("B","U","L")]}
    
    
    
    #This function can help you gague how close you are to a solution.
    def correctly_placed_cubies(self, other=None, orientation: bool = False):
        '''
        Input: other is a PocketCube or None.
        Returns: the number of cubies in the correct spot, relative to other. 
        Ignores the orientation if orientation==False
        By default, other=None, and we take this to mean that 
        we are comparing to the solved cube.
        '''
        if other is None:
            other=self.__class__()
        correctly_placed_cubies=[]
        if orientation==False:   
            for cubie in PocketCubeDecomposition.cubie_faces:
                face1,face2,face3 = PocketCubeDecomposition.cubie_faces[cubie]
                if {self.state[face1],self.state[face2],self.state[face3]}=={other.state[face1],other.state[face2],other.state[face3]}:
                    correctly_placed_cubies.append(cubie)
        else: #In this case, orientation==True and we check the order of the faces of the cubies by using lists.
            for cubie in PocketCubeDecomposition.cubie_faces:
                face1,face2,face3 = PocketCubeDecomposition.cubie_faces[cubie]
                if [self.state[face1],self.state[face2],self.state[face3]]==[other.state[face1],other.state[face2],other.state[face3]]:
                    correctly_placed_cubies.append(cubie)
        return correctly_placed_cubies    
    def get_adjacent_pair_of_correctly_placed_and_oriented_cubies(self,other=None):
        '''
        Input: other is a PocketCube to compare self to.
        Returns a pair of adjacent cubies that are in the correct spot with the correct orientation if they exist.
        #otherwise returns None.'''
        correctly_placed = self.correctly_placed_cubies(other=other,orientation=True)
        for c1, c2 in itertools.combinations(correctly_placed,2):
            if len([ "_" for x,y in zip(c1,c2) if x!=y])==1:
                return c1,c2
        return None
    
    @classmethod
    def sequence_is_basic(cls,move_seq):
        '''Returns true if the sequence cannot be obviously reduced. 
        Used to construct the commutators.'''
        prev = move_seq[-1]
        for mv in move_seq:
            if prev[0]==mv[0]:
                return False
            prev = mv
        return True
    @classmethod
    def commutators(cls,length = 2):
        '''Returns the iteratable of commutator moves, like ["R","L","Rp","Lp"] of length 2*length.
        Commutators are known to be helpful in solving rubik's-type puzzles.'''
        def commutate(move_seq):
            return move_seq + cls.invert_move_sequence(move_seq)[::-1]
        return itertools.chain.from_iterable([[commutate(list(move_seq)) for move_seq in itertools.product(cls.move_permutation_dict.keys(), repeat = rep) if cls.sequence_is_basic(move_seq)] for rep in range(2,length+1)] )
    
    def get_commutator_neighbors(self,length=2):
        '''Returns the set of cubes that can be reached using a commutator.'''
        return {(self.perform_move_sequence(move_seq,mutate=False), tuple(move_seq)) for move_seq in PocketCube.commutators(length=length)}
    def get_neighbors_avoiding(self, cubie):
        '''expects cubie to be a tuple, like(0,0,0)
        Returns the cubes that can be reached by moves that do not affect the cubie.'''
        return {(self.perform_move(move, mutate=False), move ) for move in self.__class__.avoiding_moves[cubie]}
