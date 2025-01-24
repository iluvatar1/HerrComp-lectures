from scipy.integrate import solve_ivp
import numpy as np


# Global constants could be removed using a multiarg function
A=1.2
B=0.6
C=0.8
D=0.3

X0=2
Y0=1
T0=0
TF=50
DT=0.0625

def fderiv(t, y): 
    return np.array([A*y[0] - B*y[0]*y[1], -C*y[1] + D*y[0]*y[1]])

sol = solve_ivp(fderiv, t_span=[T0, TF], t_eval=np.arange(T0, TF+DT, DT), y0=[X0, Y0])

#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context("poster")

fig, ax = plt.subplots(1,2, figsize=(14, 6))
ax[0].plot(sol.t, sol.y[0], label=r"Prey")
ax[0].plot(sol.t, sol.y[1], label=r"Predator")
ax[0].set_xlabel(r"$t$[s]")
ax[0].set_ylabel(r"$x(t), y(t)$")
ax[0].legend()
ax[1].plot(sol.y[0], sol.y[1])
ax[1].set_xlabel(r"$x$")
ax[1].set_ylabel(r"$y$")

fig.savefig("lv.pdf")

# Can you compoute the critical points?