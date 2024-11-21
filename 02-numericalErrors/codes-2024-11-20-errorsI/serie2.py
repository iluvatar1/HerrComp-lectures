import numpy as np

def expA(x, k):
    suma = 0.0
    for ii in range(k):
        term = ((-1)**ii)*(x**ii)/factorial(ii)
        suma += term
    return suma

def factorial(n):
    result = 1
    for ii in range(1, n+1):
        result *= ii
    return result

def expB(x, k):
    suma = 1.0
    term = 1.0
    for ii in range(1, k):
        term = -x*term/(ii+1)
        suma += term
    return suma


# ##############################################################
# main
X = 29.3456
print(f"{np.exp(-X)}")
for k in range(1, 10):
    print(f"{k=:5d} {expA(X, k)=:21.16e} {expB(X, k)=:21.16e}")


