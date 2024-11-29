import numpy as np
from scipy.integrate import quad

def k(theta, x):
    return 1.0/np.sqrt(1 - np.square(x*np.sin(theta)))

x = np.linspace(0.0, 1.0, 100, endpoint=False)
y = np.zeros_like(x)

for ix in np.arange(len(x)):
    y[ix] = quad(k, 0.0, np.pi/2, args=(x[ix]))[0]

# plot
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1, 1)
ax.plot(x, y, '-o', label = "Eliptical")
plt.legend()

plt.show()