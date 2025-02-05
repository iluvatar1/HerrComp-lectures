class TimeIntegrator:
    """
    Class that uses Leapfrog to advance in time
    """
    dt = 0.01 # should be changed according to the simulation needs
    def __init__(self, dt): # constructor
        self.dt = dt
        
    def startIntegration(self, body):
        body.V = body.V - 0.5*self.dt*body.F/body.mass
        
    def timestep(self, body):
        body.V = body.V + self.dt*body.F/body.mass
        body.R = body.R + self.dt*body.V
        