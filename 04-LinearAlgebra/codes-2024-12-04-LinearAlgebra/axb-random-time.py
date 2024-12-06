# compute time as function of N
import numpy as np
import time 

#np.random.seed(10) # Play with this value
NMAX = 20000
N = 10
while N <= NMAX:
    A = np.random.rand(N,N)
    b = np.random.rand(N)
    t1 = time.time()
    x = np.linalg.solve(A, b) # magic
    t2 = time.time()
    #print("Solution: \n", x[:10])
    # confirm
    #print("Delta:\n",A.dot(x) - b)
    print(f"{N}\t{t2-t1:.16e}")
    N = 2*N