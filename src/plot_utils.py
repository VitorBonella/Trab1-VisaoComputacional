import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def set_plot(ax=None,figure = None):
    if figure == None:
        figure = plt.figure(figsize=(8,8))
    if ax==None:
        ax = plt.axes(projection='3d')
    else:
        ax = plt.axes()
    
    ax.set_title("3d Plot")
    ax.set_xlim((-7.5,10))
    ax.set_xlabel("X axis")
    ax.set_ylim((0,12))
    ax.set_ylabel("Y axis")
    ax.set_zlim((-10,5))
    ax.set_zlabel("Z axis")
    return ax


def draw_arrows(point,base,axis,length=1.5):
    # The object base is a matrix, where each column represents the vector 
    # of one of the axis, written in homogeneous coordinates (ax,ay,az,0)
    
    # Plot vector of x-axis
    axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail',  length=length)
    # Plot vector of y-axis
    axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail',  length=length)
    # Plot vector of z-axis
    axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail',  length=length)

    return axis 