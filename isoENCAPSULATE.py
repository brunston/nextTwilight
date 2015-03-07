# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 11:09:32 2014
@author: B Poon (demure)
"""

import numpy as np
from matplotlib import pyplot as plt

#definitions
first = r"C:\ast\iso100Mfixed.txt"
third = r"C:\ast\iso10G.txt"
second = r"C:\ast\iso1G.txt"
first_c = 'b.'
third_c = 'g.'
second_c = 'y.'

def iso(filepath, color):
    """
    Plots isochrones based on file and color given
    """
    data = np.loadtxt(filepath)
    logteff = data[:,0]
    mbol = data[:,1]
    #logteff_inv = list(reversed(logteff))
    plt.plot(logteff, mbol, color ,markersize = 5)
    plt.title("Isochrones, 1gyr, 10gyr, 100myr")
    plt.xlabel("logTeff")
    plt.ylabel("Mbol")
    plt.xlim(4.3,3.3)
    plt.show()


def main():
    iso(first, first_c)
    iso(second, second_c)
    iso(third, third_c)


if __name__ == '__main__':
    main()