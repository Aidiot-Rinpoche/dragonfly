"""
    straw hat function
"""
import numpy as np

def straw_hat(x):
    x1 = x[0]
    x2 = x[1]
    r = np.sqrt(np.square(x1)+np.square(x2))
    return np.true_divide(np.sin(r),r+0.0001)

def objective(x):
    return straw_hat(x)

def main(x):
    """Main function"""
    return straw_hat(x)

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X1 = np.arange(-15, 15, 0.25)
X2 = np.arange(-15, 15, 0.25)
X1, X2 = np.meshgrid(X1, X2)
x = [X1,X2]
z = straw_hat(x)


# Plot the surface.
surf = ax.plot_surface(X1, X2, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
 
# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
 
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
 
plt.show()
"""