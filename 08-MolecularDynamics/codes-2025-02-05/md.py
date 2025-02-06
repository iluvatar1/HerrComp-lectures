import numpy as np
import body as bd
import collider as col
import integrator as tint 

#%matplotlib inline
import matplotlib.pyplot as plt

# Pre-processing: Setup. For more particless: mass distribution, random positions, etc

particles = np.array([bd.Body([1.23, 2.34, 0.0], [2.1, 10.2, 0.0], 0.654, 0.23)])

# Collider
collider = col.Collider()
collider.computeForce(particles) # Initial force

# Time evolution stuff
DT = 0.005
T = np.arange(0.0, 20.5, DT)
NSTEPS = T.size
leapfrog = tint.TimeIntegrator(DT)
leapfrog.startIntegration(particles) # mover la velocidad a -dt/2

# Save data
Ry = np.zeros(NSTEPS); 
Vy = np.zeros(NSTEPS)
Rx = np.zeros(NSTEPS); 
Vx = np.zeros(NSTEPS)

# main evolution loop
it = 0
while it < NSTEPS:
    Ry[it] = particles[0].R[1]; 
    Vy[it] = particles[0].V[1]
    Rx[it] = particles[0].R[0]; 
    Vx[it] = particles[0].V[0]
    collider.computeForce(particles)
    leapfrog.timestep(particles)
    it = it + 1

print(Vy[-1])

# plot
# plot final trayectories 
fig, ax = plt.subplots(1, 2, figsize=(9,4))
ax[0].plot(T, Ry, 'o', label="R-lf")
#ax[0].plot(T, R0[1] + V0[1]*T + 0.5*T*T*G[1], '-', label="Exact", lw=3)
ax[1].plot(Rx, Ry, 'o', label="RxRy-lf")
ax[0].legend()
ax[1].legend()
ax[0].set_xlabel(r"$t[s]$", fontsize=23)
ax[0].set_ylabel(r"$R_y[m]$", fontsize=23)
ax[1].set_xlabel(r"$R_x[m]$", fontsize=23)
ax[1].set_ylabel(r"$R_y[m]$", fontsize=23)
plt.tight_layout()
fig.savefig("md.pdf")

# # fit
# from scipy.optimize import curve_fit
# def f(x, a, b, c):
#     return a + b*x + c*x*x

# result = curve_fit(f, T, Ry)
# print(result)