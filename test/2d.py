import numpy as np
import matplotlib.pyplot as plt


for i in range(1, 4):
  yu=plt.plot([-10, 10], [15, 15], c='Black')
  yd=plt.plot([-10, 10], [-15, -15], c='Black')
  plt.xlim(-20, 20)
  plt.ylim(-20, 20)
  l1,= plt.plot([-10+i, 10-i], [-15, 15])
#  plt.show(block=False)
  plt.show()
#  plt.close()
#  l2, =plt.plot([2, 4, 6])

#plt.show()
plt.close()
#print(plt.gca().lines)
