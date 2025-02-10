# Printing data for paraview visualization. 
import os
import numpy as np
from pyevtk.hl import pointsToVTK

# Check that DISPLAY dir exists
DISPLAY_DIR="./DISPLAY"
if not os.path.exists(DISPLAY_DIR):
    os.makedirs(DISPLAY_DIR)  # Creates parent directories if needed
    print(f"Directory '{DISPLAY_DIR}' created.")
else:
    print(f"Directory '{DISPLAY_DIR}' already exists.")

# Write a vtk file using pyevtk, assume particles moving uniformly
T = np.arange(0.0, 10.0, 0.1)
V1 = 0.14
V2 = 0.34
for ii in range(len(T)):
    pointsToVTK(f"./DISPLAY/system_{ii:05d}", # filename
                np.array([0.0 + V1*T[ii], -4.5 + V2*T[ii]]), # x
                np.array([0.1, 0.3]), # y
                np.array([0.0, 0.0]), # z
                data={"radius": np.array([0.087, 0.187]), 
                      "speed": np.array([np.linalg.norm([V1, 0.0]), 
                                         np.linalg.norm([V2, 0.0])])})