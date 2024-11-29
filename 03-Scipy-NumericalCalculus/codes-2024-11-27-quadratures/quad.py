import numpy as np 
from scipy.integrate import quad, dblquad, tplquad
print(quad(np.square, 0, 1))
integral_val, error = quad(np.square, 0, 1)
vquad = np.vectorize(quad)
print(vquad(np.square, 0, [1, 2, 3]))

# Indefinite integral
val, abserr = quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)
print(f"numerical  = {val}, {abserr}")
print(f"analytical = {np.sqrt(np.pi)}")