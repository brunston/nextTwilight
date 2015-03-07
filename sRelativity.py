# -*- coding: utf-8 -*-
"""
@date: 2014.10.13
@author: Brunston Poon
@description: Special Relativity Data worksheet / lab thing
"""

import numpy as np
from matplotlib import pyplot as plt
from math import *
file = r"C:\ast\momentumdecay.txt"

#A1 A1 A1 A1 A1 A1
#Predict results using Galilean relativity
cMesonVelocity = 0.999 # units c
cMesonLifetime = 4.0 * 10**(-14) #from Special Relativity PDF on rutgers.edu
lengthDecay = cMesonVelocity * cMesonLifetime

#B4 B4 B4 B4 B4 B4
#see Answer Supplement

cMesonMass = 1.865 #units GeV/c^2

#B5 B5 B5 B5 B5 B5
data = np.loadtxt(file)
cMesonMomentum = data[:,0] #units GeV/c
cMesonDecayLength = data[:,1] #units cm
gamma = 1 / sqrt(1 - (cMesonVelocity**2 / 1))

#B6 B6 B6 B6 B6 B6
cMesonRVelocity = []
for i in range(0, len(cMesonMomentum - 1)):
    cMesonRVelocity.append(sqrt((-(cMesonMomentum[i]**2))/(-(cMesonMomentum[i]**2)-cMesonMass**2)))
    
print(cMesonRVelocity)

#B7 B7 B7 B7 B7 B7
plt.figure(0)
plt.clf()
plt.plot(cMesonRVelocity, cMesonDecayLength, 'b.', markersize = 2)
plt.title("Decay Length vs Velocity")
plt.ylabel("Decay Length (cm)")
plt.xlabel("Velocity (times c)")
plt.show()