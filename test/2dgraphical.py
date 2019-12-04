import numpy as np
import matplotlib.pyplot as plt

l1,= plt.plot([1, 2, 3])
plt.clf()
l2, =plt.plot([2, 4, 6])

plt.show()
print(plt.gca().lines)
