import numpy as np
class Body:
    """
    Class to model a simple point body
    """
    def __init__(self, R0, V0, m0, r0 = 0.0): # constructor
        self.mass = m0
        self.rad = r0
        self.R = np.array(R0)
        self.V = np.array(V0)
        self.F = np.zeros(3)


if __name__ == "__main__":
    R0 = np.array([0, 0.9, 0.0])
    V0 = np.array([0.98, 1.23, 0.0])
    mass = 0.4343
    body = Body(R0, V0, mass)
    print(body.mass)
    print(body.V[1])
