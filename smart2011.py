# -*- coding: utf-8 -*-
"""
SMART_2011 Assignment
Includes Conversion from Scilab to Python3
Brunston Poon

begun 2014.09.22 - completed 2014.09.25
"""

import numpy as np
from matplotlib import pyplot as plt

file = r"C:\ast\SMART_data.txt"
numberOfColumns = 7
data = np.loadtxt(file)

radii = data[:,0] # Distance column, in kiloparsecs (kpc)
neutralGasMass = data[:,1] # Neutral Gas column, in solar masses (m_sun)
luminosityB = data[:,2] # Luminosity in the B band, solar luminosities (l_sun)
luminosityR = data[:,3] # Luminosity in R band, l_sun
velocityModel = data[:,4] # Velocity, modeled to "smooth" the data (kms) 
colCounterRotating = data[:,5] # This velocity array includes counter-rotating elements. 
velocity = data[:,6] # Velocity column in kilometers/second (kms)

number = 1
plt.figure(number)
plt.clf() #housekeeping, clears plot
plt.cla() #housekeeping, clears plot
number = number + 1

# plot velocity (km/s) versus distance (kpc)
plt.plot(radii,velocity,'b.', markersize = 3)
plt.plot(radii,velocityModel,'g.',markersize = 3)
plt.title("Plot of Velocity Data and Velocity Model versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (m_sun)")

# plot gas mass (m_sun) versus distance (kpc)
plt.figure(number)
plt.clf() #housekeeping
plt.cla()#housekeeping
number = number + 1
plt.plot(radii,neutralGasMass,'b.', markersize = 3)
plt.title("Plot of Neutral Gas Mass versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Mass (m_sun)")

# plot luminosity (l_sun) versus distance (kpc)
plt.figure(number)
plt.clf() #housekeeping
plt.cla() #housekeeping
number = number + 1
plt.plot(radii,luminosityR,'b.', markersize = 3)
plt.title("Plot of Luminosity versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Luminosity (l_sun)")

#luminosity profile to mass profile
mlr1 = 0.477
mlr2 = 0.891

massStarsR1 = luminosityR * mlr1
massStarsR2 = luminosityR * mlr2
massStarsR1b = luminosityB * mlr1
massStarsR2b = luminosityB * mlr2

plt.figure(number)
plt.clf() #housekeeping
plt.cla() #housekeeping
number = number + 1

plt.plot(radii,massStarsR1,'b.', markersize = 3) 
plt.plot(radii,massStarsR2,'g.', markersize = 3)
plt.title("Plot of Stellar Mass (R1 B, R2 G) versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Stellar Mass (m_sun)")

grav = 4.28*10**(-6) # units of kpc*km^2/(M_sun*s^2)
massEnc = velocityModel**2*radii/grav
#this is the total mass within each radius (from zero) based on the rotation curve formula
indexArray = []
for i in range(0,len(massEnc-1)):
    n = 2 + i
    indexArray.append(n)

incrementalMass = []
for i in range(0,len(indexArray)):
    incrementalMass.append(massEnc[i]-massEnc[i-1])
incrementalMass[0] = velocityModel[0]**2*radii[0]/grav

#this will plot the incremental mass versus radius 
plt.figure(number)
plt.clf() #housekeeping
plt.cla() #housekeeping
number = number + 1

plt.plot(radii,incrementalMass, 'b.', markersize = 3)
plt.title("Plot of ""Incremental"" Mass versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Incremental Mass (m_sun)")

darkMatter = incrementalMass - neutralGasMass - massStarsR1
darkMatterb = incrementalMass - neutralGasMass - massStarsR1b
plt.figure(number)
plt.clf() #housekeeping
plt.cla() #housekeeping
number = number + 1

#INCREMENTAL MASS = TOTAL MASS, incMass = darkMatter + neutralGasMass + massStarsR1 or R2

plt.plot(radii,darkMatter, 'b.', markersize = 3)
plt.plot(radii,massStarsR1, 'g.', markersize = 3)
plt.plot(radii, darkMatterb, 'r.', markersize = 5)
plt.plot(radii,incrementalMass, 'r.', markersize = 3)
plt.plot(radii,neutralGasMass, 'y.', markersize = 3)
plt.title("Total Mass (red), Stellar Mass (green),\n Dark Matter Bband (thickRed), Dark Matter Rband (blue), \n\
Neutral Gas Mass (red), versus Radius")
plt.xlabel("Radius (kpc)")
plt.ylabel("Mass (m_sun)")


plt.show()