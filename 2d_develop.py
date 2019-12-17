# -*- coding: utf-8 -*-
import ctypes
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import re
#from matplotlib.widgets import Button

f = open('lengthfile.dat', 'rt')
s=f.read()
print(s)
length = re.sub("\\D", "", s)
ulength=int(length)/2
dlength=-int(length)/2
print()

''' define function '''
def st_line(x1, x2, x):
    y = (int(length)/(x2-x1))*(x-x1)+dlength
    return y

''' main content code '''
def main():
    ''' read data file part'''
    xu_list = []
    xd_list = []

    f = open('value.dat', 'rt')
    for line in f:
        data = line[:-1].split(',')
        xd_list.append(float(data[0]))
        xu_list.append(float(data[1]))

    xd_list = np.array(xd_list)
    xu_list = np.array(xu_list)
    plt.ion

    ''' read file '''
    i = 0
    while i < 100000:
        #    for i in range(0, 200):
        ''' adjust x,y range '''
        plt.xlim(-13, 13)
        plt.ylim(-20, 20)

        ''' plot Scintillator '''
        yu, = plt.plot([-3, 3], [ulength, ulength], c='Black', lw=10)
        yd, = plt.plot([-10, 10], [dlength, dlength], c='Black', lw=10)

        plt.plot(xd_list[i], dlength, "*", markersize=12)
        plt.plot(xu_list[i], ulength, "*", markersize=12)

        ''' plot y=a*x+b '''
        print("No {0} hit !!!!".format(i+1))
        print("down_hitposition = {0}, up_hitposition = {1}".format(
            xd_list[i], xu_list[i]))

        if xd_list[i] != xu_list[i]:
            plt.plot([-13, 13], [st_line(xd_list[i], xu_list[i], -13),
                                 st_line(xd_list[i], xu_list[i], 13)], "r-", c='Red')
        else:
            plt.axvline(xd_list[i], c='Red')
#
        #''' draw part '''
        plt.draw()
        plt.pause(0.3)
        plt.cla()

        key = input()
        if key == 'b':
            i -= 1
        elif key == '':
            i += 1
            pass
        elif key == 'q':
            break
        print("{0} hit finish!!!\n".format(i))
    plt.close()


''' this is omajinai that excecute main()'''
if __name__ == '__main__':
    main()
