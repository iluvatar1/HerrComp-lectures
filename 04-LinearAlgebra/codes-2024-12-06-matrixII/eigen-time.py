# See : https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html#scipy.linalg.eig
import numpy as np
from scipy import linalg
import time
import sys

def get_time(N):
    A = np.random.rand(N, N)
    t1 = time.time()
    sol = linalg.eig(A) # magic
    t2 = time.time()
    return t2-t1

def get_mean_sigma(N, nsamples):
    """
    Repeat nsamples times the comptutation and return the mean and sigma
    """
    mytime = np.zeros(nsamples)
    for ii in range(nsamples):
        mytime[ii] = get_time(N)
    return mytime.mean(), mytime.std()

#####################################################
if __name__ == "__main__":
    NMAX = int(sys.argv[1])
    NSAMPLES = int(sys.argv[2])
    N = []
    T = []
    TSTD = []

    n = 10
    while n <= NMAX:
        tmean, tstd = get_mean_sigma(n, NSAMPLES)
        N.append(n)
        T.append(tmean)
        TSTD.append(tstd)
        n *= 2
    
    print(N)
    print(T)
    print(TSTD)

    # merge data
    data = np.column_stack((N, T, TSTD))
    print(data)

    # sava data
    np.savetxt("data.txt", data)