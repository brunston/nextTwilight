# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:48:44 2014
@author: B Poon (demure) v2
Worksheet: Interpreting Galaxy Redshift Survey Data: Sky Coordinates
"""

#import modules
import numpy as np
from matplotlib import pyplot as plt
from math import *

def plotter(filepath, color, x, y, xname, yname,find=-1,
            findbound = -1):
    """
    Plots x and y and labels xname and yname
    """
    data = np.loadtxt(filepath) #load data file
    plotx = data[:,x] #assign xvar column source
    ploty = data[:,y] #assign yvar column source
    ra = data[:,0]
    red = data[:,2]
    
    #conversions
    distance = red/(70 * 1000)
    rarad = (360/24)*(ra-13)*(math.pi/180)
    
    #plot
    ion()
    plt.figure(0)
    plt.clf()
    plt.plot(plotx, ploty, color, markersize = 2)
    plt.title(xname+"vs. "+yname)
    plt.xlabel(xname)
    plt.ylabel(yname)

    #find command, uses find and findbound to search ploty and overplot
    if find != -1:    
        bound = np.where((ploty>find)&(ploty<findbound))
        plt.figure(0)
        plt.plot(plotx[bound], ploty[bound], 'g.', markersize = 5)
        
    #polar plot using x = rsin(theta), y = rcos(theta) transformation
    plt.figure(1)
    plt.clf()
    plt.plot(distance*np.sin(rarad),distance*np.cos(rarad), 'b.',
	markersize = 5)
    plt.title("Polar Dist and RA")
    

def main():
    #filename selection, color selection, calling the plot function
    file_selector = r"C:\pyf\ast\cfa2_1.txt"
    file_color = 'b.'
    plotter(file_selector,file_color, 0, 1, "RA", "Dec", 25, 35)


if __name__ == '__main__':
    #Runs if this program is executed as a standalone and not used
    #as a module
    main()