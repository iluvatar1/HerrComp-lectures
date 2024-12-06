import numpy as np 
import matplotlib.pyplot as plt 
import sys

fname = sys.argv[1]

# read data
data = np.loadtxt(fname)

# plot data
fig, ax = plt.subplots(1, 1)
ax.errorbar(data[:,0], data[:, 1], data[:, 2])
ax.set_xscale("log")
ax.set_yscale("log")
plt.show()