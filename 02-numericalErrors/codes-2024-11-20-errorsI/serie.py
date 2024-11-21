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

# ##############################################################
# main
X = 29.3456
print(f"{np.exp(-X)}")
print(f"{expA(X, 5)}")
print(f"{expA(X, 15)}")
print(f"{expA(X, 30)}")
print(f"{expA(X, 50)}")

print(f"{factorial(10)}")
print(f"{factorial(100)}")
print(f"{factorial(200)}")

