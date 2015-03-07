# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
"""
Created on Mon Apr 14 21:20:27 2014

@author: demure
"""
data = np.loadtxt(r"C:\pyf\ast\testdata.in")
temperature = data[:,0]
humidity = data[:,1]
plt.plot(humidity, temperature, 'b.', markersize = 12)
plt.title('fantastic plot 1')
plt.xlabel('humidity, %')
plt.ylabel('temperature F')
plt.xlim(10,60)
plt.ylim(75,100)