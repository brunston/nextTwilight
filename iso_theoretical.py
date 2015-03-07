# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:23:19 2014
@author: B Poon (demure)
"""

import numpy as np
from matplotlib import pyplot as plt
#from math import log10

#definitions
first = r"C:\pyf\ast\iso100Mfixed.txt"
second = r"C:\pyf\ast\iso1G.txt"
third = r"C:\pyf\ast\iso10G.txt"

def iso_theo(filepath, color, dist):
    """
    Plots theoretical isochrones using file and color
    """
    data = np.loadtxt(filepath)
    i = data[:,2]
    v = data[:,3]
    mbol = data[:,1]
    #optdist = 1 #replaces dist because of worksheet
    optdist = log10(dist)
    i_mag = mbol - i + 5 * optdist - 5
    v_mag = mbol - v + 5 * optdist - 5
    v_minus_i = v_mag - i_mag
    plt.plot(v_minus_i, i_mag, color ,markersize = 5)
    plt.title("Theoretical Isochrones, 100Myr, 1Gyr, 10Gyr")
    plt.xlabel("V-i (mag)")
    plt.ylabel("i (mag)")
    #y axis bottom to top, positive to negative value switch
    plt.ylim(26, 10)
    
def main():
    #lmc_dist doesn't do anything, because calc from worksheet
    lmc_dist = 39810 #parsecs to LMC
    iso_theo(first, 'b.', lmc_dist)
    iso_theo(second, 'y.', lmc_dist)
    iso_theo(third, 'g.', lmc_dist)


if __name__ == '__main__':
    main()