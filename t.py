import sys
import numpy as np
import matplotlib.pyplot as plt
import math

# unit is [m] and [s] description
l=0.3
L=0.15
c=3e+8
v_pri=0.5*c

x=np.arange(-l/2., l/1.5, l/10.)
def func(x, v_pri):
  return ((l/2)/v_pri+x/v_pri)+np.sqrt(L**2+x**2)/(c)

# set grid and xlim
plt.grid(True)
plt.xlim([-0.15, 0.15])

# plot part
plt.plot(x, func(x, v_pri=0.3*c), color='r', linewidth=2.0, linestyle = "-", label = "0.3c")
plt.plot(x, func(x, v_pri=0.5*c), color='b', linewidth=2.0, linestyle = "-", label = "0.5c")
plt.plot(x, func(x, v_pri=0.8*c), color='g', linewidth=2.0, linestyle = "-", label = "0.8c")
plt.plot(x, func(x, v_pri=c    ), color='y', linewidth=2.0, linestyle = "-", label = "c")

# labeling part 
plt.xlabel('position[m]')
plt.ylabel('time[s]')
plt.legend(loc = "best")

plt.draw()
plt.pause(0.5)

plt.savefig("Separation.png")

key = input()
if key == 'q':
    sys.exit()

plt.close()