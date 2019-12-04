import matplotlib.pyplot as plt
import numpy as np

def case1():
  fig, ax=plt.subplots()
  num_plot=0
  fig.show()

  while time.time()-t_start <1:
      ax.clear()
      ax.plot(np.random.randn(100))
      plt.pause(0.001)
      num_plot+=1

  return num_plot

  if __name__== "__main__":
      case1()
