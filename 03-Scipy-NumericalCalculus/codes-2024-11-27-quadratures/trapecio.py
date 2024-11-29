import numpy as np

def trapezoid(f, a, b, n):
    """
    Function to compute an integral using the trapezoid rule
    f: function to integrate
    a, b: integral limits, b>a
    n: Number of intervals to use
    """
    npoints = n+1
    xk, dx = np.linspace(a, b, npoints, retstep = True)
    result = dx*(0.5*f(xk[0]) + np.sum(f(xk[1:-1])) + 0.5*f(xk[-1]))
    return result

trapezoid = np.vectorize(trapezoid) # magic to allow to receive vectorized limits

def simpson(f, a, b, n):
    """
    Function to compute an integral using the simpsons rule
    f: function to integrate
    a, b: integral limits, b>a
    n: Number of intervals to use
    """
    npoints = n+1
    if n%2 != 0: 
        npoints += 1
    result = 0
    xk, dx = np.linspace(a, b, npoints, retstep = True)
    result += f(a) + f(b)
    result += 4*np.sum(f(xk[1::2])) + 2*np.sum(f(xk[2:-1:2]))
    result *= dx/3.0
    return result

simpson = np.vectorize(simpson) # magic to allow to receive vectorized limits


print(trapezoid(np.square, 0, 1, 10))
print(trapezoid(np.square, 0, 1, 1000))
print(trapezoid(np.square, 0, 1, 10000000))
print(trapezoid(np.square, [0, 2], [1, 2], 10)) # Check , two limits for two integrals

print(trapezoid(lambda x: np.sin(x*x), 0, 2.565645, 100))

print(simpson(np.square, 0, 1, 10))
print(simpson(np.square, 0, [1, 2], 10)) # Check , two limits for two integrals