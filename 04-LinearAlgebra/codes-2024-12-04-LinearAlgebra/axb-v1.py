import numpy as np

A = np.array([[150, -100, 0], 
              [-100, 150, -50], 
              [0, -50, 50]])
b = np.array([588.6, 686.7, 784.8])
x = np.linalg.solve(A, b) # magic
print("Solution: \n", x)
# confirm
print("Delta:\n", A.dot(x) - b)