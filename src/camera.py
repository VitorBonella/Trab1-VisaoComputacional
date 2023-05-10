import numpy as np
from rigid_body import RigidBody as rb

class Camera():
    def __init__(self, motion_matrix, focal_distance=50, width_px=1280, height_px=720, width_mm = 36, height_mm = 24):

        self.origin = np.eye(4)
        
        self.cam = np.dot(motion_matrix,self.origin)

        self.focal_distance = focal_distance
        
        self.width_px = width_px
        self.heigth_px = height_px
        self.width_mm = width_mm
        self.heigth_mm = height_mm

        #intrinsic parameters
        self.sx = width_px/width_mm
        self.sy = height_px/height_mm
        self.sdelta = 0 

        #intrinsic matrix
        self.intrinsic_matrix = np.eye(3)
        self.intrinsic_matrix[0,0] = focal_distance * self.sx
        self.intrinsic_matrix[0,1] = focal_distance * self.sdelta
        self.intrinsic_matrix[0,2] = width_px/2

        self.intrinsic_matrix[1,1] = focal_distance * self.sy
        self.intrinsic_matrix[1,2] = height_px/2

        #extrinsic matrix
        self.extrinsic_matrix = np.linalg.inv(motion_matrix)

        #projection matrix
        self.projection_matrix = np.hstack((np.eye(3),[[0],[0],[0]]))

        #image projection matrix
        self.img_projection_matrix = self.intrinsic_matrix@self.projection_matrix@self.extrinsic_matrix

    def camera_motion(self,motion_matrix):

        self.cam = np.dot(self.cam,np.dot(self.origin,motion_matrix))


    def get_pose(self,object):

        image = np.dot(self.img_projection_matrix,object)

        image_x = image[0]/image[2]
        image_y = image[1]/image[2]

        return image_x,image_y
