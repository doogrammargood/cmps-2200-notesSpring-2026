'''
This file contains the PocketCubeDecomposition class that augements the PocketCubeBase class with
additional methods for working with the permutation twist representation, defined below.

--Permutation Twist Representation--

We have a system for naming the cubies. In the solved state, we name the 8 cubies according to
                        location           name      index   orientation  faces
                       Back  Top  Left:   (0,0,0)    0       1            [0,4,11]
                       Back  Top  Right:  (0,0,1)    1      -1            [1,9,10]
                       Back  Down Left:   (0,1,0)    2      -1            [12,19,22]
                       Back  Down Right:  (0,1,1)    3       1            [17,18,23]
                       Front Top  Left:   (1,0,0)    4      -1            [2,5,6]
                       Front Top  Right:  (1,0,1)    5      -1            [3,7,8]
                       Front Down Left:   (1,1,0)    6       1            [13,14,20]
                       Front Down Right:  (1,1,1)    7       1            [15,16,21]

We also give the same names to the 8 positions. 
We must be careful to not confuse whether we're discussing the cubie that is in a position (e.g. cubie position (0,0,0))
                                                 or the cubie that should be in a position (e.g  cubie          (0,0,0))

Each cubie has an orientation. 
-1 means that rotating the cubie counter-clockwise is the same as moving its largest face onto its smallest face.
 1 means that rotating the cubie         clockwise is the same as moving its largest face onto its smallest face.

This allows us to define the twist of a position. 
It is either 0, -1 or 1 depending on whether the cubie currently in the position 
       0: is oriented correctly, 
      -1: needs to be turned counter-clockwise, 
       1: needs to be turned clockwise
in order to align that cubie's largest face with the position's largest face.
    
A basic invariant of the cube is that the sum of the twists is always 0.
Other than this constraint, all cubie permutations and twists for the cubies can occur.

The permutation twist representation of the cubie is a list of length 8 
                            representing a permutation of the cubies
and a list of length 8 with values -1, 0, 1 representing twists in each position.
'''
import numpy as np
import itertools
from functools import total_ordering
from pocket_cube_base import *

class PocketCubeDecomposition(PocketCubeBase):
    '''
    This class aguments PocketCubeBase with additional methods.
    '''
    #--The following functions may be helpful to extract information about the PocketCube.---#
    #cubie_faces is a dictionary from cubies to the list of faces of that cubie. Each face is a number, 0-23
    cubie_faces={(0,0,0):[0,4,11],  #back  top  left
                 (0,0,1):[1,9,10],  #back  top  right
                 (0,1,0):[12,19,22],#back  down left
                 (0,1,1):[17,18,23],#back  down right
                 (1,0,0):[2,5,6],   #front top  left
                 (1,0,1):[3,7,8],   #front top  right
                 (1,1,0):[13,14,20],#front down left
                 (1,1,1):[15,16,21] #front down right
                 }

    #cubie_faces_rotations is a dictionary from cubies to {-1,1}. -1 means that rotating the cubie counterclockwise is the same as moving its largest face onto its smallest face.
    #                                                              1 means that rotating the cubie        clockwise is the same as moving its largest face onto its smallest face.
    cubie_faces_rotations={(0,0,0): 1,
                           (0,0,1):-1,
                           (0,1,0):-1,
                           (0,1,1): 1,
                           (1,0,0):-1,
                           (1,0,1):-1,
                           (1,1,0): 1,
                           (1,1,1): 1}
    
    #The next few methods help to extract information about the current state.
    def identify_cubie(self,position):
        '''
        Input: a position (cubie in solved state) 
        Returns the cubie currently in that position.
        '''
        faces = self.cubie_faces[position]
        faces = {self.state[faces[0]],self.state[faces[1]],self.state[faces[2]]}
        for index, cubie in enumerate(PocketCubeDecomposition.cubie_faces):
            if set(PocketCubeDecomposition.cubie_faces[cubie])==faces:
                return index
    def cubie_permutation(self):
        '''
        Returns a list of length 8 
        that represents the permutation of the cubies, 
        ignoring their orientations.
        '''
        return [self.identify_cubie(position) for position in itertools.product([0,1],repeat =3)]
    
    def get_twist_of_cubie(self,position):
        '''
        Expects position to be a cubie position.
        Returns 0, -1 or 1 depending on whether the cubie currently in posititon is oriented correctly, needs to be turned counter clockwise, or needs to be turned clockwise
        in order for the largest face of that cubie to be in the position of the largest face of the cubie in that position when the cube is solved.
        A basic invariant of the cube is that the sum of the twists is always 0.
        '''
        faces = self.cubie_faces[position]
        current_faces = [self.state[index] for index in faces] #The faces that are currently on the cubie.
        largest_current_face = max(current_faces) #The largest face of the cubie currently in position.

        largest_solved_face = max(faces) #The largest face of that cubie in the solved position.
        smallest_solved_face = min(faces)
        if largest_solved_face==self.state.index(largest_current_face):
            return 0
        elif smallest_solved_face ==self.state.index(largest_current_face):
            return -1*self.cubie_faces_rotations[position]
        else:
            return 1*self.cubie_faces_rotations[position]
    
    def cubie_twists(self):
        '''
        returns a list of the twists of cubies in each position.
        '''
        return [self.get_twist_of_cubie(position) for position in itertools.product([0,1],repeat =3)]

    #This function turns out to be very useful.
    def get_permutation_twist_rep(self):
        '''Returns a pair. The 0th element is the cubie permutation. 
                           The 1st element is a list of twists of cubies.'''
        return self.cubie_permutation(), self.cubie_twists()
    
    @classmethod
    def get_facelist_from_permutation_twists(cls,permutation:list[int],twists:list[int])-> list[int]:
        '''
        Args:
            permutation is a list of the numbers 0-7 that represents a permutation of the cubies.
            twists is a list of +1, -1 of length 8 that represents the twist of each cubie.
        Returns:
            A list of integers that can be used to create a PocketCube.
        This class method is part of the inverse of PocketCube.get_permutation_twist_rep().
        '''
        facelist = [-1] * 24 #temporarily write -1 to each entry
        cubies = list(itertools.product([0,1],repeat =3))
        for i, cubie_index in enumerate(permutation):
            position = cubies[i]
            cubie = cubies[cubie_index]
            faces = PocketCubeDecomposition.cubie_faces[cubie][:]
            twist = twists[i]

            #orient the faces so that the largest face is in the correct direction.
            if twist != 0: 
                if PocketCubeDecomposition.cubie_faces_rotations[position]  == 1:
                    target_index_for_max = 0
                else:
                    target_index_for_max = 1
                if twist == 1:
                    target_index_for_max = (target_index_for_max -1)//(-1) #swap 0 for 1 and vice versa

                while faces.index(max(faces))!=target_index_for_max:
                    faces = [faces[(j+1)%3] for j in range(3)] 
            
            #detect when cubies are flipped. Unflip them.
            min_index = faces.index(min(faces))
            max_index = faces.index(max(faces))
            middle_index = [index for index in range(3) if index not in [min_index, max_index]][0]
 
            if PocketCubeDecomposition.cubie_faces_rotations[cubie] == 1:
                index_directly_clockwise_of_max_index = min_index
            else:
                index_directly_clockwise_of_max_index = middle_index

            if PocketCubeDecomposition.cubie_faces_rotations[position] == 1:
                other_index_directly_clockwise_of_max_index = (max_index+1)%3
            else:
                other_index_directly_clockwise_of_max_index = (max_index-1)%3
            if index_directly_clockwise_of_max_index != other_index_directly_clockwise_of_max_index:
                faces[min_index], faces[middle_index] = faces[middle_index],faces[min_index]
            
            for j, index_to_fill in enumerate(PocketCubeDecomposition.cubie_faces[position]):
                facelist[index_to_fill] = faces[j]

        return facelist