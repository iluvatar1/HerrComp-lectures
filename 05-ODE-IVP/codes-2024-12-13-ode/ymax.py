#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import seaborn as sns
sns.set()
sns.set_context("paper")

def fderiv(t, y, G, R):
    x, v = y
    return np.array([v, -G*R**2/(R+x)**2])
    #return np.array([y[1], -G*R**2/(R+y[0])**2])

# With event
#def hitground(t, y) : 
def hitground(t, y, G, R) : 
    return y[0]
hitground.terminal = True # stops if hitground == 0
hitground.direction = -1 # only when going down

def solve_system(T0, TF, Y0, DT, G, R, event=None):
    T = np.arange(T0, TF+DT, DT)
    sol = solve_ivp(fderiv, t_span=[T.min(), T.max()], t_eval=T, y0=Y0, args=(G, R), events=hitground)
    # fig, ax = plt.subplots(1, 2)
    # ax[0].plot(sol.t, sol.y[0], label=r"$y(t)$")
    # ax[1].plot(sol.t, sol.y[1], label=r"$v_y(t)$")
    # ax[0].set_xlabel(r"$t$ [s]")
    # ax[0].set_ylabel(r"$y(t)$ [m]")
    # ax[0].legend()    
    return sol.t[-1], np.max(sol.y[0])

G = 9.81
R0 = 6.37e6
gvals=np.arange(0.1, 10.0, 0.1)*G
ymax = np.zeros_like(gvals)
tfly = np.zeros_like(gvals)
for ii, g in enumerate(gvals):
    tfly[ii], ymax[ii] = solve_system(T0=0.0, TF=35000, Y0=[0.0, 1500], DT=0.1, 
                                      G=g, R=R0, event=hitground)
ymax = ymax/R0

fig, ax = plt.subplots(1, 2)
ax[0].plot(gvals, tfly, label=r"$tfly")
ax[1].plot(gvals, ymax, label=r"ymax")
ax[0].set_xlabel(r"$G$")
ax[0].set_ylabel(r"$t$ [s]")
ax[0].legend()    
fig.savefig("tmp.pdf")
plt.show()


