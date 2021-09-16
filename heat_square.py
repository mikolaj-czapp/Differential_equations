import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, pi
from matplotlib.colors import Normalize

from matplotlib.animation import FuncAnimation

"""This is a program that models the heat equation on a square with Dirichlet boundary conditions (constant on the 
boundary). We use here a simple Euler scheme for the computations. """

# Prepare the grid
X, Y = np.meshgrid(np.linspace(0, 1, 50), np.linspace(0, 1, 50))
NJ, NI = X.shape


# Set initial condition (this can be dramatically disconinuous, heat equation should smooth it out)
def u0(x1, x2):
    return sin(2 * pi * x1) * sin(2 * pi * x2)
    # return 1 if x1 < 0.5 and x2 < 0.5 else 0


# Parameters for the equation and Euler scheme (dt and dx should stay small)
DIFF_CONST = 1
dt = 0.3
dx = 1 / 500
res = []
k = 1500

# Compute the state at time T
for T in range(k):
    u, H = np.meshgrid(np.linspace(0, 1, 50), np.linspace(0, 1, 50))
    tmp = np.linspace(0, 1, 50)
    for x1 in range(1, NJ - 1):
        for x2 in range(1, NI - 1):
            if T == 0:
                u[x1, x2] = u0(tmp[x1], tmp[x2])
            else:
                t = len(res) - 1
                u[x1, x2] = res[t][x1, x2] + dt * (
                        res[t][x1 + 1, x2] + res[t][x1 - 1, x2] + res[t][x1, x2 + 1] + res[t][x1, x2 - 1] -
                        4 * res[t][x1, x2])
    for x in range(NI):
        u[x, 0] = u[x, 1]
        u[x, NI - 1] = u[x, NI - 2]
        u[0, x] = -1
        u[NI - 1, x] = 0
    res.append(u)


# Creating plot
fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# animation
norm = Normalize(-1, 1)
ax.set_zlim(-1.1, 1.1)


def animate(i):
    ax.collections.clear()
    ax.plot_surface(X, Y, res[i], norm=norm, cmap="RdPu_r")


ani = FuncAnimation(fig, animate, interval=70)
ani.save('SineWaveHeatEquation.gif', writer='imagemagick')
plt.show()