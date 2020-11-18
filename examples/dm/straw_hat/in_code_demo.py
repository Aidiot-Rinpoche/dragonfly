from dragonfly import maximise_function
import numpy as np
import time

# local imports
try:
    from .straw_hat import straw_hat
except:
    from straw_hat import straw_hat

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def single_fidelity():
    """Main function"""
    domain_bounds = [[-20,20],[-20,20]]
    max_capital = 200
    time_start=time.time()
    opt_val,opt_pt,history=maximise_function(straw_hat, domain_bounds, max_capital)#,opt_method='rand')
    time_end=time.time()
    print('totally cost',time_end-time_start)
    curr_opt_points = history.curr_opt_points
    curr_opt_vals = history.curr_opt_vals 

    # plot sample points
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make function surface.
    X1 = np.arange(-20, 20, 0.25)
    X2 = np.arange(-20, 20, 0.25)
    X1, X2 = np.meshgrid(X1, X2)
    x = [X1,X2]
    z = straw_hat(x)

    # Make sample points
    n = len(curr_opt_vals)
    smaple_z = curr_opt_vals
    sample_x = np.zeros(n)
    sample_y = np.zeros(n)
    for idx in range(n):
        sample_x[idx] = curr_opt_points[idx][0]
        sample_y[idx] = curr_opt_points[idx][1]

    # Plot the surface.
    #surf = ax.plot_surface(X1, X2, z, cmap=cm.coolwarm，linewidth=0, antialiased=False)

    # Plot a basic wireframe.
    ax.plot_wireframe(X1, X2, z, rstride=10, cstride=10)
    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
 
    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.plot(sample_x, sample_y, smaple_z, label='parametric curve',c = 'red')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    single_fidelity()