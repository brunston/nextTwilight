# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:48:44 2014
@author: B Poon (demure)
Worksheet: Interpreting Galaxy Redshift Survey Data: Sky Coordinates
"""

import numpy as np
from matplotlib import pyplot as plt
from math import *

def plotter(filepath, color, x, y, xname, yname, find=-1,findbound = -1):
    """
    Plots x and y and labels xname and yname
    """
    data = np.loadtxt(filepath)
    plotx = data[:,x]
    ploty = data[:,y]
    plt.figure(0)
    plt.clf()
    plt.plot(plotx, ploty, color, markersize = 5)
    plt.title(xname+"vs. "+yname)
    plt.xlabel(xname)
    plt.ylabel(yname)
    
    #find command (deprecated)
    """
    if find!=-1:
        findbound = find + 10
        ploty_new = [i for i in ploty if findbound > i > find]
        plt.figure(1)
        plt.plot(plotx,ploty_new, 'g.', markersize = 5)
    """
    if find != -1:    
        bound = np.where((ploty>find)&(ploty<findbound))
        plt.figure(0)
        plt.plot(plotx[bound], ploty[bound], 'g.', markersize = 5)

def polarplot(hubbleval, filepath):
    ppdata = np.loadtxt(filepath)
    ra = ppdata[:,0]
    red = ppdata[:,2]
    dist = red/(hubbleval * 1000)
    rarad = (360/24)*(ra-13)*(math.pi/180)
    plt.figure(1)
    plt.clf()
    newx = dist*sin(rarad)
    newy = dist*cos(rarad)
    plt.plot(newx, newy, 'b.', markersize = 5)
    plt.title("Polar Dist and RA")

def main():
    #definitions
    ourfile = r"C:\pyf\ast\cfa2_1.txt"
    ourfile_color = 'b.'
    hubbleval = 70
    plotter(ourfile,ourfile_color, 0, 1, "RA", "Dec", 25, 35)
    polarplot(hubbleval, ourfile)


if __name__ == '__main__':
    main()