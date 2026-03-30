'''
The pocket cube is a 2x2x2 variant of the Rubik's cube.
It is equivalent to just the corners of the Rubik's cube.
This file contains the code for our PocketCube class, which simulates the pocket cube.

The pocket cube consists of 8 "cubies." Each cubie can be twisted in any of 3 ways.
If we specify the twist of 7 cubies, the last cubie's twist is fixed.
This means that there are 8!x3^7=88,179,840 states.
You might see the claim that there are 3,674,160 states. This is because there are 24 orientations of the entire cube.
But we are not accounting for these 24 orientations in this assignment.

Further information can be found on Jaap's puzzle page: https://www.jaapsch.net/puzzles/cube2.htm

The allowable moves consist of rotating a face of the cube clockwise 90, 180, or 270 degrees.
We denote the faces Front (F), Back(B), Right(R), Left(L), Up(U), Down(D). The notation is standard from David Singmaster's original notes on the Rubik's cube.
To denote a move, we name the face to turn, followed by a suffix.
If the face is alone, it is a 90 degree turn clockwise.
If the face is followed by "p" (for prime), we turn the face 270 degrees (or 90 degrees counter-clockwise).
If the face is followed by "2", we turn the face 180 degrees. 
For example, "F" stands for rotating the front face clockwise.
"F2" stands for rotating the front face 180 degrees.
The method PocketCube.perform_move("F2") will simulate rotating the front face of the cube 180 degrees.

There are multiple ways to quantify the smallest solution to the solved cube from a given state.
Quarter Turn Metric (QTM): Each 90 degree or 270 degree turn counts as 1 move. A 180 degree turn counts as 2 moves.
Half Turn Metric (HTM): Each allowable move counts as 1 move
General metrics: (ALT):  Assume we empirically determine how long it takes to perform each move. 
                        Assume for simplicity that each move and its inverse take the same amount of time.
                        Assume the amount of time each move takes is independent of the previous and subsequent moves.)
It is claimed that the pocket cube can be solved from any state in 11 moves using HTM and 14 moves using QTM.
But we consider global orientation to be different, so for us it should take at most 15 moves using HTM and 22 using QTM.

We will use Dijkstra's algorithm and Breadth First Search (BFS) to solve the pocket cube.
The number of states is too large to solve this directly, so we will need a better approach.
We will see that the A* algorithm can be fruitfully applied.

----Representing the PocketCube-----

Facelist Representation:

Our main representation of the state of the PocketCube is a list of length 24.
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

When the cube gets twisted, the faces of the cubies become permuted. 
We represent the state of the cube as a list of length 24 where the ith element contains the number of the face in position i.

Cubie Permutation Twist Representation:
          
We also have a system for naming the cubies. In the solved state, we name the 8 cubies according to
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

from pocket_cube_advanced import *

class PocketCube(PocketCubeAdvanced):
    '''
    This is the main object in this file. It simulates the pocket cube.
    Feel free to add any additional functionality to the cube here.
    But you should not need to, in order to complete the lab.
    '''