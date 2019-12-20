import numpy as np
import matplotlib.pyplot as plt
import math

init= -0.15/2
max_steps=300

def function(x, l=0.3, L=0.15, v_pri=0.3*3e+8): # unit is [m] and [s] description
   return ((l/2)/v_pri+x/v_pri)+math.sqrt(L**2+x**2)/3e+8


def integrate(max_steps=max_steps):
    data_steps = np.zeros([max_steps+1])
    data_steps[0] = init
    x = init

    for i in range(max_steps):
        x = function(x)
        data_steps[i+1] = x

    return data_steps

plt.plot(integrate(), color='r', linewidth=2.0, linestyle = "-", label = "0.3c")
plt.plot(integrate(), color='b', linewidth=2.0, linestyle = "-", label = "0.5c")
plt.plot(integrate(), color='g', linewidth=2.0, linestyle = "-", label = "0.8c")

plt.show()
plt.close()