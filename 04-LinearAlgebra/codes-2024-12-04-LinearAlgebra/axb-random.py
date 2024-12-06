import numpy as np

#np.random.seed(10) # Play with this value

N = 10000

A = np.random.rand(N,N)
b = np.random.rand(N)
x = np.linalg.solve(A, b) # magic
print("Solution: \n", x[:10])
# confirm
#print("Delta:\n",A.dot(x) - b)