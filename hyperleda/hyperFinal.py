# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 11:46:12 2014

@title: Hyperleda Final Project
@author: bp
"""

import numpy as np
from matplotlib import pyplot as plt
from math import log10

afile = r"C:\ast\hyperleda\bhbDataC.txt"
adata = np.loadtxt(afile, usecols=[1,2,3,4,6,7,8,9,10,11,12,13,14,17,18])

#graph a
mbh = adata[:,2] #mbh, msun
reff = adata[:,14] #Reff in i-band, arcsec
mbhSr = []
reffSr = []

#graph c
rinf = adata[:,12] #Rinf, arcsec
mbh2Sr = []
rinfSr = []

#graph d
mbh3Sr = []
sigma = adata[:,4] #velocity dispersion km/s
sigmaSr = []

#graph e
sigma2Sr = []
rinf2Sr = []

#graph h
dist = adata[:,0]
mbh4Sr = []
distSr = []

#graph b
bfile = r"C:\ast\hyperleda\hyperledaAGN.cgi"
bdata = np.loadtxt(bfile)
bdataX = bdata[:,0]
bdataY = bdata[:,1]
bdataSrX = []
bdataSrY = []

#graph f
ffile = r"C:\ast\hyperleda\hyperledaQmabs-noname.cgi"
fdata = np.loadtxt(ffile, usecols=[0,3])
fdataX = fdata[:,1]
fdataY = fdata[:,0]
fdataSrX = []
fdataSrY = []

#graph g
gfile = r"C:\ast\hyperleda\hyperledaSeyfertmabs-noname.cgi"
gdata = np.loadtxt(gfile, usecols=[0,3])
gdataX = gdata[:,1]
gdataY = gdata[:,0]
gdataSrX = []
gdataSrY = []

def errDetectorBH(dataX, dataY, dataSrX, dataSrY):
    for i in range(0,len(dataX)-1):
        if dataX[i] != 0 and dataY[i] != 0:
            dataSrX.append(dataX[i])
            dataSrY.append(dataY[i])

def logify(array):
    retArray = []
    for i in range(0, len(array)):
        retArray.append(log10(array[i]))
    return retArray
            
def errDetector(dataX, dataY, dataSrX, dataSrY):
    for i in range(0,len(dataX)):
        if dataX[i] != -99999 and dataY[i] != -99999:
            dataSrX.append(dataX[i])
            dataSrY.append(dataY[i])

def plot(x,y,title,xlbl,ylbl,i):
    plt.figure(i)
    plt.clf()
    plt.plot(x,y,'g.',markersize = 4)
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.show()

def plotAlt(x,y,title,xlbl,ylbl,i):
    plt.figure(i)
    plt.clf()
    plt.plot(x,y,'g.',markersize = 4)
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)

if __name__ == '__main__':
    
    aTitle = "Black Hole Mass vs Effective Radius"
    axlbl = "Effective Radius (arcsec)"
    aylbl = "Black Hole Mass (log(Msun))"
    errDetectorBH(reff, mbh, reffSr, mbhSr)
    plot(reffSr,logify(mbhSr),aTitle,axlbl,aylbl, 0)
    
    bTitle = "MABS vs Galaxy Morphology (for agnclass S1)"
    bylbl = "MABS"
    bxlbl = "Morphology"
    errDetector(bdataX, bdataY, bdataSrX, bdataSrY)
    plot(bdataSrX,bdataSrY,bTitle,bxlbl,bylbl, 1)
    
    cTitle = "Radius of Influence vs Black Hole Mass"
    cxlbl = "Black Hole Mass (log(Msun))"
    cylbl = "Radius of Influence (arcsec)"
    errDetectorBH(mbh, rinf, mbh2Sr, rinfSr)
    #plotAlt(mbh2Sr, rinfSr, cTitle, cxlbl, cylbl, 2)
    #cfit = np.polyfit(mbh2Sr, rinfSr, 4)
    #cpoly = poly1d(cfit)
    #plt.plot(mbh2Sr, cpoly(mbh2Sr), 'b.')
    #plt.show()
    plot(logify(mbh2Sr), rinfSr, cTitle, cxlbl, cylbl, 2)
    
    dTitle = "Velocity Dispersion vs Black Hole Mass"
    dx = "Black Hole Mass (log(Msun))"
    dy = "Velocity Dispersion (km/s)"
    errDetectorBH(mbh, sigma, mbh3Sr, sigmaSr) #do log of mbh and figure out wtf is wrong with y lbl
    plotAlt(logify(mbh3Sr), sigmaSr, dTitle, dx, dy, 3)
    dfit = np.polyfit(logify(mbh3Sr), sigmaSr, 1)
    dpoly = np.poly1d(dfit)
    plt.plot(logify(mbh3Sr), dpoly(logify(mbh3Sr)), '-')
    
    eTitle = "Radius of Influence vs Velocity Dispersion"
    ey = "Radius of Influence (arcsec)"
    ex = "Velocity Dispersion (km/s)"
    errDetectorBH(rinf, sigma, rinf2Sr, sigma2Sr)
    plot(sigma2Sr, rinf2Sr, eTitle, ex, ey, 4)
    
    fTitle = "MABS vs Galaxy Morphology (for agnclass Q)"
    fylbl = "MABS"
    fxlbl = "Morphology"
    errDetector(fdataX, fdataY, fdataSrX, fdataSrY)
    plot(fdataSrX,fdataSrY,fTitle,fxlbl,fylbl, 5)
    
    gTitle = "MABS vs Galaxy Morphology (for agnclass S1 and S1n)"
    gylbl = "MABS"
    gxlbl = "Morphology"
    errDetector(gdataX, gdataY, gdataSrX, gdataSrY)
    plot(gdataSrX,gdataSrY,gTitle,gxlbl,gylbl, 6)
    
    hTitle = "Black Hole Mass vs Distance"
    hylbl = "Black Hole Mass (log(Msun))"
    hxlbl = "Distance (Mpc)"
    errDetectorBH(mbh, dist, mbh4Sr, distSr)
    plot(distSr, mbh4Sr, hTitle, hxlbl, hylbl, 7)