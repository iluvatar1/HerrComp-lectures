import numpy as np
A = np.array([[1, 2],  # primera fila, indice es 0
              [3, 4]]) # Segunda fila, indice es 1
print(A[0][1])
print(f"Matrix : \n", A)
#
A = np.array([1, 2, 3, 4]).reshape(2,2)
print("Matrix : \n", A)
print("A[1,0] : \n", A[1,0])
print("A[1][0] : \n", A[1][0])

print("A[:,-1] : \n", A[:,-1])
