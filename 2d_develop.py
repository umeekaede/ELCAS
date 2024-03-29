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
length = float(re.sub("\\D", "", s))
ulength=(length)/2
dlength=-(length)/2
print()

v_prime=2.6e+8 # m/s
c=3.0e+8 # m/s

l=0.30 # m sin length
L=0.15 # m btw sts
t=0.5*10**(-9)  #s 30cm/1ns

a=4*((v_prime/c)**2-1)
b=4*(2*v_prime*t-l)
c=(4*(L*v_prime/c)**2)-4*(v_prime*t)**2-l**2+4*v_prime*t*l

''' define function '''
def st_line(x1, x2, x):
    y = (float(length)/(x2-x1))*(x-x1)+dlength
    return y

''' quadratic_equation '''
def solv_quadratic_equation(a, b, c):
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    return x_1, x_2

''' main content code '''
def main():
    ans=solv_quadratic_equation(a, b, c)
    print(ans)

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

        key = input()
        if key == 'b':
            i -= 1
        elif key == '':
            i += 1
            pass
        elif key == 'q':
            break
        print("{0} hit finish!!!\n".format(i))
        plt.cla()
    plt.close()


''' this is omajinai that excecute main()'''
if __name__ == '__main__':
    main()
