import numpy as np
from mpl_toolkits import mplot3d

from camera import Camera
from object import Object
from plot_utils import *
from rigid_body import RigidBody as rb

import re

from math import pi,radians

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
np.set_printoptions(precision=3,suppress=True)   

def initial_camera():
    Rx = rb.x_rotation(-pi/2)
    Rz = rb.z_rotation(pi/2)
    T = rb.translation(15,0,2)
    M = np.dot(np.dot(T,Rz),Rx)

    return Camera(motion_matrix=M,focal_distance=50)

def get_translation_by_string(translation_string):
    
    translation_tuple = eval(translation_string)

    T = rb.translation(translation_tuple[0],translation_tuple[1],translation_tuple[2])

    return T

def get_rotation_by_string(rotation_string,eixo):

    rotation_degree = float(rotation_string)
    eixo = int(eixo)

    rotation_rad = radians(rotation_degree)

    rotation_matrix = []

    if eixo == 1:
        rotation_matrix = rb.x_rotation(rotation_rad)
    elif eixo == 2: 
        rotation_matrix = rb.y_rotation(rotation_rad)
    elif eixo == 3:
        rotation_matrix = rb.z_rotation(rotation_rad)

    return rotation_matrix



def modify_state(cam,obj,translation_string,rotation_string,referencial):

    referencial = int(referencial) #string to int

    if rotation_string[0].lstrip('-').isdigit():
        #rotação
        R = get_rotation_by_string(rotation_string[0],rotation_string[1])

        cam.camera_motion(R,referencial)

    valid_translation = re.match('\([-.0-9]+,[-.0-9]+,[-.0-9]+\)',translation_string)
    if valid_translation:
        #translação
        T = get_translation_by_string(translation_string)
        
        cam.camera_motion(T,referencial)

    return cam
   

def gerar_imagens(cam,obj):
    
    obj_coord = obj.get_object()

    ax0 = set_plot()

    draw_arrows(cam.origin[:,-1],cam.origin[:,0:3],ax0)

    ax0.plot3D(obj_coord[0], obj_coord[1], obj_coord[2], 'red')
    ax0.scatter(obj.object[0,0], obj.object[1,0], obj.object[2,0],'b',marker="*")
    #ax0.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.object_points.vectors, color='r'))

    draw_arrows(cam.cam[:,-1],cam.cam[:,0:3],ax0)

    ax0.set_aspect('equal')

    plt.savefig("static/fig.png")

    image_x,image_y = cam.get_pose(obj.object)

    plt.clf()
    ax1 = ax0
    ax1 = plt.axes()
    ax1.set_title("Imagem")

    ax1.set_xlim([0,cam.width_px])
    ax1.set_ylim([cam.height_px,0])
    ax1.grid('True')

    ax1.plot(image_x,image_y)
    
    plt.savefig("static/fig2.png")
 