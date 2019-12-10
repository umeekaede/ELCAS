# -*- coding: utf-8 -*-

import ctypes
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

def st_line(x1, x2, x):
    y=(30/(x2-x1))*(x-x1)-15
    return y

def main():
    xu_list=[]
    xd_list=[]

    f=open('value.dat', 'rt')
    for line in f:
        data=line[:-1].split(',')
        xu_list.append(float(data[0]))
        xd_list.append(float(data[1]))

#    print(xu_list)
    xu_list=np.array(xu_list)
    xd_list=np.array(xd_list)
#    print(xu_list, xd_list)
    plt.ion

    for i in range(1, 200):
      yu=plt.plot([-10, 10], [15, 15], c='Black', lw=10)
      yd=plt.plot([-10, 10], [-15, -15], c='Black', lw=10)
      plt.xlim(-13, 13)
      plt.ylim(-20, 20)
      #l1,= plt.plot([xd_list[i], xu_list[i]], [st_line(xd_list[i], xu_list[i], -12), st_line(xd_list[i], xu_list[i], 12)])
      if xd_list[i]!=xu_list[i]:
          l1,= plt.plot([-10, 10], [st_line(xd_list[i], xu_list[i], -15), st_line(xd_list[i], xu_list[i], 15)], c='Red')
      else:
          print("hogehoge")
          l1=plt.axvline(xd_list[i], c='Red')
          print("hogehoge")
      #l2,= plt.plot([xd_list[i], xu_list[i]], [-15, 15], color='Red') #for check
      plt.draw()

      #axprev = plt.axes([0.7, 0.01, 0.1, 0.04])
      #axnext = plt.axes([0.81, 0.01, 0.1, 0.04])
      #bnext = Button(axnext, 'Next')
      #bprev = Button(axprev, 'Previous')

      plt.pause(0.3)
      plt.cla()
      if input()=='q':
          break
    plt.close()

if __name__=='__main__':
    main()
