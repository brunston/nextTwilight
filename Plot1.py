import numpy as np
from matplotlib import pyplot as plt
data = np.loadtxt(r"C:\pyf\ast\cfa2_1.txt")
one = data[:,0]
two = data[:,2]
plt.plot(one, two, 'b.', markersize = 12)
