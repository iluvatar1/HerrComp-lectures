import numpy as np
class Collider:
    """
    Class to compute forces on each body
    """
    # Parameters
    G = np.array([0.0, 0.0, 0.0])
    B = 3.9
    K = 1000.345
    L = 5.0987

    # Functions
    def computeForce(self, body): # For now operate on a single body
        body.F = np.zeros(3) # Reset the force
        body.F += body.mass*self.G # Add gravity
        #body.F += -body.mass*self.B*body.V # -mbv , air friction
        # floor
        delta = body.rad - body.R[1]
        if delta > 0:
            body.F[1] += self.K*delta - body.mass*self.B*body.V[1]

        # right wall
        delta = body.R[0] + body.rad - self.L/2
        if delta > 0:
            body.F[0] -= self.K*delta - body.mass*self.B*body.V[0]
    
        # left wall
        delta = body.R[0] - body.rad + self.L/2
        if delta < 0:
            body.F[0] += -self.K*delta - body.mass*self.B*body.V[0]
    
        # top wall
        delta = body.R[1] + body.rad - self.L
        if delta > 0:
            body.F[1] -= self.K*delta - body.mass*self.B*body.V[0]
