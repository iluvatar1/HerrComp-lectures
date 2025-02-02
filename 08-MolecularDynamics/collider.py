import numpy as np
class Collider:
    """
    Class to compute forces on each body
    """
    # Parameters
    G = np.array([0.0, -9.81, 0.0])
    B = 3.9
    K = 1000.345

    # Functions
    def computeForce(self, body): # For now operate on a single body
        body.F = np.zeros(3) # Reset the force
        body.F += body.mass*self.G # Add gravity
