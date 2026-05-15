### BEGIN SOLUTION
from scipy import linalg
import numpy as np
import time # use time.process_time_ns() , compare with monotonic_ns()

MINSIZE=1
MAXSIZE=5000
NSAMPLES=10
data = np.zeros((NSAMPLES, 3))

for ii,N in enumerate(np.geomspace(MINSIZE, MAXSIZE, num=NSAMPLES)) :
    A = np.random.rand(int(N), int(N))
    start = time.process_time_ns() 
    #start = time.monotonic_ns() 
    kappa = linalg.norm(A)*linalg.norm(linalg.inv(A))
    end = time.process_time_ns() 
    #end = time.monotonic_ns() 
    elapsed = (end-start)*1.0e-9
    data[ii, 0] = int(N)
    data[ii, 1] = kappa
    data[ii, 2] = elapsed
    print(f"{int(N)}  {kappa}  {elapsed}")

    
### END SOLUTION
