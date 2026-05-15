
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as spderiv

def forward(f, x, h):
    return (f(x+h)-f(x))/h

def central(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

def central_richardson(f, x, h):
    ### BEGIN SOLUTION
    val1 = central(f, x, h)
    val2 = central(f, x, h/2)
    return val2 + (val2-val1)/3
    ### END SOLUTION

def compare_derivatives():    
    fig, ax = plt.subplots()
    h = np.power(10.0, np.arange(-18, 0, +1))
    x = np.pi/3
    ### BEGIN SOLUTION
    deriv_exact = np.cos
    fun = np.sin
    algnames=["forward", "central", "central_richardson", "scipyderiv"]
    for alg, algname in zip([forward, central, central_richardson, spderiv], algnames):
        diff = np.abs(1 - alg(fun, x, h)/deriv_exact(x))
        ax.loglog(h, diff, '-o', label=algname)
    ax.set_xlabel(rf"$h$", fontsize=20)
    ax.set_ylabel(rf"$\Delta$", fontsize=20)
    fig.legend()
    plt.show()
    fig.savefig("derivs.pdf")
    ### END SOLUTION
    

compare_derivatives()

