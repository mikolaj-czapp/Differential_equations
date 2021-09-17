import matplotlib.pyplot as plt
import numpy as np

"""A simple simulation of a predator-prey system (Lotka-Volterra equations). Uses a simple Runge-Kutta method.
The output images are plots of the predator and prey population and a phase portrait of the system."""

# Parameters for the equations
# dx/dy = Ax + Bxy
# dy/dx = Cxy - Dy
A = 7
B = 1
C = 2
D = 2
T = 300


def dx(x, y):
    return A * x - B * x * y


def dy(x, y):
    return C * x * y - D * y


def lot_vol(arr):
    return [dx(arr[0], arr[1]), dy(arr[0], arr[1])]

# Calculate integral curves
def intcurve_pair_RK(init1, init2, func):
    # warunki poczatkowe
    res = np.array([[init1, init2]])

    # rozwiązanie numeryczne
    while len(res) < T:
        h = 0.05
        try:
            k1 = h * np.array(func(res[len(res) - 1]))
            k2 = h * np.array(func(res[len(res) - 1] + k1 / 2))
            k3 = h * np.array(func(res[len(res) - 1] + k2 / 2))
            k4 = h * np.array(func(res[len(res) - 1] + k3))
            res = np.append(res, [res[len(res) - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6], axis=0)
        except:
            break
    res = res.T
    return res


# Extract the results
predator = intcurve_pair_RK(1, 2, lot_vol)[0]
prey = intcurve_pair_RK(1, 2, lot_vol)[1]

t = [p / 10 for p in range(0, T)]
plt.plot(t, predator, label='predator')
plt.plot(t, prey, label='prey')
plt.show()

plt.plot(predator, prey)
plt.show()
