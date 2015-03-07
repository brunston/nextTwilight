# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 10:19:03 2014

@author: demure
"""
import numpy as np
from matplotlib import pyplot as plt
data = np.loadtxt(r"C:\pyf\ast\iso10G.txt")
logteff = data[:,0]
mbol = data[:,1]
#logteff_inv = list(reversed(logteff))
plt.plot(logteff, mbol, 'g.',markersize = 5)
plt.title("Isochrone, 10Gyr")
plt.xlabel("logTeff")
plt.ylabel("Mbol")
plt.xlim(4.3,3.3)
plt.ylim(8,-8)