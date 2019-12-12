import numpy as np
import matplotlib.pyplot as plt

dt = 0.0025
init = 0.0001
max_steps = 100000


def function(x, r = 0.1, K = 20.0):
    return x + dt * (r * x * (1.0 - x / K))


def integrate(max_steps=max_steps):
    data_steps = np.zeros([max_steps+1])
    data_steps[0] = init
    x = init

    for i in range(max_steps):
        x = function(x)
        data_steps[i+1] = x+np.random.randn()

    return data_steps

print(integrate(max_steps))
plt.plot(integrate(max_steps))
plt.show()
