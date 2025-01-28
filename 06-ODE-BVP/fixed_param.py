# This is an example on how to handle fixed and changing params
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
sns.set()
sns.set_context("talk")

def deriv(t, y, params, fixed_params):
    ### BEGIN SOLUTION
    return [y[1], fixed_params[1]*y[0]/fixed_params[0] - fixed_params[2]*y[1]]
    ### END SOLUTION
    

def bc(ya, yb, params, fixed_params):
    ### BEGIN SOLUTION
    return [ya[0]-0.1, yb[0], ya[1] - params[0]] # change the initial velocity
    ### END SOLUTION
    

def mysolve_bvp(x, y0, params, fixed_params):
    ### BEGIN SOLUTION
    sol = solve_bvp(lambda x, y0, params: deriv(x, y0, params, fixed_params), # model it as a 3-arg funtion, does not change fixed_params
                    lambda ya, yb, params: bc(ya, yb, params, fixed_params),  # model it as a 3-arg funtion, does not change fixed_params
                    x, y0, p=params, 
                    verbose=2) # print more info
    ### END SOLUTION
    
    return sol

for PARAMS in [np.array([1.5e-6, 5e-6, 0.0]), np.array([1.5e-6, 5e-6, 4.8920])]:
    x = np.linspace(0, 4.0, 100)
    y0 = np.ones((2, x.size))
    sol = mysolve_bvp(x, y0, np.array([1.0]), PARAMS)
    fig, ax = plt.subplots()
    ax.plot(sol.x, sol.y[0])
    print(sol.p)
