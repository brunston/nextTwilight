# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:52:02 2014
@author: B Poon (demure)
creates a Redshift v Distance diagram from cfa2_1.txt data
"""

import numpy as np
from matplotlib import pyplot as plt

#definitions
ourfile = r"C:\pyf\ast\cfa2_1.txt"
ourfile_color = 'b.'
hubbleval = 73

def plotter(filepath, color, hubble_value):
    """
    Plots distance and redshift
    """
    data = np.loadtxt(filepath)
    vrec = data[:,2]
    dist = vrec/(hubble_value*1000)
    plt.plot(dist, vrec, color, markersize = 5)
    plt.title("Redshift vs. Distance")
    plt.xlabel("Distance")
    plt.ylabel("Redshift")


def main():
    plotter(ourfile,ourfile_color, hubbleval)


if __name__ == '__main__':
    main()