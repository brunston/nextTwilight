# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:16:17 2014

@title: hyperleda1
@author: bp
"""

import numpy as np
from matplotlib import pyplot as plt
from math import *
afile = r"C:\ast\hyperleda1-noname.cgi"
adata = np.loadtxt(afile)
adataX = data[:,0]
adataY = data[:,1]
adataSrX = []
adataSrY = []

bfile = r"C:\ast\hyperledaAGN.cgi"
bdata = np.loadtxt(bfile)
bdataX = data[:,0]
bdataY = data[:,1]
bdataSrX = []
bdataSrY = []

def errDetector(dataX, dataY, dataSrX, dataSrY):
    for i in range(0,len(dataX)-1):
        if dataX[i] != -99999 and dataY[i] != -99999:
            dataSrX.append(dataX[i])
            dataSrY.append(dataY[i])

def plot(x,y,title,xlbl,ylbl,i):
    plt.figure(i)
    plt.clf()
    plt.plot(x,y,'g.',markersize = 2)
    plt.title(title)
    plt.ylabel(xlbl)
    plt.xlabel(ylbl)
    plt.show()

if __name__ == '__main__':
    aTitle = "MABS vs Galaxy Morphology (for quasars)"
    axlbl = "MABS"
    aylbl = "Morphology"
    errDetector(adataX, adataY, adataSrX, adataSrY)
    plot(adataSrX,adataSrY,aTitle,axlbl,aylbl, 0)
    
    bTitle = "MABS vs Galaxy Morphology (for agnclass S1)"
    bxlbl = "MABS"
    bylbl = "Morphology"
    errDetector(bdataX, bdataY, bdataSrX, bdataSrY)
    plot(bdataSrX,bdataSrY,bTitle,bxlbl,bylbl, 1)