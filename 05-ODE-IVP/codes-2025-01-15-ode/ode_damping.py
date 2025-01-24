import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context("talk")

def fderiv(t, y, m, b, g):
    z, v = y
    return np.array([v, -b*v - g])


def final_vel(m, b, g):
    # Definir el sistema: condiciones iniciales y tiempo
    T = np.arange(0.0, 10.0/b, 0.01/b)
    y0 = [10.0, 0.0]
    # resolver el sistema con solve_ivp
    sol = solve_ivp(fderiv, t_span=[T.min(), T.max()], t_eval=T,
                    y0=y0, args=(m, b, g))
    # Verificar si la velocidad se estabilizo?
    # Retornar la ultima velocidad
    return sol.y[1][-1]
final_vel = np.vectorize(final_vel)

def solve_plot():
    M = 60.7
    G = 9.81
    B = np.arange(0.1, 2.5, 0.1)
    VF = final_vel(M, B, G) # Uses the vectorized version
    #VF = np.zeros_like(B)
    #for ib, b in enumerate(B):
    #    VF[ib] = final_vel(M, b, G)
    print(VF)

    fig, ax = plt.subplots(1, 1)
    ax.plot(B, VF, '-o', label="Data")
    ax.legend()
    fig.savefig("vf.pdf")
    
solve_plot()
# TODO: Decouple plot and simulation
# TODO: Normalize the system and the plot
