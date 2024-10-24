class Point3D :
    """This is a doctring. This allows to embed documentation inside the class definition.
    You can split it 
    across several lines.
    """
    def __init__(self, x = 0, y = 0, z = 0): 
        """ This is the constructor"""
        self.x_ = x # attribute x_
        self.y_ = y # attribute y_
        self.z_ = z # attribute z_
        
    def coordinates(self):
        return self.x_, self.y_, self.z_
    
    def __str__(self):
        """Cast method to convert to string"""
        return (f"Coordinates : ( {self.x_:25.16e}, {self.y_:25.16e}, , {self.z_:25.16e} )")
