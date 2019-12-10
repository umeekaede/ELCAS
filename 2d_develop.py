# -*- coding: utf-8 -*-
import ctypes
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

''' define function '''
def st_line(x1, x2, x):
    y=(30/(x2-x1))*(x-x1)-15
    return y

''' main content code '''
def main():
    ''' read data file  part'''
    xu_list=[]
    xd_list=[]

    f=open('value.dat', 'rt')
    for line in f:
        data=line[:-1].split(',')
        xu_list.append(float(data[0]))
        xd_list.append(float(data[1]))

    xu_list=np.array(xu_list)
    xd_list=np.array(xd_list)
    plt.ion

    ''' read file '''
    for i in range(1, 200):
      ''' plot Scintillator '''
      yu=plt.plot([-10, 10], [15, 15], c='Black', lw=10)
      yd=plt.plot([-10, 10], [-15, -15], c='Black', lw=10)

      ''' adjust x,y range '''
      plt.xlim(-13, 13)
      plt.ylim(-20, 20)
      ''' plot y=a*x+b '''
      if xd_list[i]!=xu_list[i]:
          l1,= plt.plot([-10, 10], [st_line(xd_list[i], xu_list[i], -15), st_line(xd_list[i], xu_list[i], 15)], c='Red')
      else:
          l1=plt.axvline(xd_list[i], c='Red')

      ''' draw part '''
      plt.draw()
      plt.pause(0.3)
      plt.cla()
      if input()=='q':
          break
    plt.close()

''' this is omajinai that excecute main()'''
if __name__=='__main__':
    main()