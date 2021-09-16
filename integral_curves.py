import matplotlib.pyplot as plt

"""This is some sort of program for calculating and showing integral curves."""


# Integral step for population equation (returns 0 if population dies out)
def logstep(u):
    h = 0.1
    k = 0.028
    out = u + h * u * (1 - u) - k
    if out > 0:
        return out
    else:
        return 0


# Some numeric scheme for saving the integral curve for the integral step defined by func and initial conditions init
def intcurve(init, func):
    x = [p / 10 for p in range(0, 100)]
    # initial conditions
    y = [init]

    # solution
    while len(y) < len(x):
        yn = func(y[len(y) - 1])
        y.append(yn)
    return y


x = [p / 10 for p in range(0, 100)]
plt.plot(x, intcurve(0.5, logstep))
plt.show()
