import matplotlib.pyplot as plt 
from scipy import linalg
import numpy as np
N = 1000
A = np.random.rand(N, N)
#plt.imshow(A, cmap='viridis')
B = linalg.inv(A) # magic
#print("A : \n", A)
#print("B : \n", B)
# verify
#print("A A^-1 : \n", A.dot(B))
plt.imshow(A.dot(B), cmap='viridis')
plt.colorbar()
plt.show()