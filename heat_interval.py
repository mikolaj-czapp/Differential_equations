import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, pi
from matplotlib.colors import Normalize

"""This is a program that simulates the heat equation on an interval with Neumann boundary conditions (outward derivative
is zero. Simple Euler scheme is used. The output image shows the temperature on the interval over time with y axis being
the time."""

u, T = np.meshgrid(np.linspace(0, 1, 200), np.linspace(0, 100, 10000))
X, Y = np.meshgrid(np.linspace(0, 1, 200), np.linspace(0, 100, 10000))
NJ, NI = u.shape


# Initial condition
def u0(x):
    return sin(2 * pi * x)


# Return the i-th row of u
def row(i):
    return [u[i, x] for x in range(200)]


# Parameters for the equation and Euler scheme (dt and dx should stay small)
diff_const = 50
dt = 1 / 100

# Compute the state at time t
for t in range(NJ):
    for x in range(1, NI - 1):
        if t == 0:
            tmp = u[0, x]
            u[t, x] = u0(tmp)
            u[0, 0] = u0(0)
            u[0, NI - 1] = u0(NI - 1)
        else:
            u[t, x] = u[t - 1, x] + dt * diff_const * (u[t - 1, x - 1] + u[t - 1, x + 1] - 2 * u[t - 1, x])
            u[t, 0] = 0
            u[t, NI - 1] = u[t, NI - 2]

fig = plt.figure()
ax = Axes3D(fig)

# Creating plot
ax.plot_surface(X, Y, u, norm=Normalize(-1, 1.05), cmap='hot')

# show plot
plt.show()

## No idea what does not work here nor do I care at this point
# fig = plt.figure()
# ax = plt.axes(xlim=(0,50), ylim=(0, 5))
# line, = ax.plot([], [], lw=3)
#
#
# def init():
#     line.set_data([], [])
#     return line,
#
# def animate(i):
#     x = np.linspace(0, 50, 50)
#     y = row(10*i)
#     line.set_data(x, y)
#     return line,
#
# anim = FuncAnimation(fig, animate, init_func=init,
#                          frames=50, interval=1, blit=True)
#
#
# anim.save('sine_wave2.gif', writer='imagemagick')
