import numpy as np
import matplotlib.pyplot as plt


def sumk (k):
    suma = 0.0
    for i in range(1, k+1): 
        suma += 0.1
    return np.abs((k/10.0)-suma)




#print(f"5 {sumk(5)}")
#print(f"10 {sumk(10)}")
#print(f"50 {sumk(50)}")
#print(f"500 {sumk(500)}")


k = np.arange(1, 100000)
sumas = np.zeros(len(k))
for ii, ik in enumerate(k):
    sumas[ii] = sumk(ik)

plt.plot(k, sumas)
plt.xlabel("k")
plt.ylabel("Sum k")

plt.show()

