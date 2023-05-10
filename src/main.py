import numpy as np
from mpl_toolkits import mplot3d

from camera import Camera
from object import Object
from plot_utils import *
from rigid_body import RigidBody as rb


from math import pi

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
np.set_printoptions(precision=3,suppress=True)   

Rx = rb.x_rotation(-pi/2)
Rz = rb.z_rotation(pi/2)
T = rb.translation(15,-5,6)
M = np.dot(np.dot(T,Rz),Rx)

cam = Camera(motion_matrix=M,focal_distance=50)

obj = Object('old_wolf3.stl')

obj_coord = obj.get_object()

print(f"Camera Origin \n {cam.origin}")

print(f"Camera Cam \n {cam.cam}")

ax0 = set_plot()

draw_arrows(cam.origin[:,-1],cam.origin[:,0:3],ax0)

ax0.plot3D(obj_coord[0], obj_coord[1], obj_coord[2], 'red')
ax0.scatter(obj.object[0,0], obj.object[1,0], obj.object[2,0],'b',marker="*")
#ax0.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.object_points.vectors, color='r'))

draw_arrows(cam.cam[:,-1],cam.cam[:,0:3],ax0)

plt.savefig("fig.png")

image_x,image_y = cam.get_pose(obj.object)

fig = plt.figure()
ax1 = plt.axes()
ax1.set_title("Imagem")

ax1.set_xlim([0,1280])
ax1.set_ylim([720,0])
ax1.grid('True')

ax1.plot(image_x,image_y)

plt.savefig("fig2.png")