import numpy as np 
import matplotlib.pyplot as plt 

def solve(M, c):
    return np.linalg.solve(M, c)

# define system
A = np.array([[-2.48/5, 1], [-0.5, 1]])
b = np.array([1.1, 1.0])

x = solve(A, b)
print(x)
print(A.dot(x) - b)

print(np.linalg.cond(A))

# plot
fig, ax = plt.subplots(1, 1)
xdata = np.linspace(-10.0, 10.0, 100)
ax.plot(xdata, 1.1 + 2.3*xdata/5)
ax.plot(xdata, 1.0 + 0.5*xdata)
fig.savefig('condition.pdf')
