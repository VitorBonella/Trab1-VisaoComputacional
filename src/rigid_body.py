import numpy as np
from math import cos,sin

class RigidBody():

    def translation(dx,dy,dz):
        T = np.eye(4)
        T[0,-1] = dx
        T[1,-1] = dy
        T[2,-1] = dz
        return T
    
    def z_rotation(angle):
        rotation_matrix = np.array([[cos(angle),-sin(angle),0,0],
                                    [sin(angle),cos(angle),0,0],
                                    [0,0,1,0],
                                    [0,0,0,1]])
        return rotation_matrix
    
    def x_rotation(angle):
        rotation_matrix = np.array([[1,0,0,0],
                                    [0, cos(angle),-sin(angle),0],
                                    [0, sin(angle),cos(angle),0],
                                    [0,0,0,1]])
        return rotation_matrix

    def y_rotation(angle):
        rotation_matrix= np.array([[cos(angle),0, sin(angle),0],
                                   [0,1,0,0],
                                   [-sin(angle), 0, cos(angle),0],
                                   [0,0,0,1]])
        return rotation_matrix