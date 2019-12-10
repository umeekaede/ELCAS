import ctypes
import matplotlib.pyplot as plt

def main():
    xu_list=[]
    xd_list=[]

    f=open('value.dat', 'rt')
    for line in f:
        data=line[:-1].split(',')
        xu_list.append(float(data[0]))
        xd_list.append(float(data[1]))

    plt.ion

    for i in range(1, 200):
      yu=plt.plot([-10, 10], [15, 15], c='Black')
      yd=plt.plot([-10, 10], [-15, -15], c='Black')
      plt.xlim(-13, 13)
      plt.ylim(-20, 20)
      l1,= plt.plot([xd_list[i], xu_list[i]], [-15, 15])
    #  plt.show(block=False)
      plt.draw()
    #  q=input()
      plt.pause(0.3)
      plt.cla()
      if input()=='q':
          break
    plt.close()

if __name__=='__main__':
    main()
