from stl import mesh
import numpy as np

class Object():
    def __init__(self,stl_path = 'Dragon.stl'):

        self.object_points = mesh.Mesh.from_file(stl_path)

        self.x = self.object_points.x.flatten().T
        self.y = self.object_points.y.flatten().T
        self.z = self.object_points.z.flatten().T

        self.size = self.object_points.x.flatten().size

        self.object = np.array([self.x,self.y,self.z,np.ones(self.size)])

        self.object[0] = self.object[0] - self.object[0][0]
        self.object[1] = self.object[1] - self.object[1][0]
        self.object[2] = self.object[2] - self.object[2][0]

    def get_object(self):
        return self.object[0],self.object[1],self.object[2]

    def object_motion(self,motion_matrix):

        self.object = np.dot(self.object,motion_matrix)